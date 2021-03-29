# should contain a name, type, deadline, difficulty

class Task:
  def __init__(self, name:str, task_type: str, deadline = None, difficulty:int = 1):
    # save the values to the object, name @ task_type are mandatory
    self.name = name
    self.task_type = task_type
    # save deadline value, will be None if no value was given
    self.deadline = deadline
    self.difficulty = difficulty

# will execute only when we call the file py task.py or from pycharm
# will not execute when importing
if __name__ == "__main__":
  task1 = Task('clean the house', 'chores', None, 5)
  task2 = Task('buy fruits', 'eating', difficulty=2)
  task3 = Task('cook food', 'eating', 'Tomorow')

  print(task1.__dict__)
  print(task2.__dict__)
  print(task3.__dict__)










