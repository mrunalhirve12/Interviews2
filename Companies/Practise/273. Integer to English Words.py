"""
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"


Constraints:

0 <= num <= 231 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        single_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        double_map = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"}

        cents = ["thousand", "million", "billion"]

        def get_word(num_str):
            """perform arithmetic in sets of three
            """
            num = int(num_str)
            if num == 0:
                return ""
            if 1 <= num <= 19:  # single digit
                return single_map[num]
            elif 20 <= num <= 99:
                num_str = str(num)
                current_num = int(num_str[0])
                buffer = double_map[current_num]
                return (buffer + " " + get_word(num_str[1:])).strip()
            elif 100 <= num <= 999:
                num_str = str(num)
                current_num = int(num_str[0])
                buffer = single_map[current_num]
                final_value = buffer + " Hundred " + get_word(num_str[1:])
                return final_value.strip()

        # break the number into 3 sets (international repr)
        if num == 0:
            return "Zero"
        num_str = str(num)
        buffer = ""
        count = 0
        while num_str:
            temp = get_word(num_str[-3:])
            if count < 3:
                buffer = temp + buffer
            elif count == 3 and temp:
                buffer = temp + " Thousand " + buffer
            elif count == 6 and temp:
                buffer = temp + " Million " + buffer
            elif count == 9 and temp:
                buffer = temp + " Billion " + buffer
            buffer = buffer.strip()
            num_str = num_str[:-3]
            count += 3

        return buffer.strip()

s = Solution()
s.numberToWords(123)