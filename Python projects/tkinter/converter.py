from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=km)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="Km")
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
