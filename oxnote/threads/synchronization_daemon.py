#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

from PyQt5.QtCore import QObject, QThread, QTimer, Qt, pyqtSignal

from appsuite_api_wrapper.models.drive_extended_action import DriveExtendedAction
from threads.synchronize_notes import SynchronizeNotesThreadWorker

logger = logging.getLogger(__name__)


class SynchronizationDaemon(QObject):
    signal_synchronization_synchronize = pyqtSignal()
    signal_synchronization_started = pyqtSignal()
    signal_synchronization_status_update = pyqtSignal(str)
    signal_synchronization_note_updated = pyqtSignal(str, str, str, int, DriveExtendedAction)
    signal_synchronization_finished = pyqtSignal()

    def __init__(self):
        super(SynchronizationDaemon, self).__init__()

        self.signal_synchronization_synchronize.connect(self.synchronize)

        self._synchronize_notes_thread_timer = QTimer()
        self._synchronize_notes_thread = QThread()
        self._synchronize_notes_thread_worker = SynchronizeNotesThreadWorker()

    def enable(self):
        if not self.enabled():
            self._synchronize_notes_thread_timer = QTimer()
            self._synchronize_notes_thread_timer.setTimerType(Qt.VeryCoarseTimer)
            self._synchronize_notes_thread_timer.setInterval(60000)
            self._synchronize_notes_thread_timer.timeout.connect(self.synchronize)
            self._synchronize_notes_thread_timer.start()

    def disable(self):
        if self.enabled():
            self._synchronize_notes_thread_timer.stop()
            if self.synchronizing() and self._synchronize_notes_thread_worker.receivers(
                    self._synchronize_notes_thread_worker.signal_restart_timer) > 0:
                self._synchronize_notes_thread_worker.signal_restart_timer.disconnect()

    def enabled(self) -> bool:
        return self._synchronize_notes_thread_timer.isActive()

    def synchronize(self):
        if not self.synchronizing():
            self._synchronize_notes_thread = QThread()
            self._synchronize_notes_thread_worker = SynchronizeNotesThreadWorker()

            self._synchronize_notes_thread.started.connect(self.signal_synchronization_started)
            self._synchronize_notes_thread.started.connect(self._synchronize_notes_thread_worker.run)
            self._synchronize_notes_thread_worker.signal_synchronization_finished.connect(self.signal_synchronization_finished)
            self._synchronize_notes_thread_worker.signal_synchronization_status_update.connect(self.signal_synchronization_status_update)
            self._synchronize_notes_thread_worker.signal_synchronization_note_updated.connect(self.signal_synchronization_note_updated)
            if self.enabled():
                self._synchronize_notes_thread_worker.signal_restart_timer.connect(self._synchronize_notes_thread_timer.start)
            self._synchronize_notes_thread_worker.signal_synchronization_finished.connect(self._synchronize_notes_thread.quit)

            self._synchronize_notes_thread_worker.moveToThread(self._synchronize_notes_thread)
            self._synchronize_notes_thread.start()

    def synchronizing(self) -> bool:
        return self._synchronize_notes_thread.isRunning()


