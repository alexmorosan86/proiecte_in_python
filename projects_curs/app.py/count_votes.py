from homework_13.voting import Party, User

list_parties = [Party(0), Party(1), Party(2), Party(3)]

list_users = []
# range (0, 99) = [0,1,2,3....99]
for i in range(0,99):
  # concatenate toghether the string name with i converted to string
  new_user = User('name' + str(i))
  # add the User object to the list
  list_users.append(new_user)

list_users[50].vote(0)
list_users[51].vote(1)
list_users[52].vote(2)
list_users[53].vote(1)

def count_the_votes():
  #open the file for reading
  file = open('votes.txt')
  #read the files
  votes = file.readlines()
  #close the file
  file.close()
  for vote in votes:
    vote = int(vote.strip('\n'))
    list_parties[vote].votes += 1


count_the_votes()
for party in list_parties:
  print(party.__dict__)
