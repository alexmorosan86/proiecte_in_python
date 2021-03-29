import requests

# requests.delete('http://127.0.0.1:5000/task/3')
from persistance.repository import TaskRepository
from persistance.task_store_sql import TaskStoreSql

if __name__ == "__main__":
  store = TaskStoreSql('..\\src\\database\\tasks.db')
  tasks = store.get_all('type1')
  print(type)



  # repo = TaskRepository(TaskStoreSql('..\\src\\database\\tasks.db''..\\src\\database\\tasks.db'))
  # tasks = repo.get()
  # print(tasks)
  # tasks_of_type = [(t.name, t.task_type) for t in tasks if t.task_type == 'automotive']
  # print(tasks_of_type)
