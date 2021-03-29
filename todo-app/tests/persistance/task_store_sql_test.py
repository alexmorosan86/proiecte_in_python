import unittest
import os
import sys

dir_src = os.path.dirname(os.path.realpath(__file__)) + '/../../src/'
sys.path.insert(0, dir_src)


from persistance.task_store_sql import TaskStoreSql


class TaskStoreSqlTest(unittest.TestCase):
  DB_FILE_PATH = 'test_db2'

  def setUp(self):
    self.store = TaskStoreSql(self.DB_FILE_PATH)

  def tearDown(self):
    os.remove(self.DB_FILE_PATH)



  def test_creates_databases_when_adding_firs_element(self):
    # execution
    self.store.add({'name': 'name1', 'type': 'type1'})
    # assertion
    is_db_created = os.path.exists(self.DB_FILE_PATH)
    self.assertTrue(is_db_created)


  def test_reads_the_added_element(self):
    # set up
    self.store.add({'name': 'name1', 'type': 'type1'})
    # execution
    tasks = self.store.get_all()
    # assertion
    self.assertEqual([{'name': 'name1', 'type': 'type1', 'id': 1}], tasks)

  def test_deletes_element(self):
    #set up
    self.store.add({'name': 'name1', 'type': 'type1'})
    # execution
    self.store.delete(1)
    # assertion
    self.assertEqual([], self.store.get_all())

  def test_deletes_all_elements_of_type(self):
    self.store.add({'name': 'name1', 'type':'type1'})
    self.store.add({'name': 'name2', 'type': 'type2'})

    self.store.delete_type('type2')

    tasks = self.store.get_all()


    self.assertEqual([{'name': 'name1', 'type': 'type1', 'id': 1}], tasks)





if __name__ == '__main__':
  unittest.main()
