from system.core.controller import *
class logins(Controller):
	def __init__(self, action):
		super(logins, self).__init__(action)
		
		self.load_model('user')
		self.db = self._app.db
		
	def index(self):
		return self.load_view('loginReg.html')
		
	def create_user(self):
		user_info = {
			"frstname" : request.form['Fst_Name'],
			"lstname" : request.form['Lst_Name'],
			"email" : request.form['email'],
			"password" : request.form['Password'],
			"pw_confirmation" : request.form['passvalid']
		}
		create_status = self.models['user'].create_user(user_info)
		#if create_status['status'] == True:
		session['id'] = create_status['user']['id'] 
		session['name'] = create_status['user']['name']

