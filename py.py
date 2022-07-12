class PogoList:
    def __init__(self):
        self._data=[]

    def __setitem__(self, key, value):
        self._data[key]=value
    def __getitem__(self, item):
        return self._data[item]
    def append(self, item):
        self._data.append(item)
    def __len__(self):
        return len(self._data)
    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        if x<len(self._data):
            return self._data[x]
        else:
            raise StopIteration



def sort_function(list,comparison_function):
    k=[]
    result=[]
    for i in range(len(list)):
        k.append(0)
        result.append(0)
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if comparison_function(list[i],list[j])==True:
                k[i]+=1
            else:

                k[j]+=1
    for i in range(len(list)):
        result[k[i]]=list[i]
    return result




def filter(list,acceptance_function,input):
    result=[]
    for i in range(len(list)):
        if acceptance_function(list[i],input)==True:
            result.append(list[i])
    return result
