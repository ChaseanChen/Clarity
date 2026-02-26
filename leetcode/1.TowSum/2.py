# 哈希表 Dict
# 遍历次数 n
# 复杂度 O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums): # enumerate 会返回数组的索引和数值
            temp = target - num
            if temp in hash_map:
                return [hash_map[temp], i]
            hash_map[num] = i
        return []