from user import User
from werkzeug.security import safe_str_cmp

def authenticate(email, password):
  user = User.find_by_email(email)
  if user and safe_str_cmp(user.password, password):
    return user

def identity(payload):
  user_id = payload['identity']
  return User.find_by_id(user_id)