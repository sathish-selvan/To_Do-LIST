from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("TO-Do LisT")
root.geometry('500x400')

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    if my_entry.get() != "":
        my_list.insert(END,my_entry.get())
        my_entry.delete(0,END)

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"

    )
    my_list.selection_clear(0,END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"

    )
    my_list.selection_clear(0,END)

def del_cross_item():
    
    for i in range(0,my_list.size()):
        try:
            if my_list.itemcget(i,"fg") == "#dedede":
                my_list.delete(i)
                        
        except:
            continue
        

my_font = Font(
    family="Brush Script MT",
    size = 25,
    weight="bold")
#creating a frame 
my_frame = Frame(root)
my_frame.pack(pady=10)
#creating a listbox
my_list=Listbox(
    my_frame,
    font=my_font,
    width=25,
    height= 5,
    bg="SystemButtonFace",
    bd =0,
    fg = "#464646",
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none"
    )

my_list.pack(side=LEFT,fill=BOTH)

stuffs = ["Wanna tobe a software programer", "Try Algoexpert.io","Type some code and run","and again type it and run"]
for items in stuffs:
    my_list.insert(END, items)

#addling scroll bar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=20)
#button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

delete_button = Button(button_frame,text="Delete item",command=delete_item)
add_button = Button(button_frame,text="Add item",command=add_item)
cross_button = Button(button_frame,text="cross item",command=cross_item)
uncross_button = Button(button_frame,text="Uncross item",command=uncross_item)
del_cross_button = Button(button_frame,text="Delelte Cross item",command=del_cross_item)
delete_button.grid(row=0,column=0,padx=10)
add_button.grid(row=0,column=1,padx=10)
cross_button.grid(row=0,column=2,padx=10)
uncross_button.grid(row=0,column=3,padx=10)
del_cross_button.grid(row=0,column=4,padx=10)


root.mainloop()
