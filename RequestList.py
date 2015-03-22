class RequestList:
	"""Maintains list of requests currently present in the system"""
	requestsList = []

	def addToRequestList(self, request = None, list = None):
		if request is not None:
			self.requestsList.append(request)
		else:
			self.requestsList = self.requestsList + list


	def removeFromRequestList(self):
		self.requestsList = self.requestsList[2:]		