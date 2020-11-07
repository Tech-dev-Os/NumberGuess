import random, time


class NumGuess:
    def __init__(self):
        self.com = random.randint(1, 50)
        self.my = 0
        self.point = 0
        self.chance = 7

    def hints(self):       
        if(self.com % 2 == 0):
            print("Hints Number is Even")
        else:
            print("Hints Number is Odd")

        if(self.com <= 50 and self.com >= 25):
            print("Number should be 25-50")
        elif(self.com <= 25 and self.com >=1):
            print("Number should be 1-25")

        if(self.my > self.com):
            print("Try Small Number Than", self.my)
        elif(self.my < self.com):
            print("Try Big Number Than", self.my)

    def start(self):
        while self.chance > 0:
            print("Guess between 1-50 \n")
            self.hints()
            # print(self.com)
            self.my = int(input(">"))
            
            if self.my == self.com:
                self.point += 50
                for i in range(1, 15):
                    print('-'*i, end=' ')
                print("\nYou Got it..")
                print("Your Point is: ", self.point,"/50")
                print("-"*15)

                break
            else:
                print("Wrong Try agian")
                print("Left try =>", self.chance)
                self.point -= 3
                self.chance -= 1
        else:
            print("Out Of chance\nCorrect Number is: ",self.com)
        

n = NumGuess()
n.start()