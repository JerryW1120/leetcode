'''
Author: Jerry9403 940341746@qq.com
Date: 2023-03-01 23:06:57
LastEditors: Jerry9403 940341746@qq.com
LastEditTime: 2023-03-01 23:11:35
FilePath: /leetcode/largest-local-values-in-a-matrix.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def largestLocal(grid):
        length = len(grid)
        maxLocal = []
        
        for i in range(length - 2):
            maxLocal.append([])
            for j in range(length - 2):
                max_num = grid[i][j]

                for temp_i in range(i, i + 3):
                    for temp_j in range(j, j + 3):
                        max_num = max(max_num, grid[temp_i][temp_j])

                maxLocal[i].append(max_num)

        return maxLocal 

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
a = largestLocal(grid)
print(a)
