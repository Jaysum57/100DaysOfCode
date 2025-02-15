from tkinter import *

ARIAL_BOLD = ("Arial", 12, "bold")
ARIAL_NORMAL = ("Arial", 12, "normal")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=30,pady=20)

# Miles Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


# Miles label
miles_label = Label(text="Miles", font=ARIAL_NORMAL)
miles_label.grid(column=2, row=0)
miles_label.config(padx=5)

# is equal to label
is_equal_label = Label(text="is equal to", font=ARIAL_NORMAL)
is_equal_label.grid(column=0, row=1)

# kilometer label variable
km_label_variable = Label(text=0, font=ARIAL_BOLD)
km_label_variable.grid(column=1, row=1)

# kilometer label
km_label = Label(text="Km", font=ARIAL_NORMAL)
km_label.grid(column=2, row=1)

# Calculate button
def conversion():
    miles = float(miles_input.get())
    km_label_variable.config(text= round(miles * 1.609344,2))

calculate_button = Button(text="Calculate", command=conversion)
calculate_button.grid(column=1, row=2)

window.mainloop()