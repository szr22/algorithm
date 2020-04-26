"""
Given n ropes of different lengths, we need to connect these ropes into one rope.
We can connect only 2 ropes at a time.
The cost required to connect 2 ropes is equal to sum of their lengths.
The length of this connected rope is also equal to the sum of their lengths.
This process is repeated until n ropes are connected into a single rope.
Find the min possible cost required to connect all ropes.

Input: ropes = [8, 4, 6, 12]
    Output: 58
    Explanation: The optimal way to connect ropes is as follows
    1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
    2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
    3. Connect the ropes of length 18 and 12 (cost is 30).
    Total cost to connect the ropes is 10 + 18 + 30 = 58

hint: min heap
"""

import heapq

ropes = [8, 4, 6, 12]
heapq.heapify(ropes)
total_cost = 0

def connect_ropes(total_cost):
    rope1 = heapq.heappop(ropes)
    rope2 = heapq.heappop(ropes)
    cost = rope1+rope2
    heapq.heappush(ropes, cost)
    return cost

while len(ropes)>1:
    total_cost += connect_ropes(total_cost)

print(ropes)
print(total_cost)