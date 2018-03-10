#!/usr/bin/python3#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class SynchronizationActionType(object):
    Acknowledge = 0
    New = 1
    Rename = 2
    Download = 3
    Upload = 4
    Remove = 5
