# Link: https://leetcode.com/problems/car-fleet


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        count = 0
        arr = list(zip(position, speed))

        leadTime = None
        for p, s in sorted(arr)[::-1]:
            time = (target - p) / s
            if not leadTime or time > leadTime:
                leadTime = time
                count += 1
            # print(f"i: {i}; time: {time}; leadTime: {leadTime}; count: {count}")
        return count


# print("carFleet:", Solution().carFleet(target=10, position=[1, 4], speed=[3, 2]))  # 1
# print(
#     "carFleet:",
#     Solution().carFleet(target=10, position=[4, 1, 0, 7], speed=[2, 2, 1, 1]),
# )  # 13
# print(
#     "carFleet:",
#     Solution().carFleet(
#         target=10, position=[8, 3, 7, 4, 6, 5], speed=[4, 4, 4, 4, 4, 4]
#     ),
# )  # 6
