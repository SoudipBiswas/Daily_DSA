class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:

        graph = {i: [] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)
            
        suspicious = [False] * n
        suspicious[k] = True
        queue = [k]
        
        for u in queue:
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    queue.append(v)
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
                
        return [i for i in range(n) if not suspicious[i]]
