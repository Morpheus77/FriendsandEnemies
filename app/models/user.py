""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class user(Model):
    def __init__(self):
        super(user, self).__init__()
	  
    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def create_user(self,user_info):
		sql = "INSERT into users (name_first, name_last,  email) values(:frstname, :lstname, :email)"
		data = {'frstname': 'name_first', 'lstname' : 'name_last' , 'frstname': 'name_first', 'email':'email'}
		self.db.query_db(sql, data)
		return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)