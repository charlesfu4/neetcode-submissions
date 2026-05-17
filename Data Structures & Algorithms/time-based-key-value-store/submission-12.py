class TimeMap:

    def __init__(self):
        self.hmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hmap:
            self.hmap[key] = [(timestamp, value)]
        else:
            self.hmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.hmap:
            return ""
        else:
            if timestamp < self.hmap[key][0][0]:
                return ""

            else:
                l = 0 
                r = len(self.hmap[key]) - 1
    
                while l <= r:
                    m = l + (r - l) // 2
                    if timestamp > self.hmap[key][m][0]:
                        l = m + 1
                    elif timestamp < self.hmap[key][m][0]:
                        r =  m - 1
                    else:
                        return self.hmap[key][m][1]
                return self.hmap[key][min(m,l,r)][1]
        
