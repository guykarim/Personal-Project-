class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define constants for 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle edge case: overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Take the absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Subtract divisor shifted by the maximum possible power of 2 from dividend
        while dividend >= divisor:
            # Find the largest multiple
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # Subtract the found multiple from the dividend
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the result
        if negative:
            quotient = -quotient
        
        # Clamp the result to the 32-bit signed integer range
        return min(max(quotient, INT_MIN), INT_MAX)