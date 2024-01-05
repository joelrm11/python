class Kite():
    __count = 0

    def __init__(self):
        # self.__count += 1
        Kite.__count += 1

    @staticmethod
    def kite_count():
        return Kite.__count
    
k1 = Kite()
k2 = Kite()
k3 = Kite()

print(Kite.kite_count())
# print(k2.__count)