#!/usr/bin/env python3
#
# A Web Desktop Application
#
# use for panels, launchers, anything you want.

import sys
import os
import pprint

import webview
from webview.dom import DOMEventHandler

from util.sequence import containsMoreThanOne

RESOURCE_DIR = "res"
INDEX_FILE_NAME = "index.html"

app = None

class App:
    
    def __init__(self, window):
        self.window = window
    
    def quit(self):
        window.destroy()
        
    def hide(self):
        window.hide()
    
    

def run_shell_command(cmd):
    print(f'Run shell command: {cmd}')

def run_app_command(cmd):
    print(f'Run app command: {cmd}')
    match cmd:
        case 'quit':
            app.quit()
        case 'hide':
            app.hide()
            

def run_session_command(cmd):
    print(f'Run session command: {cmd}')


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
        print(f'Run session command: {anchor_attributes["sessioncmd"]}')
        return
    
    print(f'Link target is {e["target"]["href"]}')
    
def bindEventHandlers(window):
    anchors = window.dom.get_elements('a')
    for anchor in anchors:
        anchor.events.click += DOMEventHandler(link_handler, prevent_default=True)    

if __name__ == '__main__':
    
    if len (sys.argv) == 1:
        sys.exit("No module name specified")
    
    module_name = sys.argv[1]
    print(module_name)
    module_index = os.path.join(RESOURCE_DIR, module_name, INDEX_FILE_NAME)
    print(module_index)

    
    window = webview.create_window('Hello world', module_index, width=300, height=200)
    app = App(window)
    webview.start(bindEventHandlers, window)
    
    
