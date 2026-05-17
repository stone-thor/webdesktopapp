#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  This file is part of Webdesktopapp
#
#  Copyright 2011-2017 xDaks <http://xdaks.deviantart.com/>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import sys, os, urllib, string, subprocess

import appconfig.configfile 

class javascriptObject():
    
    def __init__(self):
        self.menuFile = appconfig.configfile.ConfigFile(appconfig.configfile.get_default_config_base_path(),"menu")
    
    def getMenuEntries(self):
        config = self.menuFile.getConfig()
        print("config:" + str(config))
        return config

    def run_shell_command(self, command, escape = False):
        print("command" + command)
        print("escape" + str(escape))
        commandToRun =  command.replace("apos;","\'").replace("quot;","\"").replace("\\\\","\\") if escape else command
        
        
        print("commandToRun '" + commandToRun +"'")
        return subprocess.run(commandToRun, shell=True)
    
    def run_session_command(self, command):
        print ("session command " + command)
        
def init(app):
    jsObj = javascriptObject()
    
    app.window.expose(jsObj.getMenuEntries)
    app.window.expose(jsObj.run_shell_command)

    print('jsObject init')

