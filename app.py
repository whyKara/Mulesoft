import sqlite3
from sqlite3 import Error


def db_connection():
    # file_path = "mulesoftDB.db"
    conn = None

    try:
        conn = sqlite3.connect("mulesoftDB.db")
        # print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

    return conn


def crea_table(conn, create_table_query, c):
    try:
        c.execute(create_table_query)
    except Error as e:
        print(e)


def insert_movie_roles(conn, c):
    querry = """INSERT INTO movie_roles VALUES (?,?);"""
    role_1 = (1, 'Actor')
    role_2 = (2, 'Actress')
    role_3 = (3, 'Director')
    c.execute(querry, role_1)
    c.execute(querry, role_2)
    c.execute(querry, role_3)
    conn.commit()
    return


def insert_movie(conn, movie_v, c):
    querry = """INSERT INTO movies (m_name,m_dor) VALUES (?,?)"""

    c.execute(querry, movie_v)
    conn.commit()
    return c.lastrowid


def insert_cast_movie_role(conn, c_m_role_v, c):
    querry = """INSERT INTO r_cast_movie (r_cid,r_mid) VALUES (?,?)"""

    c.execute(querry, c_m_role_v)
    conn.commit()
    return


def insert_cast(conn, cast_v, c):
    querry = """INSERT INTO movie_cast (c_name,c_role) VALUES (?,?)"""

    c.execute(querry, cast_v)
    conn.commit()
    return c.lastrowid


def get_cid(conn, name, c):
    querry_cid = """SELECT c_id FROM movie_cast where c_name =?"""

    c.execute(querry_cid, name)
    cid = int(c.fetchall())

    return cid


def check_db(conn, actor_list, actres_list, director_list, mid, c):
    querry_actor = """SELECT c_name FROM movie_cast where c_role =1"""
    querry_actres = """SELECT c_name FROM movie_cast where c_role =2"""
    querry_director = """SELECT c_name FROM movie_cast where c_role =3"""

    c.execute(querry_actor)
    row_actor = c.fetchall()
    c.execute(querry_actres)
    row_actres = c.fetchall()
    c.execute(querry_director)
    row_director = c.fetchall()

    for actor in actor_list:
        if actor not in row_actor:
            cast_v = (actor, 1)
            insert_cast(conn, cast_v, c)
        cid = get_cid(conn, actor, c)
        role_c_m = (cid, mid)
        insert_cast_movie_role(conn, role_c_m, c)

    for actres in actres_list:
        if actres not in row_actres:
            cast_v = (actres, 2)
            insert_cast(conn, cast_v, c)
        cid = get_cid(conn, actres, c)
        role_c_m = (cid, mid)
        insert_cast_movie_role(conn, role_c_m, c)

    for dicrector in director_list:
        if dicrector not in row_director:
            cast_v = (dicrector, 3)
            insert_cast(conn, cast_v, c)
        cid = get_cid(conn, dicrector, c)
        role_c_m = (cid, mid)
        insert_cast_movie_role(conn, role_c_m, c)
    return


def details(c):
    m_name = input("Enter the name of the Movie: ")
    m_dor = input("Enter the date of release of the Movie: ")

    m_details = (m_name, m_dor)

    m_id = insert_movie(conn, m_details, c)

    print("Enter Cast details of the Movie: ")
    actor_list = list(input(
        "Enter the name of the Actors in the Movie(saperated by a come ','): ").split(','))
    actres_list = list(input(
        "Enter the name of the Actreses in the Movie(saperated by a come ','): ").split(','))
    director_list = list(input(
        "Enter the name of the Director in the Movie(saperated by a come ','): ").split(','))

    check_db(conn, actor_list, actres_list, director_list, m_id, c)
    return


conn = db_connection()
c = conn.cursor()

querry1 = """CREATE TABLE IF NOT EXISTS movies(
    m_id integer PRIMARY KEY AUTOINCREMENT,
    m_name text NOT NULL,
    m_dor text
);"""
querry2 = """CREATE TABLE IF NOT EXISTS movie_roles(
    r_id integer PRIMARY KEY AUTOINCREMENT,
    r_role text NOT NULL
);"""
querry3 = """CREATE TABLE IF NOT EXISTS movie_cast(
    c_id integer PRIMARY KEY AUTOINCREMENT,
    c_name text NOT NULL,
    c_role integer NOT NULL,
    FOREIGN KEY (c_role) REFERENCES movie_roles(r_id)
);"""
querry4 = """CREATE TABLE IF NOT EXISTS r_cast_movie(
    r_cid integer NOT NULL,
    r_mid integer NOT NULL,
    FOREIGN KEY (r_cid) REFERENCES movie_cast(c_id),
    FOREIGN KEY (r_mid) REFERENCES movie_cast(m_id)
);"""

if conn is not None:
    crea_table(conn, querry1, c)
    crea_table(conn, querry2, c)
    crea_table(conn, querry3, c)
    crea_table(conn, querry4, c)

else:
    print("Error")

# insert_movie_roles(conn)
details(c)
