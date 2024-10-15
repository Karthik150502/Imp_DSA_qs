from math import ceil, floor
def minEatingSpeed(piles, h):

    maxPiles = max(piles)
    def checkHours(n):
        hours = 0
        for pile in piles:
            hours += ceil(pile/n)
        return hours
    
    
        
    l,r = 1, maxPiles
    speed = maxPiles
    while l <= r:
        mid = l + (r - l)//2
        s = checkHours(mid)
        if s > h:
            l = mid + 1
        elif s <= h:
            r = mid - 1
            speed = min(speed, mid)

    return speed

piles = [3,6,7,11]
h = 8
res =  minEatingSpeed(piles, h)
print(res)

        



# print(ceil(5.01))
# print(floor(5.99))
# print(round(5.49))
# print(round(5.44))
# print(round(5.50))