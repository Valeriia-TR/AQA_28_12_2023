from abc import ABC, abstractmethod


class ArtObject(ABC):
    def __init__(self,title, artist, year):
        self._title = title
        self._artist = artist
        self._year = year

    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def year(self):
        return self._year

    @artist.setter
    def artist(self, new_artist):
        self._artist = new_artist

    @abstractmethod
    def get_info(self):
        pass


class Painting(ArtObject):
    def __init__(self, title, artist, year, place_to_see):
        super().__init__(title, artist, year)
        self._place_to_see = place_to_see

    def get_info(self):
        return f"You can see it in {self._place_to_see}"


class Sculpture(ArtObject):
    def __init__(self, title, artist, year, material):
        super().__init__(title, artist, year)
        self._material = material

    def get_info(self):
        return f"Material: {self._material}"


painting = Painting("Mona Lisa", "Leonardo da Vinci", 1503, "Louvre Museum")
sculpture = Sculpture("David", "Michelangelo", 1504, "Marble")

painting.artist = "Pablo Picasso"

print(painting.artist)
print(sculpture.title)
print(sculpture.get_info())
print(painting.get_info())
