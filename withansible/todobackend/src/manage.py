#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # shows which specific application settings allows to set specific application settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todobackend.settings.base")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
