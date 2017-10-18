

from alc_conf import AlchemyConfig
from alc import *


mariadb_creds_path='creds.mysql'
db_name='account_manager'
debug=True

a = AlchemyConfig.from_creds_file_path(mariadb_creds_path, db_name, debug)

#a.eng
#a.session
#a.Session

'''
class User(Base):
   __tablename__ == 'users'

   id = idc()

   uname = stringc(35)
   email = stringc(45)
   pass_info = stringc()

   flags = stringc()

   def __repr__(self):
      args = (self.name, self.fullname, self.password)
      return "<User(name='%s', fullname='%s', password='%s')>" % args

   def add_user(uname, email, pass_info):
      pass

   #pass

class UserData(Base):
   __tablename__ = 'user_data'

   id = idc()

   fname = stringc(35)
   lname = stringc(35)
   mname = stringc(35)

   phone = intc()
   age = intc()

   address = stringc(35)

   #pass
'''

class Comment(Base):
   uname = stringc(35)

   title = stringc(140)

   content = stringc()




