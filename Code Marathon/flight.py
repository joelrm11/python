class Flight:
    def __init__(self,flightno='',frm='',destination='',distance=''):
        self.flightno=flightno
        self.frm=frm
        self.fare=0
        self.destination=destination
        self.distance=distance
        self.fuel=0
        # self.calculateFare(distance)
        # self.calculateFuelQuantity(distance)
    def calculateFuelQuantity(self,dist):
        dist=int(dist)
        if dist<=1000:
            self.fuel=500
            # print('The Fuel required for the flight is %d'%(self.fuel))
        elif dist>1000 and dist<=1500:
            self.fuel=1100
            # print('The Fuel required for the flight is %d'%(self.fuel))
        elif dist>1500 and dist<=2000:
            self.fuel=2200
            # print('The Fuel required for the flight is %d'%(self.fuel))
        elif dist>2000:
            self.fuel=3100
            # print('The Fuel required for the flight is %d'%(self.fuel))
    def calculateFare(self,dist):
        dist=int(dist)
        if dist <= 1000:
            self.fare=4000
            # print('\n The total cost of the flight is %d'%(self.fare))
        elif dist>1000 and dist<=1500:
            self.fare=6000
            # print('\n The total cost of the flight is %d'%(self.fare))
        elif dist>1500 and dist<=2000:
            self.fare=7500
            # print('\n The total cost of the flight is %d'%(self.fare))
        elif dist>2000:
            self.fare=9500
            # print('\n The total cost of the flight is %d'%(self.fare))
   
    def feedInfo(self):
        flightno=input('\nenter the flight no: ')
        frm=input('from place : ')
        destination=input('enter the destination: ')
        distance=int(input("enter the distance: "))
        self.__init__(flightno,frm,destination,distance)
        self.calculateFare(distance)
        self.calculateFuelQuantity(distance)
    
    def showInfo(self):
        print('\nFlight no %s'%(self.flightno))
        print('From : %s'%(self.frm))
        print('Destination : %s'%(self.destination))
        print('Distance : %s'%(self.distance))
        print('Fare : %s'%(self.fare))
        print('Fuel : %s\n'%(self.fuel))

flights=[]
n=int(input('\nenter the no of flights: '))
for i in range(1,n+1):
    f=Flight()
    f.feedInfo()
    flights.append(f)

while True:
    print('\nMenu\n1.Show Details\n2.Search flight details\n3.Modify flight details\n4.exit\n')
    ch=int(input('enter your choice: '))
    
    if ch==1:
        print('\nDetails of Data members are:\n')
        for i in flights:
            i.showInfo()
    elif ch==2:
        flag=0
        fno=input('\nenter the flight no : ')
        for i in flights:
            if fno==i.flightno:
                flag=0
                i.showInfo()
                break
            elif fno!=i.flightno:
                flag=1
        if flag==1:
            print('\ninvalid flight no')
    elif ch==3:
        fno=input('\nenter the flight no : ')
        flag=0
        for i in flights:
            if fno==i.flightno:
                print('\nEnter the new details for flight no %s:'%(fno))
                i.feedInfo()
                print('\nthe new details for flight no %s are:'%(fno))
                i.showInfo()
                flag=0
                break
            elif fno!=i.flightno:
                flag=1
        if flag==1:
            print('\ninvalid flight no')           
    elif ch==4:
        exit()
    else:
        print('invalid input')
            

