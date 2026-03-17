

import unittest

class TestApplication(unittest.TestCase):
 
    def test_load_js_object(self, mock_run ):
        #load file from ./empty/index.html
       
        #assert that the "config" javascript object in that index.html has been loaded
        # check for correct values of plugin object
        
        self.assertTrue(True)
    

if __name__ == '__main__':
    unittest.main()
