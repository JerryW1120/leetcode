'''
Author: Jerry9403 940341746@qq.com
Date: 2023-03-02 22:42:14
LastEditors: Jerry9403 940341746@qq.com
LastEditTime: 2023-03-02 22:42:42
FilePath: /leetcode/rotate-array.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        left = nums[0: -k]
        right = nums[-k: ]
        len_right = len(right)
        for i in range(len(nums)):
            if i < len_right:
                nums[i] = right[i]
            else:
                nums[i] = left[i - len_right]