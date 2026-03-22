# Link: https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set)  # index: (row//3 , col//3)

        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == ".":
                    continue

                if (
                    ele in rows[r]
                    or ele in cols[c]
                    or ele in sub_boxes[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(ele)
                cols[c].add(ele)
                sub_boxes[(r // 3, c // 3)].add(ele)
        return True


# board = [
#     ["1", "2", ".", ".", "3", ".", ".", ".", "."],
#     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
#     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
#     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", ".", ".", ".", ".", ".", "2", ".", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print("first:", Solution().isValidSudoku(board))

# board = [
#     ["1", "2", ".", ".", "3", ".", ".", ".", "."],
#     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
#     [".", "9", "1", ".", ".", ".", ".", ".", "3"],
#     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
#     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", ".", ".", ".", ".", ".", "2", ".", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print("second:", Solution().isValidSudoku(board))
