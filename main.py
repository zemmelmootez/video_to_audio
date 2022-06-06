import tkinter as tk

from tkinter import filedialog
from tkinter import filedialog as fd

from moviepy.editor import *
filesrc=""
root = tk.Tk(className="convertini")
root.title('Convert mp4 to mp3 by MO3' )

root.geometry('450x450')
label = tk.Label(root,
    text="welcome to convirtini",
    font = "Times 20",
    fg= "red",
    pady=4
)

label.pack()


def save(ch):
        files = [('All Files', '*.*'),
             ('Audio Document', '*.mp3')]
        file = tk.filedialog.asksaveasfile(initialfile="converted.mp3" ,filetypes = files)

        mp4_file = rf"{ch}"
        mp3_file = rf'{file.name}'
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()





def convert(ch):
    btn = tk.Button(root, text='Save',width=15,height=5,command=lambda: save(ch))

    btn.place(x=160,y=280)


def select_file():
    filetypes = (
        ('video files', '*.mp4'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    convert(filename)
 





open_button = tk.Button(
    root,
    text='Open a File',
    command=select_file,
    width=15,
    height=5,



)
open_button.place(x=160, y=80)



root.mainloop()
