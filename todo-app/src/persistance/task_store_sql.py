import sqlite3
from typing import List

from persistance.task_store import TaskStore


class TaskStoreSql(TaskStore):
  def __init__(self, db_file_path: str = 'database/tasks.db'):
    self.db_file_path = db_file_path


  def get_all(self,task_type: str = None) -> List[dict]:
    connection = self.__get_connection()
    cursor = connection.cursor()
    condition = f"WHERE type='{task_type}'" if task_type else ""

    try:
      cursor.execute(f"SELECT * FROM tasks {condition}")
    except sqlite3.OperationalError as e:
      print('no tasks were added yet, error: ' + str(e))
      return []
    tasks = cursor.fetchall()
    connection.close()
    dict = [{'name': x[1], 'type': x[2], 'id': x[0]} for x in tasks]
    return dict

  def __get_connection(self):
    connection = sqlite3.connect(self.db_file_path)
    return connection



  def add(self, task_info: dict):
    if not self.__is_table_created():
      self.__execute_command('CREATE TABLE "tasks" ("id"	INTEGER,"name"	TEXT NOT NULL,"type"	TEXT,PRIMARY KEY("id" AUTOINCREMENT));')

    # open the connection to the database file
    self.__execute_command(f"INSERT INTO tasks (name, type) VALUES ('{task_info['name']}', '{task_info['type']}')")


  def delete(self, task_id: int):
    condition = f"id = {task_id}"
    self.delete_where(condition)


  def delete_type(self, task_type: str):
    condition = f"type = '{task_type}'"
    self.delete_where(condition)



  def delete_where(self, condition : str):
    # the variable after as takes the value from the function on the left
    # with calls connecton.close() automatically even if eror
    # useful for files and databases
    with self.__get_connection() as conn:
      cursor = conn.cursor()
      command = f"DELETE FROM tasks WHERE {condition}"
      cursor.execute(command)
      conn.commit()




  def update(self, old_name: str, new_name: str ):
    with self.__get_connection() as connection:
      cursor = connection.cursor()
      command = f"UPDATE tasks SET name='{new_name}' WHERE name='{old_name}'"
      cursor.execute(command)
      connection.commit()

  def __is_table_created(self) -> bool:
    with self.__get_connection() as connection:
      cursor = connection.cursor()
      try:
        cursor.execute("SELECT * FROM tasks")
      except sqlite3.OperationalError:
        return False
    return True

  def __execute_command(self, command: str):
    with self.__get_connection() as connection:
      cursor = connection.cursor()
      cursor.execute(command)
      connection.commit()



