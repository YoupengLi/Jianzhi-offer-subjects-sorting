# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 0013 下午 10:30
# @Author  : Youpeng Li
# @Site    : 
# @File    : jumpFloor.py
# @Software: PyCharm

'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

对于本题,前提只有 一次 1阶或者2阶的跳法。
a.如果两种跳法，1阶或者2阶，那么假定第一次跳的是一阶，那么剩下的是n-1个台阶，跳法是f(n-1);
b.假定第一次跳的是2阶，那么剩下的是n-2个台阶，跳法是f(n-2)
c.由a、b假设可以得出总跳法为: f(n) = f(n-1) + f(n-2) 
d.然后通过实际的情况可以得出：只有一阶的时候有 f(1) = 1 ,只有两阶的时候有 f(2) = 2
e.可以发现最终得出的是一个斐波那契数列：
       | 1, (n=1)
f(n) = | 2, (n=2)
       | f(n-1)+f(n-2) ,(n>2,n为整数)
'''

class Solution:
    def jumpFloor(self, num: 'int') -> 'int':
        res = [1, 2]
        while len(res) < num:
            res.append(res[-1] + res[-2])
        if num == 1:
            return 1
        else:
            return res[num - 1]

if __name__ == "__main__":
    a = Solution()
    num = 38
    print(a.jumpFloor(num))