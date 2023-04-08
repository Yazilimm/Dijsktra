import sys
from heapq import heapify, heappush

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data={"1":{'cost':inf,'pred':[]},
               "2":{'cost':inf,'pred':[]},
               "3":{'cost':inf,'pred':[]},
               "4":{'cost':inf,'pred':[]},
               "5":{'cost':inf,'pred':[]},
               "6":{'cost':inf,'pred':[]},
               "7":{'cost':inf,'pred':[]}
               }
    node_data[src]['cost']=0
    visited=[]
    temp=src
    
    for i in range(6):
        if temp not in visited: 
            visited.append(temp)
            min_heap=[]
            for j in graph[temp]:
                if j not in visited:
                    cost =  node_data[temp]['cost']+ graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost']=cost
                        node_data[j]['pred']=node_data[temp]['pred'] + list(temp)
                    heappush(min_heap, (node_data[j]['cost'],j))    
        heapify(min_heap)
        temp = min_heap[0][1]
    print("shortest distance:"+str(node_data[dest]['cost']))
    print("shortest path:"+ str(node_data[dest]['pred']+list(dest)))
        
    
if __name__=="__main__":
    graph ={
        "1":{"2":5,"3":7},
        "2":{"4":3,"5":6},
        "3":{"1":7,"4":4, "5":5},
        "4":{"2":3,"3":4,"6":2},
        "5":{"2":6,"3":5,"7":4},
        "6":{"4":2,"7":2},
        "7":{"5":4,"6":2}
        }
    source="1"
    destination ="7"
    dijsktra(graph,source,destination)