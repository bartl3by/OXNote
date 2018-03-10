#!/usr/bin/python3
# -*- coding: utf-8 -*-

import hashlib
import logging

logger = logging.getLogger(__name__)


class Util():

    @staticmethod
    def calculate_file_checksum(file: str) -> str:
        hash_md5 = hashlib.md5()
        with open(file, "rb") as f:
            for buffer in iter(lambda: f.read(4096), b""):
                hash_md5.update(buffer)
        return hash_md5.hexdigest()
