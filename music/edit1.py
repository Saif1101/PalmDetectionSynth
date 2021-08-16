import tkinter as tk
from playsound import playsound
import threading

notesW = {}
j = 3
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
notesB = {}
k=3
for i in range(3):
    for z in range(5*i,(5*i)+5):
        if z in [0,5,10]:
            notesB[z]="Db{}".format(k)
        elif z in [1,6,11]:
            notesB[z]="Eb{}".format(k)
        elif z in [2,7,12]:
            notesB[z]="Gb{}".format(k)
        elif z in [3,8,13]:
            notesB[z]="Ab{}".format(k)
        elif z in [4,9,14]:
            notesB[z]="Bb{}".format(k)
    k+=1


print(notesB)




def clicked(color,num):
    print(color,num)
    if color == "W":
        playsound('music/{}.wav'.format(notesW[num]))
    else:
        playsound('music/{}.wav'.format(notesB[num]))
    
            

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

root.mainloop()
