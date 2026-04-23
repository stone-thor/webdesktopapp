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

first = itemgetter(0)

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
        #return window.evaluate_js("return "+ variableName +";", callback=None)
        return window.evaluate_js(variableName, callback=None)
    
    def _on_window_loaded(self,window):
       self.pageConfig = self._getPageConfig(window)

       print("window loaded")
       print("pageConfig:" + str(self.pageConfig), flush = True)
     
       window.move(self.pageConfig["Left"], self.pageConfig["Top"])
       window.resize(self.pageConfig["Width"], self.pageConfig["Height"])

       self.initPlugins()
       
       self.window.run_js("""
            document.dispatchEvent(document.pluginsinitializedevent);
            console.log("dispatched")
        """)

       window.events.loaded -= self._on_window_loaded
    
    def initPlugins(self):
        import plugins
        plugins.init(self)
    
    #-------------------------------------#
    # bare mininmum application functions
    #-------------------------------------#
    def quit(self):
        window.destroy()
        
    def hide(self):
        window.hide()
    

def run_shell_command(cmd):
    print(f'Run shell command: {cmd}', flush = True)

def run_app_command(cmd):
    print(f'Run app command: {cmd}', flush = True)
    match cmd:
        case 'quit':
            app.quit()
        case 'hide':
            app.hide()
            
def run_session_command(cmd):
    print(f'Run session command: {cmd}', flush = True)


# 
# the anchor element should have one of these attributes
#   
#   execCmd: execute a shell command, 'vlc', 'firefox', 'c:\games\gtr\gtr.exe'
#   appCmd: run a command concerning the application itself: something like: 'quit', 'hide', 'reload'
#   sessionCmd: run a command, controlling the desktop session or the os: 'logout', 'reboot', 'shutdown'
#
def link_handler(e):
    anchor_attributes = e['target']['attributes']
    print(anchor_attributes)
    if containsMoreThanOne(list(anchor_attributes.keys()), ["execcmd","appcmd","sessioncmd"]):
        raise ValueError
        
    if 'execcmd' in anchor_attributes:
        run_shell_command(anchor_attributes["execcmd"])
        return
    elif 'appcmd' in anchor_attributes:
        run_app_command(anchor_attributes["appcmd"])
        return
    elif 'sessioncmd' in anchor_attributes:
        run_app_command(anchor_attributes["sessioncmd"])
        return
    
    print(f'Link target is {e["target"]["href"]}', flush = True)
    
def bindEventHandlers(window):
    anchors = window.dom.get_elements('a')
    for anchor in anchors:
        anchor.events.click += DOMEventHandler(link_handler, prevent_default=True)    

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
    
    window = webview.create_window('Hello world', module_index, width=300, height=200, min_size=(0, 0), frameless=True)
    app = App(window, module_name, module_path, module_index)
    webview.start(bindEventHandlers, window, debug=True)
    
    
    