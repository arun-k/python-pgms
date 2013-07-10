class reverse_iter:
    def __init__(self,List):
        self.List=List;
        self.count=len(self.List)-1

    def __iter__(self):
        return self

    def next(self):
        if 0 <= self.count < len(self.List):
            ele=self.List[self.count]
            self.count-=1
            return ele
        else:
            raise StopIteration()
