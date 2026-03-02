class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        init_lenght = 0 
        max_lenght = 0
        for i, num in enumerate(s):
            if num in dict: # 判断新的值是否在哈希表中
                if dict[num] >= init_lenght: # 判断值是否在左边界以外
                    init_lenght = dict[num] + 1  # 更新左边界位置

            lenght = i - init_lenght + 1 # 更新此时长度
            if lenght > max_lenght: # 比较此时长度和上一次长度
                max_lenght = lenght  # 如果此时长度大于上一次长度，更新
            
            dict[num] = i # 更新右边界
        return max_lenght # 最终返回最长长度
        