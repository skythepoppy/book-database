from tkinter import Tk, Button,Label,Scrollbar,Listbox,StringVar,Entry,W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox

root = Tk()

# GUI configuration
root.title("My Books Database Application")
root.configure(background='light blue')
root.geometry("850x500")
root.resizable(width=False, height=False)

# title textbox
title_label = ttk.Label(root, text="Title", background="light blue", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

# author text box
author_label = ttk.Label(root, text="Author", background="light blue", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24, textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

# ISBN text box
isbn_label = ttk.Label(root, text="ISBN", background="light blue", font=("TkDefaultFont", 14))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

# add button
add_btn = Button(root, text="Add a Book", bg="white", fg="black", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)

# list box
list_box = Listbox(root, height=16, width=40, font="helvetica 13", bg="white")
list_box.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

# scroll bar
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)

# configuration of list box and scroll box
list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

# change record, delete, view, exit application, and clear button
modify_button = Button(root, text="Change Record", bg='purple', fg='black', font='helvetica 10 bold', command="")
modify_button.grid(row=15, column=4)

del_button = Button(root, text="Delete Record", bg='purple', fg='black', font='helvetica 10 bold', command="")
del_button.grid(row=15, column=5)

view_button = Button(root, text="View all Records", bg='purple', fg='black', font='helvetica 10 bold', command="")
view_button.grid(row=15, column=1)

clear_button = Button(root, text="Clear Records", bg='purple', fg='black', font='helvetica 10 bold', command="")
clear_button.grid(row=15, column=2)

exit_button = Button(root, text="Exit Application", bg='purple', fg='black', font='helvetica 10 bold', command="")
exit_button.grid(row=15, column=3)


root.mainloop()