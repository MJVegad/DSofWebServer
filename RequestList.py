class RequestList:
	"""Maintains list of requests currently present in the system"""
	
	requestList = []

	def addToRequestList(self, request):
		self.requestList.append(request)
		

	def removeFromRequestList(self):
		self.requestList = self.requestList[2:]		
