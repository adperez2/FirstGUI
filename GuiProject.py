
from tkinter import *                       #allows us to create a graphical-user-interface

root = Tk()                                 #creates root window

root.title("CoolKidsClub")                  #display window heading
root.geometry('350x200')                    #sets geometry widthxheight


menu = Menu(root)                           #allows for a menu in root window
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

lbl = Label(root, text="Are you an otter?") #inserts a question on root window
lbl.grid()                                  #add to grid


txt = Entry(root, width=10)                 #inserts entry field in order for user to answer question above
txt.grid(column=1, row=0)                   #placement of the entry field



def clicked():                              #allow user to click on button and display answer
    res = txt.get() + " you are cool!"      #allows to add text with response
    lbl.configure(text=res)                 #display response plus the additonal quote added


btn = Button(root, text="Click me",         #allows us to insert text inside the button
             fg="Green", command=clicked)   #font color is inserted
btn.grid(column=2, row=0)                   #position on grid

root.mainloop()                             #closes code and runs it



#source where this project was obtained
#https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/


