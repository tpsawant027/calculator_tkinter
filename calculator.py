from math import pi, e, sqrt
import tkinter as tk

operator_list = [
    ["\N{SQUARE ROOT}", "\N{GREEK SMALL LETTER PI}", "e", " \N{Circumflex Accent} "],
    ["AC", "\N{Left Parenthesis}", "\N{Right Parenthesis}", " \N{Division Sign} "],
    ["7", "8", "9", " \N{Multiplication Sign} "],
    ["6", "5", "4", " \N{Plus Sign} "],
    ["3", "2", "1", " \N{Minus Sign} "],
    ["0", "\N{Full Stop}", "\N{Erase To the Left}", "\N{Equals Sign} "],
]

operator_dict = {
    operator_list[2][3]: " * ",
    operator_list[0][3]: " ** ",
    operator_list[1][3]: " / ",
    operator_list[4][3]: " - ",
    operator_list[0][1]: str(pi),
    operator_list[0][2]: str(e),
}


def backspace():
    nw = entry.get(0.0, tk.END)[:-2]
    entry.delete(0.0, tk.END)
    entry.insert(tk.END, nw)


def _rep(s: str) -> str:
    s2 = ""
    for i, c in enumerate(s):
        if c == "\N{SQUARE ROOT}":
            s2 = s[:i] + "sqrt("
            j = i + 1
            while j < len(s) and s[j] != " ":
                s2 += s[j]
                j += 1
            s2 += ")" + s[j:]
    return s2


def parse_input(s: str) -> str:
    s = s.replace(" ", "")
    if "\N{SQUARE ROOT}(" in s:
        s = s.replace("\N{SQUARE ROOT}(", "sqrt(")
    while "\N{SQUARE ROOT}" in s:
        s = _rep(s)
    for k, v in operator_dict.items():
        s = s.replace(k.strip(), v.strip())
    return s


def inp(element: str):
    entry.insert(tk.END, element)


def evaluate():
    eqn = entry.get(0.0, tk.END)
    eqn = parse_input(eqn)
    entry.delete(0.0, tk.END)
    try:
        entry.insert(tk.END, eval(eqn, globals()))
    except SyntaxError:
        entry.insert(tk.END, "INVALID INPUT")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator")
    ico = tk.PhotoImage(file="./resources/logo.png")
    window.iconphoto(False, ico)
    window.resizable(width=False, height=False)

    entry = tk.Text(master=window, width=20, height=5)
    entry.pack(padx=5, pady=5)

    frame = tk.Frame(master=window)
    frame.pack(padx=5, pady=5)
    b_1 = tk.Button(
        master=frame,
        text=operator_list[0][0],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[0][0]),
    )
    b_1.grid(ipadx=5, ipady=5, row=0, column=0)
    b_2 = tk.Button(
        master=frame,
        text=operator_list[0][1],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[0][1]),
    )
    b_2.grid(ipadx=5, ipady=5, row=0, column=1)
    b_3 = tk.Button(
        master=frame,
        text=operator_list[0][2],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[0][2]),
    )
    b_3.grid(ipadx=5, ipady=5, row=0, column=2)
    b_4 = tk.Button(
        master=frame,
        text=operator_list[0][3],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[0][3]),
    )
    b_4.grid(ipadx=5, ipady=5, row=0, column=3)
    b_5 = tk.Button(
        master=frame,
        text=operator_list[1][0],
        relief=tk.FLAT,
        command=lambda: entry.delete(0.0, tk.END),
    )
    b_5.grid(ipadx=5, ipady=5, row=1, column=0)
    b_6 = tk.Button(
        master=frame,
        text=operator_list[1][1],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[1][1]),
    )
    b_6.grid(ipadx=5, ipady=5, row=1, column=1)
    b_7 = tk.Button(
        master=frame,
        text=operator_list[1][2],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[1][2]),
    )
    b_7.grid(ipadx=5, ipady=5, row=1, column=2)
    b_8 = tk.Button(
        master=frame,
        text=operator_list[1][3],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[1][3]),
    )
    b_8.grid(ipadx=5, ipady=5, row=1, column=3)
    b_9 = tk.Button(
        master=frame,
        text=operator_list[2][0],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[2][0]),
    )
    b_9.grid(ipadx=5, ipady=5, row=2, column=0)
    b_10 = tk.Button(
        master=frame,
        text=operator_list[2][1],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[2][1]),
    )
    b_10.grid(ipadx=5, ipady=5, row=2, column=1)
    b_11 = tk.Button(
        master=frame,
        text=operator_list[2][2],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[2][2]),
    )
    b_11.grid(ipadx=5, ipady=5, row=2, column=2)
    b_12 = tk.Button(
        master=frame,
        text=operator_list[2][3],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[2][3]),
    )
    b_12.grid(ipadx=5, ipady=5, row=2, column=3)
    b_13 = tk.Button(
        master=frame,
        text=operator_list[3][0],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[3][0]),
    )
    b_13.grid(ipadx=5, ipady=5, row=3, column=0)
    b_14 = tk.Button(
        master=frame,
        text=operator_list[3][1],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[3][1]),
    )
    b_14.grid(ipadx=5, ipady=5, row=3, column=1)
    b_15 = tk.Button(
        master=frame,
        text=operator_list[3][2],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[3][2]),
    )
    b_15.grid(ipadx=5, ipady=5, row=3, column=2)
    b_16 = tk.Button(
        master=frame,
        text=operator_list[3][3],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[3][3]),
    )
    b_16.grid(ipadx=5, ipady=5, row=3, column=3)
    b_17 = tk.Button(
        master=frame,
        text=operator_list[4][0],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[4][0]),
    )
    b_17.grid(ipadx=5, ipady=5, row=4, column=0)
    b_18 = tk.Button(
        master=frame,
        text=operator_list[4][1],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[4][1]),
    )
    b_18.grid(ipadx=5, ipady=5, row=4, column=1)
    b_19 = tk.Button(
        master=frame,
        text=operator_list[4][2],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[4][2]),
    )
    b_19.grid(ipadx=5, ipady=5, row=4, column=2)
    b_20 = tk.Button(
        master=frame,
        text=operator_list[4][3],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[4][3]),
    )
    b_20.grid(ipadx=5, ipady=5, row=4, column=3)
    b_21 = tk.Button(
        master=frame,
        text=operator_list[5][0],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[5][0]),
    )
    b_21.grid(ipadx=5, ipady=5, row=5, column=0)
    b_22 = tk.Button(
        master=frame,
        text=operator_list[5][1],
        relief=tk.FLAT,
        command=lambda: inp(operator_list[5][1]),
    )
    b_22.grid(ipadx=5, ipady=5, row=5, column=1)
    b_23 = tk.Button(
        master=frame, text=operator_list[5][2], relief=tk.FLAT, command=backspace
    )
    b_23.grid(ipadx=5, ipady=5, row=5, column=2)
    b_24 = tk.Button(
        master=frame, text=operator_list[5][3], relief=tk.FLAT, command=evaluate
    )
    b_24.grid(ipadx=5, ipady=5, row=5, column=3)

    window.mainloop()
