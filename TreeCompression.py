# -*- coding: utf-8 -*-
"""
@Name: Tree Compression
"""
from collections import defaultdict

class Tree:
    def __init__(self, n):
        self.V = n
        self.tree = None
    
    def PruferCode(self):
        deg = defaultdict(int)
        PruferCode = []
        
        for egde in self.tree:
            deg[egde[0]] += 1
            deg[egde[1]] += 1
            
        for i in range(self.V - 1):
            for x in range(self.V):
                if deg[x] == 1:
                    break
            
            y = None
            for edge in self.tree:
                if edge[0] == x:
                    y = edge[1]
                elif edge[1] == x:
                    y = edge[0]
                if y is not None:
                    break
            
            PruferCode.append(y)
            for ver in (x, y):
                deg[ver] -= 1
                if not deg[ver]:
                    deg.pop(ver)
                    
            self.tree.remove(edge)
        
        return PruferCode


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        
    T = Tree(n)
    T.tree = arr
    x = T.PruferCode()
    print(x)
    
    

