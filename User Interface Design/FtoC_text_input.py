import tkinter as tk
import tkinter.ttk as ttk


# I decided to include functionality because I forgot to re-read the
# assignment before I started working on it.
def calcTemp(event):
    global outText
    global radioVar

    try:
        startTemp = float(inTemp.get())
        if radioVar.get() == 1:
            celsius = (startTemp - 32)*(5/9)
            celsius = round(celsius, 2)
            outTemp['text'] = str(celsius)
        else:
            fahrenheit = (startTemp * (9/5)) + 32
            fahrenheit = round(fahrenheit, 2)
            outTemp['text'] = str(fahrenheit)

    except:
        outTemp['text'] = "Whoops!"



window = tk.Tk()


# The radio buttons
radioVar = tk.IntVar(window, 1)
btnVals = {"F to C" : 1,
           "C to F" : 2,}
btnNum = 0
for (text, value) in btnVals.items():
    btnNum += 1
    currBtn = ttk.Radiobutton(window, text = text, variable = radioVar, 
                    value = value)
    currBtn.bind("<Button-1>", calcTemp)
    currBtn.grid(row = btnNum, column = 1, padx = 10, pady = 5)


# The in-Temperature entry field
inTemp = tk.Entry(width = 8)
inTemp.bind("<Key>", calcTemp)
inTemp.grid(row = 3, column = 0, padx = 4, pady = 5)


#The arrow
arrow = tk.Label(text = "\N{RIGHTWARDS BLACK ARROW}")
arrow.grid(row = 3, column = 1, padx = 2)


#And the output field
outTemp = tk.Label(text="", background="white", relief="raised", width=8)
outTemp.grid(row = 3, column = 2, pady = 5, padx=4)


window.mainloop()
