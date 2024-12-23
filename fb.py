import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('serviceAccountKey.json')

firebase_admin.initialize_app(cred, {
	'databaseURL':'https://pyapp-42669-default-rtdb.firebaseio.com/'
	})

#--- save data
ref = db.reference('MyDB/')
users_ref = ref.child('users')

obj = {
	'mkodaramola':{
	'fullname':'Daramola Oluwafemi',
	'dob':'April 20, 1998',
	'gender':'male',
	'email':'mkodaramola@gmail.com'
	},
	'samosparkle':{
	'fullname':'Oyeleye Samuel',
	'dob':'August 13, 1958',
	'gender':'male',
	'email':'samuelOye2@gmail.com'
	}
}

users_ref.set(obj)
print ("Saved to Database")

#--- Update Database
hopper_ref = users_ref.child('samosparkle')
hopper_ref.update({'nickname':'sam'})

#--- Read All Data
print(ref.get())

#--- Read Specific Data
handle = db.reference('MyDB/users/mkodaramola')
print(handle.get())


#--- Delete Data
new_ref = users_ref.child('mkodaramola')
new_ref.delete()
