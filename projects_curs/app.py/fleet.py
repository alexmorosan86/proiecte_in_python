# import the classes we need
from transportation import Minivan, Car, Morgan, Bus, Motorcycle, Bicycle


class Fleet:
  def __init__(self):
    self.list = [
      Bus(), Bus(),
      Car(), Car(), Car(),Car(),
      Minivan(),
      Motorcycle(),Motorcycle(),Motorcycle()
    ]
    i = 0
    while i < 6:
      self.list.append(Bicycle())
      i += 1

  def get_capacity(self):
    capacity = 0
    for transport in self.list:
      capacity += transport.capacity
    return capacity
  def get_electronics_capacity(self):
    capacity = 0
    for transport in self.list:
      if transport.type == 'electronics':
        capacity += transport.capacity
    return capacity
  def get_number_of_orders(self):
    actual_time = 400 # in minutes
    number_of_orders = 0
    for transport in self.list:
      if transport.type == 'food':
        number_of_orders += actual_time / transport.delivery_time
    return number_of_orders





fleet = Fleet()
cap = fleet.get_capacity()
print(cap)
cap_el = fleet.get_electronics_capacity()
print(cap_el)
orders = fleet.get_number_of_orders()
print(orders)


