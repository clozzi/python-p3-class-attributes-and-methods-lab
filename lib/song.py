class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.genres.append(genre)
        self.artists.append(artist)
        self.genre = genre
        self.name = name
        self.artist = artist

    @classmethod
    def add_song_to_count(cls, inc=1):
        cls.count += inc

    def add_to_genre_count():
        pass

    def add_to_artist_count():
        pass