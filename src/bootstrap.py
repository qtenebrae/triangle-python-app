from App import App


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
