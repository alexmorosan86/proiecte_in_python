import flask
# .. = the above folder
# from .. import repository
from persistance.repository import TaskRepository
from task import Task
from persistance.task_store_sql import TaskStoreSql

server = flask.Flask(__name__)


# define an API endpoint
@server.route('/hello')
def hello():
  return 'Hello world!'


# define the menu root page
@server.route('/')
def menu():
  template = flask.render_template('menu.html')
  return template


# define what to show when accessing the server/
@server.route('/list')
def list():
  repo = TaskRepository(TaskStoreSql())
  tasks = repo.get()
  paragraph = 'content of our paragraph'
  html_template = flask.render_template('hello.html', p=paragraph, tasks=tasks)
  return html_template


@server.route('/new', methods=('GET', 'POST'))
def new():
  if flask.request.method == 'GET':
    return flask.render_template('new.html')
  if flask.request.method == 'POST':
    new_task = Task(flask.request.form['task-name'],
                    flask.request.form['task-type'])
    repo = TaskRepository(TaskStoreSql())
    repo.add(new_task)
    return flask.redirect(flask.url_for('list'))

@server.route('/task/<id>', methods=['DELETE'])
def task(id: int):
  print("hello")
  repo = TaskRepository(TaskStoreSql())
  task_name = name.replace('_', ' ')
  repo.delete(id)
  return flask.redirect(flask.url_for("list"))

@server.route('/task/type/<type>', methods= {'DELETE'})
def type_task(type: str):
  repo = TaskRepository(TaskStoreSql())
  repo.delete_type(type)

if __name__ == "__main__":
  repo = TaskRepository(TaskStoreSql())

  task = repo.get_by_name('other_name')
  print(task)


