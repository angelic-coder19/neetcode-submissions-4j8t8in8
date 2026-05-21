"""
Understanding:
    Input: 2 arrays for distance and speed (integars) and integer target (final distance)
    Output: number of distinct fleets (groups of cars) to arrive at destination

    - A car cannot surpass a car that is before it, it con only catch up
    - If a car catches up at destination, it is part of the fleet
    - One car is considered a fleet

Match: 
    - Distinct groups that have the same arrival time
    - Stack (monotonically increasing stack)

Planning:
    - Declare an arry to count arrival times (distinct arrival times)
    - Iterate through the position and speed arrays
        - Calculate the time it takes for each car to arrive at destination
        - T = D / S
        - Compare this to the last item in the stack (if there are elements on the stack)
            - If last item on the stack is smaller than this time, add it to stack
            - Else skip the item because it is assumed that this car will catch up
    - Return the length of the stack because those are the distint times
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [i for i in zip(position, speed)]
        times = []
        
        for d, s in reversed(sorted(cars)):
            t = (target - d) / s
            if times and times[-1] < t or len(times) == 0:
                times.append(t)
        
        return len(times)