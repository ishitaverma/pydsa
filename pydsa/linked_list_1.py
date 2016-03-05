class linked_list_node(object):
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node=next_node

	def return_next(self):
		return self.next_node

	def return_data(self):
		return self.data

	def make_next(self, new_next_node):
		self.next_node=new_next_node

class linked_list(object):
	def __init__(self, head=None):
		self.head=head

	def insert_beginning(self, data):
		new_node=linked_list_node(data)
		new_node.make_next(self.head)
		self.head=new_node

	def insert_end(self,data):
		curr_node=self.head
		while curr_node.return_next() is not None:
			curr_node.make_next(curr_node.return_next())
		new_node=linked_list_node(data)
		new_node=curr_node
		new_node.make_next(None)

	def find(self, data):
		found_flag=False
		curr_node=self.head
		while(curr_node is not None and found_flag is False):
			if curr_node.return_data==data:
				found_flag=True
			else:
				curr_node.make_next(curr_node.return_next())
		if curr_node is None:
			raise ValueError("not present")
		return curr_node

	def delete(self, data):
		curr_node=self.head
		prev_node=None
		found_flag=False
		while curr_node is not None and found_flag is False:
			if curr_node.return_data()==data:
				found_flag=True
			else:
				prev_node=curr_node
				curr_node=curr_node.return_next()
		if curr_node is None:
			raise ValueError("Not present")
		if prev_node is None:
			self.head=curr_node.return_next()
		else:
			prev_node.make_next(curr_node.return_next())

		





