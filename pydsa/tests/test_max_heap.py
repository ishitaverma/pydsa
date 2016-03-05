from pydsa.max_heap import *


def test_max_heap():
    bst = MaxHeap()
    bst.add(30)
    bst.add(20)
    bst.add(40)
    bst.add(70)
    bst.add(60)
    bst.add(80)

    assert bst.top()==80
    assert bst.top()==70
    assert bst.top()==60
    assert bst.top()==40
    assert bst.top()==30
    assert bst.top()==20
