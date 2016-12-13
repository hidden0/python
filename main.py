#!/usr/bin/python
'''
Description:	Entry point for adding and testing code.

Author:			Johnathan Thorne
Date:			12/12/16
'''

'''
Description:	Object that represents a dashboard organization.

Fields:
	Loaded from file db_api_cred.key
	self.* ->
		apikey
		orgId
		networks[]

Methods:
	- listNetworks(): Enumerates networds per the given organization ID
	- getClientsList(networkId): Returns list of all clients on given networkId

Credentials File:
	- Should end in .key, to be properly ignored by source control
	- Should contain the API key and nothing but the API key, character for character
	[APIKEY]


Author:			Johnathan Thorne
Date:			12/12/16
'''
import requests as r
import json
import os

run = True

class DashboardOrganization:

	def __init__(self, creds):
    	# Check for credentials file - creds = path/to/creds/file
		keyFile = open(creds, 'r')
		if keyFile.closed:
			self.apikey = False
		else:
			self.apikey = keyFile.read()
			keyFile.close()
			self.apiUrl = "https://dashboard.meraki.com/api/v0/"
			self.apiAction = "organizations"
			self.getHeaders = {
				'x-cisco-meraki-api-key': self.getKey(),
    			'content-type': "application/json"
			}

	def getKey(self):
		return self.apikey

	def getOrgs(self):
		if self.apikey != False:
			# List all org IDs
			response = r.request("GET", self.apiUrl+self.apiAction, headers=self.getHeaders)
			parsed = json.loads(response.text)

			print "Organization ID's this API key has access to:\n"
			for i in range(len(parsed)):
				print parsed[i]['id']

def menu()
	print "1. Set API Key file\t2. List Organization IDs"
	print "3. Set Current Org\t4. Exit"
	
	os.system('cls')

while run:
	menu()