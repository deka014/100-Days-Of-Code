# 981. Time Based Key-Value Store
# Medium
# 4.2K
# 401
# Companies

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

#     TimeMap() Initializes the object of the data structure.
#     void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#     String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"



class TimeMap:

    def __init__(self):
        self.keyMap = {}
        self.time = []
        self.value = []
        

    def set(self, key, value, timestamp) :
        if key in self.keyMap :
            self.keyMap[key][0].append(value)
            self.keyMap[key][1].append(timestamp)
        else :
            self.keyMap[key] = [[value],[timestamp]]     

    def get(self, key, timestamp):
        if key not in self.keyMap:
            return ""
        timearr = self.keyMap[key][1]
        valuearr = self.keyMap[key][0]

        l = 0 
        r = len(timearr) - 1

        while l <= r :
            m = (l + r) // 2 
            if timearr[m] == timestamp:

                return valuearr[m]
            
            if timearr[m] < timestamp :
                l = m+1
            else :
                r = m-1
        
        return valuearr[r] if r>=0 else ""
            

            




        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
