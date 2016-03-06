
class MaxHeap():

    def __init__(self):
        self.size = 0
        self.heap=[0]

    def add(self,num):
        self.size+=1
        self.heap.append(num)
        self.siftUp(self.size)

    def top(self):
        temp = self.heap[1]
        self.heap[1]=self.heap[self.size]
        self.heap[self.size]=temp
        self.size-=1
        self.siftDown(1)
        return temp

    def remove(self,i):
        temp = self.heap[i]
        self.heap[i]=self.heap[self.size]
        self.heap[self.size]=temp
        self.size-=1
        self.siftDown(self,i)
        return temp

    def siftUp(self,child):
        if child==1: 
            return
        parent = child/2
        #print child,parent
        while child>=2 and self.heap[child]>self.heap[parent]:
         #   return child
            temp = self.heap[child]
            self.heap[child]=self.heap[parent]
            self.heap[parent]=temp
            child = parent
            parent = parent/2

    def siftDown(self,r):
        left = 2*r
        right = 2*r+1

        if left>self.size:
            return
        
        if right>self.size: 
            mmax=left
        else:
            if self.heap[left]<self.heap[right]:
                mmax = right
            else:
                mmax = left
        if self.heap[mmax]>self.heap[r]:
            temp = self.heap[mmax]
            self.heap[mmax]=self.heap[r]
            self.heap[r]=temp
            self.siftDown(mmax)

def test_max_heap():
    bst = MaxHeap()
    bst.add(30)
    bst.add(20)
    bst.add(40)
    bst.add(70)
    bst.add(60)
    bst.add(80)
    print bst.top()