
class Credentials:
  def __init__(self, user, password):
    self.user = user
    self.password = password

    #extend Credentials
class EmptyCredentials(Credentials):
  def __init__(self):
    super().__init__('', '')

dict = {
    'amazon': Credentials('alex', '123456'),
    'netflix': Credentials('alex', 'abcdefg'),
    'spotify': Credentials('alex','ab12beeee' ),
}


def get_user_and_password(website_name):
  try:
    return dict[website_name]
  except KeyError:
    return EmptyCredentials()

