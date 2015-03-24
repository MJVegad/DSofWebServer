class RequestList:
	"""Maintains list of requests currently present in the system"""
	
	requestList = []

	def addToRequestList(self, request):
		RequestList.requestList.append(request)
		

	def removeFromRequestList(self):
		RequestList.requestList = self.requestList[1:]
