class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ls = self.dictionary[key]
        left = 0
        right = len(ls) - 1
        possibleVal = ""
        while (left <= right):
            mid = left + (right - left)//2
            if (ls[mid][0] == timestamp):
                return ls[mid][1]
            if ls[mid][0]<= timestamp:
                possibleVal = ls[mid][1]
            if (timestamp < ls[mid][0]):
                right = mid -1 
            else:
                left = mid + 1
        return possibleVal

"""
5, 10
timestamp =  1
1 < 5
"""