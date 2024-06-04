class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        q.append(startGene)

        dist = {}
        dist[startGene] = 0

        def delta(a, b):
            count = 0
            for x, y in zip(a,b):
                if x!=y:
                    count += 1
            return count
        
        while q:
            cur = q.popleft()
            for candidate in bank:
                if candidate not in dist and delta(candidate, cur) <=1:
                    dist[candidate] = dist[cur] + 1
                    q.append(candidate)

        if endGene not in dist:
            return -1
        return dist[endGene]
