import tkinter as tk
from playsound import playsound
import threading
import cv2
import numpy as np 
import pyautogui
import time



notesW = {}
j = 3 #Number of octaves
for i in range(3):
    for z in range(7*i,(7*i)+7):
        if z in [0,7,14]:
            notesW[z] = "C{}".format(j)
        elif z in [1,8,15]:
            notesW[z] = "D{}".format(j)
        elif z in [2,9,16]:
            notesW[z] = "E{}".format(j)
        elif z in [3,10,17]:
            notesW[z] = "F{}".format(j)
        elif z in [4,11,18]:
            notesW[z] = "G{}".format(j)
        elif z in [5,12,19]:
            notesW[z] = "A{}".format(j)
        elif z in [6,13,20]:
            notesW[z] = "B{}".format(j)
    j+=1
notesB ={ 0: "Db3", 1 : "Eb3" , 3 : "Gb3", 4 : "Ab3", 5 : "Bb3" , 7 : "Db4",8 : "Eb4", 10 : "Gb4" ,11 :"Ab4" ,12 : "Bb4" , 14 :"Db5" ,15 : "Eb5" ,17 : "Gb5",18 : "Ab5" ,19 :"Bb5"}

def clicked(color,num):
    print(color,num)
    if color == "W":
        playsound('music/{}.wav'.format(notesW[num]))
    else:
        playsound('music/{}.wav'.format(notesB[num]))

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
fingers_cascade = cv2.CascadeClassifier('hands.xml')
cap = cv2.VideoCapture(0)
    
            

root = tk.Tk()

octaves = 3

root.geometry('{}x200'.format(300 * octaves))

white_keys = 7 * octaves
black = [1, 1, 0, 1, 1, 1, 0] * octaves

for i in range(white_keys):
    tk.Button(root, bg='white', activebackground='gray87',  command=lambda i=i: threading.Thread(target = clicked,args=('W', i)).start()).grid(row=0, column=i*3, rowspan=2, columnspan=3, sticky='nsew')

for i in range(white_keys - 1):
    if black[i]:
        tk.Button(root, bg='black', activebackground='gray12', command=lambda i=i: threading.Thread(target = clicked,args=('B', i)).start()).grid(row=0, column=(i*3)+2, rowspan=1, columnspan=2, sticky='nsew')

for i in range(white_keys * 3):
    root.columnconfigure(i, weight=1)

for i in range(2):
    root.rowconfigure(i, weight=1)

window_width = 1130
window_height = 250
# get the screen size of your computer [width and height using the root object as foolows]
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Get the window position from the top dynamically as well as position from left or right as follows
position_top = int(screen_height/2 -window_height/2)
position_right = int(screen_width / 2 - window_width/2)
# this is the line that will center your window
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}') #Centering the synth

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    fingers = fingers_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in fingers:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        if(((960+5*x) <= 1525) and (960+5*x) >= 395) and ((540+2*y)>= 415 and (540+2*y)<= 665): #Making sure the cursor doesn't perform clicks outside the synth window
            time.sleep(0.75)
            pyautogui.click(960+5*x,540+2*y)
            print(5*x,2*y)

    cv2.imshow('Image',img)
    k = cv2.waitKey(30) & 0xff
    root.update()
    if k==27:
        cap.release()
        cv2.destroyAllWindows()






