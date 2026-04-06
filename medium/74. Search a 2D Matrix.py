# Link: https://leetcode.com/problems/search-a-2d-matrix


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        # find the right array
        while l <= r:
            m = l + ((r - l) // 2)
            # print(f"l: {l}, r: {r}, m: {m}")

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                # print(f"found the rigth array: {matrix[m]}")
                # find the right num inside the array
                arr_l, arr_r = 0, len(matrix[m])

                while arr_l <= arr_r:
                    arr_m = arr_l + ((arr_r - arr_l) // 2)
                    # print(f"arr_l: {arr_l}, arr_r: {arr_r}, arr_m: {arr_m}")
                    if matrix[m][arr_m] == target:
                        return True
                    elif matrix[m][arr_m] > target:
                        arr_r = arr_m - 1
                    else:
                        arr_l = arr_m + 1
                return False

            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        return False


# matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
# target = 10
# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target = 15
# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 3
# matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
# target = 15

# print(Solution().searchMatrix(matrix, target))
