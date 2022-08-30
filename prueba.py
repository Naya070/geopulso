from tkinter import *
root=Tk()
textBox=Text(root, height=2, width=10)
textBox.pack()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)


buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

mainloop()