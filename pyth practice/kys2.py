from datetime import datetime

class MyStr(str):

    def __new__(cls, value: str, author: str, time = None):
        if time is None:
            time = datetime.now().strftime('%Y-%m-%d %H:%M')
        obj = super().__new__(cls, value)
        #obj.value = value
        obj.author = author
        obj.time = time
        return obj
    
    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: [{self.time}])"
    
    def __repr__(self):
        return f"MyStr('{super().__repr__()}',{self.author}"
    

my_string = MyStr("Заключительный текст", "Достоевский")
print(my_string)