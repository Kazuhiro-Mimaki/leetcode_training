class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x == 1 or x == -1:
            return x
        abs_v = abs(x)
        while abs_v % 10 == 0:
            abs_v //= 10
        if abs_v == 1:
            if x < 0:
                return -1
            else:
                return 1
        stack = ''
        while abs_v // 10 != 0:
            curr = abs_v % 10
            abs_v //= 10
            stack += str(curr)
            if abs_v // 10 == 0:
                stack += str(abs_v)
        if x < 0:
            return '-' + str(stack)
        else:
            return stack
