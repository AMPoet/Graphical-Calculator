import tkinter as tk
calculation=""



def add_to_calculation(symbol):
    global calculation 
    calculation+=str(symbol)
    text_result.delete(1.00 , "end")
    text_result.insert(1.00,calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        result=str(eval(calculation))
        text_result.delete(1.00,"end")
        text_result.insert(1.00, calculation)
    except:
        clear_field()
        text_result.insert(1.00, "Error")


def clear_field():
    global calculation
    calculation= ""
    text_result.delete(1.00,"end")
    

def update_display():
   text_result.delete(1.00, "end")
   text_result.insert(1.00, calculation)


def on_key_press(event):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '(', ')','C']:
        add_to_calculation(key)
    elif key == '\r':
        evaluate_calculation()



root=tk.Tk()
root.title("My Calculator")
root.geometry("350x327")
root.iconbitmap(r"E:\My python projects\Graphical Calculator\calculator icon.ico")
text_result=tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)
bg_color= "#1d1f20"
fg_color="#faff55"
root.resizable(False,False)

buttons = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
    ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
    ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
    ("0", 5, 2),
    ("+", 2, 4), ("-", 3, 4), ("*", 4, 4), ("/", 5, 4),
    ("(", 5, 1), (")", 5, 3), ("C", 6, 1),
    
]

for (text, row, column) in buttons:
    btn = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t),
                    width=5, font=("Arial", 14), bg="#1d1f20", fg="#faff55")
    btn.grid(row=row, column=column)

#Clear_Field_Button
btn_clear= tk.Button(root, text="C", command=clear_field, width=5, font=("Arial",14),bg=bg_color, fg=fg_color)
btn_clear.grid(row=6,column=1)

#Equal_Button
btn_equals=tk.Button(root, text="=", command=evaluate_calculation, width=5 , font=("Arial",14), bg=bg_color, fg=fg_color)
btn_equals.grid(row=6, column=4, columnspan=2)



root.bind("<Key>", on_key_press)

root.mainloop()




