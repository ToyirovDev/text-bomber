from art import tprint 
import time
import keyboard
import pyautogui
import os
from colorama import init, Fore, Style

# Initialize the colorama module
init() 

os.system("cls")
os.system("color 4")

time.sleep(1)
tprint("TEXT-BOMBER")
time.sleep(1)
tprint("  by  Toyirov Programmer!", "italic")
print("")
print("")
print("")
try:
	global necha
	print("How many times to send!")
	necha = int(input(Fore.BLUE + "--> "))
except:
	necha = 10
	print(Style.RESET_ALL + "You can only enter a number!")
	print(Style.RESET_ALL + "Default value is 10!")


time.sleep(1)
print("")
print(Style.RESET_ALL + "What to send!")
words = input(Fore.BLUE + "--> ")


print(Fore.YELLOW + "15-second time!")
time.sleep(1)

def countdown(t):
	while t:
		mins, secs = divmod(t,60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
countdown(int(15))

print("\n\n")

for x in range(necha):
	keyboard.write(words)
	keyboard.press("Enter")
	time.sleep(0.1)

