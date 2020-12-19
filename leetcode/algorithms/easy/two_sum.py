#!/bin/python3
"""
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Pass through each value while keeping track of complements.

        Runtime: 40 ms
        Memory usage: 14.3 MB
        """
        # Initialise a dict for storing compliments
        complements = {}
        for i in range(len(nums)):
            # Check if current value is a complement of another
            c = nums[i]
            if c in complements:
                return [complements[c], i]
            # Store the complement of the current value
            complements[target - c] = i
