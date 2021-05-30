from typing import *
'''
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        hashmap = {}
        maxvalue = 0
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 1
            else:
                hashmap[task] += 1
            maxvalue = max(hashmap[task],maxvalue)
        output = (maxvalue-1)*(n+1)
        for key in hashmap:
            if hashmap[key] == maxvalue:
                output += 1
        return max(len(tasks),output)