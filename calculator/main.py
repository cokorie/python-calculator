import _tkinter as tk;

calculation = "";

def add_to_calculation(symbol):
    global calculation;
    calculation += str(symbol);

def eval_calculation():
    pass;

def clear_field():
    pass;

root = tk.Tk();
root.geometry("300x275");

text_result = tk.Text(root, height=2, width=16, font=("Helvetica", 24));
text_result.grid(columnspan=5);
root.mainloop();