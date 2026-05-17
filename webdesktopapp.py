#!/usr/bin/env python3
#
# A Web Desktop Application
#
# use for panels, launchers, anything you want.

import Global

import sys
import os
import pprint

import webview
from webview.dom import DOMEventHandler

from util.sequence import containsMoreThanOne

from operator import itemgetter 

APP_PATH = os.path.dirname(os.path.realpath( __file__ ))
RESOURCE_DIR = "res"
INDEX_FILE_NAME = "index.html"

app = None

class App:
    
    def __init__(self, window, module_name, module_path, module_index):
        self.window = window
        
        self.module_name = module_name
        self.module_path = module_path
        self.module_index = module_index
        
        self.pageConfig = {}
        
        window.events.loaded += self._on_window_loaded
    
    def _getPageConfig(self,window):
        return self._getJavaScriptVariable(window,"config")

    def _getJavaScriptVariable(self, window, variableName):
        return window.evaluate_js(variableName, callback=None)
    
    def _on_window_loaded(self,window):
       self.pageConfig = self._getPageConfig(window)

       window.expose(self.run_app_command)
    
       print("window loaded")
       print("pageConfig:" + str(self.pageConfig), flush = True)
     
       window.move(self.pageConfig["Left"], self.pageConfig["Top"])
       window.resize(self.pageConfig["Width"], self.pageConfig["Height"])

       self._initPlugins()
       
       self.window.run_js("""
            document.dispatchEvent(document.pluginsinitializedevent);
            console.log("dispatched")
        """)

       window.events.loaded -= self._on_window_loaded
    
    def _initPlugins(self):
        import plugins
        plugins.init(self)
        
    def run_app_command(self, cmd):
        print(f'Run app command: {cmd}', flush = True)
        match cmd:
            case 'quit':
                self.quit()
            case 'hide':
                self.hide()
            case _:
                raise ValueError("Command should be one of: 'hide', 'quit'")

    #-------------------------------------#
    # bare mininmum application functions
    #-------------------------------------#
    def quit(self):
        window.destroy()
        
    def hide(self):
        window.hide()


if __name__ == '__main__':
    
    if len (sys.argv) == 1:
        sys.exit("No module name specified")
    
    module_name = sys.argv[1]
    print(module_name)
    module_path = os.path.join(RESOURCE_DIR, module_name)
    print(module_path)
    module_index = os.path.join(RESOURCE_DIR, module_name, INDEX_FILE_NAME)
    print(module_index)
    
    Global.APP_PATH = APP_PATH
    Global.RESOURCE_DIR = RESOURCE_DIR
    
    window = webview.create_window('Web Desktop App', module_index, width=300, height=200, min_size=(0, 0), frameless=True, transparent = True)
    app = App(window, module_name, module_path, module_index)
    webview.start(func=None, debug=False)
    
