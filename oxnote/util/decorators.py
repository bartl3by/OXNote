#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


def requires_cursor(fn):
    def decorator(instance, *args, **kwargs):
        if hasattr(instance, 'text_edit_editor') and instance.text_edit_editor.textCursor():
            return fn(instance, *args, **kwargs)
    return decorator

def requires_note_selection(fn):
    def decorator(instance, *args, **kwargs):
        if hasattr(instance, 'list_widget_notelist'):
            if instance.list_widget_notelist.count() <= 0 or instance.list_widget_notelist.currentRow() < 0:
                return
        return fn(instance, *args, **kwargs)
    return decorator
