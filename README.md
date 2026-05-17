# HTML 5 App Module in Python using pywebview

This is a proof of concept for a reimplementation of [webkit_app_bar](https://github.com/codepage/webkit_app_bar) using [pywebview](https://pywebview.flowrl.com/).  
As this is a proof of concept, it is still rough around the edges. 

---

## TODOs

 - [ ] refactor all remaining plugins from [webkit_app_bar](https://github.com/codepage/webkit_app_bar)
 
### pywebview
 - [ ] transparent windows under msft windows (pywebview thinks this is not possible)
 
---

## run application 
`$ python webdesktopapp.py <plugin_name>`

see folder `./res` for plugins. name of folder is `<plugin_name>`.

## run unittests
`$ python -m unittest ./test/applauncher/test_applauncher.py`
