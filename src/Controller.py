class Controller:
    """Класс, представляющий контроллер системы.

    Methods:
        get_version(storage): Возвращает версию системы.
    """

    def get_version(self, storage):
        """Возвращает версию системы.

        Args:
            storage (Storage): Экземпляр класса Storage.

        Returns:
            str: Версия системы.
        """
        return storage.get_version()

    def get_help(self, storage):
        """Возвращает текст справки.

        Args:
            storage (Storage): Экземпляр класса Storage.

        Returns:
            str: Текст справки.
        """
        return storage.get_help()
