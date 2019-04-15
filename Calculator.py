import tkinter as tk
window = tk.Tk()
window.title("Calulator")
output = tk.Entry(window, width="50")
output.pack()
def button1 ():
    output.insert("end", "1")
def button2 ():
    output.insert("end", "2")
def button3 ():
    output.insert("end", "3")
def button4 ():
    output.insert("end", "4")
def button5 ():
    output.insert("end", "5")
def button6 ():
    output.insert("end", "6")
def button7 ():
    output.insert("end", "7")
def button8 ():
    output.insert("end", "8")
def button9 ():
    output.insert("end", "9")
def button0 ():
    output.insert("end", "0")
def buttonplus ():
    output.insert("end"," + ")
def buttonminus ():
    output.insert("end"," - ")
def buttontimes ():
    output.insert("end"," * ")
def buttonex ():
    output.insert("end"," ** ")
def buttondivide ():
    output.insert("end"," / ")
def buttonequal ():
    string = output.get()
    answer = eval(string)
    output.delete(0, "end")
    output.insert("end", answer)
def buttonclear ():
    output.delete(0, "end")
def deletelast ():
    output.delete(1,"end")
button1 = tk.Button(window, text="1", command=button1)
button1.pack(side="left")
button2 = tk.Button(window, text="2", command=button2)
button2.pack(side="left")
button3 = tk.Button(window, text="3", command=button3)
button3.pack(side="left")
button4 = tk.Button(window, text="4", command=button4)
button4.pack(side="left")
button5 = tk.Button(window, text="5", command=button5)
button5.pack(side="left")
button6 = tk.Button(window, text="6", command=button6)
button6.pack(side="left")
button7 = tk.Button(window, text="7", command=button7)
button7.pack(side="left")
button8 = tk.Button(window, text="8", command=button8)
button8.pack(side="left")
button9 = tk.Button(window, text="9", command=button9)
button9.pack(side="left")
button0 = tk.Button(window, text="0", command=button0)
button0.pack(side="left")
buttonplus = tk.Button(window, text="+", command=buttonplus)
buttonplus.pack(side="left")
buttonminus = tk.Button(window, text="-", command=buttonminus)
buttonminus.pack(side="left")
buttondivide = tk.Button(window, text="/", command=buttondivide)
buttondivide.pack(side="left")
buttontimes = tk.Button(window, text="*", command=buttontimes)
buttontimes.pack(side="left")
buttonequal = tk.Button(window, text="=", command=buttonequal)
buttonequal.pack(side="left")
buttonex = tk.Button(window, text="exponent", command=buttonex)
buttonex.pack(side="left")
buttonclear = tk.Button(window, text="clear", command=buttonclear)
buttonclear.pack(side="left")
delete = tk.Button(window, text="delete", command=deletelast)
delete.pack()
window.mainloop()
