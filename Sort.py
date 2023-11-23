import random

class Sort:


    def __init__(self,num = 10):
        self.num = num

    def fill_random(self):
        self.spisok = []
        self.spisok = [ int(random.randint(1, self.num)) for i in range(self.num)]
        return self.spisok 
    
    def bubble(self,array):
        try:
            for i in range(self.num-1):
                for j in range(self.num-i-1):
                    if array[j] > array[j+1]:
                        buff = array[j]
                        array[j] = array[j+1]
                        array[j+1] = buff           
            return array
        except TypeError:
            print('Wrong type ARRAY')

  

s= Sort(5)

#l = s.fill_random()

l = [1,'22',3,4,5]
print (l)

l1 = s.bubble(l)

print (l1)


