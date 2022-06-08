class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))




class Service (Car):
    def __init__(self,car_list):            # Initializes the instance variable, car_list
        self.car_list = None


    def get_car_list(self):
       self.get_model(car_list)
       


    def find_cars_by_year(year):        # Finds and returns the list of models of all the cars with the year as the
                                         # one passed as the argument. If there are no cars, return None.
        pass


    def add_cars(new_car_list):          # The new_car_list should be added to the instance variable car_list.
                                        # The car_list should be still sorted such that the years are in ascending order.
        pass


    def remove_cars_from_karnataka():      # Finds and removes all cars with registration number beginning with “KA” from the car_list.
        pass



        


car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]

ser = Service(car_list)
#Create object of Service class, invoke the methods and test your program
