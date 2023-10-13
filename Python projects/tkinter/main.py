from tkinter import *

window = Tk()
# creating windows
window.title("My first GUI program")
window.minsize(width=500, height=300)

# creating label
my_label = Label(text="I am a label", font=("Aria", 24, "bold"))
my_label.place(x=100, y=200)
# editing properties
my_label['text'] = "New text"
my_label.config(text="New Text")


# buttons
def clicked():
    my_label['text'] = input.get()


button = Button(text="Click Me", command=clicked)
button.pack()

# entry
input = Entry(width=10)
input.pack()

window.mainloop()
