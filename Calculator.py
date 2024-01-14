import tkinter as tk

calculation=""

def evaluation(symbol):
    global calculation
    calculation += str(symbol)
    output_field.delete(1.0,"end")
    output_field.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
    
        output_field.delete(1.0,"end")
        output_field.insert(1.0,calculation)

    except:
        clear_field()
        output_field.insert(1.0,"ERROR")

def clear_field():
    global calculation
    calculation=""
    output_field.delete(1.0,"end")



root =tk.Tk()
root.title('Simple Calculator')
root.geometry('430x280')
root.resizable(width=False, height=False)

FONT=('NORMAL',15, 'bold')
output_field=tk.Text(root,height=2,width=32,font=FONT,bg='black',fg='red',borderwidth=10)
output_field.grid(columnspan=5,sticky=tk.NSEW)



button_CE=tk.Button(root,text='CE',command=clear_field,width=8,font=FONT,bg='pink',fg='black')
button_CE.grid(row=2,column=1,columnspan=2,sticky=tk.NSEW)

button_equal_to=tk.Button(root,font=FONT,text='=',command=evaluate_calculation,width=8,bg='pink',fg='black')
button_equal_to.grid(row=2,column=3,columnspan=2,sticky=tk.NSEW)

button_seven=tk.Button(root,font=FONT,text='7',command=lambda:evaluation(7),width=8,bg='pink',fg='black')
button_seven.grid(row=3,column=1,sticky=tk.NSEW)

button_eight=tk.Button(root,font=FONT,text='8',command=lambda:evaluation(8),width=8,bg='pink',fg='black')
button_eight.grid(row=3,column=2,sticky=tk.NSEW)

button_nine=tk.Button(root,font=FONT,text='9',command=lambda:evaluation(9),width=8,bg='pink',fg='black')
button_nine.grid(row=3,column=3,sticky=tk.NSEW)

button_four=tk.Button(root,font=FONT,text='4',command=lambda:evaluation(4),width=8,bg='pink',fg='black')
button_four.grid(row=4,column=1,sticky=tk.NSEW)

button_five=tk.Button(root,font=FONT,text='5',command=lambda:evaluation(5),width=8,bg='pink',fg='black')
button_five.grid(row=4,column=2,sticky=tk.NSEW)

button_six=tk.Button(root,font=FONT,text='6',command=lambda:evaluation(6),width=8,bg='pink',fg='black')
button_six.grid(row=4,column=3,sticky=tk.NSEW)

button_one=tk.Button(root,font=FONT,text='1',command=lambda:evaluation(1),width=8,bg='pink',fg='black')
button_one.grid(row=5,column=1,sticky=tk.NSEW)

button_two=tk.Button(root,font=FONT,text='2',command=lambda:evaluation(2),width=8,bg='pink',fg='black')
button_two.grid(row=5,column=2,sticky=tk.NSEW)

button_three=tk.Button(root,font=FONT,text='3',command=lambda:evaluation(3),width=8,bg='pink',fg='black')
button_three.grid(row=5,column=3,sticky=tk.NSEW)

button_zero=tk.Button(root,font=FONT,text='0',command=lambda:evaluation(0),width=8,bg='pink',fg='black')
button_zero.grid(row=6,column=1,columnspan=2,sticky=tk.NSEW)

button_dot=tk.Button(root,font=FONT,text='.',command=lambda:evaluation("."),width=8,bg='pink',fg='black')
button_dot.grid(row=6,column=3,sticky=tk.NSEW)

button_plus=tk.Button(root,font=FONT,text='+',command=lambda:evaluation("+"),width=7,bg='pink',fg='black')
button_plus.grid(row=3,column=4,sticky=tk.NSEW)

button_minus=tk.Button(root,font=FONT,text='-',command=lambda:evaluation("-"),width=8,bg='pink',fg='black')
button_minus.grid(row=4,column=4,sticky=tk.NSEW)

button_mul=tk.Button(root,font=FONT,text='x',command=lambda:evaluation("*"),width=8,bg='pink',fg='black')
button_mul.grid(row=5,column=4,sticky=tk.NSEW)

button_divide=tk.Button(root,font=FONT,text='/',command=lambda:evaluation("/"),width=8,bg='pink',fg='black')
button_divide.grid(row=6,column=4,sticky=tk.NSEW)

root.mainloop()

