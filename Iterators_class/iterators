class Letters:
    def __init__(self,length):
        print('Calling __init__ ...')
        self._letters=letters[:(length+1)]
    
    def __len__(self):
        print('Calling __len__ ...')
        return len(self._letters)

    def __getitem__(self, s):
        print('Calling __getitem__ ...')
        return self._letters[s]
    
    def __iter__(self):
        print('Calling __iter__')
        return self.LettersIterator(self)
    def __repr__(self):
        return "Letters: {}".format(self._letters)
   
    
        
    class LettersIterator:
        def __init__(self,Letters_obj):
            print('Calling CityIterator __init__')
            self._Letters_obj=Letters_obj
            self._index=0
        def __iter__(self):
            print('Calling CitiyIterator __iter__')
            return self
        def __next__(self):
            if self._index >= len(self._Letters_obj):
                raise StopIteration
            else:
                ret=self._Letters_obj._letters[self._index]
                self._index += 1
                return ret


class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
        
    def __len__(self):
        return len(self._cities)
    
    def __getitem__(self, s):
        print('getting item...')
        return self._cities[s]
    
    def __iter__(self):
        print('Calling Cities instance __iter__')
        return self.CityIterator(self)
    
    class CityIterator:
        def __init__(self, city_obj):
            # cities is an instance of Cities
            print('Calling CityIterator __init__')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('Calling CitiyIterator instance __iter__')
            return self

        def __next__(self):
            print('Calling __next__')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item
cities = Cities()
for i in cities:
    print(i)

class set1:
    def __init__(self):
        self._index=0
        self._set=['a', 'b', 'c', 'd']
    def __repr__(self):
        return "set: {}".format(self._set)
    def __len__(self):
        return len(self._set)
    def __next__(self):
        if self._index >= len(self._set):
            raise StopIteration
        else:
            ret=self._set[self._index]
            self._index += 1
            return ret
    def  __iter__(self):
        self._index=0
        return self

class set1:
    def __init__(self):
        #self._index=0
        self._set={'a', 'b', 'c', 'd'}
    def __repr__(self):
        return "set: {}".format(self._set)
    def __len__(self):
        return len(self._set)
    def  __iter__(self):
        return iter(self._set)
st=set1();st
for i in st:
    print(i)
for i in st:
    print(i)
