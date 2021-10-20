import base64
from apiReq import reqAPI

# login klass för att encoda lösen å decoda det samt typ logga in å byta sparade inloggningsuppgifter


class login:
    def __init__(self) -> None: # kollar typ om de finns sparat då provar den logga in annars så får man skriva in nya saker
        self.key = "lenghtofkeyisthislongsothatscool"
        password = ""
        username = ""
        ra = reqAPI()
        while 1:
            try:
                f = open("login.txt", "r")
                data = f.readline()
                f.close()
                password = data[data.find(":") + 1:len(data)]
                username = data[0:data.find(":")]
            except:
                print("error(file already open? (login.txt)) dosent exist?")
            self.password = self.decode(password)
            self.username = username
            print("logging in...")
            if (ra.login(self.username, self.password) == 200):
                print("logged in as", self.username)
                break
            print("login failed")
            self.save(input("login - (email:password) - "))

    def encode(self, clear): #namnet säger de
        key = self.key
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def save(self, pswNuname): # spara i fil
        password = pswNuname[pswNuname.find(":") + 1:len(pswNuname)]
        username = pswNuname[0:pswNuname.find(":")]
        try:
            f = open("login.txt", "w")
            f.write(username + ":" + self.encode(password))
        except:
            print("error(file already open? (login.txt))")

    def decode(self, enc): # namnet säger
        key = self.key
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)

    def getUsername(self): # vet inte varför jag ville ha en funktion men ja var trött och nu tycker jag det är kul och skriva sånt här så lol
        return self.username
