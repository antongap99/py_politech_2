class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} by {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages should be a positive integer.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, {self.pages} pages"

    def __repr__(self):
        return f"{super().__repr__()}, pages={self.pages}"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Duration should be a positive number.")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()}, {self.duration} hours"

    def __repr__(self):
        return f"{super().__repr__()}, duration={self.duration}"