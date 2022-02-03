class disjointSet:
 parent={}

 def makeset(self,universe):
      for i in universe:
          self.parent[i]=i  

 def find(self,k):
     if (self.parent[k]==k):
         return k
     
     return(self.find(self.parent[k]))     

 def Union(self,a,b):

     x=self.find(a)
     y=self.find(b)

     self.parent[x]=y        

 def print(universe,ds):
      print([ds.find(i) for i in universe])     