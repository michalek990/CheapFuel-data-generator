from datetime import datetime
from Generators.RandomTimeGenerator import RandomTimeGenerator
from Models.StationChain import StationChain

generator = RandomTimeGenerator(datetime.now(), datetime.now())
generator.next()

StationChains = [
    StationChain(1, "Orlen", generator.last(), 2, generator.last(), 2),
    StationChain(2, "Shell", generator.last(), 2, generator.last(), 2),
    StationChain(3, "CheapFuel", generator.last(), 2, generator.last(), 2),
    StationChain(4, "Lotos", generator.last(), 2, generator.last(), 2),
    StationChain(5, "BP", generator.last(), 2, generator.last(), 2),
    StationChain(6, "Circle K.", generator.last(), 2, generator.last(), 2),
    StationChain(7, "Amic Energy", generator.last(), 2, generator.last(), 2),
]