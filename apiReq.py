import requests
import json
# liten klass för att göra requests till olika saker typ det jag gör ja

class reqAPI:
    def __init__(self):
        self.URL = "https://mittkak.nu/v1/orders/current"
        self.loginURL = "https://mittkak.nu/v1/login"
    def getFood(self,usrname,paswrod): # 'oj vänta den använder ju allrid uppgifter vafan'
        r = requests.get(url=self.URL,auth=(usrname, paswrod))
        return json.loads(r.text)
    def login(self, email, password): # prova logga in å skicka tillbaks koden för status 
        r = requests.get(url=self.loginURL, auth=(email, password))
        return r.status_code
