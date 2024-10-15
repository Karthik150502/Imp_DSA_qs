def mostWater(heights):
    l,r = 0,len(heights) - 1
    mostWater =  float("-inf")
    while l < r:
        water = min(heights[l], heights[r]) * (r - l)
        mostWater = max(water, mostWater)
        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1
    
    return mostWater
    ...



heights = [1,8,6,2,5,4,8,3,7]

res = mostWater(heights)
print(res)