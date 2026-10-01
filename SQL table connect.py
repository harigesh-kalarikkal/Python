# import sqlite3
#
# conn = sqlite3.connect("Mybook.db")
# cursor = conn.cursor()
#
# # Create Author table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Author(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(20),
#         email VARCHAR(20),
#         phone INTEGER
#     )
# """)
#
# # Create Book table
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS Book(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title VARCHAR(20),
#         des TEXT,
#         price INTEGER,
#         author_id INTEGER,
#         FOREIGN KEY (author_id) REFERENCES Author(id)
#     )
# """)
#
# conn.commit()
# conn.close()

# Foreign Key – connecting two tables:
#
# FOREIGN KEY (author_id) REFERENCES Author(id)

