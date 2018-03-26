import tkinter
import tkinter.scrolledtext as scrolledtext
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

#initiate Window/menu
editor = tkinter.Tk()
textpad = scrolledtext.ScrolledText()
menubar = tkinter.Menu(editor)
filemenu = tkinter.Menu(menubar)

#Window Configurations
editor.title("Aaron's Editor")
editor.config(menu=menubar)
textpad.pack(fill="both", expand=True)

#Menu Button Actions
def dummy():
    print("This is a placeholder command!")

def new_command():
    if messagebox.askyesno(title = 'New File', message = 'Would you like to save your changes before creating a new file?'):
        save_command()
        textpad.delete('1.0', tkinter.END)
    else:
        textpad.delete('1.0', tkinter.END)

def open_command():
    file = filedialog.askopenfile(parent = editor, mode = 'rb', title = 'Select a file')
    if file != None:
        textpad.delete('1.0', tkinter.END)
        contents = file.read()
        textpad.insert('1.0', contents)
        file.close()

def save_command():
    file = filedialog.asksaveasfile(mode = 'w')
    if file != None:
        data = textpad.get('1.0', tkinter.END+'-1c')
        file.write(data)
        file.close()

def exit_command():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Aaron's Editor?"):
        editor.destroy()

#Menu items creation/configuration
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New", command = new_command)
filemenu.add_command(label = "Open", command = open_command)
filemenu.add_command(label = "Save", command = save_command)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_command)

editor.mainloop()