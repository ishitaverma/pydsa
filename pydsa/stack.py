class stack():
	def __init__(self,size):
		self.size=size
		self.data=[]

	def is_Stack_Full(self):
		if len(self.data)==self.size:
			return True
		else:
			return False

	def is_Stack_Empty(self):
		if len(self.data)==0:
			return True
		else:
			return False

	def push(self,data):
		if is_Stack_Full() is False:
			self.data.append(data)
		else:
			raise ValueError("Stack is full")

	def pop(self):
		if is_Stack_Empty is False:
			del_item = self.data[len(self.data) -1]
			del self.data[len(self.data) -1]
			return del_item
		else:
			raise ValueError ("Stack is empty")

	def top(self):
		if is_Stack_Empty is False:
			return self.data[len(self.data)-1]
		else:
			raise ValueError("Stack is empty")
