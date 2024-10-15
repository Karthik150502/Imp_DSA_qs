def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    posAndSpeed = [[p,s] for p,s in zip(position, speed)]
    posAndSpeed.sort(key=lambda x:x[0], reverse = True)

    
    hours = [] #Is a stack, is the hours needed to reach the destination/ target, from the position and speed.

    for p,s in posAndSpeed:
        hours.append((target - p)/s)
        if len(hours) >= 2 and hours[-2] >= hours[-1]:
            hours.pop()
    return len(hours) 
    

positions = [10,8,0,5,3]
speeds = [2,4,1,1,3]

# posAndSpeed = [
#     [10, 2],   => (target - p)/s = (12 - 10)/2 = 1
#     [8, 4],   => (target - p)/s = (12 - 8)/4 = 1
#     [5, 1],   => (target - p)/s = (12 - 5)/1 = 7
#     [3, 3],   => (target - p)/s = (12 - 3)/3 = 3
#     [0, 1],   => (target - p)/s = (12 - 0)/1 = 12
# ]
target = 12
res = carFleet(target,positions, speeds)
print(res) 


