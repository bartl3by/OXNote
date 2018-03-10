#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import os
from random import randint

from PyQt5.QtCore import QByteArray, QSize, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QSizePolicy
from PyQt5.uic import loadUi

from models.note import Note
from util.environment import Environment

logger = logging.getLogger(__name__)


class SortableListWidgetItem(QListWidgetItem):

    def __init__(self, note: Note = None, *__args):
        super().__init__(*__args)

        self._note = note

    def __eq__(self, other):
        try:
            return self.comparator == other.comparator
        except:
            return self.comparator == other.text()

    def __ge__(self, other):
        try:
            return self.comparator >= other.comparator
        except:
            return self.comparator >= other.text()

    def __gt__(self, other):
        try:
            return self.comparator > other.comparator
        except:
            return self.comparator > other.text()

    def __le__(self, other):
        try:
            return self.comparator <= other.comparator
        except:
            return self.comparator <= other.text()

    def __lt__(self, other):
        try:
            return self.comparator < other.comparator
        except:
            return self.comparator < other.text()

    def __ne__(self, other):
        try:
            return self.comparator != other.comparator
        except:
            return self.comparator != other.text()

    @property
    def comparator(self):
        return str(self._note.last_modified) if self._note and self._note.file else self.text()

    @property
    def note(self) -> Note:
        return self._note

    @note.setter
    def note(self, note: Note):
        self._note = note


class NotesListWidgetItemWidget(QWidget):

    def __init__(self, filename: str, checksum: str, parent=None):
        super(NotesListWidgetItemWidget, self).__init__(parent)

        self._filename = filename
        self._checksum = checksum

        loadUi(os.path.join(Environment.get_resource_path(), 'designs/default/list_widget.ui'), self)

        if os.path.isfile(os.path.join(Environment.get_resource_path(), 'designs/default/list_widget.qss')):
            with open(os.path.join(Environment.get_resource_path(), 'designs/default/list_widget.qss'), "r") as f:
                self.setStyleSheet(f.read())

        self.label_preview_image.hide()

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self._filename = filename

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        self._checksum = checksum

    def get_title(self):
        return self.label_title.text()

    def set_title(self, title):
        self.label_title.setText(title)

    def get_preview_text(self):
        return self.label_preview_text.text()

    def set_preview_text(self, preview_text):
        self.label_preview_text.setText(preview_text)

    def set_icon(self, base64_image: str):
        if not base64_image:
            self.label_preview_image.clear()
            self.label_preview_image.hide()
        else:
            self.label_preview_image.setPixmap(
                    QPixmap().fromImage(QImage().fromData(QByteArray().fromBase64(str.encode(base64_image)))).scaled(
                            self.label_preview_image.maximumSize(), Qt.KeepAspectRatio))

            self.label_preview_image.setFixedWidth(self.label_preview_image.pixmap().width())
            self.label_preview_image.setMinimumWidth(self.label_preview_image.pixmap().width())

            self.label_preview_image.show()
