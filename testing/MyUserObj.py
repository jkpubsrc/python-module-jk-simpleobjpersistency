





class MyUserObj(object):

	def __init__(self):
		self.userName = None
		self.password = None
		self.eMail = None
		self.yearOfBirth = None
		self.comment = None
	#

	def deserialize(self, jData:dict):
		self.userName = jData.get("userName")
		self.password = jData.get("password")
		self.eMail = jData.get("eMail")
		self.yearOfBirth = jData.get("yearOfBirth")
		self.comment = jData.get("comment")
	#

	def serialize(self):
		return {
			"userName": self.userName,
			"password": self.password,
			"eMail": self.eMail,
			"yearOfBirth": self.yearOfBirth,
			"comment": self.comment,
		}
	#

#
























