class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i, cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or sum(cur) > target:
                return

            cur.append(candidates[i])
            bt(i, cur)
            cur.pop()
            bt(i + 1, cur)

        bt(0,[])
        return res

        