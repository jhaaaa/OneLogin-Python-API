import requests
import xml.etree.ElementTree as ET
from user import User

class OneLogin(User):
	'''Functions available from OneLogin for Users'''

	def __init__(self, user, api_key):
		"""create the User object for use with the OneLogin API key for each call"""
		self.user = user
		self.apikey = api_key

	def buildUserPayload(self, user):
		"""build payload based on user object"""
		user_details = user.FirstNamePayload() + user.LastNamePayload() + user.EmailPayload() + user.UserNamePayload()
		pre_payload = ''
		if user.Roles and not user.Group:
			pre_payload = user.RolePayload()
		elif user.Roles and user.Group:
			pre_payload = user.RolePayload() + user.GroupPayload()
		elif not user.Roles and user.Group:
			pre_payload = user.GroupPayload()
		elif not user.Roles and not user.Group:
			pre_payload = ''

		payload = "<user>" + user_details + pre_payload + "</user>"
		return payload

	def buildCustomAttributePayload(self, user):
		"""build payload based on user object"""
		user_details = user.FirstNamePayload() + user.LastNamePayload() + user.EmailPayload() + user.UserNamePayload()
		pre_payload = ''
		for each in user.Attribute:
			pre_payload = user.CustomAttributePayload()
			payload = "<user>" + user_details + pre_payload + "</user>"
		print payload


	def getUserIDByUsername(self, user):
		"""fetch userID using the Username of the user"""
		headers = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/username/" + user.Username + "?api_key=" + self.apikey
		r = requests.get(target, headers=headers)
		root = ET.fromstring(r.text)
		if r.status_code in (200,205):
			userID = root[8].text
			user.UserID = userID
			print "UserID for user: %s is: %s." % (user.Username, user.UserID)
		else:
			print r.status_code

	def getUserByUsername(self, user):
		"""fetch user using the Username of the user"""
		headers = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/username/" + user.Username + "?api_key=" + self.apikey
		r = requests.get(target, headers=headers)
		root = ET.fromstring(r.text)
		if r.status_code in (200,205):
			print "User informatino for user: %s is: %s." % (user.Username, r.text)
		else:
			print r.status_code

	def getUserByID(self, user):
		"""fetch user using the UserID of the user"""
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/" + str(user.UserID) + ".xml?api_key=" + self.apikey
		r = requests.get(target)
		print r.text

	def CreateUser(self, user):
		"""Create User in OneLogin using user object attributes
		calls getUserIDByUsername after user creation to update user object """
		#pre_payload = user.FirstNamePayload() + user.LastNamePayload() + user.EmailPayload() + user.UserNamePayload()
		payload = self.buildUserPayload(user)
		header = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users.xml?api_key=" + str(self.apikey)
		r = requests.post(target, headers=header, data=payload)
		self.getUserIDByUsername(user)
		if r.status_code in (200,205):
			print "User: %s has been created." % (user.Username)
		else:
			print target, payload
			print r.status_code

	def DeleteUserByUsername(self, user):
		"""Delete user using the Username of the user"""
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/username/" + user.Username + "?api_key=" + self.apikey
		r = requests.delete(target)
		if r.status_code in (200,205):
			print "%s has been deleted." % (user.Username)
		else:
			print r.status_code

	def DeleteUserByUserID(self,user):
		"""Delete user using the UserID of the user"""
		if not user.UserID:
			user.UserID = self.getUserIDByUsername(user)
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/" + str(user.UserID) + ".xml?api_key=" + self.apikey
		r = requests.delete(target)
		if r.status_code in (200,205):
			print "%s has been deleted." % (str(user.UserID))
		else:
			print r.status_code

	def UpdateUserByUsername(self, user):
		"""Update the user (PUT) by Username
		Used for Roles, Group, and Custom Attribute updates.
		Can also be used to set initial password for user in OneLogin"""
		if user.Attribute:
			payload = self.buildCustomAttributePayload(user)
			print payload
		else:
			payload = self.buildUserPayload(user)
			print payload
		header = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/username/"+ user.Username +"?api_key=" + str(self.apikey)
		r = requests.put(target, headers=header, data=payload)
		if r.status_code in range(200,204,205):
			print payload
			print "%s has been updated." % (user.Username)
		else:
			print payload
			print r.status_code


	def UpdateUserByUserID(self, user):
		"""Update the user (PUT) by UserID
		Used for Roles, Group, and Custom Attribute updates.
		Can also be used to set initial password for user in OneLogin"""
		if user.Attribute:
			payload = self.buildCustomAttributePayload(user)
			print payload
		else:
			payload = self.buildUserPayload(user)
			print payload
		header = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + ".onelogin.com/api/v3/users/"+ str(user.UserID) +".xml?api_key=" + str(self.apikey)
		r = requests.put(target, headers=header, data=payload)
		if r.status_code in (200,204,205):
			print payload
			print "%s has been updated." % (str(user.UserID))
		else:
			print payload
			print r.status_code




	
		