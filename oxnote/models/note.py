#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import logging
import os
import re
import ruamel
import sys
import typing
import uuid

from PyQt5.QtCore import QSizeF
from PyQt5.QtGui import QTextCursor, QTextDocument
from PyQt5.QtPrintSupport import QPrinter
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import SingleQuotedScalarString
from slugify import slugify

from models.accounts import Account, AccountManager

logger = logging.getLogger(__name__)


class Note(object):

    def __init__(self,
                 account_id: str,
                 file: str = None,
                 title: str = None,
                 html_content: str = None,
                 document: QTextDocument = None):
        self._document = document if document else QTextDocument()

        self._account_id = account_id
        self._file = file
        self._title = title
        self._document.setHtml(html_content)
        self._last_modified_timestamp = None

        if file:
            self.load()

    @property
    def account(self) -> Account:
        return AccountManager().get_account(self._account_id)

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def file(self) -> str:
        return self._file

    @file.setter
    def file(self, file: str):
        self._file = file

    @property
    def filename(self) -> (str, None):
        if not self.file:
            return None

        return os.path.basename(self.file) if len(os.path.basename(self.file)) > 0 else None

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def html_content(self) -> str:
        return self._document.toHtml()

    @html_content.setter
    def html_content(self, html_content: str):
        self._document.setHtml(html_content)

    @property
    def document(self) -> QTextDocument:
        return self._document

    @document.setter
    def document(self, document: QTextDocument):
        self._document = document

    @property
    def checksum(self) -> str:
        logger.debug('Calculating checksum for note file for account {}: {}'.format(self._account_id,
                                                                                    self._file))

        return self.__calculate_file_checksum()

    @property
    def last_modified(self) -> str:
        if not self._last_modified_timestamp:
            self._last_modified_timestamp = self.__get_last_modified_timestamp()

        return self._last_modified_timestamp

    @property
    def note_list_preview_image(self):
        return self._note_list_preview_image

    def create(self):
        logger.debug('Creating new note for account {}'.format(self._account_id))

        id = str(uuid.uuid4())
        while os.path.isfile(os.path.join(self.account.get_application_data_folder_path(), '{}.oxn'.format(id))):
            id = str(uuid.uuid4())

        self._file = os.path.join(self.account.get_application_data_folder_path(), '{}.oxn'.format(id))

        self.save()

    def delete(self):
        self._note_list_preview_image = None
        self.__delete_preview()

        if os.path.isfile(self.file):
            os.remove(self.file)

    def load(self, file: str = None):
        self._last_modified_timestamp = None

        if not file and not self._file:
            logger.error('Neither instance nor method have a file identifier')
            return

        if file:
            self._file = file

        with open(self._file, "rb") as f:
            logger.debug('Loading note file for account {}: {}'.format(self._account_id, f.name))

            self._document.setHtml(f.read().decode('utf-8'))
            self._title = self._document.metaInformation(QTextDocument.DocumentTitle)

            self.__update_note_list_preview_image()

    def save(self):
        self._last_modified_timestamp = None

        self._document.setMetaInformation(QTextDocument.DocumentTitle, self._title)

        with open(self.file, 'wb') as f:
            logger.debug('Saving note file for account {}: {}'.format(self._account_id, f.name))

            f.write(self._document.toHtml().encode('utf-8'))

        self.__update_note_list_preview_image()
        self.__generate_preview()

    @staticmethod
    def generate_normalized_filename(prefix: str,
                                     suffix: str,
                                     find_nonexisting_filename: bool = False,
                                     nonexisting_filename_directory: str = None) -> str:
        assert nonexisting_filename_directory if find_nonexisting_filename else True

        filename_syntax = '{}{}.{}'.format(slugify(prefix), '{}', suffix)

        if not find_nonexisting_filename:
            return filename_syntax.format('')

        if not os.path.isfile(os.path.join(nonexisting_filename_directory, filename_syntax.format(''))):
            return filename_syntax.format('')

        file_naming_extension = 1
        while os.path.isfile(os.path.join(nonexisting_filename_directory,
                                          filename_syntax.format(' ({})'.format(str(file_naming_extension))))):
            file_naming_extension += 1

        return filename_syntax.format(' ({})'.format(str(file_naming_extension)))

    def __calculate_file_checksum(self) -> str:
        hash_md5 = hashlib.md5()
        with open(self._file, "rb") as f:
            for buffer in iter(lambda: f.read(4096), b""):
                hash_md5.update(buffer)
        return hash_md5.hexdigest()

    def __delete_preview(self):
        synchronization_state = self.__load_synchronization_state()
        if self.filename in synchronization_state['preview_files']:
            if os.path.isfile(synchronization_state['preview_files'][self.filename]):
                os.remove(synchronization_state['preview_files'][self.filename])
            del synchronization_state['preview_files'][self.filename]
            self.__save_synchronization_state(synchronization_state)

    def __generate_preview(self):
        logger.debug('Generating preview document for {}'.format(self._file))

        synchronization_state = self.__load_synchronization_state()
        if self.filename in synchronization_state['preview_files'] and os.path.isfile(
                synchronization_state['preview_files'][self.filename]):
            os.remove(synchronization_state['preview_files'][self.filename])

        preview_filename = os.path.join(self.account.get_oxnote_home_folder_path(),
                                        Note.generate_normalized_filename(self._title,
                                                                          'pdf',
                                                                          True,
                                                                          self.account.get_oxnote_home_folder_path()))

        synchronization_state['preview_files'][self.filename] = SingleQuotedScalarString(preview_filename)

        pdf_printer = QPrinter(QPrinter.ScreenResolution)
        pdf_printer.setOutputFormat(QPrinter.PdfFormat)
        pdf_printer.setPaperSize(QPrinter.Letter)
        pdf_printer.setPageMargins(0.56, 0.56, 0.56, 0.56, QPrinter.Inch)
        pdf_printer.setOutputFileName(preview_filename)

        pdf_paper_size = QSizeF()
        pdf_paper_size.setWidth(pdf_printer.width())
        pdf_paper_size.setHeight(pdf_printer.height())

        pdf_document: QTextDocument = QTextDocument()
        pdf_cursor: QTextCursor = QTextCursor(pdf_document)
        pdf_cursor.movePosition(QTextCursor.Start)
        pdf_cursor.insertHtml('<h1>{}</h1><hr><br>'.format(self._title))
        pdf_cursor.movePosition(QTextCursor.End)
        pdf_cursor.insertHtml(self.html_content)

        pdf_document.setMetaInformation(QTextDocument.DocumentTitle, self._title)
        pdf_document.setPageSize(pdf_paper_size)

        pdf_document.print(pdf_printer)

        self.__save_synchronization_state(synchronization_state)

    def __get_last_modified_timestamp(self):
        logger.debug('Getting last modified timestamp from note file: {}'.format(self._file))

        if sys.platform.startswith('win32'):
            return os.path.getmtime(self._file)
        else:
            return os.stat(self._file).st_mtime

    def __load_synchronization_state(self) -> typing.Dict:
        synchronization_state = CommentedMap()
        if os.path.isfile(self.account.get_synchronization_statefile()):
            with open(self.account.get_synchronization_statefile(), 'r') as f:
                synchronization_state = ruamel.yaml.round_trip_load(f, preserve_quotes=True)

        if 'version' not in synchronization_state:
            synchronization_state['version'] = 1.2
        if 'preview_files' not in synchronization_state:
            synchronization_state['preview_files'] = CommentedMap()

        return synchronization_state

    def __save_synchronization_state(self, synchronization_state: typing.Dict):
        with open(self.account.get_synchronization_statefile(), 'w') as f:
            ruamel.yaml.round_trip_dump(synchronization_state, f, default_flow_style=False)

    def __update_note_list_preview_image(self):
        match = re.search('src=\"data:image\/([a-zA-Z]*);base64,([^\"]*)\"', self._document.toHtml(), re.M)

        self._note_list_preview_image = match[2] if match else None
