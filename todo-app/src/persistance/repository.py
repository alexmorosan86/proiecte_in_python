from task import Task
import os
import json
from mapper import TaskMapper
from persistance.task_store import TaskStore


class TaskRepository:
  def __init__(self, task_store: TaskStore):
    self.task_store = task_store


  def add(self, task:Task):
    task_dict = TaskMapper.to_dict(task)
    self.task_store.add(task_dict)


  def get(self) -> list[Task]:
    saved_info = self.task_store.get_all()
    tasks = [TaskMapper.to_object(info) for info in saved_info]
    tasks = list(map(TaskMapper.to_object, saved_info))
    print(tasks)
    return tasks

  def get_by_name(self, name: str)-> Task:
    saved_info = self.task_store.get_all()
    return next((i for i in saved_info if i['name'] == name), None)
    for info in saved_info:
      if info['name'] == name:
        return info
      return None





  def delete(self, task_id: int):
    self.task_store.delete(task_id)

  def delete_type(self, task_type: str):
    self.task_store.delete_type(task_type)



  def __add_task_info(self, list_of_tasks, task):
    # extract the info from the Task object
    list_of_tasks.append(TaskMapper.to_dict(task))
    # create  a JSON
    return list_of_tasks


  def __write_to_file(self, list_of_tasks):
    #create a JSON
    file_content = json.dumps(list_of_tasks)
    # open the file for writing it if does not exist
    file = open(self.file_name, 'w')
    file.write(file_content)
    file.close()








