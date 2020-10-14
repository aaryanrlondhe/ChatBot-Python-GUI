from playsound import playsound
import tkinter
from tkinter import filedialog
main_win = tkinter.Tk() 
main_win.withdraw()
main_win.overrideredirect(True)
main_win.geometry('0x0+0+0')
main_win.deiconify()
main_win.lift()
main_win.focus_force()
main_win.sourceFile = filedialog.askopenfilename(parent=main_win, initialdir= "/",title='Please select a directory') 
main_win.destroy()
playsound(main_win.sourceFile)#it will play audio files
print(main_win.sourceFile)

