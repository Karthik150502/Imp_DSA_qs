from collections import defaultdict

class TimeBasedD():

    def __init__(self):
        self.hash = {}

    def get(self, key, timestamp):
        return self.hash.get(key).get(self.getnextLeastValue(key, timestamp), "")
    
    def set(self, key, val, timestamp):
        if key not in self.hash:
            self.hash[key] = {}
        self.hash[key][timestamp] = val


    def getnextLeastValue(self, key, timeStamp):
        if timeStamp in self.hash[key]:
            return timeStamp
        keys =  list(self.hash[key].keys())
        N = len(keys)
        l,r = 0, N - 1
        greaterLeast = float("-inf")
        while l<=r:
            mid = l + (r - l)//2
            if keys[mid] < timeStamp:
                greaterLeast = max(greaterLeast,keys[mid])
                l = mid + 1
            else:
                r = mid - 1
        return greaterLeast if greaterLeast != float("-inf") else -1 


timeDict = TimeBasedD()
print(timeDict.set("foo", "bar", 1))
print(timeDict.get("foo", 1))
print(timeDict.get("foo", 3))
print(timeDict.set("foo", "bar2", 4))
print(timeDict.get("foo", 4))
print(timeDict.get("foo", 5))



'''
o/p
None
bar
bar
None
bar2
bar2
'''