class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 确保 nums1 是较短的那个数组，这样二分查找会更快
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2  # 左半部分需要的元素个数
        
        while left <= right:
            i = (left + right) // 2  # 在 nums1 中切一刀的位置
            j = half_len - i         # 对应的，在 nums2 中切一刀的位置
            
            # 边界处理：如果切到了最左边或最右边，用无穷大/小代替
            nums1_left_max = nums1[i-1] if i > 0 else float('-inf')
            nums1_right_min = nums1[i] if i < m else float('inf')
            
            nums2_left_max = nums2[j-1] if j > 0 else float('-inf')
            nums2_right_min = nums2[j] if j < n else float('inf')
            
            # 核心判断：
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 找到了完美的切分点！
                
                # 如果总数是奇数，中位数就是左半部分最大的那个
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                else:
                    # 如果总数是偶数，中位数是 (左边最大 + 右边最小) / 2
                    return (max(nums1_left_max, nums2_left_max) + 
                            min(nums1_right_min, nums2_right_min)) / 2.0
            
            elif nums1_left_max > nums2_right_min:
                # nums1 左边太大了，要把切口往左移
                right = i - 1
            else:
                # nums1 左边太小了，要把切口往右移
                left = i + 1