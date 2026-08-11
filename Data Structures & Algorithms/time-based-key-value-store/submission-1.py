class TimeMap:

    def __init__(self):
        self.time_map = {} # key -> [(ts1, val1), (ts2, val2)...]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        # Get the list of timestamp tuples
        timestamps = self.time_map[key]

        # First and last entry determine the bounds of our binary search
        left, right = 0, len(timestamps) - 1
        res_idx = -1

        while left <= right:
            mid = (left + right) // 2

            ts, entry = timestamps[mid]

            if ts <= timestamp:
                left = mid + 1
                # since times are monotonically increasing, anytime we find a new
                # ts <= timestamp, it will always be the newer one
                res_idx = mid
            else:
                right = mid - 1
        
        return "" if res_idx == -1 else timestamps[res_idx][1]


        
        
        
