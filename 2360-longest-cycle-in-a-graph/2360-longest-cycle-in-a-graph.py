class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def dfs(node,dist,nodes):
            
            if node in nodes:
                return dist - nodes[node]
            
            if seen[node]:
                return -1
            
            seen[node] = True
            
            if edges[node] != -1:
                nodes[node] = dist
                return dfs(edges[node],dist+1,nodes)
            else:
                return -1
        
        
        n = len(edges)
        seen = [False]*n
        result = -1
        
        for node in range(len(edges)):
            if not seen[node]:
                result = max(result,dfs(node,0,{}))
        
        return result
        