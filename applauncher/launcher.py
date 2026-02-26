#!/usr/bin/env python3
#
# A simple application launcher
#
import applauncher.entry
import subprocess

class ApplicationLauncher:

    def launch(self, entry):
        return subprocess.run(entry.execute)
