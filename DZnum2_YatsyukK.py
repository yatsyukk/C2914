import random
class Kitty:
    def __init__(self, name):
        self.name=name
        self.gladness=50
        self.famine=0
        self.communication=20
        self.alive=True

    def to_sleep(self):
        print("Час спати")
        self.gladness+=3
        self.communication-=2
    def to_eat(self):
        print("Час їсти")
        self.gladness+=4
    def to_chill(self):
        print("Час віпочивати")
        self.gladness+=5
        self.communication-=1
    def to_communicate(self):
        print("Час спілкуватись")
        self.communication+=3
        self.gladness+=2
    def is_live(self):
        if self.famine<0:
            print("Голодування...")
        elif self.communication<-0.5:
            print("Здичавіння...")
        elif self.gladness<0:
            print("Депресія...")
        elif self.communication>7:
            print("Щаслива сім'я")

    def end_of_day(self):
        print(f"Радість = {self.gladness}")
        print(f"Голод = {round(self.famine, 2)}")
        print(f"Сім'я = {round(self.communication, 3)}")
    def live(self, day):
        day ="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1, 4)
        if live_cube==1:
            self.to_eat()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.to_communicate()
        self.end_of_day()
        self.is_live()

nick=Kitty(name="Aoi")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
