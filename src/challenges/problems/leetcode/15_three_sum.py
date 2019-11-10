import itertools
from typing import List


class ThreeSum:
    def solve(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        triplets = []
        zeros, negatives, positives = self.split_nums(nums)
        # case zero: [zero, zero, zero]
        if zeros >= 3:
            triplets.append([0, 0, 0])
        # case 1:  [negative, zero, positive]
        if zeros > 0:
            for n in negatives:
                if -n in positives:
                    triplets.append([n, 0, -n])

        # case 2:  [negative, negative, positive]
        pairs = itertools.combinations_with_replacement(negatives.keys(), 2)
        for n1, n2 in pairs:
            if n1 == n2 and negatives[n1] < 2:
                continue
            comp = -(n1 + n2)
            if comp in positives:
                triplets.append([n1, n2, comp])

        # case 3:  [negative, positive, positive]
        pairs = itertools.combinations_with_replacement(positives.keys(), 2)
        for p1, p2 in pairs:
            if p1 == p2 and positives[p1] < 2:
                continue
            comp = -(p1 + p2)
            if comp in negatives:
                triplets.append([comp, p1, p2])

        return triplets

    @staticmethod
    def split_nums(elements):
        zeros = 0
        negatives = dict()
        positives = dict()

        for e in elements:
            if e == 0:
                zeros += 1
            elif e < 0:
                if e not in negatives:
                    negatives[e] = 0
                negatives[e] += 1
            else:
                if e not in positives:
                    positives[e] = 0
                positives[e] += 1
        return zeros, negatives, positives

    @staticmethod
    def _pair_combination_with_replacement(elements):
        """DEPRECATED in favor of itertools.
        This method is here only to illustrate a combination
        with replacement simple implementation.
        It is not optimized, and therefor much slower
        than itertools' implementation
        """
        n = len(elements)
        result = []
        for i in range(n):
            for j in range(i, n):
                result.append((elements[i], elements[j]))
        return result


if __name__ == '__main__':

    # big_list = [-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15,
    #             -14, 5, -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11,
    #             -1, 14, 10, -9, -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2,
    #             -5, 14, -3, -1, -10, -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4,
    #             1, 8, 1]

    input_lists = [
        [],
        [1, -1],
        [1, 0, -1],
        [1, 2, 3],
        [-1, -2, 3],
        [-1, 0, 1, 2, -1, -4],
        [3, 0, -2, -1, 1, 2],
    ]
    for l in input_lists:
        print(f"original list: {l}")
        print(f"\tsolution: {ThreeSum().solve(l)}")
        print("------\n")
