import Request

class Buffer:
    """It realizes a FIFO queue of requests which are waiting (which doesn’t get any thread) to get executed.
       sizeOfBuffer : maximum number of requests that cab be buffered
       requestsInBuffer : contains list of Request objects, one for each request in the system
       bufferCount : maintains count of number of full slots in buffer """

    requestsInBuffer = []
    bufferCount = 0

    def __init__(self, sizeOfBuffer):
        Buffer.sizeOfBuffer = sizeOfBuffer

    def addToBuffer(self,request, requestList):
        if(Buffer.bufferCount < Buffer.sizeOfBuffer):
            print ('@@@@@@@@@@@ Buffered')
            self.requestsInBuffer.append(request)
            Buffer.bufferCount = Buffer.bufferCount + 1
        else:
            #remove request from requestList
            for x in range(len(requestList.requestList)):
                if (requestList.requestList[x].requestId == request.requestId):
                    print ('$$$$$$$$$$ Request '+ str(request.requestId) + ' is dropped due to buffer overflow.')
                    requestList.requestList = requestList.requestList[:x] + requestList.requestList[x+1:]
                    break

    @staticmethod
    def initBufferCount():
        Buffer.bufferCount = 0

    def removeFromBuffer(self):
        request = Request.Request(-1,-1,-1,-1,-1)

        if len(self.requestsInBuffer) != 0 :
            print ('@@@@@@@@@ Removed from buffer')
            Buffer.bufferCount = Buffer.bufferCount - 1
            request = self.requestsInBuffer[0]
            if len(self.requestsInBuffer) == 1 :
                self.requestsInBuffer = []
            else :
                self.requestsInBuffer = self.requestsInBuffer[1:]
        return request