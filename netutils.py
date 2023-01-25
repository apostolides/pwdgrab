import requests as r
import base64

def send_file(filepath, targetname, recvserv):
    with open(filepath, "rb") as f:
        contents = f.read()
        contents = base64.b64encode(contents)
        resp = r.post(recvserv, files={targetname, contents})
