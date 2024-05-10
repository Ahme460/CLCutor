from tkinter import *

class CLCutor:
    def __init__(self, result_label):
        self.result_label = result_label
    def plus(self, *args):
        current_text = self.result_label.get()
        if '/' in current_text:
            self.division()
        elif '-' in current_text:
            self.minus()
        elif '*' in current_text:
            self.odd()

        current_text=self.result_label.get()
        if '.' in current_text:
            numbers = list(map(float, current_text.split("+")))
        else:    
            numbers = list(map(int, current_text.split("+")))
        result=numbers[0]
        for i in numbers[1:]:
            result=result+i

        if result % 2 == 1:
         
            self.result_label.set(int(result))
        elif result % 2 == 0:
         
            self.result_label.set(int(result))
        else:
            self.result_label.set(float(result))

    def minus(self):
        current_text = self.result_label.get()
        
        # افترض أن النص عبارة عن عمليات طرح متتالية بالرمز "-"
        if '.' in current_text:
            numbers = list(map(float, current_text.split("-")))
        else:    
            numbers = list(map(int, current_text.split("-")))
        
      
        # قم بطرح الأرقام بشكل متتالي
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        
        if result % 2 == 1:
         
            self.result_label.set(int(result))
        elif result % 2 == 0:
         
            self.result_label.set(int(result))
        else:
            self.result_label.set(float(result))

    def odd(self):
        current_text=self.result_label.get()
        if '.' in current_text:
            numbers = list(map(float, current_text.split("*")))
        else:    
            numbers = list(map(int, current_text.split("*")))
        result=numbers[0]
        for i in numbers[1:]:
            result=result*i

        if result % 2 == 1:
         
            self.result_label.set(int(result))
        elif result % 2 == 0:
         
            self.result_label.set(int(result))
        else:
            self.result_label.set(float(result))
    
    def division (self):

        current_text=self.result_label.get()
        if '.' in current_text:
            numbers = list(map(float, current_text.split("/")))
        else:    
            numbers = list(map(int, current_text.split("/")))
        result=numbers[0]
        for i in numbers[1:]:
            result=result/i
    
        if result % 2 == 1:
         
            self.result_label.set(int(result))
        elif result % 2 == 0:
         
            self.result_label.set(int(result))
        else:
            self.result_label.set(float(result))

def button_click(number):
    current_text = result_label.get()
    if current_text == "0":
        result_label.set(number)
    else:
        result_label.set(current_text + number)


def clear():
    result_label.set("0")


def calculate():
    clc = CLCutor(result_label)
    clc.plus()
    clc.minus()
    clc.odd()
    clc.division()


# إنشاء نافذة الحاسبة
root = Tk()
root.title("Calculator")

# إنشاء وعرض عنصر العرض
result_label = StringVar()
result_label.set("0")
display_label = Label(root, textvariable=result_label, font=('Helvetica', 20), anchor="e", bd=5)
display_label.grid(row=0, column=0, columnspan=4)

# قائمة الأزرار
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
# إنشاء وعرض الأزرار
for (text, row, column) in buttons:
    if text == '=':
        button = Button(root, text=text, font=('Helvetica', 20), width=5, height=2, command=calculate)
    elif text == 'C':
        button = Button(root, text=text, font=('Helvetica', 20), width=5, height=2, command=clear)
    else:
        button = Button(root, text=text, font=('Helvetica', 20), width=5, height=2, command=lambda num=text: button_click(num))
    button.grid(row=row, column=column)

# تشغيل النافذة
root.mainloop()