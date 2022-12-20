import random
class Student:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.famine=0
        self.alive=True

    def to_sleep(self):
        print("Час спати")
        self.gladness+=3
    def to_study(self):
        print("Час навчатись")
        self.progress+=8.12
        self.gladness-=3
    def to_chill(self):
        print("Час відпочивати")
        self.gladness+=5
        self.progress-=0.01
    def to_eat(self):
        self.gladness+=4
    def is_live(self):
        if self.progress<-0.5:
            print("Відрахування...")
            self.alive=False
        elif self.gladness<=0:
            print("Депресія...")
            self.alive=False
        elif self.progress>5:
            print("Закінчив екстерном")
            self.alive=False
        elif self.famine<0:
            print("Голодування...")

    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Прогрес = {round(self.progress,2)}")
        print(f"Голод = {round(self.famine,3)}")
    def live(self, day):
        day ="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.to_eat()
        self.end_of_day()
        self.is_live()

nick=Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
