from App import App
from Controller import Controller
from Storage import Storage
from Validator import Validator


def bootstrap(validator, storage, controller):
    """Создает и возвращает экземпляр класса App.

    Args:
        validator (Validator): Экземпляр класса Validator.
        storage (Storage): Экземпляр класса Storage.
        controller (Controller): Экземпляр класса Controller.

    Returns:
        App: Экземпляр класса App.
    """
    return App(validator, storage, controller)


def main():
    """Основная функция программы.

    Создает экземпляры классов Validator, Storage и Controller,
    и передает их в функцию bootstrap для создания экземпляра класса App.
    Затем запускает главный цикл экземпляра App.
    """
    validator = Validator()
    storage = Storage()
    controller = Controller()
    app = bootstrap(validator, storage, controller)
    app.mainloop()


if __name__ == "__main__":
    main()
