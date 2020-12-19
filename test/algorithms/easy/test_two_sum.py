#!/bin/python3
"""
Given an array of integers nums and an integer target, return indices of the two 
numbers such that they add up to target.
"""
import pytest

from leetcode.algorithms.easy.two_sum import Solution


class TestTwoSum:
    def test_two_sum(self):
        """Case of valid data."""
        s = Solution()

        case = s.twoSum([2, 7, 11, 15], 9)
        expected = [0, 1]

        assert case == expected

    def test_two_sum_duplicates(self):
        """Case of valid data with duplicate elements in list."""
        s = Solution()

        case = s.twoSum([2, 2, 2, 2], 4)
        expected = [0, 1]

        assert case == expected

    def test_two_sum_erroneous(self):
        """Case of erroneous data using expected inputs."""
        s = Solution()

        case = s.twoSum([1, 2, 3, 4], 100)
        expected = None

        assert case == expected

    def test_two_sum_empty(self):
        """Case of erroneous data using an empty list."""
        s = Solution()

        case = s.twoSum([], 1000)
        expected = None

        assert case == expected

    def test_two_sum_single(self):
        """Case of erroneous data using a singleton list."""
        s = Solution()

        case = s.twoSum([1], 12345)
        expected = None

        assert case == expected
