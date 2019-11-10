from typing import List
import re


class MostCommonWord:
    @staticmethod
    def solve(paragraph: str, banned: List[str]) -> str:
        # Regular expression to ignore characters which are not alphabets,
        # transform to lower case, and split into a list of words
        words = re.sub(r'[^\w\s]', ' ', paragraph).lower().split(" ")

        to_ignore = set(banned)
        to_ignore.add('')
        table = dict()
        for w in words:
            if w not in to_ignore:
                table[w] = table.get(w, 0) + 1
        return sorted(table.keys(), key=lambda k: table[k], reverse=True)[0]


if __name__ == '__main__':
    paragraphs = ["Bob hit a ball, the hit BALL flew far after it was hit.", "Bob. hIt, baLl", "a, a, a, a, b,b,b,c, c"]
    banned_words = [["hit"], ["bob", "hit"], ["a"]]
    expected = ["ball", "ball", "b"]

    for p, b, e in zip(paragraphs, banned_words, expected):
        actual = MostCommonWord.solve(p, b)
        print(f"Input paragraph: '{p}'")
        print(f"Banned words: {b}")
        print(f"Expected: {e}")
        print(f"\tResponse: {actual}\n\n")
