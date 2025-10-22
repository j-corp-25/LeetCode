# Last updated: 10/22/2025, 12:09:14 AM
class TimeMap:

    def __init__(self):
        self.map =defaultdict(list)



    # ["foo", "bar", 1]
    
    # ["foo", "bar2", 2]
    # map = {
    #     "foo": [("bar",1), ("bar2", 4)] 


    # }
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        #  mymap = defaultdict(list)
        # if key not in self.map:
        #     # value = []
        #     self.map[key] = []
        
        # print(self.map)
        # print(self.map[key])
        self.map[key].append((value,timestamp))
        # print(self.map)
        

        


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        array = self.map[key]
        answer = ""
 


        l, r = 0, len(array) - 1

        while l <= r:   
            
            mid = (l + r) // 2
            v = array[mid][0]
            t = array[mid][1]
            if t == timestamp:
                return v
            elif t > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                answer = v
        return answer
            


        




        

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)