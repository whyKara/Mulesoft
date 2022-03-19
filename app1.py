import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS movies(
                m_name text NOT NULL,
                m_actor text,
                m_actress text,
                m_director text,
                m_yor text
            )""")


class movies:
    def __init__(self, name, actor, actress, director, yor) -> None:
        self.name = name
        self.actor = actor
        self.actress = actress
        self.director = director
        self.yor = yor


def insert_movie(movie):
    with conn:
        c.execute("INSERT INTO movies VALUES (?,?,?,?,?)", (movie.name,
                  movie.actor, movie.actress, movie.director, movie.yor))


def get_movie_by_name(name):
    c.execute("SELECT * FROM movies WHERE m_name = ?", (name,))
    return c.fetchall()


def get_movie_by_actor(actor):
    c.execute("SELECT * FROM movies WHERE m_actor = ?", (actor,))
    return c.fetchall()


def get_movie_by_actress(actress):
    c.execute("SELECT * FROM movies WHERE m_actress = ?", (actress,))
    return c.fetchall()


def get_movie_by_director(director):
    c.execute("SELECT * FROM movies WHERE m_director = ?", (director,))
    return c.fetchall()


def get_movie_by_yor(yor):
    c.execute("SELECT * FROM movies WHERE m_yor = ?", (yor,))
    return c.fetchall()


movie1 = movies('Iron Man', 'Robert Downey Jr.',
                'Gwyneth Paltrow', 'Jon Favreau', '2008')
movie2 = movies('Iron Man 2', 'Robert Downey Jr.',
                'Gwyneth Paltrow', 'Jon Favreau', '2010')
movie3 = movies('Iron Man 3', 'Robert Downey Jr.',
                'Gwyneth Paltrow', 'Shane Black', '2013')

insert_movie(movie1)
insert_movie(movie2)
insert_movie(movie3)


movie = get_movie_by_name('Iron Man')
print(movie)

movie = get_movie_by_actor('Robert Downey Jr.')
print(movie)

movie = get_movie_by_actress('Gwyneth Paltrow')
print(movie)

movie = get_movie_by_director('Jon Favreau')
print(movie)

movie = get_movie_by_yor('2013')
print(movie)
