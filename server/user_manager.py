class UserManager:
   def __init__(self, users):
      self.users = users

   def get_user(self, user_id):
      return self.users.get(user_id)

class Users:
   def __init__(self, username, password):
      self.username = username
      self.password = password

