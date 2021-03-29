from it_team_solution import Name
from skill import BackendSkill

class Dev:
  def __init__(self, name, expierence,backend_skill):
    self.name = name
    self.expierence = expierence
    self.backend_skill = backend_skill


class JuniorDev(Dev):
  def __init__(self, name,expierence, backend_skill):
    if 0<= expierence <= 2:
      super().__init__(name, expierence, backend_skill)
    else:
      raise Exception('xp should be betwen 0 and 2')

class BackendJuniorDev(JuniorDev):
  def __init__(self, name, expierence, backend_skill: BackendSkill):
    if backend_skill.rating > 5 :
      super().__init__(name,expierence, backend_skill)
    else:
      raise Exception('skill should be higher')

  def show(self):
    self.name.show()
    self.backend_skill.show()

jr = BackendJuniorDev(Name('first','last'), 2, BackendSkill(6))
jr.show()

