from os import system
import cv2
from imageio import imread
from apiReq import reqAPI
from login import login


daysArray = ["monday", "tuesday", "wednesday", "thursday", "friday"] # dag array vet inte vraför men har hängt med säns test med api inte effektiv inte nödvendig men som sagt koden är skit och jag bryr mig inte för jag årkar inte tänka


def nicePrint(msg): # ja du fattar
    print("->", msg)


def check(DAY):
    for i in daysArray:
        if (i == DAY):
            return True
    return False


def openPic(link): # typ öppna bild å gö om länk för å ta bort ' '
    link = link.replace(" ", "%20")
    image = imread(link)
    RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow("klicka på tanget för att stänga", RGB_img)
    cv2.waitKey()
    cv2.destroyAllWindows()


loginManager = login() # ja ny loginmanager inte bra kod fortfarande
system("title mitt käk på dator fast inte gjort av dem som gjorde mitt käk för dom inte ville göra någon dator verision och jag gillar inte  å jobba med ui så det blev så här   koden är skit men jag årkar inte bry mig")
reqMan = reqAPI() # ja sån här sak som gör request

if (reqMan.login(loginManager.username, loginManager.password) != 200): # ba kolla ifall man får nå annat än 200
    nicePrint("login failed/you should not see this/error with server or something with access or any thing")
    exit()

print("[!] laddar vänta") # fett cool
data = reqMan.getFood(loginManager.username,loginManager.password)
system("cls")

def numToDay(n):
    return daysArray[n]

def showMat(): # typ ba för å visa maten
    print("\n-> Mitt käk fast ja typ dator")
    nicePrint("Logged in as " + loginManager.getUsername() + "\n")
    c = 1
    for day in data["current"]:
        try:
            if (check(day)):
                nicePrint(str(c) + " - " + day + " - " +
                          data["current"][day]["dish"]["name"])
            else:
                c -= 1
        except:
            nicePrint(str(c) + " - " + day + " - Ingen mat/fel")
        c += 1


showMat()
 # loop för allt som händer typ eller ja input
while 1:
    iDag = input(
        "\n-> (clear för att ränsa skärmen)\n-> Få fram information (dag): ")
    if (iDag == "clear"):
        system("cls")
        showMat()
    iDagSTR = iDag
    try:
        iDagSTR = numToDay(int(iDag) - 1)
    except:
        pass
    if (check(iDagSTR)):
        try:
            print("\n\n", data["current"][iDagSTR]["dish"]["name"], "\n",
                  data["current"][iDagSTR]["dish"]["description"], "\n\n")
            openPic(data["current"][iDagSTR]["dish"]["image"])
        except:
            nicePrint("error troligen att du inte har någon mat denna dag")
    elif (iDag != "clear"):
        nicePrint("Fel foramt skriv 1-5")


# ja jag vet att koden är skit ja den suger och ja jag är trött och har tråkigt men den funkar och jag tänker inte skriva om. Första gången jag jobba med json i python
# nu har jag tråkigt och leker som att nån annan än jag kommer se koden men ja nej det kommer inte hända kan väll lägga t en setup när jag håller på