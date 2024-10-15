from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash = {}

    def get(self, key, timestamp):
        return self.getnextLeastValue(key, timestamp)
    
    def set(self, key, value, timestamp):
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append([value, timestamp])


    def getnextLeastValue(self, key, timeStamp):
        values = self.hash.get(key, [])
        N = len(values)
        l,r = 0, N - 1
        res = ""
        while l<=r:
            mid = l + (r - l)//2
            if values[mid][1] == timeStamp:
                return values[mid][0]
            elif values[mid][1] < timeStamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res




timeDict = TimeMap()
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