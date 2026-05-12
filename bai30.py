class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeros_to_duplicate = 0
        n = len(arr) - 1

        i = 0
        while i <= n - zeros_to_duplicate:
            if arr[i] == 0:
  
                if i == n - zeros_to_duplicate:
                    arr[n] = 0
                    n -= 1
                    break
                zeros_to_duplicate += 1
            i += 1
        last_idx = n - zeros_to_duplicate
        for j in range(last_idx, -1, -1):
            if arr[j] == 0:
                arr[j + zeros_to_duplicate] = 0
                zeros_to_duplicate -= 1
                arr[j + zeros_to_duplicate] = 0
            else:
                arr[j + zeros_to_duplicate] = arr[j]
        