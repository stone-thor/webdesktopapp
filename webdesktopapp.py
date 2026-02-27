#!/usr/bin/env python3
#
# A Web Desktop Application
#
# use for panels, launchers, anything you want.

import sys
import os

import webview
from webview.dom import DOMEventHandler


RESOURCE_DIR = "res"
INDEX_FILE_NAME = "index.html"

def link_handler(e):
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
    webview.start(bindEventHandlers, window)
    
    
