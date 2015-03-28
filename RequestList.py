class RequestList:
	"""Maintains list of requests currently present in the system
       requestList : list of request type objects"""
	
	requestList = []

    #to add new request object to requestList
	def addToRequestList(self, request):
		self.requestList.append(request)

    #to remove a request from requestList in FIFO manner
	def removeFromRequestList(self):
		self.requestList = self.requestList[1:]
