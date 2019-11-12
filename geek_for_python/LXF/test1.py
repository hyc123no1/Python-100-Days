from collections import OrderedDict
from contextlib import contextmanager

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict,self).__init__()
        self._capacity = capacity
    
    def __setitem__(self, key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield 
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")
