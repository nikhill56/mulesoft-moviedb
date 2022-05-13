import sqlite3
connection=sqlite3.connect('movie.db') #connect to the database

cursor=connection.cursor() #create a cursor object to run the queries

cursor.execute("""CREATE TABLE movies (             
    id INTEGER PRIMARY KEY,
    movie_name TEXT,
    lead_actor TEXT,
    lead_actress TEXT,
    release_year TEXT,
    director_name TEXT
    )""")                           #create a table called movies with the required parameters

#insert values into the table
cursor.execute("INSERT INTO movies VALUES (1, 'Inception','Leonardo Di Caprio', 'Marion Cottilard', '2010', 'Christopher Nolan')") 

cursor.execute("INSERT INTO movies VALUES (2,'Avengers','Robert Downey Jr', 'Scarlett Johansson', '2012', 'Joss Whedon')")

cursor.execute("INSERT INTO movies VALUES (3,'Mission Impossible 4', 'Tom Cruise', 'Paula Patton', '2011', 'Brad Bird')")

cursor.execute("INSERT INTO movies VALUES (4,'Pirates of Carrabiean', 'Johnny Depp', 'Keira Knightley', '2003', 'Gore Verbinski')")

cursor.execute("INSERT INTO movies VALUES (5,'The Dark Knight','Christian Bale', 'Maggie Gyllenhaal', '2008', 'Christopher Nolan')")

#queries
#1 - select all the movies starring Leonardo Di Caprio
cursor.execute("SELECT * FROM movies WHERE lead_actor='Leonardo Di Caprio'")
print(" Query #1:",cursor.fetchall())

#2 - select all the movies directed by Christopher Nolan
cursor.execute("SELECT * FROM movies WHERE director_name='Christopher Nolan'")
print(" Query #2:",cursor.fetchall())

#3 - select all the movies released in the year above 2008
cursor.execute("SELECT * FROM movies WHERE release_year>='2008'")
print(" Query #3:",cursor.fetchall())

#4 - select all the movies in the database
cursor.execute("SELECT * FROM movies")
print(" Query #4:",cursor.fetchall())

#5 - select all the movies with lead actress Scarlett Johansson and director Joss Whedon
cursor.execute("SELECT * FROM movies WHERE lead_actress='Scarlett Johansson' AND director_name='Joss Whedon'")
print(" Query #5:",cursor.fetchall())


connection.commit() #commit the changes
connection.close() #close the connection

