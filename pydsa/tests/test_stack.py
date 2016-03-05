from pydsa import stack
def test_stack():
	def __init__(self, size):
		self.stack= stack()
		stack.size=5

	def test_push(self):
		self.stack.push("1")
		self.stack.push("2")
		self.stack.push("3")
		self.stack.push("4")
		self.assertTrue(len(self.stack.data)==4)
		self.assertTrue(self.stack.top()==4)

	def test_pop(self):
		self.stack.push("1")
		self.stack.push("2")
		self.stack.push("3")
		self.stack.push("4")
		self.stack.pop()
		self.assertTrue(len(self.stack.data)==3)
		self.assertTrue(self.stack.top()==3)
