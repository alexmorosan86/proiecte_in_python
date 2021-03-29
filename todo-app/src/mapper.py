from task import Task

class TaskMapper:
  @staticmethod
  def to_dict( task: Task) -> dict:
    return {
      'name': task.name,
      'type': task.task_type,
      'deadline': task.deadline,
      'difficulty': task.difficulty,
    }
  @staticmethod
  def to_object(task_info: dict) -> Task:
    return Task(task_info['name'],
              task_info['type'],
              # task_info['deadline'],
              # task_info['difficulty']
    )