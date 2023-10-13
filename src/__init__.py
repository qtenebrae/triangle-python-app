from Controller import Controller
from Storage import Storage
from Validator import Validator
from bootstrap import bootstrap


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
