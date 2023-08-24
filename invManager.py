from tkinter import *
from tkinter import ttk
import sqlite3

#creating window
root = Tk()
root.title("Inventory Manager")
root.geometry("1000x500")

#connecting/creating db file
conn = sqlite3.connect('inventoryManager.db')
c = conn.cursor()

c.execute(""" CREATE TABLE if not exists inventory (
                card_id TEXT,
                card_name TEXT,
                card_tcg TEXT,
                card_type TEXT,
                card_amount TEXT,
                card_price TEXT,
                card_location TEXT,
                card_note TEXT)
                """)

conn.commit()
conn.close()

def query_database():
    conn = sqlite3.connect('inventoryManager.db')
    c = conn.cursor()

    c.execute("SELECT * FROM inventory")
    records = c.fetchall()
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))

        count += 1

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

#striped rows
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightgrey")

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

#clear entry boxes

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

#Select Record
def select_record(e):

    clear_entries()

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

#Update Selected Record
def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(id_entry.get(), name_entry.get(), tcg_entry.get(), type_entry.get(), amount_entry.get(), price_entry.get(), location_entry.get(), note_entry.get(),))

    #update the database
    conn = sqlite3.connect('inventoryManager.db')
    c = conn.cursor()

    c.execute("""UPDATE inventory SET
                        card_name = :name,
                        card_tcg = :tcg,
                        card_type = :type,
                        card_amount = :amount,
                        card_price = :price,
                        card_location = :location,
                        card_note = :note

                   WHERE card_id = :id""",
                   {
                        'name': name_entry.get(),
                        'tcg': tcg_entry.get(),
                        'type': type_entry.get(),
                        'amount': amount_entry.get(),
                        'price': price_entry.get(),
                        'location': location_entry.get(),
                        'note': note_entry.get(),
                        'id': id_entry.get(),
                   })

    conn.commit()
    conn.close()

    clear_entries()

#add a new record to db
def add_record():

    conn = sqlite3.connect('inventoryManager.db')
    c = conn.cursor()

    c.execute("INSERT INTO inventory VALUES (:id, :name, :tcg, :type, :amount, :price, :location, :note)",
                   {
                        'id': id_entry.get(),
                        'name': name_entry.get(),
                        'tcg': tcg_entry.get(),
                        'type': type_entry.get(),
                        'amount': amount_entry.get(),
                        'price': price_entry.get(),
                        'location': location_entry.get(),
                        'note': note_entry.get(),
                   })

    conn.commit()
    conn.close()

    clear_entries()

    #clear the treeview table
    my_tree.delete(*my_tree.get_children())
    query_database()

#delete entry in db
def delete_record():
    
    conn = sqlite3.connect('inventoryManager.db')
    c = conn.cursor()

    c.execute("DELETE FROM inventory WHERE card_id =" + id_entry.get())

    conn.commit()
    conn.close()

    clear_entries()

    #clear the treeview table
    my_tree.delete(*my_tree.get_children())
    query_database()

#search database
def search_record():
    my_tree.delete(*my_tree.get_children())

    conn = sqlite3.connect('inventoryManager.db')
    c = conn.cursor()

    c.execute("SELECT * FROM inventory WHERE card_id=" + id_entry.get())
    records = c.fetchall()
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))

        count += 1

    conn.commit()
    conn.close()

    clear_entries()

#Add buttons
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_button = Button(button_frame, text="Add Record", command = add_record)
add_button.grid(row=0, column=0, padx=10, pady=10)

update_button = Button(button_frame, text="Update Record", command = update_record)
update_button.grid(row=0, column=1, padx=10, pady=10)

remove_selected_button = Button(button_frame, text="Delete Selected", command = delete_record)
remove_selected_button.grid(row=0, column=2, padx=10, pady=10)

remove_selected_button = Button(button_frame, text="Search", command = search_record)
remove_selected_button.grid(row=0, column=3, padx=10, pady=10)

clear_record_button = Button(button_frame, text="Clear Entries", command = clear_entries)
clear_record_button.grid(row=0, column=4, padx=10, pady=10)

clear_record_button = Button(button_frame, text="Reset View", command = query_database)
clear_record_button.grid(row=0, column=5, padx=10, pady=10)

#Bind the treeview

my_tree.bind("<ButtonRelease-1>", select_record)

#pull data from db on start
query_database()

root.mainloop()