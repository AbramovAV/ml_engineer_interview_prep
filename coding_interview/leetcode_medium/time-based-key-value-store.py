class TimeMap:

    def __init__(self):
        self.data = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = {}
            self.data[key]["timestamps"] = []
        self.data[key][timestamp] = value
        self.data[key]["timestamps"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        low = 0
        if key not in self.data or timestamp < self.data[key]["timestamps"][0]:
            return ""
        high = len(self.data[key]["timestamps"])-1
        searched = None
        while low < high:
            idx = (high+low)//2 + 1
            mid = self.data[key]["timestamps"][idx]
            if mid < timestamp:
                low = idx + 1
            elif mid > timestamp:
                high = idx - 1
            else:
                searched = idx
                break
        if searched is None:
            searched = high
        return self.data[key][self.data[key]["timestamps"][searched]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)