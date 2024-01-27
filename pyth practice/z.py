import tkinter as tk
from tkinter import WORD, Label, filedialog
import pygments.lexers
from chlorophyll import CodeView
from spellchecker import SpellChecker
import re

spell = SpellChecker()

#Параметры текста по умолчанию
font_default = "Times New Roman"
size_default = 14
additional_default = "bold"

def open_file():
    # Функция открытия файла
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text_editor.delete('1.0', tk.END)
        text_editor.insert('1.0', file.read())

def save_file():
    # Функция сохраниения файла
    file_path = filedialog.asksaveasfilename()
    with open(file_path, 'w') as file:
        file.write(text_editor.get('1.0', tk.END))

def change_theme(theme):
    # Функция для изменения цветовой темы
    text_editor["color_scheme"] = theme_variants[theme]["color_scheme"]
    #text_editor["fg"] = theme_variants[theme]["fg"]
    #text_editor["insertbackground"] = theme_variants[theme]["cursor"]
    #text_editor["selectbackground"] = theme_variants[theme]["select"]

def change_font_size(size):
    # Функция для измениения размера текста
    global size_default
    size_default = size
    text_editor.config(font=(font_default, size_default, additional_default))

def change_font_style(fonts):
    # Функция для измениения шрифта
    global font_default
    font_default = fonts_change[fonts]["font"][0]
    text_editor.config(font=(font_default, size_default, additional_default))

def find_text(text_to_find):
    # Функция для поиска текста
    start_index = "1.0"
    while True:
        start_index = text_editor.search(text_to_find, start_index, stopindex=tk.END)
        if not start_index:
            break
        end_index = f"{start_index}+{len(text_to_find)}c"
        text_editor.tag_add("found", start_index, end_index)
        start_index = end_index
    text_editor.tag_config("found", background="yellow")

def replace_text(text_to_find, replacement_text):
    # Функция для замены текста
    find_text(text_to_find)
    text_editor.mark_set("insert", "1.0")
    text_editor.delete("found.first", "found.last")
    text_editor.insert("insert", replacement_text)

def undo_action():
    # Функция для отмены действия
    text_editor.edit_undo()

def redo_action():
    # Функция для повтора действия
    text_editor.edit_redo()

def toggle_line_numbers():
    # Функция для переключения отображения номеров строк
    if text_editor.tag_ranges("linenumbers"):
        text_editor.tag_remove("linenumbers", "1.0", "end")
    else:
        for i in range(1, int(text_editor.index("end").split(".")[0]) + 1):
            text_editor.insert(f"{i}.0", f"{i}\n")
        text_editor.tag_add("linenumbers", "1.0", "end")

def toggle_multiline_selection():
    # Функция для переключения многострочного выделения
    text_editor.tag_add("sel", "1.0", "3.0")

def dev_mode_python():
    # Подсветка синтаксиса Python
    global text_editor
    text_editor.configure(lexer=pygments.lexers.PythonLexer)
    return text_editor

def dev_mode_cpp():
    # Подсветка синтаксиса C++
    global text_editor
    text_editor.configure(lexer=pygments.lexers.CppLexer)
    return text_editor

def default_mode():
    # Режим блокнота
    global text_editor
    text_editor.configure(lexer=' ')
    return text_editor

def mistakes_mode():
    text = text_widget.get("1.0", "end-1c")
    words = re.findall(r'\b\w+\b', text)
    for word in words:
        if word.lower() not in spell:
            start = "1.0"
            while True:
                pos = text_widget.search(word, start, stopindex="end", nocase=1)
                if not pos:
                    break
                end = f"{pos}+{len(word)}c"
                text_widget.tag_add("error", pos, end)
                start = end

root = tk.Tk()
root.title("TextsMaster")





#Параметры по умолчанию
text_editor = CodeView(
    root,
    #bg='white',
    #fg ='black',
    height=30, 
    width=100, 
    undo=True, 
    #insertbackground="black", 
    #selectbackground="#C4C4C4", 
    spacing3=10, 
    wrap=WORD, 
    pady=10, 
    padx=10,
    color_scheme="ayu-light",
    font=(font_default, size_default, additional_default)
)

text_editor.pack(fill="both", expand=True)

#Варианты шрифтов
fonts_change = {
    "TimesNewRoman": {
        "font": ("Times New Roman", size_default, "bold")
    },
    "Arial": {
        "font": ("Arial", size_default, "bold")
    }
}

#Варианты цветовых тем
theme_variants = {
    "dark":{
        "color_scheme": "dracula",
    },
    "light":{
        "color_scheme": "ayu-light",
    }
} 



#Файл
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Выход", command=root.quit)
menu_bar.add_cascade(label="Файл", menu=file_menu)

#Правка
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Найти", command=find_text)
edit_menu.add_command(label="Заменить", command=replace_text)
edit_menu.add_separator()
menu_bar.add_cascade(label="Правка", menu=edit_menu)

#Вид
view_menu = tk.Menu(menu_bar, tearoff=0)
font_menu = tk.Menu(view_menu, tearoff=0)
theme_menu = tk.Menu(view_menu, tearoff=0)
font_size_menu = tk.Menu(view_menu, tearoff=0)

#Вид / Изменить цветовую тему
theme_menu.add_command(label="Светлая", command=lambda: change_theme("light")) #Светлая
theme_menu.add_command(label="Темная", command=lambda: change_theme("dark")) #Темная
view_menu.add_cascade(label="Изменить цветовую тему", menu=theme_menu) #Добавить подменю темы

#Вид / Изменить размер текста
font_size_menu.add_command(label="Мелкий", command=lambda: change_font_size(10))
font_size_menu.add_command(label="Средний", command=lambda: change_font_size(14))
font_size_menu.add_command(label="Крупный", command=lambda: change_font_size(18))
view_menu.add_cascade(label="Изменить размер текста", menu=font_size_menu)

#Вид / Изменить шрифт
font_menu.add_command(label="Times New Roman", command=lambda: change_font_style("TimesNewRoman"))
font_menu.add_command(label="Arial", command=lambda: change_font_style("Arial"))
view_menu.add_cascade(label="Изменить шрифт", menu=font_menu)

view_menu.add_separator()
view_menu.add_command(label="Показать/скрыть номера строк", command=toggle_line_numbers)
view_menu.add_command(label="Многострочное выделение", command=toggle_multiline_selection)
menu_bar.add_cascade(label="Вид", menu=view_menu)

#Специальные возможности
special_menu = tk.Menu(menu_bar, tearoff=0)
dev_mode = tk.Menu(special_menu, tearoff=0)
mistakes_mode = tk.Menu(special_menu, tearoff=0)
menu_bar.add_cascade(label="Специальные возможности", menu=special_menu)
dev_mode.add_command(label="Блокнот", command=default_mode)
dev_mode.add_command(label="Python", command=dev_mode_python)
dev_mode.add_command(label="C++", command=dev_mode_cpp)
special_menu.add_cascade(label="Для разработчиков", menu=dev_mode)
special_menu.add_command(label="Режим исправления ошибок")


# Подменю для отмены и возврата действия
edit_undo_redo_menu = tk.Menu(menu_bar, tearoff=0)
edit_undo_redo_menu.add_command(label="Отменить", command=undo_action)
edit_undo_redo_menu.add_command(label="Вернуть", command=redo_action)

# Добавление подменю в меню "Правка"
menu_bar.add_cascade(label="Отмена/Возврат", menu=edit_undo_redo_menu)

root.config(menu=menu_bar)

root.mainloop()
