#!/usr/bin/env python3
"""Modules initialization file."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
