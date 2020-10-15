class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        alpha = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        combination = []
        combinations = []

        def traceback(index: int):
            if index == len(digits):
                combinations.append(''.join(combination))
            else:
                digit = digits[index]
                for letter in alpha[digit]:
                    combination.append(letter)
                    traceback(index + 1)
                    combination.pop()

        traceback(0)
        return combinations
