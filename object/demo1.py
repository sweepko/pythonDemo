class Programer():
    hobby='play Computer'

    def __init__(self,name,age,weight):
        self.name=name
        self._age=age
        self.__weight=weight
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    @property
    def get_weight(self):
        return self.get_weight()

    def self_introduction(self):
        print('My name is %s \nI am %s years old\n ' % (self.name, self._age))


class BackendProgramer(Programer):
    def __init__(self,name,age,weight,language):
            super(BackendProgramer, self).__init__(name,age,weight)
            self.language=language

if __name__=='__main__':
    programer=BackendProgramer('sweep',20,130,'汉语')
    print(dir(programer))
    print(programer.__dict__)
    print(type(programer))
    print(isinstance(programer, Programer))
