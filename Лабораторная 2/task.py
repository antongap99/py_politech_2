class Book:
    """
    Класс Книги

    Attributes:
        id (int): Идентификатор книги.
        name (str): Имя книги.
        pages (int): Число страниц книги.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги с переданными атрибутами

        Args:
            id (int): Идентификатор книги.
            name (str): Имя книги.
            pages (int): Число страниц книги.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """

        Returns:
           Название книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Строка инициализации экземпляра книги.

        Returns:
            str: Valid Python string for creating an instance of the Book.
        """
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


class Library:
    """
    Класс Библиотека

    Attributes:
        books (list): Список книг в библиотеке
    """

    def __init__(self, books=None):
        """
        Инициализация библиотеки с переданным списком книг

        Args:
            books (list, optional): список книг. По умолчанию присваивается пустой список.
        """
        self.books = books or []

    def get_next_book_id(self) -> int:
        """
        Возращает следующий доступный идентификатор книги при добавлении

        Returns:
            int: следующий доступный идентификатор.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возращает индекс книги по переданному идентификатору

        Args:
            book_id (int): идентификатор книги.

        Returns:
            int: индекс книги.

        Raises:
            ValueError: Если нет книги с переданным идентификатором.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")



book = Book(1, 'Книги', 130)

book1 = book.__repr__()

lib = Library([Book(1, 'Книги1', 130), Book(2, 'Книги2', 130), Book(3, 'Книги3', 130)])
print(book)
print(book1)
print(lib.get_index_by_book_id(1))