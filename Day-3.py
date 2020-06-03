class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: x[1]-x[0])
        print(costs)
        if(costs[0][0]<costs[0][1]):
            first=0
            second=1
        else:
            second=0
            first=1
        cost=0
        for i in range(len(costs)//2):
            print(costs[i][first])
            cost=cost+costs[i][first]
        for i in range(len(costs)//2,len(costs)):
            print(costs[i][second])
            cost=cost+costs[i][second]
        return cost    