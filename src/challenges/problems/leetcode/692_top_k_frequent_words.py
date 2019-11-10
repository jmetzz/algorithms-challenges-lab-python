from typing import List


class TopKFrequentWords:
    @staticmethod
    def solve(words: List[str], k: int) -> List[str]:
        table = dict()
        for w in words:
            table[w] = table.get(w, 0) + 1
        alphabetically = sorted(table.keys())

        return sorted(alphabetically, key=lambda k: table[k], reverse=True)[:k]


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    expected = ["i", "love"]
    actual = TopKFrequentWords.solve(words, 2)
    print(f"expected: {expected}")
    print(f"solution: {actual}")
    assert (expected == actual)
