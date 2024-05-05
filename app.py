class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Hashmap:

    def __init__(self, occupiedBuckets = 0):
        self.size = 10
        self.map = [None] * self.size
        self.loadFactor = 0.7
        self.occupiedBuckets = occupiedBuckets

    def hash(self, key):
        hashCode = 0
      
        primeNumber = 31
        for char in key:
            hashCode = primeNumber * hashCode + ord(char)
        
        bucket = hashCode % self.size

        return bucket
    
    def rehash(self):
        oldMap = self.map

        self.size *= 2
        self.map = [None] * self.size
        self.occupiedBuckets = 0

        for bucket in oldMap:
            if bucket is not None:
                key, value = bucket.val
                self.set(key, value)

    def set(self, key, value):
        bucket = self.hash(key)

        if self.map[bucket] is not None:
            head = self.map[bucket]
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = Node((key, value))
        else:
            self.map[bucket] = Node((key, value))

        self.occupiedBuckets += 1

        if self.occupiedBuckets / self.size == self.loadFactor:
            self.rehash()

        return self.map
    
    def get(self, key):
        bucket = self.hash(key)

        if self.map[bucket] is None:
            return None
        else:
            head = self.map[bucket]
            curr = head

            while curr:
                if curr.val[0] == key:
                    return curr.val[1]
                else:
                    curr = curr.next

            return None
    
    def has(self, key):
        bucket = self.hash(key)

        if self.map[bucket] is None:
            return False
        else:
            head = self.map[bucket]
            curr = head

            while curr:
                if curr.val[0] == key:
                    return True
                else:
                    curr = curr.next

            return False

    def remove(self, key):
        bucket = self.hash(key)

        if self.map[bucket] is None:
            return False
        else:
            head = self.map[bucket]
            curr = head

            if curr.next == None:
                self.map[bucket] = None

            elif curr.val[0] == key:
                self.map[bucket] = curr.next
                return True
            
            else:
                while curr.next:
                    prev = curr
                    curr = curr.next
                    next = curr.next
                    if curr.val[0] == key:
                        prev.next = next
                        return True

                return False

    def length(self):
        count = 0
        for i in range(self.size):
            if self.map[i] is not None:
                curr = self.map[i]
                while curr:
                    count += 1
                    curr = curr.next
        return count
    
    def clear(self):
        self.map = [None] * self.size
        return self.map

    def keys(self):
        keysArr = []
        for i in range(self.size):
            if self.map[i] is not None:
                curr = self.map[i]
                while curr:
                    keysArr.append(curr.val[0])
                    curr = curr.next
        return keysArr
    
    def values(self):
        valsArr = []
        for i in range(self.size):
            if self.map[i] is not None:
                curr = self.map[i]
                while curr:
                    valsArr.append(curr.val[1])
                    curr = curr.next
        return valsArr
    
    def entries(self):
        output = []
        for i in range(self.size):
            if self.map[i] is not None:
                curr = self.map[i]
                while curr:
                    output.append([curr.val[0], curr.val[1]])
                    curr = curr.next
        return output

x = Hashmap()
x.set('key1', 'val1') #index 8
x.set('key2', 'val2') #index 9
x.set('key3', 'val3') #index 0
x.set('key4', 'val4') #index 1
x.set('1key', 'val6') #index 8
x.set('ke1y', 'val7') #index 8
print(x.entries())
