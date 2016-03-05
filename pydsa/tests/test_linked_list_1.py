from pydsa import linked_list_1
def test_linked_list_1():

    def __init__(self):
        self.test_list = linked_list()

    def test_insert_beg(self):
        self.test_list.insert_beginning("Ishita")
        self.assertTrue(self.test_list.head.return_data() == "Ishita")
        self.assertTrue(self.test_list.head.return_next() is None)

    def test_insert_end(self):
        self.test_list.insert_end("yo")
        curr=self.test_list.head
        while curr.return_next() is not None:
            curr.make_next(curr.return_next())
        self.assertTrue(curr.return_data=="yo")
        self.assertTrue(curr.return_next is None)

    def yes_search(self):
        self.test_list.insert_beginning("a")
        self.test_list.insert_beginning("b")
        self.test_list.insert_beginning("c")

        found = self.test_list.find("a")
        self.assertTrue(found.return_data() == "a")

        found = self.test_list.find("b")
        self.assertTrue(found.return_data() == "b")

        found = self.test_list.find("c")
        self.assertTrue(found.return_data() == "c")

    def test_delete(self):
        self.test_list.insert_beginning("a")
        self.test_list.insert_beginning("b")
        self.test_list.insert_beginning("c")

        self.test_list.delete("c")
        self.assertTrue(self.test_list.head.return_data() == "b")
        self.list.delete("a")
        self.assertTrue(self.test_list.head.return_next() is None)

        
