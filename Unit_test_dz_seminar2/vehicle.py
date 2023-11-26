
class Vehicle:
    def __init__(self, company: str,
                 model: str,
                 year_release: int,
                 num_wheels: int,
                 speed: int):
        self.company = company
        self.model = model
        self.year_release = year_release
        self.num_wheels = num_wheels
        self.speed = speed

    def test_drive(self):
        pass

    def park(self):
        pass

    def company(self):
        return self.company

    def model(self):
        return self.model

    def year_release(self):
        return self.year_release

    def num_wheels(self):
        return self.num_wheels


    def speed(self):
        return self.speed


class Motorcycle(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        super().__init__(company, model, year_release, num_wheels=2, speed=0)

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def __repr__(self):
        return f'Motorcycle("{self.company}", "{self.model}", {self.year_release})'

class Car(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        super().__init__(company, model, year_release, num_wheels=4, speed=0)

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def __repr__(self):
        return f'Car("{self.company}", "{self.model}", {self.year_release})'
