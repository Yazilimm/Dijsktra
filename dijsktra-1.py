from collections import defaultdict
import heapq as heap

def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heap.heappush(pq, (0, startingNode))
 
	while pq:
		_, node = heap.heappop(pq)
		visited.add(node)
 
		for adjNode, weight in G[node].items():
			if adjNode in visited:	continue
				
			newCost = nodeCosts[node] + weight
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heap.heappush(pq, (newCost, adjNode))
        
	return parentsMap, nodeCosts

if __name__=="__main__":
    graph ={
        "1":{"2":5,"3":7},
        "2":{"1":5,"4":3,"5":6},
        "3":{"1":7,"4":4, "5":5},
        "4":{"2":3,"3":4,"6":2},
        "5":{"2":6,"3":5,"7":4},
        "6":{"4":2,"7":2},
        "7":{"5":4,"6":2}
        }
    source="1"
    dijkstra(graph,source)