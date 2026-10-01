# import sqlite3
#
# # Create database
# conn = sqlite3.connect('task1.db')
# cursor = conn.cursor()
#
# # Create table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS tasks(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(200),
#         description VARCHAR(200)
#     )
# ''')
#
# conn.close()
#
#
# # Add task
# def addtask():
#     conn = sqlite3.connect('task1.db')
#     cursor = conn.cursor()
#
#     name = input("Enter task name: ")
#     description = input("Enter task description: ")
#
#     cursor.execute('''
#         INSERT INTO tasks (name, description)
#         VALUES (?, ?)
#     ''', (name, description))
#
#     conn.commit()
#
#     print("Task added successfully")
#
#     conn.close()
#
#
# # View tasks
# def viewtasks():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     cursor.execute('''
#         SELECT * FROM tasks
#     ''')
#
#     data = cursor.fetchall() #Retrieve a list of data from the last query
#
#     print("\nTasks found ☑")
#
#     for i in data:
#         print(f"{i[0]} task --- {i[1]} task description --- {i[2]}")
#
#     conn.close()
#
# # Search task
# def searchtask():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     t_id = int(input("Enter your task id: "))
#
#     cursor.execute(
#         "SELECT * FROM tasks WHERE id = ?",
#         (t_id,)
#     )
#
#     task = cursor.fetchone()
#
#     if task:
#         print("Task found ☑")
#         print(f"{task[0]} --- {task[1]} --- {task[2]}")
#     else:
#         print("No such task 😕")
#
#     conn.close()
#
# def edittask():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     t_id = int(input("Enter task id: "))
#     name = input("Enter new task name: ")
#     des = input("Enter new description: ")
#
#     cursor.execute(
#         '''
#         UPDATE tasks
#         SET name = ?, description = ?
#         WHERE id = ?
#         ''',
#         (name, des, t_id)
#     )
#
#     conn.commit()
#
#     print("Task updated")
#
#     conn.close()
#
# def deletetask():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     t_id = int(input("enter task id:-"))
#
#     ch = input("Are you sure you want to delete this task y/n:-")
#
#     if ch == "y":
#         cursor.execute(
#             "DELETE FROM tasks WHERE id = ?",
#             (t_id,)
#         )
#         conn.commit()
#
#         print("Task deleted !!!!!!!!!!!!!")
#     else:
#         print("Task not deleted !!!!!!!!!!!!")
#
#
# # Main function
# def main():
#     print("Welcome to task management system")
#
#     while True:
#         ch = int(input(
#             "Enter your choice\n"
#             "1. Add Task\n"
#             "2. View Tasks\n"
#             "3. Search Task\n"
#             "4. Update Task\n"
#             "5. Delete Task\n"
#             "6. Quit\n"
#         ))
#
#         if ch == 1:
#             addtask()
#
#         elif ch == 2:
#             viewtasks()
#
#         elif ch == 3:
#             searchtask()
#
#         elif ch == 4:
#             edittask()
#
#         elif ch == 5:
#             deletetask()
#
#         elif ch == 6:
#             print("Goodbye!")
#             break
#
#         else:
#             print("Invalid option")
#
#
# main()

