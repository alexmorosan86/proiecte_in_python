import json
import os
from typing import List

from persistance.task_store import TaskStore


class TaskStoreFile(TaskStore):
  file_name = 'task.json'
  
  def get_all(self) -> List[dict]:
    if os.path.exists(self.file_name):
      # open the file for read
      file = open(self.file_name)
      # read and decode the file
      list_of_tasks = json.loads(file.read())
      file.close()
    else:
      # if no file => we have an empty list(no task were added)
      list_of_tasks = []
    return list_of_tasks

  def delete(self, task_name: str):
    list_of_tasks = self.__read_from_file()
    tasks = [x for x in list_of_tasks if x['name'] != task.name]
    self.__write_to_file(tasks)