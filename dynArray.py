#!usr/bin/python

class dynArray(object):

	def __init__(self):
		self.arr=[]
		self.limit = 1
		self.count = 0
		self.current = -1
		
	def putData(self,data):
		
		if self.count < self.limit:
			self.arr.append(data)
			self.count +=1
			
		else:
			self.resize()
			self.arr.append(data)
			
			
	
	def getData(self):
		if self.count is 0:
			return "array is empty"
			
		else:
			self.current +=1
			return self.arr[self.current]
			
			
	def resize(self):
	
		newArray = list(self.arr)
		self.limit = 2*self.limit
		self.arr = newArray
		
		
d1 = dynArray()
d1.putData("hi")
d1.putData("i")
d1.putData("am")
d1.putData("mrugesh")
d1.putData("and")
d1.putData("you")
print(d1.getData())
print(d1.getData())
print(d1.getData())
print(d1.getData())