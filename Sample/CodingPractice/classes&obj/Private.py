class Test():
    __a = 12

    def __geta(self):
        print(self.__a)

    def seta(self, a):
        self.__geta()
        self.__a = a

t = Test()
t.seta(99)
