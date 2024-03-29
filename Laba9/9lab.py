from tkinter import *
import hashlib

class Program:
    def __init__(self):
        open('File.txt', 'a').close()
        self.window = Tk()
        self.window.title('Добрый день, пользователь!')
        window = self.window
        window.eval('tk::PlaceWindow . center')
        window.geometry('300x250')
        window.configure(background='#849974')
        Label(window, text='', background='#849974').pack()
        Label(window, text='', background='#849974').pack()
        Button(window, font=14, text="Регистрация", command=self.start).pack()
        Label(window, text='', background='#849974').pack()
        Button(window, font=14, text="Вход", command=self.start_2).pack()
        but=Button(window, text="Выход", command=window.destroy)
        but.config( font=('Helvetica', 12))
        Label(window, text='', background='#849974').pack()
        but.pack()
        self.window.mainloop()

    def window_entry(self, description):
        Label(self.window, text=description).pack()
        entry = Entry(self.window, font=14, width=20, justify='center')
        entry.pack()
        return entry

    def wind_entry(self, description):
        Label(self.wind, font=14, text=description).pack()
        entry = Entry(self.wind, font=14, width=20, justify='center')
        entry.pack()
        return entry

    def wind_start(self, title, log, passw, command):
        self.window.destroy()
        self.wind = Tk()
        self.wind.title(title)
        wind = self.wind
        wind.eval('tk::PlaceWindow . center')
        wind.geometry('300x200')
        wind.configure(background='#849974')

        self.login_user = self.wind_entry(log)
        Label(wind, text='', background='#849974').pack()
        self.password_user = self.wind_entry(passw)
        Label(wind, text='', background='#849974').pack()
        Button(wind, font=14, text="Продолжить", command=command).pack()

    def start(self):
        self.wind_start('Регистрация', 'Придумайте логин', 'Придумайте пароль', self.write_txt)

    def start_2(self):
        self.wind_start('Вход', 'Введите логин', 'Введите пароль', self.open_txt)

    def open_txt(self):
        NotFound = True
        with open('File.txt', 'r') as f:
            read = f.readlines()
            password_sha = hashlib.sha1(str.encode(self.password_user.get())).hexdigest()
            for i in range(1, len(read), 2):
                if self.login_user.get() == read[i].rstrip('\n') and password_sha == read[i + 1].rstrip('\n'):
                    Program.text_window('Вы успешно авторизовались', 'Авторизация')
                    self.wind.destroy()
                    NotFound = False
                    break
                if self.login_user.get() == '' or self.password_user.get() == '':
                    Program.text_window('Вы оставили поле пустым.')
                    return
        if NotFound == True:
            Program.text_window('Не удалось авторизоваться. Не подходящие логин или пароль.')

    def write_txt(self):
        with open('File.txt', 'r') as f:
            read = f.readlines()
            for i in range(1, len(read), 2):
                if self.login_user.get() == read[i].rstrip('\n'):
                    Program.text_window('Выбранный вами логин уже используется.')
                    return
            if self.login_user.get() == '' or self.password_user.get() == '':
                Program.text_window('Вы оставили поле пустым.')
                return
        with open('File.txt', 'a') as f:
            Program.text_window('Вы успешно зарегистрировались и вошли.', 'Регистрация')
            f.write('\n' + self.login_user.get() + '\n' + hashlib.sha1(str.encode(self.password_user.get())).hexdigest())
            f.close()
            self.wind.destroy()

    def text_window(message, title = None):  # функция для вывода текста об ошибке
        window = Tk()
        if title != None:
            window.title(title)
        else:
            window.title('Ошибка')
        Label(window, font=14, text=message).pack()
        window.eval('tk::PlaceWindow . center')

program = Program()