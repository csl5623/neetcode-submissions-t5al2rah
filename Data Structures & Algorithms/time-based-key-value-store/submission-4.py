class TimeMap:

    def __init__(self):
        self.values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        self.values[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        max_value = ""
        if len(self.values) > 0:
            if key in self.values:
                values = self.values[key]
                max_timestamp = values[0][1]
                for v,t in values:
                    if t<=timestamp:
                        if t >= max_timestamp:
                            max_timestamp = t
                            max_value = v
                return max_value
        return max_value
