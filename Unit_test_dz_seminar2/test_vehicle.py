import unittest

from vehicle import *


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Car('Hyundai', 'Tucson', 2017)
        self.motorcycle = Motorcycle('Минск', 'SKR 250', 2019)

# проверка того, что экземпляр объекта Car также является экземпляром транспортного средства
    def test_car_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))

# проверка того, объект Car создается с 4-мя колесами
    def test_num_wheel_car(self):
        self.assertEqual(self.car.num_wheels, 4)

# проверка того, объект Motorcycle создается с 2-мя колесами
    def test_num_wheel_motorcycle(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

# проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
    def test_car_speed(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

# проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
    def test_motorcycle_speed(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

# проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта) машина останавливается (speed = 0)
    def test_car_park(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

# проверить, что в режиме парковки (сначала testDrive, потом park  т.е эмуляция движения транспорта) мотоцикл останавливается (speed = 0)
    def test_motorcycle_park(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)