# A database is a place where we store data in an organized way so that
# we can save, retrieve, update, and delete information.

#For example, instead of storing student information like this:
#
# name1 = "Hari"
# age1 = 21
# course1 = "Python"
#
# We can use like this:
#
# ID	Name	Age	Course

# 1	Hari	21	Python
# 2	Arun	22	Cyber Security
# 3	Rahul	20	Python
#
# Instead of keeping this information only in Python variables, we can store it permanently in a database.

# The database allows us to:
#
# Create data
# Read/Retrieve data
# Update data
# Delete data
#
# These are commonly called CRUD operations:

# Create → Read → Update → Delete
#
# import sqlite3
#
# conn = sqlite3.connect('database.db')  # To connect to the DB
#
# cursor = conn.cursor()  # To interact with the DB
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Students
#     (
#         id INTEGER,
#         Name VARCHAR(255),
#         Address TEXT
#     )
# ''')
#
# cursor.execute(
#     '''
#     INSERT INTO Students ( id, Name, Address)
#     VALUES ( 1, "Tony", "Manhattan" ),
#     (2,"Peter", "Queens")
#
#     ''')
#
# conn.commit()
#
# conn.close()

# conn = sqlite3.connect('database.db')  # To connect to the DB
#
# cursor = conn.cursor()  # To interact with the DB
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Employers
#     (
#         id INTEGER,
#         Name VARCHAR(255),
#         Description TEXT
#     )
# ''')
#
# cursor.execute(
#     '''
#     INSERT INTO Employers ( id, Name, Description)
#     VALUES ( 1, "Bruce", "Gotham city" ),
#     (2,"Clark", "Texas")
#
#     ''')
#
# conn.commit()
#
# conn.close()