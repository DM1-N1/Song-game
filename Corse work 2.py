# This for the Username and password

name=input("Please enter your name")
age=input("Please enter your age")
year=input("What year are you in")
password=input("Please enter a password")
username=name+age+year
dav = open("N:\dt and ict\D1.txt","a+")
dav.write(username+"\n")
dav.write(password+"\n")
dav.close()
print("This is your username")
print(username)
print("This is your password")
print(password)

#This the authentication
print("You will only get one chance to login")
check1=input("Please enter your username")
check2=input("Enter your password")
if check1==username and check2==password:
    print("You are logged in")
    print("Welcome to the game")
else:
    print("Incorrect")
    print("Restart and try again")
    quit()
    

# This is storing the songs and names in seperate files

Artist1=("AjTracey")
Artist2=("HeadieOne")
Artist3=("DaveftJhus")
Artist4=("Ramz")
Artist5=("Fredo")
Artist6=("HopeDealers")

dav = open("N:\dt and ict\inst.txt","a+")
dav.write(Artist1+"\n")
dav.write(Artist2+"\n")
dav.write(Artist3+"\n")
dav.write(Artist4+"\n")
dav.write(Artist5+"\n")
dav.write(Artist6+"\n")
dav.close()

song1=("Butterflies")
song2=("18Hunna")
song3=("Samantha")
song4=("FamilyTree")
song5=("AyCurumba")
song6=("Trapmash")

bob = open("name.txt","a+")
bob.write(song1+"\n")
bob.write(song2+"\n")
bob.write(song3+"\n")
bob.write(song4+"\n")
bob.write(song5+"\n")
bob.write(song6+"\n")
bob.close()


print("Here are the instructions for the game")
print("A random artist and the first letter of each word of the song title will be displayed on the screen")
print("You need to try and guess the song")
print("You will get 2 chances to guess the song")
print("2 points if you guess it right first time and 1 point for guessing it right second time")
print("Once you get one wrong the game will end")
point=0

#This is the actual game with a point system
guess1=dav = open("N:\dt and ict\inst.txt","r")
scripta1= dav.read (8)
dav.close()

guess12=dav = open("name.txt","r")
scriptaS= dav.read (1)
dav.close()

print(scripta1)
print(scriptaS)
g1=input("What song is this")
if g1==("ajtraceybutterflies"):
    print("correect")
    point=point+3
else:
    print("Incorrect")
    g12=input("What song is this")
    if g12==("ajtraceybutterflies"):
        print("Correct")
        point=point+1
    else:
        print("Incorrect")
        quit()
print(point)



        











                                                     

    






                                                     

    
