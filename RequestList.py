class RequestList:
	"""Maintains list of requests currently present in the system"""
	requestsList = []

	def addToRequestList(self, request):
		self.requestsList.append(request)
		

	def removeFromRequestList(self):
		self.requestsList = self.requestsList[2:]		
