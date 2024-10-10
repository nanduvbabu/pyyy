#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro.settings")

    import django
    django.setup()

    # Override default port for `runserver` command
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_port = "8123"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
