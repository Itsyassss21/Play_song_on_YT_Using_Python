import pywhatkit

try:

    song=input("Enter Song Name: ")
    pywhatkit.playonyt(song)


    print("Song Played")

except:
    print("Error While feching")
