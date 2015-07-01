import requests
import xml.etree.ElementTree as ET
from user import User
import urllib3

urllib3.disable_warnings()

class OneLogin(User):
	'''Functions available from OneLogin for Users'''

	def __init__(self, user, api_key):
		"""create the User object for use with the OneLogin API key for each call"""
		self.user = user
		self.apikey = api_key
		self.url = ".onelogin.com/api/v3/users"

	def PreparePayload(self, payload):
		'''wrap payload in user tags for consumption'''
		return "<user>" + payload + "</user>"

	def buildUserCreatePayload(self, user):
		"""build payload based on user object"""
		user_details = user.FirstNamePayload() + user.LastNamePayload() + user.EmailPayload() + user.UserNamePayload()
		payload = self.PreparePayload(user_details)
		return payload

	def buildUserUpdatePayload(self, user):
		"""build payload based on user object"""
		user_details = user.FirstNamePayload() + user.LastNamePayload() + user.EmailPayload() + user.UserNamePayload()
		pre_payload = ''
		if user.Roles:
			pre_payload += user.RolePayload()
		if user.Group:
			pre_payload += user.GroupPayload()
		if user.Attribute:
			pre_payload += user.CustomAttributePayload()
		#if user.Password:
		#	pre_payload += user.PasswordPayload()
		payload = self.PreparePayload(user_details + pre_payload)
		return payload

	def getUserIDByUsername(self, user):
		"""fetch userID using the Username of the user"""
		headers = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + self.url + "/username/" + user.Username.lower() + "?api_key=" + self.apikey
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
		target = "https://" + user.Subdomain +  self.url + "/username/" + user.Username.lower() + "?api_key=" + self.apikey
		r = requests.get(target, headers=headers)
		root = ET.fromstring(r.text)
		if r.status_code in (200,205):
			print "User informatino for user: %s is: %s." % (user.Username, r.text)
		else:
			print r.status_code

	def getUserByID(self, user):
		"""fetch user using the UserID of the user"""
		target = "https://" + user.Subdomain + self.url + "/" + str(user.UserID) + ".xml?api_key=" + self.apikey
		r = requests.get(target)
		print r.text

	def CreateUser(self, user):
		"""Create User in OneLogin using user object attributes
		calls getUserIDByUsername after user creation to update user object """
		#pre_payload = user.FirstNamePayload() + user.LastNamePayload() + user.EmailPayload() + user.UserNamePayload()
		payload = self.buildUserCreatePayload(user)
		header = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + self.url + ".xml?api_key=" + str(self.apikey)
		r = requests.post(target, headers=header, data=payload)
		#self.getUserIDByUsername(user)
		if r.status_code in (200,201,205):
			print "Success"
		else:
			print target, payload
			print r.status_code

	def DeleteUserByUsername(self, user):
		"""Delete user using the Username of the user"""
		target = "https://" + user.Subdomain + self.url + "/username/" + user.Username.lower() + "?api_key=" + self.apikey
		r = requests.delete(target)
		if r.status_code in (200,205):
			print "%s has been deleted." % (user.Username)
		else:
			print r.status_code

	def DeleteUserByUserID(self,user):
		"""Delete user using the UserID of the user"""
		#if not user.UserID:
		#	user.UserID = self.getUserIDByUsername(user)
		target = "https://" + user.Subdomain + self.url + "/" + str(user.UserID) + ".xml?api_key=" + self.apikey
		r = requests.delete(target)
		if r.status_code in (200,205):
			print "%s has been deleted." % (str(user.UserID))
		else:
			print r.status_code

	def UpdateUserByUsername(self, user):
		"""Update the user (PUT) by Username
		Used for Roles, Group, and Custom Attribute updates.
		Can also be used to set initial password for user in OneLogin"""
		payload = self.buildUserUpdatePayload(user)
		header = {'Content-Type':'application/xml'}
		target = "https://" + user.Subdomain + self.url + "/username/"+ user.Username.lower() +"?api_key=" + str(self.apikey)
		r = requests.put(target, headers=header, data=payload)
		if r.status_code in range(200,204,205):
			print payload
			print "%s has been updated." % (user.Username)
		else:
			print target, payload
			print r.status_code


	def UpdateUserByUserID(self, user):
		"""Update the user (PUT) by UserID
		Used for Roles, Group, and Custom Attribute updates.
		Can also be used to set initial password for user in OneLogin"""
		'''
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
		'''



	
		