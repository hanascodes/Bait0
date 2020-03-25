import os
import time

print('Hey')
time.sleep(1)

print('You\'re pretty cool')
time.sleep(1)

os.system('clear')
#os.system('cls') for Windows

answerInput = str(input("Wanna go out sometime? y/n "))

if answerInput == 'y':
    print("Cool. ")
else:
    print("Fine. Ko te jebe. ")
