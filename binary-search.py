'''
Author: Jerry9403 940341746@qq.com
Date: 2023-02-28 23:30:07
LastEditors: Jerry9403 940341746@qq.com
LastEditTime: 2023-02-28 23:54:03
FilePath: /leetcode/binary-search.py
url: https://leetcode-cn.com/problems/binary-search/
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def search(nums, target):
        length = len(nums)
        num = 0     
        left = nums[0 : length // 2]
        right = nums[length // 2 : ]
        if length == 1 and nums[0] == target:
            return num
        elif target in left:
            return search(left, target)
        elif target in right:
            return search(right, target) + len(left)
        else:
            return -1

        

nums = [-1,0,3,5,9,12]
target = 12
a = search(nums, target)
print(a)

# 思路：爷就是递归，注意在递归的时候直接return函数（17、19行），然后如果target在右边，要注意加上 len(left) 来保持索引值