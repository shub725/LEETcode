class Solution:
    def minOperations(self, nums):
        
        # function to check binary palindrome
        def isBinaryPalindrome(x):
            b = bin(x)[2:]
            return b == b[::-1]

        # precompute binary palindrome numbers
        pals = []
        for i in range(1, 10001):
            if isBinaryPalindrome(i):
                pals.append(i)

        ans = []

        for num in nums:
            best = float('inf')
            for p in pals:
                best = min(best, abs(num - p))
            ans.append(best)

        return ans