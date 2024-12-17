from collections import defaultdict

# Define gcd manually for compatibility
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 1:
            return n
        
        def calculate_slope(p1, p2):
            """Calculate the slope as a simplified tuple (dy, dx)."""
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            if dx == 0:  # Vertical line
                return (1, 0)
            if dy == 0:  # Horizontal line
                return (0, 1)
            d = gcd(dy, dx)
            return (dy // d, dx // d)
        
        max_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1  # Count the current point itself
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    duplicates += 1
                else:
                    slope = calculate_slope(points[i], points[j])
                    slopes[slope] += 1
            max_points_on_line = duplicates + (max(slopes.values()) if slopes else 0)
            max_points = max(max_points, max_points_on_line)
        
        return max_points