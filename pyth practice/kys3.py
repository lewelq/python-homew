
class Archive:
   # _instance = None
   # archive_text = []
   # archive_number = []

    def __new__(cls, text: str, number: float):
        #if cls._instance is None:
         #   cls._instance = super().__new__(cls)
        #else:
         #   cls.archive_text.append(super().__new__(cls))
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        cls._instance.archive_text.append(text)
        cls._instance.archive_number.append(number)
        #cls.archive_text.append(cls.text)
        #cls.archive_number.append(cls.number)
        return cls._instance
        #print(cls._instance)

    def __init__(self, text: str, number: float):
        self.text = text
        self.number = number
        
       # print(f"Text is {self.text} and number is {self.number}, {self.archive_text}")

    def __repr__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)
#print(id(archive1), id(archive2))
print(archive1)