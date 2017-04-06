#define graph
class Graph(object):
    class AdjNode(object):
        #src,dst,cst
        def __init__(self,src,dst,cst=1):
            self.source=src
            self.destination=dst
            self.cost=cst
            self.next=None
    class AdjList(object):
        def __init__(self):
            self.head=None
    def __init__(self,cnt):
        self.count=cnt
        self.list=[None]*cnt
        i=0
        while i<cnt:
            self.list[i]=self.AdjList()
            self.list[i].head =None
            i +=1
    def AddEdge(self,source,destination,cost=1):
        node=self.AdjNode(source,destination,cost)
        node.next=self.list[source].head
        self.list[source].head=node
    def AddBiEdge(self,source,destination,cost=1):
        self.AddEdge(source,destination,cost)
        self.AddEdge(destination,source,cost)
    def Print(self):
        add=self.AdjNode()
        i=0
        while i<self.count:
            ad=self.list[i].head
            if ad!=None:
                print("Vertex",i,"is connected to:")
                while ad!=None:
                    print (ad.destination)
                    ad=ad.next
                print("")
            i+=1
