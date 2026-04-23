#!/usr/bin/env python3
#
# A simple application launcher
#
from applauncher.entry import Entry
import subprocess

class ApplicationLauncher:

    def launch(self, entry):
        if (type(entry) is Entry):
            return subprocess.run(entry.execute)
        elif (type(entry is dict)):
            return subprocess.run(entry["execute"])
