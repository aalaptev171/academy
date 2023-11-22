#Реализовать иерархию классов автомобилей.

#Легковые
#Грузовые
#Пассажирские
#Помимо служебных методов реализовать расчёт расхода топлива в зависимости от загрузки, расчёт стоимости и/или времени поездки.

class Auto:
    def __init__(self,auto_type,spent):

        self.auto_type = auto_type
        self.spent = spent

		
    def calc_rashod (self, distance):
        return (distance/100)* self.spent
    
class Light(Auto):
    def __init__(self,auto_type,spent,passengers=1):
        super().__init__(auto_type,spent)
        self.passengers = passengers

    def calc_rashod_light(self,distance):
        spent = super().calc_rashod(distance)
        return spent*self.passengers*2 
    
    def __str__(self) -> str:
        return f"{self.auto_type},{self.spent},{self.passengers}"


class Heavy(Auto):
    def __init__(self,auto_type,spent,gruz=1):
        super().__init__(auto_type,spent)
        self.gruz = gruz

    def calc_rashod_heavy(self,distance):   
        spent = super().calc_rashod(distance)
        return spent*self.gruz*5 
    
    def __str__(self) -> str:
        return f"{self.auto_type},{self.spent},{self.gruz}"
		
light = Light('light',100,5)

print(str(light))
print(light.calc_rashod_light(100))

heavy = Heavy('Heavy',100,5)

print(str(heavy))
print(heavy.calc_rashod_heavy(100))
