class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        overall_surplus = surplus = 0
        i = j =0
        for g,c in zip(gas,cost):
            diff =g-c

            surplus += diff
            overall_surplus += diff

            if(surplus<0):
                surplus = 0
                i = j+1
            
            j +=1

        return -1 if overall_surplus<0 else i