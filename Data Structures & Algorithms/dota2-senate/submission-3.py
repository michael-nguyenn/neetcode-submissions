class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        arr = list(senate)

        while True:
            for i in range(len(arr)):
                if arr[i] == 'X': 
                    continue
                
                j = (i + 1) % len(arr)
                while j != i and (arr[j] == arr[i] or arr[j] == 'X'):
                    j = (j + 1) % len(arr)
                
                if j == i:
                    return "Dire" if arr[i] == 'D' else "Radiant"
                else:
                    arr[j] = 'X'
            

