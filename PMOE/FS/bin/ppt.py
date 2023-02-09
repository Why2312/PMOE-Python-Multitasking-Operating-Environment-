import os
import requests

action = args[0]
program = args[1]
ppt = pmoe_url + "/PPT/"
pptp = ppt + program

if action.lower() == "install":
    