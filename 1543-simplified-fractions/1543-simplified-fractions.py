import math

class Solution:
    def simplifiedFractions(self, n: int):
        result = []
        
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if math.gcd(numerator, denominator) == 1:
                    result.append(f"{numerator}/{denominator}")
        
        return result