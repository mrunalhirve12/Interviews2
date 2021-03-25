"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""
class Solution:
    """ def isRobotBounded(self, i):
           s, d = 90, [0, 0]
        for a in i:
            if a == 'L': s = (s + 90) % 360
            elif a == 'R': s = (s - 90) % 360
            else:
                if s == 90: d[1] += 1
                elif s == 180: d[0] -= 1
                elif s == 270: d[1] -= 1
                else: d[0] += 1
        return s != 90 or d == [0, 0]"""

    def isRobotBounded(self, instructions: str) -> bool:
        x, y, face = 0, 0, 0
        directions = ["North", "West", "South", "East"]

        for instruction in instructions:
            if instruction == 'G':
                if directions[face] == "North":
                    x += 1
                if directions[face] == "West":
                    y -= 1
                if directions[face] == "South":
                    x -= 1
                if directions[face] == "East":
                    y += 1
            if instruction == 'L':
                face = (face + 1) % 4
            if instruction == 'R':
                face = (face - 1) % 4

        return (x == 0 and y == 0) or face != 0

s = Solution()
s.isRobotBounded("GGLLGG")