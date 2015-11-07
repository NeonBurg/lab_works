#Лабораторная 1
#Щавровского Николая
#РИС-13

from Tkinter import *

root = Tk()

x = {
                        "name": { "value": ""},
                        "age": { "value": 0}
                }

def f():
                for element in x.keys():
                        print(element, x[element])

for element in x.keys():
                Label(root, text = element).pack()
                #t = type(x[element]["value"])
                t = x[element]["value"]
                if type(t) is int:
                        x[element]["var"] = IntVar()
                elif isinstance(t, str):
                        x[element]["var"] = StringVar()
                else:
                        raise TypeError

                x[element]["entry"] = Entry(root, textvariable = x[element]["var"])
                x[element]["entry"].pack()

Button(root, text='Ok', command=f).pack()

root.mainloop()

