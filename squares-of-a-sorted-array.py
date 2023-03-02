'''
Author: Jerry9403 940341746@qq.com
Date: 2023-03-02 22:41:29
LastEditors: Jerry9403 940341746@qq.com
LastEditTime: 2023-03-02 22:41:53
FilePath: /leetcode/squares-of-a-sorted-array.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def sortedSquares(nums):
        
        pow_list = []
        for i in nums:
            pow_list.append(pow(i, 2))
        pow_list.sort()
        return pow_list