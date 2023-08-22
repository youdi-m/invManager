from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Inventory Manager")
root.geometry("1000x500")

#create database or connect to existing

conn = sqlite3.connect('card.db')

#create a cursor
c = conn.cursor()

#create a table
c.execute(""" CREATE TABLE if not exists cards (
    card_id text,
    card_name text,
    card_tcg text,
    card_type text,
    card_amount integer,
    card_price real,
    card_location text
    card_note text
    )
    """)

conn.commit()
conn.close()

#add some style
style = ttk.Style()

#pick a theme
style.theme_use('default')

#configure treeview colors
style.configure("Treeview",
                background="#DFDFDF",
                foreground="black",
                rowheight=25,
                fieldbackground="#DFDFDF")

#Change selected color
style.map('Treeview',
          background=[('selected', "darkgrey")])

#create a treeview frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

#create treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

#create the treeview

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

#configure scrollbar
tree_scroll.config(command=my_tree.yview)

#define columns
my_tree['columns'] = ("ID", "Name", "TCG", "Type", "Amount", "Price", "Location", "Note") #note will be for something specific to a certain tcg like one piece colors or yugioh/pokemon sets, location is box/binder number

#format columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=140)
my_tree.column("Name", anchor=CENTER, width=140)
my_tree.column("TCG", anchor=CENTER, width=140)
my_tree.column("Type", anchor=CENTER, width=140)
my_tree.column("Amount", anchor=CENTER, width=140)
my_tree.column("Price", anchor=CENTER, width=140)
my_tree.column("Location", anchor=CENTER, width=140)
my_tree.column("Note", anchor=CENTER, width=140)

#create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("TCG", text="TCG", anchor=CENTER)
my_tree.heading("Type", text="Type", anchor=CENTER)
my_tree.heading("Amount", text="Amount", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)
my_tree.heading("Location", text="Location", anchor=CENTER)
my_tree.heading("Note", text="Note", anchor=CENTER)

#temp data
data = [
    ["wefwe", "weofwgeggfe", 14 ,"qwdgtgqwd", 33, "wefoiwrergerf", 233314, "wefergerwf"],
    ["wewefdfwe", "weovevfwfe", 142 ,"qwdgtgwrfwqwd", 23, "wefofegiwerf", 2353654, "wefeerfwf"],
    ["weffwefwe", "weovvhhfwfe", 1444 ,"qwdfsaqwd", 35, "wefoierffggwerf", 23314, "wefegergerwf"],
    ["wefgergergwe", "weojjtfwfe", 111 ,"qwdefegqwd", 36, "weforgfefeiwerf", 2313244, "weerfqdweegfwf"],
    ["wefefergewe", "weofhthtyhwfe", 145 ,"qwdhghqwd", 332, "wefoegergeiwerf", 232124, "wefwdfwf"]
]

#striped rows
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightgrey")

global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))

    count += 1

#adding record entry boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(data_frame, text="Name")
name_label.grid(row=0, column=2, padx=10, pady=10)
name_entry = Entry(data_frame)
name_entry.grid(row=0, column=3, padx=10, pady=10)

tcg_label = Label(data_frame, text="TCG")
tcg_label.grid(row=0, column=4, padx=10, pady=10)
tcg_entry = Entry(data_frame)
tcg_entry.grid(row=0, column=5, padx=10, pady=10)

type_label = Label(data_frame, text="Type")
type_label.grid(row=0, column=6, padx=10, pady=10)
type_entry = Entry(data_frame)
type_entry.grid(row=0, column=7, padx=10, pady=10)

amount_label = Label(data_frame, text="Amount")
amount_label.grid(row=1, column=0, padx=10, pady=10)
amount_entry = Entry(data_frame)
amount_entry.grid(row=1, column=1, padx=10, pady=10)

price_label = Label(data_frame, text="Price")
price_label.grid(row=1, column=2, padx=10, pady=10)
price_entry = Entry(data_frame)
price_entry.grid(row=1, column=3, padx=10, pady=10)

location_label = Label(data_frame, text="Location")
location_label.grid(row=1, column=4, padx=10, pady=10)
location_entry = Entry(data_frame)
location_entry.grid(row=1, column=5, padx=10, pady=10)

note_label = Label(data_frame, text="Note")
note_label.grid(row=1, column=6, padx=10, pady=10)
note_entry = Entry(data_frame)
note_entry.grid(row=1, column=7, padx=10, pady=10)

#Select Record
def select_record(e):

    #Clear entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    tcg_entry.delete(0, END)
    type_entry.delete(0, END)
    amount_entry.delete(0, END)
    price_entry.delete(0, END)
    location_entry.delete(0, END)
    note_entry.delete(0, END)

    #Grab record number
    selected = my_tree.focus()

    #Grab record values
    values = my_tree.item(selected, 'values')

    #Insert to entry boxes
    id_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    tcg_entry.insert(0, values[2])
    type_entry.insert(0, values[3])
    amount_entry.insert(0, values[4])
    price_entry.insert(0, values[5])
    location_entry.insert(0, values[6])
    note_entry.insert(0, values[7])

#Clear Entry Boxes
def clear_entries():

    #Clear entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    tcg_entry.delete(0, END)
    type_entry.delete(0, END)
    amount_entry.delete(0, END)
    price_entry.delete(0, END)
    location_entry.delete(0, END)
    note_entry.delete(0, END)

#Move Row Up
def move_up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

#Move Row Down
def move_down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

#Remove Selected Records
def remove_selected():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

#Update Selected Record
def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(id_entry.get(), name_entry.get(), tcg_entry.get(), type_entry.get(), amount_entry.get(), price_entry.get(), location_entry.get(), note_entry.get(),))

    #Clear entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    tcg_entry.delete(0, END)
    type_entry.delete(0, END)
    amount_entry.delete(0, END)
    price_entry.delete(0, END)
    location_entry.delete(0, END)
    note_entry.delete(0, END)

#Add buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command = update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_selected_button = Button(button_frame, text="Remove Selected", command = remove_selected)
remove_selected_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command = move_up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command = move_down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

clear_record_button = Button(button_frame, text="Clear", command = clear_entries)
clear_record_button.grid(row=0, column=7, padx=10, pady=10)

#Bind the treeview

my_tree.bind("<ButtonRelease-1>", select_record)

root.mainloop()