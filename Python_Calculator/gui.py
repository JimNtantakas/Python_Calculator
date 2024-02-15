import tkinter as tk
import calculator

def result():
    expression=text.get("1.0",tk.END)
    #print(expression)
    s=calculator.calculate(str(expression))  
    text.delete("1.0", tk.END)
    text.insert(tk.END, str(s))

def insert(s):
    text.insert(tk.END,s)
def clear():
    text.delete("1.0",tk.END)
    

root=tk.Tk()
root.title("Calculator")
root.geometry('500x500') 
root["background"]="#385D9F"

frame = tk.Frame(root,height=150)
frame.pack(expand=True)
frame["background"]="#808080"
frame.pack_propagate(False)  # Disable geometry propagation

text=tk.Text(frame,height=1,width=50)
text.grid(columnspan=5, pady=25) 

btn16 = tk.Button(frame, text='AC', command=clear, width=10,bg='gray')
btn16.grid(row=1, column=1)
btn17 = tk.Button(frame, text='(', command=lambda: insert("("), width=10,bg='lightgray')
btn17.grid(row=1, column=2)
btn18 = tk.Button(frame, text=')', command=lambda: insert(")"), width=10,bg='lightgray')
btn18.grid(row=1, column=3)
btn19 = tk.Button(frame, text='/', command=lambda: insert("/"), width=10,bg='lightgray')
btn19.grid(row=1, column=4)

btn1=tk.Button(frame,text='7',command=lambda:insert("7"),width=10)
btn1.grid(row=2,column=1)
btn2=tk.Button(frame,text='8',command=lambda:insert("8"),width=10)
btn2.grid(row=2,column=2)
btn3=tk.Button(frame,text='9',command=lambda:insert("9"),width=10)
btn3.grid(row=2,column=3)
btn4=tk.Button(frame,text='*',command=lambda:insert("*"),width=10,bg='lightgray')
btn4.grid(row=2,column=4)

btn5=tk.Button(frame,text='4',command=lambda:insert("4"),width=10)
btn5.grid(row=3,column=1)
btn6=tk.Button(frame,text='5',command=lambda:insert("5"),width=10)
btn6.grid(row=3,column=2)
btn7=tk.Button(frame,text='6',command=lambda:insert("6"),width=10)
btn7.grid(row=3,column=3)
btn8=tk.Button(frame,text="-",command=lambda:insert("-"),width=10,bg='lightgray')
btn8.grid(row=3,column=4)

btn9=tk.Button(frame,text='1',command=lambda:insert("1"),width=10)
btn9.grid(row=4,column=1)
btn10=tk.Button(frame,text='2',command=lambda:insert("2"),width=10)
btn10.grid(row=4,column=2)
btn11=tk.Button(frame,text='3',command=lambda:insert("3"),width=10)
btn11.grid(row=4,column=3)
btn12=tk.Button(frame,text='+',command=lambda:insert("+"),width=10,bg='lightgray')
btn12.grid(row=4,column=4)

btn13=tk.Button(frame,text='0',command=lambda:insert("0"),width=25)
btn13.grid(row=5,column=1,columnspan=2)
btn14=tk.Button(frame,text=',',command=lambda:insert("."),width=10)
btn14.grid(row=5,column=3)
btn15=tk.Button(frame,text='=',command=result,width=10,bg='lightgray')
btn15.grid(row=5,column=4)

root.mainloop()