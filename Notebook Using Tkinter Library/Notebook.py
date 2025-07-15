# ...........................importing necessary packages.............................
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
# ....................................................................................
# .........................turning text_contents into an empty dictionary.............................
text_contents = dict()
# ....................................................................................................


# .........................create_file function........................................
def create_file(content='', title='Untitled'):
    container = ttk.Frame(notebook)  # Creating this variable which will help to infuse whole text area into container
    container.pack()  # so that We can insert scroll button into the right side of our app [check line 18]

    text_area = tk.Text(container)
    text_area.insert('end', content)
    text_area.pack(side='left', fill='both', expand=True)  # side is given left, so the whole text area will be on
    # the left side so that we can put scroll button in right side
    notebook.add(container, text=title)
    notebook.select(container)

    text_contents[str(text_area)] = hash(content)  # Hashing data is done to shorten a long length data

    text_scroll = ttk.Scrollbar(container, orient='vertical', command=text_area.yview)
    text_scroll.pack(side='right', fill='y')
    text_area['yscrollcommand'] = text_scroll.set
# ........................................................................................


# .................. creating check_for_changes function ................................
def check_for_changes():
    current = get_text_widget()
    content = current.get('1.0', 'end-1c')
    name = notebook.tab('current')['text']

    if hash(content) != text_contents[str(current)]:
        if name[-1] != '*':
            notebook.tab('current', text=name + '*')
    elif name[-1] == '*':
        notebook.tab('current', text=name[:-1])  # <----- Removes the last character from the name
# ............................................................................................................


# ............... creating get_text_widget function .........................
def get_text_widget():
    tab_widget = root.nametowidget(notebook.select())
    text_widget = tab_widget.winfo_children()[0]
    # this is done to make the scroll bar and text area frame flexible with each other
    return text_widget
# ................................................................................


# .......................creating close_current_tab function................................
def close_current_tab():
    current = get_text_widget()
    if current_tab_unsaved() and not confirm_close():
        return
    if len(notebook.tabs()) == 1:
        create_file()
    notebook.forget(current)


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get('1.0', 'end-1c')
    return hash(content) != text_contents[str(text_widget)]


def confirm_close():
    return messagebox.askyesno(
        message='You have unsaved changes in this tab. Are you sure you want to close the tab?',
        icon='question',
        title="Confirm Close Tab"
    )

# ...........................................................................................


# ................... creating confirm_quit function .............................
def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        # this is done to make the scroll bar and text area frame flexible with each other
        content = text_widget.get('1.0', 'end-1c')

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break

    if unsaved:
        confirm = messagebox.askyesno(
                message='You have unsaved changes. Are you sure you want to quit?',
                icon='question',
                title="Confirm Quit"
                )
        if not confirm:
            return

    root.destroy()
# ................................................................................................


# .................... creating save_file function............................
def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)  # for cross-platform compatibility
        text_widget = get_text_widget()
        content = text_widget.get('1.0', 'end-1c')  # from the 1st character of 1st line to end without last character

        with open(file_path, 'w') as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print('Save operation failed!')
        return
    notebook.tab('current', text=filename)
    text_contents[str(text_widget)] = hash(content)

# ...........................................................................................


# ..................creating open_file function.............................................
def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)
        with open(file_path, 'r') as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print('Open operation cancelled.')

    create_file(content, filename)
# ................................................................................................


# ...........................Creating show_info function .........................................
def show_info():
    messagebox.showinfo(
        title='About Us',
        message='Hey! I’m the one-person show behind [Saby\'s Text Editor V1.0]. '
        'I built this app to scratch my own itch and figured others might find it helpful too.'
        ' It’s a work of love, coffee, and stubborn curiosity. '
        'Thanks for checking it out—I’m always improving things, so stay tuned!'
    )
# ....................................................................................................


# ........................Creating & Editing the notebook and creating File menubar...........................
root = tk.Tk()

root.title("Saby's Text Editor V1.0(Build with Python's Tkinter)")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx=1, pady=(4, 0))

menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label='File')
menubar.add_cascade(menu=help_menu, label='Help')

# .................adding options to file menubar with functions and shortcut keys.................................
file_menu.add_command(label='New', command=create_file, accelerator='Ctrl+N')
file_menu.add_command(label='Save', command=save_file,  accelerator='Ctrl+S')
file_menu.add_command(label='Open', command=open_file,  accelerator='Ctrl+O')
file_menu.add_command(label='Exit', command=confirm_quit, accelerator='Ctrl+Q')
file_menu.add_command(label='Close Tab', command=close_current_tab, accelerator='Ctrl+E')

help_menu.add_command(label='About', command=show_info, accelerator='Ctrl+H')
# ................................................................................

# ............................creating a notebook.................................
notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

create_file()  # running this so whenever we run the app its starts with a new file to write new stuff
# ....................assigning short cut keys......................
root.bind('<KeyPress>', lambda event: check_for_changes())
root.bind('<Control-n>', lambda event: create_file())
root.bind('<Control-s>', lambda event: save_file())
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-q>', lambda event: confirm_quit())
root.bind('<Control-e>', lambda event: close_current_tab())

root.bind('<Control-h>', lambda event: show_info())
# .........................................................................
root.mainloop()
# ........................................END.............................................
