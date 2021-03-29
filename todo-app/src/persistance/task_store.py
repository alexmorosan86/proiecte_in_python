from abc import ABC, abstractmethod
from typing import List

class TaskStore(ABC):
  @abstractmethod
  def get_all(self)-> List[dict]:
    pass

  @abstractmethod
  def add(self, task_info: dict):
    pass

  @abstractmethod
  def delete(self,task_id: int):
    pass

  @abstractmethod
  def delete_type(self, task_type: str):
    pass

