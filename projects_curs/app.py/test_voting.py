import unittest
from voting import User
from unittest import mock


class TestVoting(unittest.TestCase):
  @mock.patch('voting.User.read_file', return_value=['name2\n'])
  def test_user_has_not_voted(self, read_file):
    # set up
    user = User('name1')
    # execution
    user = User('name1')
    has_voted = user.has_user_already_voted()
    self.assertFalse(has_voted)


  @mock.patch('voting.User.read_file', return_value=['name2\n'])
  def test_user_voted(self,read_file):
    #setup -made it manualy :write name2 ti users.txt
    # execution
    user = User('name2')
    has_voted = user.has_user_already_voted()
    self.assertTrue(has_voted)


  @mock.patch('voting.User.write_file' )
  def test_vote_was_registred(self,write_file):
    user = User('name2')
    user.register_the_vote(1)
    write_file.assert_called_once_with('1\n')





if __name__ == '__main__':
  unittest.main()
