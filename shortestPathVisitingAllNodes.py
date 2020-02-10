'''
847. Shortest Path Visiting All Nodes

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
'''


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        dist = collections.Counter()
        dq = collections.deque()
        dest = (1 << len(graph)) - 1
        for i in range(len(graph)):
            dq.append((i, 0, 1 << i))
            dist[i, 1 << i] = 0

        while dq:
            node, total, state = dq.popleft()
            #print(node, total, state)
            if state == dest:
                return total
            for nb in graph[node]:
                next_state = state | (1 << nb)
                if (nb, next_state) in dist and dist[nb, next_state] <= total + 1:
                    continue
                dist[nb, next_state] = total + 1
                dq.append((nb, total + 1, next_state))
        return 0


