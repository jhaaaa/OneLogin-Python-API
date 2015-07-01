import urllib3

urllib3.disable_warnings()

class User(object):
	'''create the user object and store all of their associated values'''

	def __init__(self, First, Last, Email, Password, Subdomain, Attribute=None, AttributeValue=None, Roles=None, Group=None, userID=None):
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
		payload = ''
		if self.Roles:
			if type(self.Roles) != int:
				for x in range(0,len(self.Roles)):
					payload += "%s" % (self.Roles[x])
				return self.Roles
			else:
				return None

	def getGroup(self):
		"""return the user's Group attribute"""
		return self.Group

	def getSubdomain(self):
		"""return the user's Subdomain attribute"""
		return self.Subdomain

	def getUsername(self):
		"""return the user's Username attribute"""
		return self.Username.lower()

	def getUserID(self):
		"""return the user's UserID attribute"""
		return self.UserID

	def getCustomAttribute(self):
		"""return the user's custom attribute attribute"""
		return self.Attribute

	def getCustomAttributeValue(self):
		"""return the user's custom attribute value"""
		payload = ''
		if len(self.Attribute) > 0:
			for x in range(0,len(self.Attribute)):
				payload += "%s : %s" % (self.Attribute[x], self.AttributeValue[x])
			return payload
		else:
			return payload
		

	def FirstNamePayload(self):
		"""generate XML Payload for user's Firstname"""
		return "<firstname>%s</firstname>" % (self.FirstName)

	def LastNamePayload(self):
		"""generate XML Payload for user's LastName"""
		return "<lastname>%s</lastname>" % (self.LastName)

	def EmailPayload(self):
		"""generate XML Payload for user's Email"""
		return "<email>%s</email>" % (self.Email)

	def PasswordPayload(self):
		"""generate XML Payload for user's Password"""
		return "<password>%s</password><password_confirmation>%s</password_confirmation>" % (self.Password, self.Password)

	def RolePayload(self):
		"""generate XML Payload for user's Roles, can handle more than one role"""
		pre_return = ''
		if self.Roles:
			if len(self.Roles):
				for x in range(0,len(self.Roles)):
					pre_return += "<role>" + str(self.Roles[x]) + "</role>"
				return "<roles type='array'>%s</roles>" % (pre_return)
			else:
				return "<roles type='array'>%s</roles>" % (self.Roles)
		else:
			return None
		
	def GroupPayload(self):
		"""generate XML Payload for user's Group"""
		if self.Group:
			return "<group-id>%s</group-id>" % (self.Group)
		else:
			return None

	def UserNamePayload(self):
		"""generate XML Payload for user's Username"""
		return "<username>" + self.Username + "</username>"

	def CustomAttributePayload(self):
		"""generate custom attribute payload for user updates"""
		payload = ''
		if self.Attribute:
			for each in self.Attribute:
				payloadAttribute = dict(zip(self.Attribute,self.AttributeValue))
				for key in payloadAttribute:
					return "<custom_attribute_" + str(key) + ">" + str(payloadAttribute[key]) + "</custom_attribute_" + str(key) + ">"
		else:
			return None












