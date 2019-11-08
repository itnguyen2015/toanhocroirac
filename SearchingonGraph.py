
from collections import defaultdict

file = open("sgb-words.txt")
words = file.read().split('\n')
file.close()

def compare_string(str1, str2):
    count = 0
    for i in range(5):
        if str1[i] != str2[i]:
            count += 1
                
    return count == 1


class GraphA:
    def __init__(self):
        self.V = len(words)
        self.graph = [[] for _ in range(self.V)]
        
        for i in range(self.V - 1):
            for j in range(i + 1, self.V):
                if compare_string(words[i], words[j]):
                    self.graph[i].append(j)
                    self.graph[j].append(i)
  
    
    def DFS(self, v, mark):
        mark[v] = True
        for ver in self.graph[v]:
            if not mark[ver]:
                self.DFS(ver, mark)
    
    def DemSoThanhPhanLienThong(self):
        mark = [False] * (self.V)
        count = 0
        while False in mark:
            for ver in range(self.V):
                if not mark[ver]:
                    break
            
            self.DFS(ver, mark)
            count += 1
            
        return count
    
    def TimDuongNganNhat(self, str1, str2):
        u = words.index(str1)
        v = words.index(str2)
        check = False
        
        queue = [u]
        visited = []
        state = {}
        path = []
        
        while queue:
            cur = queue.pop(0)
            if cur == v:
                path.append(v)
                check = True
                break
                
            for ver in self.graph[cur]:
                if ver not in visited:
                    queue.append(ver)
                    visited.append(ver)
                    state[ver] = cur

        if check == True:
            while v != u:
                v = state[v]
                path.append(v)
                
            path.reverse()
            for v in path:
                print(words[v], end = ' ')
            return path
        else:
            print('Không tồn tại đường đi.')
        

   
            