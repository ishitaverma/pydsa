
class MinHeap():

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
        while child>=2 and self.heap[child]<self.heap[parent]:
            #print child,parent
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
            mmin=left
        else:
            if self.heap[left]>self.heap[right]:
                mmin = right
            else:
                mmin = left
        if self.heap[mmin]<self.heap[r]:
            temp = self.heap[mmin]
            self.heap[mmin]=self.heap[r]
            self.heap[r]=temp
            self.siftDown(mmin)

 





