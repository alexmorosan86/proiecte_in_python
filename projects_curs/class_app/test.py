import unittest
from main import get_user_and_password


class TestPassword(unittest.TestCase):
  def test_get_user_and_password(self):
    credentials = get_user_and_password('netflix')

    self.assertEqual('alex', credentials.user)
    self.assertEqual('abcdefg', credentials.password)


  def test_get_not_configured_website(self):

    credentials = get_user_and_password('emag')
    self.assertEqual('', credentials.user)
    self.assertEqual('', credentials.password)






