from tkinter import *
from MovingBall import MovingBall


class App(Tk):
    """
    Класс для создания приложения с движущимся шариком в треугольной области.

    Args:
        validator: объект класса Validator для проверки входных данных.
        storage: объект класса Storage для хранения данных.
        controller: объект класса Controller для управления приложением.
    """

    def __init__(self, validator, storage, controller):
        Tk.__init__(self)
        self.moving_ball = None
        self.validator = validator
        self.storage = storage
        self.controller = controller
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.window_width = round(self.screen_width / 4 * 3)
        self.window_height = round(self.screen_height / 4 * 3)

        self.x = round((self.screen_width - self.window_width) // 2)
        self.y = round((self.screen_height - self.window_height) // 2)

        self.geometry('{}x{}+{}+{}'.format(self.window_width, self.window_height, self.x, self.y))
        self.title("Движение абсолютно упругого шарика в треугольной области")
        self.resizable(False, False)

        self.menu_bar = Menu(self)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Старт", command=self.start)
        self.file_menu.add_command(label="Стоп", command=self.stop)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.quit)
        self.menu_bar.add_cascade(label="Окно", menu=self.file_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Справка", command=self.modal_help)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="О программе", command=self.modal_about)
        self.menu_bar.add_cascade(label="Справка", menu=self.help_menu)

        self.config(menu=self.menu_bar)

        self.version_label = Label(self, text=controller.get_version(storage))
        self.version_label.config(bg="medium aquamarine", fg="black", padx=10, pady=3)
        self.version_label.pack(side="right", anchor="se")

        self.pict = Frame(self)
        self.manage = Frame(self)
        self.pict.pack(side=LEFT)
        self.manage.pack(side=RIGHT)

        self.canvas = Canvas(self.pict, width=round(self.window_width / 3 * 2), height=self.window_height)
        self.canvas.create_rectangle(40, 40, round(self.window_width / 3 * 2) - 40, self.window_height - 40,
                                     outline='#000', fill='#fff')
        self.canvas.pack()

        self.canvasTopLeft_label = Label(self, text='x={}, y={}'.format(0, 0))
        self.canvasTopLeft_label.place(x=10, y=10)

        self.canvasDownRight_label = Label(self, text='x={}, y={}'.format(round(self.window_width / 3 * 2) - 40,
                                                                          self.window_height - 40))
        self.canvasDownRight_label.place(x=round(self.window_width / 3 * 2) - 35, y=self.window_height - 35)

        self.canvasDownLeft_label = Label(self, text='x={}, y={}'.format(0, self.window_height - 40))
        self.canvasDownLeft_label.place(x=10, y=self.window_height - 35)

        self.canvasTopRight_label = Label(self, text='x={}, y={}'.format(round(self.window_width / 3 * 2) - 40, 0))
        self.canvasTopRight_label.place(x=round(self.window_width / 3 * 2) - 35, y=10)

        self.var_x1 = IntVar()
        self.var_y1 = IntVar()
        self.var_x2 = IntVar()
        self.var_y2 = IntVar()
        self.var_x3 = IntVar()
        self.var_y3 = IntVar()
        self.var_x = IntVar()
        self.var_y = IntVar()
        self.var_vx = IntVar()
        self.var_vy = IntVar()
        self.reset()

        self.x1y1_coordinate_label = Label(self.manage, text='Координаты вершины 1', font=("Arial", 20))
        self.x1y1_coordinate_label.grid(row=0, columnspan=2, pady=10)

        self.x1_coordinate_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                         textvariable=self.var_x1)
        self.x1_coordinate_entry.bind("<FocusIn>", self.save_old_value)
        self.x1_coordinate_entry.bind("<FocusOut>", self.validate)
        self.x1_coordinate_entry.grid(row=1, column=0)
        self.y1_coordinate_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                         textvariable=self.var_y1)
        self.y1_coordinate_entry.bind("<FocusIn>", self.save_old_value)
        self.y1_coordinate_entry.bind("<FocusOut>", self.validate)
        self.y1_coordinate_entry.grid(row=1, column=1)

        self.x2y2_coordinate_label = Label(self.manage, text='Координаты вершины 2', font=("Arial", 20))
        self.x2y2_coordinate_label.grid(row=2, columnspan=2, pady=10)

        self.x2_coordinate_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                         textvariable=self.var_x2)
        self.x2_coordinate_entry.bind("<FocusIn>", self.save_old_value)
        self.x2_coordinate_entry.bind("<FocusOut>", self.validate)
        self.x2_coordinate_entry.grid(row=3, column=0)
        self.y2_coordinate_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                         textvariable=self.var_y2)
        self.y2_coordinate_entry.bind("<FocusIn>", self.save_old_value)
        self.y2_coordinate_entry.bind("<FocusOut>", self.validate)
        self.y2_coordinate_entry.grid(row=3, column=1)

        self.x3y3_coordinate_label = Label(self.manage, text='Координаты вершины 3', font=("Arial", 20))
        self.x3y3_coordinate_label.grid(row=4, columnspan=2, pady=10)

        self.x3_coordinate_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                         textvariable=self.var_x3)
        self.x3_coordinate_entry.bind("<FocusIn>", self.save_old_value)
        self.x3_coordinate_entry.bind("<FocusOut>", self.validate)
        self.x3_coordinate_entry.grid(row=5, column=0)
        self.y3_coordinate_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                         textvariable=self.var_y3)
        self.y3_coordinate_entry.bind("<FocusIn>", self.save_old_value)
        self.y3_coordinate_entry.bind("<FocusOut>", self.validate)
        self.y3_coordinate_entry.grid(row=5, column=1)

        self.center_circle_label = Label(self.manage, text='Координаты центра шарика', font=("Arial", 20))
        self.center_circle_label.grid(row=6, columnspan=2, pady=10)

        self.x_circle_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center', textvariable=self.var_x)
        self.x_circle_entry.bind("<FocusIn>", self.save_old_value)
        self.x_circle_entry.bind("<FocusOut>", self.validate)
        self.x_circle_entry.grid(row=7, column=0)

        self.y_circle_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center', textvariable=self.var_y)
        self.y_circle_entry.bind("<FocusIn>", self.save_old_value)
        self.y_circle_entry.bind("<FocusOut>", self.validate)
        self.y_circle_entry.grid(row=7, column=1)

        self.velocity_circle_label = Label(self.manage, text='Скорость шарика', font=("Arial", 20))
        self.velocity_circle_label.grid(row=8, columnspan=2, pady=10)

        self.x_velocity_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                      textvariable=self.var_vx)
        self.x_velocity_entry.bind("<FocusIn>", self.save_old_value)
        self.x_velocity_entry.bind("<FocusOut>", self.validate)
        self.x_velocity_entry.grid(row=9, column=0)
        self.y_velocity_entry = Entry(self.manage, width=5, font=("Arial", 20), justify='center',
                                      textvariable=self.var_vy)
        self.y_velocity_entry.bind("<FocusIn>", self.save_old_value)
        self.y_velocity_entry.bind("<FocusOut>", self.validate)
        self.y_velocity_entry.grid(row=9, column=1)

        self.start_button = Button(self.manage, text='Старт', font=("Arial", 20), background='#ccc', command=self.start)
        self.start_button.grid(row=10, column=0, pady=20)

        self.stop_button = Button(self.manage, text='Стоп', font=("Arial", 20), background='#ccc', command=self.stop)
        self.stop_button.grid(row=10, column=1, pady=20)

        self.reset_button = Button(self.manage, text='Значения по умолочанию', font=("Arial", 20), background='#ccc',
                                   command=self.reset)
        self.reset_button.grid(row=11, columnspan=3, pady=20)

    def start(self):
        """Метод для запуска движения шарика на холсте."""
        self.moving_ball = MovingBall(self.canvas, self.var_x1.get(), self.var_y1.get(), self.var_x2.get(),
                                      self.var_y2.get(), self.var_x3.get(), self.var_y3.get(), self.var_x.get(),
                                      self.var_y.get(), self.var_vx.get(), self.var_vy.get())
        self.moving_ball.move_ball()

    def stop(self):
        """Метод для остановки движения шарика на холсте."""
        self.moving_ball.clear_ball()
        self.canvas.create_rectangle(40, 40, round(self.window_width / 3 * 2) - 40, self.window_height - 40,
                                     outline='#000', fill='#fff')

    def reset(self):
        """Метод для сброса значений переменных на исходные."""
        self.var_x1.set(0)
        self.var_y1.set(0)
        self.var_x2.set(920)
        self.var_y2.set(0)
        self.var_x3.set(0)
        self.var_y3.set(770)
        self.var_x.set(100)
        self.var_y.set(100)
        self.var_vx.set(10)
        self.var_vy.set(10)

    def validate(self, event):
        """Метод для проверки валидности введенных данных в виджете.

        Args:
            event: объект события.
        """
        value = event.widget.get()
        if not self.validator.validate_int(value):
            event.widget.delete(0, END)
            event.widget.insert(0, event.widget.old_value)

    def save_old_value(self, event):
        """Метод для сохранения предыдущего значения виджета.

        Args:
            event: объект события.
        """
        event.widget.old_value = event.widget.get()

    def modal_help(self):
        """Метод для вывода модального окна с текстом справки."""
        modal_window = Toplevel()
        modal_window.transient(self)
        modal_window.grab_set()
        modal_window.title("Справка")
        modal_window.geometry("700x200")
        modal_window.resizable(False, False)
        label = Label(modal_window, text=self.controller.get_help(self.storage))
        label.pack(pady=20)

        window_width = modal_window.winfo_width()
        window_height = modal_window.winfo_height()
        x = (self.screen_width - window_width) // 2
        y = (self.screen_height - window_height) // 2
        modal_window.geometry("+{}+{}".format(x, y))
        modal_window.mainloop()

    def modal_about(self):
        """Метод для вывода модального окна "О программе"."""
        modal_window = Toplevel()
        modal_window.transient(self)
        modal_window.grab_set()
        modal_window.title("О программе")
        modal_window.geometry("200x100")
        modal_window.resizable(False, False)
        label = Label(modal_window, text=self.controller.get_version(self.storage))
        label.pack(pady=20)

        window_width = modal_window.winfo_width()
        window_height = modal_window.winfo_height()
        x = (self.screen_width - window_width) // 2
        y = (self.screen_height - window_height) // 2
        modal_window.geometry("+{}+{}".format(x, y))
        modal_window.mainloop()
