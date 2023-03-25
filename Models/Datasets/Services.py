from datetime import datetime
from Generators.RandomTimeGenerator import RandomTimeGenerator
from Models.Service import Service

generator = RandomTimeGenerator(datetime.now(), datetime.now())
generator.next()

Services = [
    Service(1, "Refueling", generator.last(), 2, generator.last(), 2),
    Service(2, "Toilets", generator.last(), 2, generator.last(), 2),
    Service(3, "Restaurant", generator.last(), 2, generator.last(), 2),
    Service(4, "Coffee", generator.last(), 2, generator.last(), 2),
    Service(5, "Place to sleep", generator.last(), 2, generator.last(), 2),
    Service(6, "Phone", generator.last(), 2, generator.last(), 2),
    Service(7, "ATM", generator.last(), 2, generator.last(), 2),
]