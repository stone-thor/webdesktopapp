#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  This file is part of Webkit App Bar.
#
#  Copyright 2011-2014 xDaks <http://xdaks.deviantart.com/>
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

import sys
import os
import types
import Global

def loadPluginList(app):
    pluginList = []

    if not 'plugin' in app.pageConfig or app.pageConfig['plugin'] == '' : return pluginList
    plugin = app.pageConfig['plugin']

    if type(plugin) == str:
        if app.module_name != '':
            plugin = '.'.join ([Global.RESOURCE_DIR, app.module_name, plugin])
        pluginList.append(plugin)

    elif type(plugin) is list:
        for val in plugin:
            if app.module_name != '':
                val = '.'.join ([Global.RESOURCE_DIR, app.module_name, val])
            pluginList.append(val)

    return pluginList

def init(app):
    sys.path.insert(1, os.path.join(Global.APP_PATH, app.module_path))

    pluginList = loadPluginList(app)
    print(pluginList)

    app.window.run_js("""
    document.pluginsinitializedevent = new Event('pluginsinitialized');
    console.log("initialized")
    """)

    for plugin in pluginList:
        print(plugin)
        exec('import ' + plugin)
        sys.modules[plugin].init(app)