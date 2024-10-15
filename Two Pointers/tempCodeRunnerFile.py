def trappedRainWater(height):
    l,r = 0,len(height) - 1
    maxLeft = height[l]
    maxRight = height[r]
    waterTrapped = 0
    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(height[l], maxLeft)
            waterTrapped += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(height[r], maxRight)
            waterTrapped += maxRight - height[r]
    return waterTrapped



height = [1,5,3,6,6,1,5,4,3,6,4,8,5]
print(trappedRainWater(height))