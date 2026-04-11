# Link: https://leetcode.com/problems/time-based-key-value-store

class TimeMap:

    def __init__(self):
        self.names = {} # key => arr of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.names:
            self.names[key].append((timestamp, value))
        else:
            self.names[key] = [(timestamp, value)]   

    def get(self, key: str, timestamp: int) -> str:
        res, arr = "", self.names.get(key, [])
        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        

# timeMap = TimeMap()
# timeMap.set("alice", "happy", 1)  # store the key "alice" and value "happy" along with timestamp = 1.
# print(timeMap.get("alice", 1))    # return "happy"
# print(timeMap.get("alice", 2))    # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3)    # store the key "alice" and value "sad" along with timestamp = 3.
# print(timeMap.get("alice", 3))    # return "sad"
# print(timeMap.get("alice", 2))    # return "happy"