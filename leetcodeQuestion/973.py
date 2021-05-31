from typing import List
'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
#Simplest method, not sort all of them and select first k
#time complexity: O(nlogn)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tempList = [[x*x+y*y,x,y] for (x,y) in points]
        tempList.sort(key= lambda P:P[0])
        output = [[lis[1],lis[2]] for lis in tempList]
        return output[:k]
#Using heap, only certain number were stored in the heap 
#time complexity: O(nlog(k)),k=maximum size of heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tempList = []
        heapq.heapify(tempList)
        for point in points:
            distance = -1*(point[0]*point[0] + point[1]*point[1])
            if len(tempList)<k:
                heapq.heappush(tempList,(distance,point))
            else:
                heapq.heappushpop(tempList,(distance,point))
        return [p for (_,p) in tempList]
