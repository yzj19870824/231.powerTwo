__author__ = 'jerry'

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # lst = []
        # while n != 0:
        #     lst.append(n%2)
        #     n /= 2
        # lst.reverse()
        #
        # if num & (num-1) == 0:
        #     return True
        # else:
        #     return False

        # bit = []
        # while True:
        #     if n == 0: break
        #     n,rem = divmod(n,2)
        #     bit.append(str(rem))
        #     # print(bit)
        # num = ''.join(bit[::-1])
        # print(num)
        # print(type(num))
        if n <= 0:
            return False

        sr = ""
        while n != 0:
            sr += str(n%2)
            n /= 2

        sr = sr[::-1]
        num = int(sr,2)
        if num & (num-1) == 0:
            return True
        else:
            return False
if __name__ == "__main__":
    n = 9
    so = Solution()
    print(so.isPowerOfTwo(n))

