from tkinter import *
from tkinter import messagebox as msg

window = Tk()
window.geometry("600x150")
window.resizable(0,0)
window.title("Weight Conversion GUI")

photo_label = PhotoImage(file = "weighing.png")

def convert():
    try:
        value = float(input_entry.get())
        if value >= 0:
            gram = value * 1000
            label_gram.config(text=f"Gram: {gram:.2f}")

            pound = value * 2.20462
            label_pound.config(text=f"Pound: {pound:.2f}")

            ounce = value * 35.274
            label_ounce.config(text=f"Ounce: {ounce:.2f}")
        else:
            msg.showwarning("WARNING!!!", "INVALID INPUT, TRY AGAIN!!!")
    except ValueError:
        msg.showwarning("WARNING!!!", "INVALID INPUT, TRY AGAIN!!!")

# tạo label & entry nhập liệu
input_label = Label(window,
                    text = "Enter the weight (kg):",
                    font = 16,
                    image = photo_label,
                    compound = "left")
input_label.place(x = 5, y = 5)

input_entry = Entry(window,
                    font = 16)
input_entry.insert(0, "60")
input_entry.place(x = 250, y = 30)

# tạo button convert
btn_convert = Button(window,
                     text = "Convert",
                     font = 16,
                     bg = "black",
                     fg = "cyan",
                     command = convert)
btn_convert.place(x = 500, y = 25)

# Tạo biểu tượng và label các đơn vị chuyển đổi gram, pound, ounce
photo_gram = PhotoImage(file = "gram.png")
label_gram = Label(window,
                   text = "Gram: 60000.00",
                   font = 16,
                   image = photo_gram,
                   compound = "top")
label_gram.place(x = 60, y = 80)

photo_pound = PhotoImage(file = "pound.png")
label_pound = Label(window,
                    text = "Pound: 132.28",
                    font = 16,
                    image = photo_pound,
                    compound = "top")
label_pound.place(x = 260, y = 80)

photo_ounce = PhotoImage(file = "ounce.png")
label_ounce = Label(window,
                    text = "Ounce: 2116.44",
                    font = 16,
                    image = photo_ounce,
                    compound = "top")
label_ounce.place(x = 460, y = 80)

window.mainloop()