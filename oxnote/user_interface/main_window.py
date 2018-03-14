#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import partial
import logging
import os

from PyQt5 import QtGui, QtPrintSupport, QtWidgets
from PyQt5.QtCore import QDir, QMimeData, QPoint, QSize, QUrl, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import (QColor, QFont, QIcon, QImage, QResizeEvent, QTextCharFormat, QTextCursor, QTextDocument,
                         QTextFrameFormat, QTextLength)
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFileDialog, QFontDialog, QListWidgetItem,
                             QMainWindow, QMessageBox, QSystemTrayIcon)
from PyQt5.uic import loadUi
import qtawesome as qta

from appsuite_api_wrapper.models.drive_extended_action import DriveExtendedAction
from appsuite_api_wrapper.types import SynchronizationActionType
from appsuite_api_wrapper.util import Util
from models.accounts import AccountManager
from models.note import Note
from threads.synchronization_daemon import SynchronizationDaemon
from user_interface.notes_list_widget_item import NotesListWidgetItemWidget, SortableListWidgetItem
from util.configuration import Configuration
from util.decorators import requires_cursor, requires_note_selection
from util.environment import Environment

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    DETAIL_WIDGET_INDEX_NOTES = 0
    DETAIL_WIDGET_INDEX_TRASH = 1
    DETAIL_WIDGET_INDEX_SHARED = 2
    DETAIL_WIDGET_INDEX_HELP = 3

    signal_account_broken = pyqtSignal()
    signal_editor_content_changed = pyqtSignal()
    signal_note_updated = pyqtSignal(str, str, str, int, DriveExtendedAction)
    signal_notify = pyqtSignal(str, str)
    signal_statusbar_message = pyqtSignal(str)

    def __init__(self, *args):
        '''
        ..todo:: Remove unnecessary fonts.
        ..todo:: qtawesome seems to create lag during window resizing, investigate.
        '''

        QMainWindow.__init__(self, *args)

        loadUi(os.path.join(Environment.get_resource_path(), 'designs/default/main_window.ui'), self)

        if os.path.isfile(os.path.join(Environment.get_resource_path(), 'designs/default/main_window.qss')):
            with open(os.path.join(Environment.get_resource_path(), 'designs/default/main_window.qss'), "r") as f:
                self.setStyleSheet(f.read())

        self._account_manager = AccountManager()

        self._synchronization_daemon = SynchronizationDaemon()
        self._synchronization_daemon.signal_synchronization_started.connect(self.notes_synchronization_initiated)
        self._synchronization_daemon.signal_synchronization_status_update.connect(self.statusbar_message)
        self._synchronization_daemon.signal_synchronization_note_updated.connect(self.signal_note_updated)
        self._synchronization_daemon.signal_synchronization_finished.connect(self.notes_synchronization_finished)
        self._synchronization_daemon.enable()

        self.__load_fonts()
        self.__set_icons()

        self.stacked_widget_detail.setCurrentIndex(self.DETAIL_WIDGET_INDEX_NOTES)

        self.__connect_signals()

        self.__initialize_notes_list()

        self._synchronization_daemon.synchronize()

    def __connect_signals(self):
        logger.debug('Connecting {} signals'.format(__name__))

        '''
        Application
        '''
        self.signal_account_broken.connect(self.account_broken)
        self.signal_note_updated.connect(self.note_updated)

        self.text_edit_editor.textChanged.connect(self.signal_editor_content_changed)
        self.line_edit_subject.textChanged.connect(self.signal_editor_content_changed)
        self.signal_editor_content_changed.connect(self.editor_content_changed)

        self.splitter_detail_edit.splitterMoved.connect(
            partial(self.resizeEvent, QResizeEvent(self.size(), self.size())))

        '''
        Status Messaging
        '''
        self.signal_notify.connect(self.system_notify)
        self.signal_statusbar_message.connect(self.statusbar_message)

        '''
        System Tray
        '''
        self.tray_icon.activated.connect(self.raise_)

        '''
        Menu Bar
        '''
        self.action_sync.triggered.connect(self._synchronization_daemon.signal_synchronization_synchronize)
        self.action_undo.triggered.connect(self.text_edit_editor.undo)
        self.action_redo.triggered.connect(self.text_edit_editor.redo)
        self.action_cut.triggered.connect(self.text_edit_editor.cut)
        self.action_copy.triggered.connect(self.text_edit_editor.copy)
        self.action_paste.triggered.connect(self.text_edit_editor.paste)
        self.action_select_all.triggered.connect(self.text_edit_editor.selectAll)

        self.action_increase_indent.triggered.connect(self.tool_button_editor_indent.released)
        self.action_decrease_indent.triggered.connect(self.tool_button_editor_outdent.released)

        self.action_increase_list_indent_level.triggered.connect(self.tool_button_editor_indent.released)
        self.action_decrease_list_indent_level.triggered.connect(self.tool_button_editor_outdent.released)

        self.tool_button_editor_bold.released.connect(self.on_action_bold_triggered)
        self.tool_button_editor_italic.released.connect(self.on_action_italic_triggered)
        self.tool_button_editor_underline.released.connect(self.on_action_underline_triggered)

        '''
        Tool Bar - Top
        '''
        self.tool_button_toolbar_top_sync.released.connect(
                self._synchronization_daemon.signal_synchronization_synchronize)

        '''
        Editor Toolbar - Bottom
        '''
        self.tool_button_editor_trash.released.connect(partial(self.action_delete_note.triggered.emit, False))

    def __load_fonts(self):
        qta.load_font('far', 'fa-regular-400.ttf', 'charmap.json',
                      directory=os.path.join(Environment.get_resource_path(), 'fonts'))
        qta.load_font('fas', 'fa-solid-900.ttf', 'charmap.json',
                      directory=os.path.join(Environment.get_resource_path(), 'fonts'))
        qta.load_font('fab', 'fa-brands-400.ttf', 'charmap.json',
                      directory=os.path.join(Environment.get_resource_path(), 'fonts'))

    def __set_icons(self):
        if not QtWidgets.QSystemTrayIcon.isSystemTrayAvailable():
            logger.error('System Tray is not accessible')
        else:
            self.tray_icon = QSystemTrayIcon(QIcon(os.path.join(Environment.get_resource_path(),
                                                                'designs/default/OXNoteTray.icns')))
            self.tray_icon.show()

        self.tool_button_toolbar_top_sync.setIcon(qta.icon('fa.refresh', color='lightgrey'))

        self.tool_button_toolbar_left_notes.setIcon(qta.icon('fa.clipboard', color='lightgrey'))
        self.tool_button_toolbar_left_trash.setIcon(qta.icon('fa.trash', color='lightgrey'))
        self.tool_button_toolbar_left_shared.setIcon(qta.icon('fa.share-alt', color='lightgrey'))
        self.tool_button_toolbar_left_toggle.setIcon(qta.icon('fa.angle-double-left', color='lightgrey'))

        self.tool_button_editor_bold.setIcon(qta.icon('fa.bold'))
        self.tool_button_editor_italic.setIcon(qta.icon('fa.italic'))
        self.tool_button_editor_underline.setIcon(qta.icon('fa.underline'))
        self.tool_button_editor_color.setIcon(qta.icon('fa.tint'))
        self.tool_button_editor_bullet_list.setIcon(qta.icon('fa.list-ul'))
        self.tool_button_editor_numbered_list.setIcon(qta.icon('fa.list-ol'))
        self.tool_button_editor_outdent.setIcon(qta.icon('fa.outdent'))
        self.tool_button_editor_indent.setIcon(qta.icon('fa.indent'))
        self.tool_button_editor_tags.setIcon(qta.icon('fa.tags'))
        self.tool_button_editor_sharing.setIcon(qta.icon('fa.cloud-upload'))
        self.tool_button_editor_information.setIcon(qta.icon('fa.info'))
        self.tool_button_editor_trash.setIcon(qta.icon('fas.trash-alt'))

    def __initialize_notes_list(self):
        accounts_to_process = self._account_manager.list_accounts()

        self.line_edit_subject.setModified(False)
        self.line_edit_subject.clear()
        self.text_edit_editor.document().setModified(False)
        self.text_edit_editor.clear()

        for current_account_id in accounts_to_process:
            current_account = self._account_manager.get_account(current_account_id)
            for filename in os.listdir(current_account.get_application_data_folder_path()):
                if filename.endswith('.oxn'):
                    self.__load_note_to_list(current_account_id,
                                             os.path.join(current_account.get_application_data_folder_path(), filename),
                                             False)

        self.__refresh_notes_list()

    def __load_note_to_list(self, account_id: str, file: str, refresh_list: bool = True):
        logger.debug('(Re)loading note from account {} to the note list: {}'.format(account_id, file))

        list_item = None
        list_item_widget = None

        list = self.list_widget_notelist.findItems(file, Qt.MatchExactly)
        if len(list) == 1:
            list_item = list[0]
            list_item_widget = self.list_widget_notelist.itemWidget(list_item)
        elif len(list) > 1:
            logger.warning('Found multiple widgets for filename \'{}\''.format(file))
            return

        if not list_item or not list_item.text() or len(list_item.text()) <= 0:
            list_item_widget = NotesListWidgetItemWidget(filename=file, checksum=Util.calculate_file_checksum(file))

            list_item = SortableListWidgetItem(Note(account_id=account_id, file=file))
            list_item.setSizeHint(QSize(self.list_widget_notelist.width(), list_item_widget.height()))
            list_item.setFont(QFont())

            self.list_widget_notelist.addItem(list_item)
            self.list_widget_notelist.setItemWidget(list_item, list_item_widget)

        list_item_widget.set_title(list_item.note.title)
        list_item_widget.set_preview_text(list_item.note.document.toPlainText()[:Configuration().get_setting(
                'oxnote',
                'application.settings.preview_content_length_maximum',
                default=200)])
        list_item_widget.set_icon(list_item.note.note_list_preview_image)

        list_item.setText(file)

        if refresh_list:
            self.__refresh_notes_list()

    def __remove_note_from_list(self, account_id: str, file: str):
        logger.debug('Removing note from account {} from the note list: {}'.format(account_id, file))

        list = self.list_widget_notelist.findItems(file, Qt.MatchExactly)
        if len(list) <= 0:
            return
        if len(list) > 1:
            logger.warning('Found multiple widgets for filename \'{}\''.format(file))

        self.list_widget_notelist.removeItemWidget(list[0])
        self.list_widget_notelist.takeItem(self.list_widget_notelist.row(list[0]))

        self.__refresh_notes_list()

    def __refresh_notes_list(self):
        logger.debug('Refreshing note list')

        self.list_widget_notelist.sortItems(Qt.DescendingOrder)

        if self.list_widget_notelist.count() >= 0 and self.list_widget_notelist.currentRow() < 0:
            self.list_widget_notelist.setCurrentRow(0)

        self.list_widget_notelist.scrollToItem(self.list_widget_notelist.currentItem(), QAbstractItemView.EnsureVisible)

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)

        for position in range(0, self.list_widget_notelist.count()):
            self.list_widget_notelist.item(position).setSizeHint(QSize(self.list_widget_notelist.width(),
                                                                       self.list_widget_notelist.itemWidget(
                                                                               self.list_widget_notelist.item(
                                                                                       position)).maximumHeight()))

    '''
    Menubar Events
    '''
    @pyqtSlot(name='on_action_about_oxnote_triggered')
    def on_action_about_oxnote_triggered(self):
        QMessageBox.information(None, None, 'About', QMessageBox.StandardButton(QMessageBox.Ok))

    @pyqtSlot(name='on_action_new_note_triggered')
    def on_action_new_note_triggered(self):
        '''
        ..todo: Add multi account support - Select target account for new notes
        '''
        if self.list_widget_notelist.currentRow() >= 0 and\
                (self.line_edit_subject.isModified() or self.text_edit_editor.document().isModified()):
            self.on_action_save_note_triggered()

        note = Note(account_id=self._account_manager.get_account(self._account_manager.list_accounts()[0]).id,
                    title='New Note')

        if not self.list_widget_notelist.currentItem() and self.list_widget_notelist.count() <= 0:
            if self.line_edit_subject.isModified() and len(self.line_edit_subject.text().strip()) > 0:
                note.title = self.line_edit_subject.text()
            if self.text_edit_editor.document().isModified() and len(
                    self.text_edit_editor.document().toPlainText().strip()) > 0:
                note.html_content = self.text_edit_editor.document().toHtml()

        note.create()

        self.__load_note_to_list(note.account_id, note.file)

        self.list_widget_notelist.setCurrentRow(0)

    @pyqtSlot(name='on_action_save_note_triggered')
    def on_action_save_note_triggered(self):
        if self.list_widget_notelist.count() <= 0 or self.list_widget_notelist.currentRow() < 0:
            self.action_new_note.triggered.emit()
            return

        if not self.line_edit_subject.isModified() and not self.text_edit_editor.document().isModified():
            return

        self.list_widget_notelist.currentItem().note.title = self.line_edit_subject.text()
        self.list_widget_notelist.currentItem().note.html_content = self.text_edit_editor.toHtml()

        self.line_edit_subject.setModified(False)
        self.text_edit_editor.document().setModified(False)

        self.list_widget_notelist.currentItem().note.save()

        self.__load_note_to_list(self.list_widget_notelist.currentItem().note.account_id,
                                 self.list_widget_notelist.currentItem().note.file)

        self.__refresh_notes_list()

    @pyqtSlot(name='on_action_delete_note_triggered')
    @requires_note_selection
    def on_action_delete_note_triggered(self):
        logger.debug('Deleting note {}'.format(self.list_widget_notelist.currentItem().note.file))

        note = self.list_widget_notelist.currentItem().note

        note.delete()

        self.__remove_note_from_list(note.account_id, note.file)

    @pyqtSlot(name='on_action_account_settings_triggered')
    def on_action_account_settings_triggered(self):
        pass

    @pyqtSlot(name='on_action_preview_triggered')
    def on_action_preview_triggered(self):
        preview = QtPrintSupport.QPrintPreviewDialog()

        preview_document: QTextDocument = QTextDocument()
        preview_cursor: QTextCursor = QTextCursor(preview_document)
        preview_cursor.movePosition(QTextCursor.Start)
        preview_cursor.insertHtml('<h1>{}</h1><hr>'.format(self.line_edit_subject.text()))
        preview_cursor.movePosition(QTextCursor.End)
        preview_cursor.insertHtml(self.text_edit_editor.document().toHtml())

        preview.paintRequested.connect(lambda printer: preview_document.print(printer))
        preview.exec()

    @pyqtSlot(name='on_action_print_note_triggered')
    def on_action_print_note_triggered(self):
        print_dialog = QtPrintSupport.QPrintDialog()
        if print_dialog.exec() == QDialog.Accepted:
            print_document: QTextDocument = QTextDocument()
            print_cursor: QTextCursor = QTextCursor(print_document)
            print_cursor.movePosition(QTextCursor.Start)
            print_cursor.insertHtml('<h1>{}</h1><hr>'.format(self.line_edit_subject.text()))
            print_cursor.movePosition(QTextCursor.End)
            print_cursor.insertHtml(self.text_edit_editor.document().toHtml())

            print_document.print(print_dialog.printer())

    @pyqtSlot(name='on_action_edit_note_title_triggered')
    def on_action_edit_note_title_triggered(self):
        pass

    @pyqtSlot(name='on_action_duplicate_note_triggered')
    @requires_note_selection
    def on_action_duplicate_note_triggered(self):
        if self.line_edit_subject.isModified() or self.text_edit_editor.document().isModified():
            self.on_action_save_note_triggered()

        note = Note(account_id=self._account_manager.get_account(self._account_manager.list_accounts()[0]).id,
                    title='{} (Copy)'.format(self.line_edit_subject.text()),
                    html_content=self.text_edit_editor.toHtml())

        note.create()

        self.__load_note_to_list(note.account_id, note.file)

        self.list_widget_notelist.setCurrentRow(0)

    @pyqtSlot(name='on_action_paste_as_plain_text_triggered')
    def on_action_paste_as_plain_text_triggered(self):
        self.text_edit_editor.insertFromMimeData(QApplication.clipboard().mimeData(), True)

    @pyqtSlot(name='on_action_insert_image_triggered')
    def on_action_insert_image_triggered(self):
        filename = QFileDialog.getOpenFileName(self, 'Insert image', QDir.homePath(), 'Images ({})'.format(
            ' '.join(map('*.{}'.format, self.text_edit_editor.supported_image_formats))))[0]

        if not filename:
            return

        if not os.path.isfile(filename) or QImage(filename).isNull():
            QMessageBox.critical(None, None, 'Could\'t open Image', QMessageBox.StandardButton(QMessageBox.Ok))
        else:
            filename_mime_data: QMimeData = QMimeData()
            filename_mime_data.setUrls([QUrl().fromUserInput(filename)])

            self.text_edit_editor.insertFromMimeData(filename_mime_data)

    @pyqtSlot(name='on_action_fonts_triggered')
    def on_action_fonts_triggered(self):
        selected_font, action = QFontDialog.getFont()
        if action:
            self.text_edit_editor.setCurrentFont(selected_font)

    @pyqtSlot(name='on_action_colors_triggered')
    def on_action_colors_triggered(self):
        self.tool_button_editor_color.released.emit()

    @pyqtSlot(name='on_action_align_left_triggered')
    def on_action_align_left_triggered(self):
        self.text_edit_editor.setAlignment(Qt.AlignLeft)

    @pyqtSlot(name='on_action_align_center_triggered')
    def on_action_align_center_triggered(self):
        self.text_edit_editor.setAlignment(Qt.AlignCenter)

    @pyqtSlot(name='on_action_align_justify_triggered')
    def on_action_align_justify_triggered(self):
        self.text_edit_editor.setAlignment(Qt.AlignJustify)

    @pyqtSlot(name='on_action_align_right_triggered')
    def on_action_align_right_triggered(self):
        self.text_edit_editor.setAlignment(Qt.AlignRight)

    @pyqtSlot(name='on_action_toggle_list_triggered')
    def on_action_toggle_list_triggered(self):
        cursor = self.text_edit_editor.textCursor()

        selection_start = cursor.selectionStart() if cursor.hasSelection() else cursor.position()
        if cursor.hasSelection():
            cursor.setPosition(cursor.selectionEnd())
            selection_end = cursor.position()
        else:
            selection_end = selection_start

        cursor.setPosition(selection_start)

        while cursor.position() <= selection_end:
            cursor.movePosition(QTextCursor.StartOfLine)

            if cursor.currentList():
                listFormat = cursor.currentList().format()
                listFormat.setIndent(0)
                cursor.createList(listFormat)
                cursor.currentList().remove(cursor.block())
            else:
                cursor.createList(QtGui.QTextListFormat.ListDisc)

            if not cursor.movePosition(QTextCursor.Down):
                break

    @pyqtSlot(name='on_action_toggle_list_type_triggered')
    def on_action_toggle_list_type_triggered(self):
        cursor = self.text_edit_editor.textCursor()

        selection_start = cursor.selectionStart() if cursor.hasSelection() else cursor.position()
        if cursor.hasSelection():
            cursor.setPosition(cursor.selectionEnd())
            selection_end = cursor.position()
        else:
            selection_end = selection_start

        cursor.setPosition(selection_start)

        while cursor.position() <= selection_end:
            cursor.movePosition(QTextCursor.StartOfLine)

            if cursor.currentList():
                if cursor.currentList().format().style() == QtGui.QTextListFormat.ListDisc:
                    cursor.createList(QtGui.QTextListFormat.ListDecimal)
                elif cursor.currentList().format().style() == QtGui.QTextListFormat.ListDecimal:
                    cursor.createList(QtGui.QTextListFormat.ListDisc)

            if not cursor.movePosition(QTextCursor.Down):
                break

    @pyqtSlot(name='on_action_insert_table_triggered')
    def on_action_insert_table_triggered(self):
        table_format = QtGui.QTextTableFormat()
        table_format.setCellPadding(5)
        table_format.setCellSpacing(-1)
        table_format.setTopMargin(5)
        table_format.setBottomMargin(5)
        table_format.setHeaderRowCount(1)
        table_format.setColumnWidthConstraints([QTextLength(QTextLength.PercentageLength, 20),
                                                QTextLength(QTextLength.PercentageLength, 20),
                                                QTextLength(QTextLength.PercentageLength, 20)])
        table_format.setBorder(1)

        table_format.setBorderBrush(Qt.darkGray)
        table_format.setBorderStyle(QTextFrameFormat.BorderStyle_Solid)

        self.text_edit_editor.textCursor().insertTable(3, 3, table_format)

    @pyqtSlot(name='on_action_insert_row_above_triggered')
    def on_action_insert_row_above_triggered(self):
        if self.text_edit_editor.textCursor().currentTable():
            self.text_edit_editor.textCursor().currentTable().insertRows(
                self.text_edit_editor.textCursor().currentTable().cellAt(self.text_edit_editor.textCursor()).row(), 1)

    @pyqtSlot(name='on_action_insert_row_below_triggered')
    def on_action_insert_row_below_triggered(self):
        if self.text_edit_editor.textCursor().currentTable():
            self.text_edit_editor.textCursor().currentTable().insertRows(
                self.text_edit_editor.textCursor().currentTable().cellAt(self.text_edit_editor.textCursor()).row() + 1,
                1)

    @pyqtSlot(name='on_action_insert_column_left_triggered')
    def on_action_insert_column_left_triggered(self):
        if self.text_edit_editor.textCursor().currentTable():
            self.text_edit_editor.textCursor().currentTable().insertColumns(
                self.text_edit_editor.textCursor().currentTable().cellAt(self.text_edit_editor.textCursor()).column(),
                1)

    @pyqtSlot(name='on_action_insert_column_right_triggered')
    def on_action_insert_column_right_triggered(self):
        if self.text_edit_editor.textCursor().currentTable():
            self.text_edit_editor.textCursor().currentTable().insertColumns(
                self.text_edit_editor.textCursor().currentTable().cellAt(
                    self.text_edit_editor.textCursor()).column() + 1, 1)

    @pyqtSlot(name='on_action_delete_row_triggered')
    def on_action_delete_row_triggered(self):
        if self.text_edit_editor.textCursor().currentTable():
            self.text_edit_editor.textCursor().currentTable().removeRows(
                self.text_edit_editor.textCursor().currentTable().cellAt(self.text_edit_editor.textCursor()).row(), 1)

    @pyqtSlot(name='on_action_delete_column_triggered')
    def on_action_delete_column_triggered(self):
        if self.text_edit_editor.textCursor().currentTable():
            self.text_edit_editor.textCursor().currentTable().removeColumns(
                self.text_edit_editor.textCursor().currentTable().cellAt(self.text_edit_editor.textCursor()).column(),
                1)

    @pyqtSlot(name='on_action_bold_triggered')
    def on_action_bold_triggered(self):
        self.text_edit_editor.setFontWeight(
            QFont.Normal) if self.text_edit_editor.fontWeight() == QFont.Bold else self.text_edit_editor.setFontWeight(
            QFont.Bold)

    @pyqtSlot(name='on_action_italic_triggered')
    def on_action_italic_triggered(self):
        self.text_edit_editor.setFontItalic(not self.text_edit_editor.fontItalic())

    @pyqtSlot(name='on_action_underline_triggered')
    def on_action_underline_triggered(self):
        self.text_edit_editor.setFontUnderline(not self.text_edit_editor.fontUnderline())

    @pyqtSlot(name='on_action_strikethrough_triggered')
    def on_action_strikethrough_triggered(self):
        format: QTextCharFormat = self.text_edit_editor.currentCharFormat()
        format.setFontStrikeOut(not self.text_edit_editor.currentCharFormat().fontStrikeOut())
        self.text_edit_editor.setCurrentCharFormat(format)

    @pyqtSlot(name='on_action_highlight_triggered')
    def on_action_highlight_triggered(self):
        if self.text_edit_editor.textBackgroundColor() == QColor(Qt.yellow):
            self.text_edit_editor.setTextBackgroundColor(self.text_edit_editor.palette().base().color())
        else:
            self.text_edit_editor.setTextBackgroundColor(Qt.yellow)

    @pyqtSlot(name='on_action_superscript_triggered')
    def on_action_superscript_triggered(self):
        format = self.text_edit_editor.currentCharFormat()

        if not format.verticalAlignment() == QTextCharFormat.AlignSuperScript:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
        else:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.text_edit_editor.setCurrentCharFormat(format)

    @pyqtSlot(name='on_action_subscript_triggered')
    def on_action_subscript_triggered(self):
        format = self.text_edit_editor.currentCharFormat()

        if not format.verticalAlignment() == QTextCharFormat.AlignSubScript:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
        else:
            format.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        self.text_edit_editor.setCurrentCharFormat(format)

    @pyqtSlot(name='on_action_bigger_triggered')
    def on_action_bigger_triggered(self):
        self.text_edit_editor.setFontPointSize(self.text_edit_editor.fontPointSize() + 1)

    @pyqtSlot(name='on_action_smaller_triggered')
    def on_action_smaller_triggered(self):
        self.text_edit_editor.setFontPointSize(self.text_edit_editor.fontPointSize() - 1)

    @pyqtSlot(name='on_action_clear_styles_triggered')
    def on_action_clear_styles_triggered(self):
        self.text_edit_editor.setCurrentCharFormat(QTextCharFormat())

    @pyqtSlot(name='on_action_remove_all_formatting_triggered')
    def on_action_remove_all_formatting_triggered(self):
        cursor = self.text_edit_editor.textCursor()
        cursor.select(QTextCursor.Document)
        cursor.setCharFormat(QTextCharFormat())
        cursor.clearSelection()
        self.text_edit_editor.setTextCursor(cursor)

    '''
    Toolbar Left Events
    '''

    def on_tool_button_toolbar_left_notes_released(self):
        self.stacked_widget_detail.setCurrentIndex(self.DETAIL_WIDGET_INDEX_NOTES)

    def on_tool_button_toolbar_left_trash_released(self):
        pass

    def on_tool_button_toolbar_left_shared_released(self):
        '''
        self.stackedWidgetDetail.setCurrentIndex(self.DETAIL_WIDGET_INDEX_SHARED)
        if self.widgetNoteslist.isVisible():
            self.widgetNoteslist.setEnabled(False)
            self.widgetNoteslist.hide()
        else:
            self.widgetNoteslist.setEnabled(True)
            self.widgetNoteslist.show()
        '''

        pass

    def on_tool_button_toolbar_left_toggle_released(self):
        self.list_widget_notelist.setVisible(not self.list_widget_notelist.isVisible())

        if self.list_widget_notelist.isVisible():
            self.tool_button_toolbar_left_toggle.setIcon(qta.icon('fa.angle-double-left', color='lightgrey'))
        else:
            self.tool_button_toolbar_left_toggle.setIcon(qta.icon('fa.angle-double-right', color='lightgrey'))

    '''
    Note List Events
    '''

    @pyqtSlot(QListWidgetItem, QListWidgetItem, name='on_list_widget_notelist_currentItemChanged')
    def on_list_widget_notelist_currentItemChanged(self,
                                                   current: SortableListWidgetItem,
                                                   previous: SortableListWidgetItem):
        if previous and self.list_widget_notelist.itemWidget(previous):
            if (self.line_edit_subject.isModified() and self.line_edit_subject.text() != previous.note.title)\
                    or self.text_edit_editor.document().isModified():
                previous.note.title = self.line_edit_subject.text()
                previous.note.html_content = self.text_edit_editor.toHtml()

                previous.note.save()

                self.line_edit_subject.setModified(False)
                self.text_edit_editor.document().setModified(False)

                self.__load_note_to_list(previous.note.account_id, previous.note.file)

        if previous and not current:
            self.line_edit_subject.setModified(False)
            self.line_edit_subject.clear()
            self.text_edit_editor.document().setModified(False)
            self.text_edit_editor.clear()

        if current:
            logger.debug('Loading {} into editor view'.format(current.note.file))

            self.line_edit_subject.setModified(False)
            self.text_edit_editor.document().setModified(False)
            self.line_edit_subject.setText(current.note.title)
            self.text_edit_editor.setHtml(current.note.html_content)

    '''
    Editor Toolbar Top Events
    '''

    def on_tool_button_editor_tags_released(self):
        pass

    '''
    Editor Events
    '''

    def on_tool_button_editor_sharing_released(self):
        pass

    def on_tool_button_editor_information_released(self):
        pass

    def on_tool_button_editor_color_released(self):
        self.text_edit_editor.setTextColor(QtWidgets.QColorDialog.getColor())

    def on_tool_button_editor_bullet_list_released(self):
        self.text_edit_editor.textCursor().createList(QtGui.QTextListFormat.ListDisc)

    def on_tool_button_editor_numbered_list_released(self):
        self.text_edit_editor.textCursor().createList(QtGui.QTextListFormat.ListDecimal)

    @pyqtSlot(int, name='on_spin_box_font_size_valueChanged')
    def on_spin_box_font_size_valueChanged(self, value):
        self.text_edit_editor.setFontPointSize(value)

    def on_font_combo_box_editor_currentFontChanged(self):
        self.text_edit_editor.setCurrentFont(self.font_combo_box_editor.currentFont())

    @requires_cursor
    def on_tool_button_editor_indent_released(self):
        cursor = self.text_edit_editor.textCursor()

        selection_start = cursor.selectionStart() if cursor.hasSelection() else cursor.position()
        if cursor.hasSelection():
            cursor.setPosition(cursor.selectionEnd())
            selection_end = cursor.position()
        else:
            selection_end = selection_start

        cursor.setPosition(selection_start)

        while cursor.position() <= selection_end:
            cursor.movePosition(QTextCursor.StartOfLine)

            if cursor.currentList():
                listFormat = cursor.currentList().format()
                listFormat.setIndent(listFormat.indent() + 1)
                cursor.createList(listFormat)
            else:
                cursor.insertText('\t')
                selection_end += len('\t')

            if not cursor.movePosition(QTextCursor.Down):
                break

    def on_tool_button_editor_outdent_released(self):
        cursor = self.text_edit_editor.textCursor()

        selection_start = cursor.selectionStart() if cursor.hasSelection() else cursor.position()
        if cursor.hasSelection():
            cursor.setPosition(cursor.selectionEnd())
            selection_end = cursor.position()
        else:
            selection_end = selection_start

        cursor.setPosition(selection_start)

        while cursor.position() <= selection_end:
            cursor.movePosition(QTextCursor.StartOfLine)

            if cursor.currentList():
                listFormat = cursor.currentList().format()

                if listFormat.indent() <= 0:
                    cursor.currentList().remove(cursor.block())
                else:
                    listFormat.setIndent(listFormat.indent() - 1)
                    cursor.createList(listFormat)
            else:
                if cursor.block().text().startswith("\t"):
                    cursor.deleteChar()
                else:
                    for char in cursor.block().text()[:4]:
                        if char != ' ':
                            break

                        cursor.deleteChar()

            if not cursor.movePosition(QTextCursor.Down):
                break

    '''
    Context Menus
    '''

    @pyqtSlot(QPoint, name='on_list_widget_notelist_customContextMenuRequested')
    def on_list_widget_notelist_customContextMenuRequested(self, position: QPoint):
        pass

    '''
    Application Events
    '''

    def account_broken(self):
        self.tray_icon.showMessage("Account Problem", 'Please verify your account information', 5000)

    @pyqtSlot(name='editor_content_changed')
    def editor_content_changed(self):
        pass

    @pyqtSlot(str, str, str, int, DriveExtendedAction, name='note_updated')
    def note_updated(self, account_id: str, file: str, directory: str, synchronization_action_type: int,
                     drive_extended_action: DriveExtendedAction):
        if not file.endswith('.oxn') and synchronization_action_type != SynchronizationActionType.Rename:
            return

        logger.debug('Received note event signal: {}'.format(file))

        if synchronization_action_type == SynchronizationActionType.Acknowledge:
            pass
        elif synchronization_action_type == SynchronizationActionType.New:
            self.signal_statusbar_message.emit('Downloaded new note from server: {}'.format(file))
            self.__load_note_to_list(account_id, file)
        elif synchronization_action_type == SynchronizationActionType.Rename:
            self.signal_statusbar_message.emit('Note {} has been renamed on server'.format(file))
            file_old = os.path.join(self._account_manager.get_account(account_id).get_account_root_directory_path(),
                                    directory,
                                    drive_extended_action.version.name)
            file_new = os.path.join(self._account_manager.get_account(account_id).get_account_root_directory_path(),
                                    directory,
                                    drive_extended_action.new_version.name)

            if file_old.endswith('.oxn') and file_new.endswith('.oxn'):
                self.__remove_note_from_list(account_id, file_old)
                self.__load_note_to_list(account_id, file_new)
            if file_old.endswith('.oxn') and not file_new.endswith('.oxn'):
                self.__remove_note_from_list(account_id, file_old)
            if not file_old.endswith('.oxn') and file_new.endswith('.oxn'):
                self.__load_note_to_list(account_id, file_new)
        elif synchronization_action_type == SynchronizationActionType.Download:
            self.signal_statusbar_message.emit('Downloaded note from server: {}'.format(file))
            self.__load_note_to_list(account_id, file)
        elif synchronization_action_type == SynchronizationActionType.Upload:
            self.signal_statusbar_message.emit('Uploaded note to server: {}'.format(file))
        elif synchronization_action_type == SynchronizationActionType.Remove:
            self.signal_statusbar_message.emit('Note has been removed from server: {}'.format(file))
            self.__remove_note_from_list(account_id, file)

    @pyqtSlot(str, str, name='system_notify')
    def system_notify(self, title: str, message: str):
        assert isinstance(title, str)
        assert isinstance(message, str)
        self.tray_icon.showMessage(title, message, 5000)

    @pyqtSlot(str, name='statusbar_message')
    def statusbar_message(self, message):
        assert isinstance(message, str)
        self.status_bar.showMessage(message, 5000)

    def notes_synchronization_initiated(self):
        self.signal_statusbar_message.emit('Synchronizing with server')
        self.tool_button_toolbar_top_sync.setIcon(qta.icon('fa.refresh',
                                                           color='steelblue',
                                                           animation=qta.Spin(self.tool_button_toolbar_top_sync)))

    @pyqtSlot(name='notes_synchronization_finished')
    def notes_synchronization_finished(self):
        self.signal_statusbar_message.emit('Synchronization finished')
        self.tool_button_toolbar_top_sync.setIcon(qta.icon('fa.refresh',
                                                           color='lightgrey'))

    def on_splitter_detail_edit_splitterMoved(self):
        for position in range(0, self.list_widget_notelist.count()):
            self.list_widget_notelist.item(position).setSizeHint(QSize(self.list_widget_notelist.width(),
                                                                       self.list_widget_notelist.itemWidget(
                                                                               self.list_widget_notelist.item(
                                                                                       position)).maximumHeight()))
