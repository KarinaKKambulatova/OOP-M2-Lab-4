import doctest

class SocialNetwork:
    """
    Базовый класс социальной сети.

    Пример свойства getter для атрибута name:
 >>> social_network = SocialNetwork('Facebook', 1852332, True)
 >>> name = social_network.name
 >>> print(name)
 Facebook
    """
    def __init__(self, name: str, user_count: int, log_in: bool):
        """
        Инициализация эксземпляра класса.
        :param name: Название социальной сети.
        :param user_count: Количество пользователей.
        :param log_in: Наличие авторизации пользователя.

        Пример:
        >>> social_network = SocialNetwork('Facebook', 1852332, True) #инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название сайта должно быть строкой")
        if not isinstance(user_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if not isinstance(log_in, bool):
            raise TypeError("Наличие авторизации должно быть булевым значением")
        if user_count < 0:
            raise ValueError("Количество пользователей должно быть неотрицательным")

        self.name = name
        self._user_count = user_count  # Приватный атрибут: количество пользователей не должно изменяться напрямую
        self.log_in = log_in

    def __str__(self):
        """
        Определение поведения магического метода __str__.
        :return: Определение поведения магического метода __str__.

        Пример:
        >>> social_network = SocialNetwork('Facebook', 1852332, True)
        >>> print(social_network)
        Сайт Facebook с 1852332 пользователями

        """
        return f'Сайт {self.name} с {self._user_count} пользователями'

    def __repr__(self):
        """
        Определение поведения магического метода __repr__.
        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> social_network = SocialNetwork('Facebook', 1852332, True)
        >>> print(f'{social_network!r}')
        SocialNetwork(name='Facebook', user_count=1852332)
        """
        return f'{self.__class__.__name__}(name={self.name!r}, user_count={self._user_count!r})'

    def access(self):
        """
        Метод, который определяет возможно ли получить доступ к сайту.

        Пример:
        >>> social_network = SocialNetwork('Facebook', 1852332, True)
        >>> social_network.access()
        Пользователь авторизован. Возможен доступ к сайту Facebook
        """
        if self.log_in:
            print(f'Пользователь авторизован. Возможен доступ к сайту {self.name}')
        else:
            print(f'Пользователь не авторизован. Невозможно получить доступ к сайту {self.name}')

class Facebook(SocialNetwork):
    """
    Дочерний класс соц. сетей.
    """
    def __init__(self, name: str, user_count: int, log_in: bool, right_password: str):
        """
        Инициализация экземпляра класса.
 Конструктор базового класса расширен, т.к. в дочернем классе больше аргументов, чем в базовом классе.
        :param name: Название класса.
        :param user_count: Количество пользователей.
        :param log_in: Наличие авторизации пользователем.
        :param right_password: Пароль для доступа к соц. сети.

        Пример:
        >>> social_network = Facebook('Facebook', 1852332, True, 'пароль12345')
        """
        super().__init__(name, user_count, log_in)
        if not isinstance(right_password, str):
            raise TypeError("Пароль должен быть строкой")
        self._right_password = right_password  # Приватный атрибут: пароль не должен быть доступен извне

    def __repr__(self):
        """
        Определение поведения магического метода __repr__.
        Метод был перегружен, т.к. в дочернем классе больше аргументов, чем в базовом классе.
        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> social_network = Facebook('Facebook', 1852332, True, 'пароль12345')
        >>> print(f'{social_network!r}')
        Facebook(name='Facebook', user_count=1852332, log_in=True, right_password='пароль12345')

        """
        return  f'{self.__class__.__name__}(name={self.name!r}, ' \
               f'user_count={self._user_count!r}, ' \
               f'log_in={self.log_in!r}, ' \
                f'right_password={self._right_password!r})'

    def access(self, password: str):
        """
        Метод, который определяет возможно ли получить доступ к сайту.
        Метод был перегружен, т.к. к приватному сайту доступ можно получить только по паролю.
        :param password: Пароль, который ввел пользователь.

        Пример:
        >>> social_network = Facebook('Facebook', 1852332, True, 'пароль12345')
        >>> social_network.access('неверныйпароль')
        Пароль не верный. Невозможно получить доступ к сайту Facebook
        >>> social_network.access('пароль12345')
        Пароль верный. Пользователем получен доступ к сайту Facebook
        """
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой")
        if password == self._right_password:
            print(f'Пароль верный. Пользователем получен доступ к сайту {self.name}')
        else:
            print(f'Пароль не верный. Невозможно получить доступ к сайту {self.name}')



if __name__ == "__main__":
    doctest.testmod()
