from tkinter import *
from tkinter.messagebox import *
listOfButtons = []
##################################
    
inCalcValue = ""

root = Tk() 
root.title("Basic calculator")
#root.config(bg="cyan")
root.geometry("205x320")







listOfNum = []
for i in range(10):
    listOfNum.append(i)
    listOfButtons.append(Button(root,text=str(i), height = 4, width = 4))
                        
    listOfButtons[i]["command"] = lambda x = listOfNum[i]:returnButtonValue(x)

indexList = [[2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3], [5,1]]

for item,num in zip(listOfButtons,indexList):
    item.grid(row = num[0],column = num[1],sticky=W)


    
consoleDisplayVar = StringVar()     
text_box = Entry(root,textvariable = consoleDisplayVar,justify = RIGHT)

consoleDisplayVar.set(0)

text_box.grid(row = 1, column = 1,columnspan = 3, pady = 5)


multiply = Button(root,text="*", height = 4, width = 4,command = lambda x = "*":returnButtonValue(x))
multiply.grid(row = 2,column=4)

clear = Button(root,text="C", height = 4, width = 4,command = lambda : clear())
clear.grid(row = 2,column=5)

divide = Button(root,text="/", height = 4, width = 4,command = lambda x = "/":returnButtonValue(x))
divide.grid(row = 3,column=4)

add = Button(root,text="+", height = 4, width = 4,command = lambda x = "+":returnButtonValue(x))
add.grid(row = 4,column=4)

minus = Button(root,text="-", height = 4, width = 4,command = lambda x = "-":returnButtonValue(x))
minus.grid(row = 5,column=4)

equals = Button(root,text="=", height = 4, width = 4,command = lambda: equals())
equals.grid(row = 5,column=3)

decimalPoint = Button(root,text=".", height = 4, width = 4,command = lambda x = ".":returnButtonValue(x))
decimalPoint.grid(row = 5,column=2)

openBrackets = Button(root,text="(", height = 4, width = 4,command = lambda x = "(":returnButtonValue(x))
openBrackets.grid(row = 4,column=5)

closeBrackets = Button(root,text=")", height = 4, width = 4,command = lambda x = ")":returnButtonValue(x))
closeBrackets.grid(row = 5,column=5)




def clear():
    global inCalcValue
    consoleDisplayVar.set("")
    inCalcValue = ""

def equals():
    global inCalcValue
    equation = consoleDisplayVar.get()
    consoleDisplayVar.set(str(eval(equation)))
    inCalcValue = str(eval(equation))


inCalcValue = "0"

def returnButtonValue(value):
    global inCalcValue
    if consoleDisplayVar.get() == "0":
        consoleDisplayVar.set(str(value))
        inCalcValue = str(value)
    else:   
        #print(value)
        value = str(value)
        temp = inCalcValue+value
        consoleDisplayVar.set(temp)
        inCalcValue = temp
    


    
root.mainloop()
