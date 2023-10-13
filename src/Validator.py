class Validator:
    """Класс, представляющий валидатор.

    Methods:
        validate_int(value): Проверяет, является ли значение целым числом.
    """

    def validate_int(self, value):
        """Проверяет, является ли значение целым числом.

        Args:
            value (str): Значение для проверки.

        Returns:
            bool: True, если значение является целым числом, False в противном случае.
        """
        return True if value.isdigit() else False
