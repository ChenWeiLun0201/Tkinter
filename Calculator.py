from tkinter import *
# from calculator import *


def plus(first_number, second_number):
    return first_number + second_number


def minus(first_number, second_number):
    return first_number - second_number


def multi(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        raise Exception("Không được chia cho 0")
    return first_number / second_number


def calculate(operator, first_number, second_number):
    if operator == "+":
        return plus(first_number, second_number)
    elif operator == "-":
        return minus(first_number, second_number)
    elif operator == "*":
        return multi(first_number, second_number)
    elif operator == "/":
        return divide(first_number, second_number)

win = Tk()
win.resizable(False, False)

first_number = ""
second_number = ""
operator = ""


def press_number(widget, number):
    global operator, first_number, second_number

    # Ấn button số lần đầu sau khi bấm toán tử
    if operator != "" and second_number == "":
        first_number = widget.get()
        widget.delete(0, 'end')
        widget.insert(0, number)
        second_number = number
    # Dãy số của toán hạng 2
    elif second_number != "":
        widget.insert(len(widget.get()), number)
        second_number = widget.get()
    # Dãy số của toán hạng 1
    else:
        widget.insert(len(widget.get()), number)


def press_operator(clicked_operator):
    global operator
    operator = clicked_operator


def press_equal():
    global operator, first_number, second_number

    txt_display.delete(0, len(txt_display.get()))
    txt_display.insert(0, calculate(operator, int(first_number), int(second_number)))


txt_display = Entry(master=win)
txt_display.pack(fill="x")

buttons_frame = Frame(master=win)
buttons_frame.pack(fill="x")

btn_ac = Button(pady=10, width=5, master=buttons_frame, text="AC")
btn_ac.grid(row=0, column=0)

btn_negative = Button(pady=10, width=5, master=buttons_frame, text="+/-")
btn_negative.grid(row=0, column=1)

btn_percent = Button(pady=10, width=5, master=buttons_frame, text="%")
btn_percent.grid(row=0, column=2)

btn_divide = Button(pady=10, width=5, master=buttons_frame, text="/", command=lambda: press_operator("/"))
btn_divide.grid(row=0, column=3)


btn_7 = Button(pady=10, width=5, master=buttons_frame, text="7", command=lambda : press_number(txt_display, "7"))
btn_7.grid(row=1, column=0)

btn_8 = Button(pady=10, width=5, master=buttons_frame, text="8", command=lambda : press_number(txt_display, "8"))
btn_8.grid(row=1, column=1)

btn_9 = Button(pady=10, width=5, master=buttons_frame, text="9", command=lambda : press_number(txt_display, "9"))
btn_9.grid(row=1, column=2)

btn_multiply = Button(pady=10, width=5, master=buttons_frame, text="*", command=lambda: press_operator("*"))
btn_multiply.grid(row=1, column=3)

btn_4 = Button(pady=10, width=5, master=buttons_frame, text="4", command=lambda : press_number(txt_display, "4"))
btn_4.grid(row=2, column=0)

btn_5 = Button(pady=10, width=5, master=buttons_frame, text="5", command=lambda : press_number(txt_display, "5"))
btn_5.grid(row=2, column=1)

btn_6 = Button(pady=10, width=5, master=buttons_frame, text="6", command=lambda : press_number(txt_display, "6"))
btn_6.grid(row=2, column=2)

btn_minus = Button(pady=10, width=5, master=buttons_frame, text="-", command=lambda: press_operator("-"))
btn_minus.grid(row=2, column=3)

btn_1 = Button(pady=10, width=5, master=buttons_frame, text="1", command=lambda : press_number(txt_display, "1"))
btn_1.grid(row=3, column=0)

btn_2 = Button(pady=10, width=5, master=buttons_frame, text="2", command=lambda : press_number(txt_display, "2"))
btn_2.grid(row=3, column=1)

btn_3 = Button(pady=10, width=5, master=buttons_frame, text="3", command=lambda : press_number(txt_display, "3"))
btn_3.grid(row=3, column=2)

btn_plus = Button(pady=10, width=5, master=buttons_frame, text="+", command=lambda: press_operator("+"))
btn_plus.grid(row=3, column=3)

btn_0 = Button(pady=10, width=15, master=buttons_frame, text="0")
btn_0.grid(row=4, columnspan=2)

btn_comma = Button(pady=10, width=5, master=buttons_frame, text=",")
btn_comma.grid(row=4, column=2)

btn_equal = Button(pady=10, width=5, master=buttons_frame, text="=", command=lambda: press_equal())
btn_equal.grid(row=4, column=3)

win.mainloop()