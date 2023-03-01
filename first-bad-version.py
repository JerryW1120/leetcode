'''
Author: Jerry9403 940341746@qq.com
Date: 2023-03-01 23:40:45
LastEditors: Jerry9403 940341746@qq.com
LastEditTime: 2023-03-02 00:36:13
FilePath: /leetcode/first-bad-version.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def isBadVersion(n: int) -> bool:
     m = 4
     return n < m
    

def firstBadVersion(n: int) -> int:
    left = 1
    right = n
    while left < right:
        mid = (right + left) // 2
        if isBadVersion(mid):
            left = mid + 1
        else:
            right = mid
            
    return left

n = 5
a = firstBadVersion(n)
print(a)

#简单版本的二分查找，不一定要用递归啊，直接用while循环就好了，注意边界条件，left < right，最后返回left就好了