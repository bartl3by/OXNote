#!/usr/bin/python3
# -*- coding: utf-8 -*-

import base64
import logging
import os
import pathlib
import uuid
import requests

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QImageReader
from PyQt5.QtWidgets import QTextEdit

from util.configuration import Configuration
from util.environment import Environment

logger = logging.getLogger(__name__)


class EmbeddedMimeTextEdit(QTextEdit):
    supported_image_formats = []

    def __init__(self, *__args):
        if not self.supported_image_formats:
            self.supported_image_formats = [f.data().decode('utf-8') for f in QImageReader.supportedImageFormats()]

        super().__init__(*__args)

    def canInsertFromMimeData(self, source: QMimeData):
        if source.hasImage():
            return True
        elif source.hasUrls():
            return True
        elif source.hasHtml():
            return True
        else:
            return super().canInsertFromMimeData(source)

    def insertFromMimeData(self, source: QMimeData, disable_richtext: bool = False):
        '''
        ..todo: Add support for embedded content when inserting html mime from clipboard
        '''
        if source.hasImage():
            temporary_file = os.path.join(Environment.get_base_path(),
                                          Configuration().get_setting('oxnote', 'application.directories.temporary',
                                                                      default='.oxnote/tmp'),
                                          '{}.png'.format((str(uuid.uuid4()))))

            source.imageData().save(temporary_file)

            with open(temporary_file, 'rb') as f:
                encoded = base64.b64encode(f.read())

            self.textCursor().insertImage('data:image/png;base64,{}'.format(encoded.decode("utf-8")))

            if os.path.isfile(temporary_file):
                os.remove(temporary_file)
        elif source.hasUrls():
            for url in source.urls():
                if pathlib.Path(url.fileName()).suffix.lower()[1:] not in self.supported_image_formats:
                    super().insertFromMimeData(source)
                    continue

                file_extension = pathlib.Path(url.fileName()).suffix.lower()[1:]

                if url.isLocalFile():
                    if not os.path.isfile(url.toLocalFile()):
                        continue

                    with open(url.toLocalFile(), 'rb') as f:
                        self.textCursor().insertImage('data:image/png;base64,{}'.format(
                                base64.b64encode(f.read()).decode("utf-8")))
                else:
                    response = requests.get(url.toString(), stream=True)
                    if response.status_code == 200:
                        self.textCursor().insertImage('data:image/{};base64,{}'.format(
                                file_extension, base64.b64encode(response.content).decode("utf-8")))
        elif source.hasHtml() and disable_richtext:
            self.textCursor().insertText(source.text())
        else:
            super().insertFromMimeData(source)
