import webbrowser
import sys
import os
import random 

LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def input_math():
    ERROR_COUNT = 0
    while(True):
        user_input = input("1 times 1 = ? ")
        if user_input == "1": 
            open_video()
            break
        elif user_input.lower() == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
            ERROR_COUNT +=1
        
def open_video():
    try:
        webbrowser.open(LINK )
    except:
        pass
        
if __name__ == "__main__":
    input_math()