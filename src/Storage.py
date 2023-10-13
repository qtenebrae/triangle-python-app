import os


class Storage:
    """Класс, представляющий хранилище.

    Attributes:
        version (str): Версия системы.

    Methods:
        get_version(): Возвращает версию системы.
    """

    def __init__(self):
        """Инициализирует экземпляр класса Storage."""
        self.version = None
        self.help = None
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.read_version()
        self.read_help()

    def read_version(self):
        """Метод для чтения версии из файла."""
        with open(os.path.join(self.root_dir, '..', 'docs', 'version.txt'), 'r') as f:
            self.version = f.readline()

    def get_version(self):
        """Возвращает версию системы.

        Returns:
            str: Версия системы.
        """
        return self.version

    def read_help(self):
        """Метод для чтения справки из файла."""
        with open(os.path.join(self.root_dir, '..', 'docs', 'help.txt'), 'r') as f:
            self.help = f.read()

    def get_help(self):
        """Возвращает текст справку.

        Returns:
            str: Текст справки.
        """
        return self.help
