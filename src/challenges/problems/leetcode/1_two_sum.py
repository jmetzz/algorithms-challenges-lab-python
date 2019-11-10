from typing import List


class TwoSum1:
    @staticmethod
    def solve(nums: List[int], target: int) -> List[int]:
        table = {e: idx for idx, e in enumerate(nums)}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in table and table[complement] != i:
                return [i, table[complement]]
        raise ValueError("no solution given the input")


class TwoSum2:
    @staticmethod
    def solve(nums: List[int], target: int) -> List[int]:
        table = {nums[0]: 0}
        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in table and table[complement] != i:
                return [table[complement], i]
            table[nums[i]] = i
        raise ValueError("no solution given the input")


if __name__ == '__main__':
    print(TwoSum2.solve([0, -2, -1, 1, 2], -3))
