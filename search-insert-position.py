'''
Author: Jerry9403 940341746@qq.com
Date: 2023-03-02 01:10:14
LastEditors: Jerry9403 940341746@qq.com
LastEditTime: 2023-03-02 01:10:38
FilePath: /leetcode/search-insert-position.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def searchInsert(self, nums, target):
        length = len(nums)
        left = 0
        right = length

        while(left < right - 1):
            cpm = (left + right) // 2
            if target == nums[cpm]:
                return cpm
            elif target > nums[cpm]:
                left = cpm               
            else:
                right = cpm


        if target <= nums[left]:
            return left
        else:
            return right
        
        # 仍然是简单的二分查找