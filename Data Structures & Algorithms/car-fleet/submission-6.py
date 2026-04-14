class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position is the number of miles in, in a target mile
        collection = []
        for p, s in zip(position, speed):
            collection.append((p, s))
        collection.sort(reverse=True)
        stack = []
        for p, s in collection:
            time = (target-p)/s
            if (stack and stack[-1] < time) or (not stack) :
                stack.append(time)
        return len(stack)

"""
dictionary- max mile : max time 
time - time required to reach target (target - mile)/speed[i]

if current mile is < mile and current time > time, we have a fleet
if current mile > mile and current time < time, we have a fleet


Input: target = 10, position = [1,4], speed = [3,2]

time
0th = (10-1)/3 = 3
1th = (10-4)/2 = 3

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

time
0th = (10-4)/2 = 3
1th = (10-1)/2 = 4.5
2th = (10-0)/1 = 10
3th = (10-7)/1 = 3
4th = (10-5)/1 = 5

0/3, 1, 2 = 3 fleets

"""
        