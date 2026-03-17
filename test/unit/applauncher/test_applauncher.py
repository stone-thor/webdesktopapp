

import unittest
from applauncher.launcher import ApplicationLauncher
from applauncher.entry import Entry
from unittest.mock import patch

class TestAppLauncher(unittest.TestCase):
 
    @patch( 'subprocess.run' )
    def test_launch(self, mock_run ):
        notepadEntry = Entry( "Notepad", "notepad.exe" )
        launcher = ApplicationLauncher()
        launcher.launch(notepadEntry)
        mock_run.assert_called_with("notepad.exe")

if __name__ == '__main__':
    unittest.main()
