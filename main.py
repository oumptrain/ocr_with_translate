import easyocr
import pyautogui
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("250x250")


def minimize():
    root.iconify()
    text_recognition()

def screenshot():
    file_path = "/home/ou/PycharmProjects/ocr/image.png"
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(r'{}'.format(file_path))


def translate():
    pass

def text_recognition():

    new_window = Toplevel(root)
    new_window.geometry("1920x1080")

    #menubar
    menubar = Menu(new_window)
    new_window.config(menu=menubar)

    #menu
    file_menu = Menu(menubar, tearoff=False)

    file_menu.add_command(label='Multitran', command=translate)
    file_menu.add_command(label='Cambridge', command=translate)
    file_menu.add_command(label='Urban', command=translate)

    menubar.add_cascade(
        label="Перевод",
        menu=file_menu
    )

    screenshot()
    bg = tk.PhotoImage(file='image.png')
    text_file_name = "test.txt"

    # # чтение с экрана
    lunaWindowLabel = Label(new_window, image=bg, bd=5)
    lunaWindowLabel.pack(padx=10, pady=10, side=RIGHT)
    lunaWindowLabel.image = bg  # this is required.


    reader = easyocr.Reader(["ru", "en"])
    result = reader.readtext("/home/ou/PycharmProjects/ocr/image.png", detail=1)
    index_result = 0
    with open(text_file_name, "w") as file:
        for line in result:
            file.write(f"{line}\n")
            text = list(result[index_result])[1]
            x = list(list(list(result[index_result])[0])[0])[0]
            y = list(list(list(result[index_result])[0])[0])[1]
            s = tk.StringVar()
            s.set(text)
            entry = tk.Entry(new_window, text=s, state='readonly', bg="#9e87b9", width=len(text))
            entry.place(x=x, y=y)

            index_result += 1

    pass


def main():
    label = Label(root,
                  text="Рабочая зона")

    label.pack(pady=10)

    # a button widget which will open a
    # new window on button click
    btn = Button(root,
                 text="Make a screenshot",
                 command=minimize)

    btn.pack(pady=10)

    # mainloop, runs infinitely
    mainloop()


if __name__ == "__main__":
    main()
