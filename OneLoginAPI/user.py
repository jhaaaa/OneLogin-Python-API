class User(object):
	'''create the user object and store all of their associated values'''

	def __init__(self, First, Last, Email, Password, Subdomain, Attribute=None, AttributeValue=None, Roles=0, Group=0, userID=0):
		"""Build a user object"""
		self.FirstName = First
		self.LastName = Last
		self.Email = Email
		self.Password = Password
		self.Roles = Roles
		self.Group = Group
		self.Subdomain = Subdomain
		self.Attribute = Attribute
		self.AttributeValue = AttributeValue
		self.Username = First + Last
		self.UserID = userID

	def getFirstName(self):
		"""return the user's FirstName attribute"""
		return self.FirstName

	def getLastName(self):
		"""return the user's LastName attribute"""
		return self.LastName

	def getEmail(self):
		"""return the user's Email attribute"""
		return self.Email

	def getPassword(self):
		"""return the user's Password attribute"""
		return self.Password

	def getRoles(self):
		"""return the user's Roles attribute"""
		return self.Roles

	def getGroup(self):
		"""return the user's Group attribute"""
		return self.Group

	def getSubdomain(self):
		"""return the user's Subdomain attribute"""
		return self.Subdomain

	def getUsername(self):
		"""return the user's Username attribute"""
		return self.UserName

	def getUserID(self):
		"""return the user's UserID attribute"""
		return self.UserID

	def getCustomAttribute(self):
		"""return the user's custom attribute attribute"""
		return self.Attribute

	def getCustomAttributeValue(self):
		"""return the user's custom attribute value"""
		return self.AttributeValue

	def FirstNamePayload(self):
		"""generate XML Payload for user's Firstname"""
		return "<firstname>" + self.FirstName + "</firstname>"

	def LastNamePayload(self):
		"""generate XML Payload for user's LastName"""
		return "<lastname>" + self.LastName + "</lastname>"

	def EmailPayload(self):
		"""generate XML Payload for user's Email"""
		return "<email>" + self.Email + "</email>"

	def PasswordPayload(self):
		"""generate XML Payload for user's Password"""
		return "<password>" + self.Password + "</password><password_confirmation>" + self.Password + "</password_confirmation>"

	def RolePayload(self):
		"""generate XML Payload for user's Roles, can handle more than one role"""
		if type(self.Roles) == int:
			return "<roles type='array'><role>" + str(self.Roles) + "</role></roles>"
		else:
			RoleCount = len(self.Roles)
			count = 0
			pre_return = ''
			if RoleCount > 1:
				while count != RoleCount:
					pre_return += "<role>" + str(self.Roles[count]) + "</role>"
					count += 1	
				return "<roles type='array'>" + pre_return + "</roles>"
		
	def GroupPayload(self):
		"""generate XML Payload for user's Group"""
		return "<group-id>" + str(self.Group) + "</group-id>"

	def UserNamePayload(self):
		"""generate XML Payload for user's Username"""
		return "<username>" + self.Username + "</username>"

	def CustomAttributePayload(self):
		"""generate custom attribute payload for user updates"""
		if self.Attribute:
			for each in self.Attribute:
				payloadAttribute = dict(zip(self.Attribute,self.AttributeValue))
				for key in payloadAttribute:
					return "<customer_attribute_" + str(key) + ">" + str(payloadAttribute[key]) + "</custom_attribute_" + str(key) + ">"