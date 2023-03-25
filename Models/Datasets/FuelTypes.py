from datetime import datetime
from Generators.RandomTimeGenerator import RandomTimeGenerator
from Models.FuelType import FuelType

generator = RandomTimeGenerator(datetime.now(), datetime.now())
generator.next()

FuelTypes = [
    FuelType(1, "PB 95", generator.last(), 2, generator.last(), 2, 5.01, 7.02),
    FuelType(2, "PB 98", generator.last(), 2, generator.last(), 2, 5.21, 7.32),
    FuelType(3, "ON SUPER", generator.last(), 2, generator.last(), 2, 4.21, 8.32),
    FuelType(4, "LPG", generator.last(), 2, generator.last(), 2, 2.21, 3.21),
    FuelType(5, "ON", generator.last(), 2, generator.last(), 2, 4.01, 8.11)
]