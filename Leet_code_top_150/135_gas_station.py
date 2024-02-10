class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
           return -1
        
        total = 0
        res = 0
        for i in range(0, len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0 
                res = i + 1

        return res
        