#Song.py


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return self.title + " " + self.artist.getName()

