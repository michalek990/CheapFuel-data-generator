import random

from Generators.RandomTimeGenerator import RandomTimeGenerator
from Models.Datasets.Cities import Cities as cities
from Models.Datasets.Streets import Streets as streets
from Models.Datasets.Services import Services as services
from Models.Datasets.StationChains import StationChains as station_chains
from Models.Datasets.FuelTypes import FuelTypes as fuel_types
from Models.Datasets.Usernames import read_usernames
from Models.FuelPrice import FuelPrice
from Models.FuelStation import FuelStation
from Models.ServiceAtStations import ServiceAtStations
from Models.FuelAtStation import FuelAtStation
from Models.User import User
from datetime import datetime

DEFAULT_PASSWORD = "AQAAAAEAACcQAAAAEIx4l5FIMC2QHbCl94VCmPBY6//9LqJfoCifq8a5vxVDbfk4CMwLB6JAL0kSDgj+kA=="

FUEL_STATION_COUNT = 300
USERS_COUNT = 100

MIN_FUEL_PRICE_COUNT = 50
MAX_FUEL_PRICE_COUNT = 200


USERS_START_INDEX = 100

timeGenerator = RandomTimeGenerator(datetime(2018, 1, 1), datetime.now())

def random_from_list(list):
    return list[random.randrange(len(list) - 1)]


def run():
    users = generate_users()
    fuel_stations = generate_fuel_stations()
    fuel_types_at_station, fuel_prices = generate_fuel_types_at_station(fuel_stations)
    services_at_station = generate_services_at_station(fuel_stations)

    f = open("data.sql", "w+", encoding="utf-8")

    write_to_file(f, users)
    write_to_file(f, fuel_types)
    write_to_file(f, services)
    write_to_file(f, station_chains)
    write_to_file(f, fuel_stations)
    write_to_file(f, fuel_types_at_station)
    write_to_file(f, services_at_station)
    write_to_file(f, fuel_prices)

    f.close()


def write_to_file(file, arr):
    for i in range(len(arr)):
        file.write(f"{arr[i].__str__()}\n")

    file.write("\n\n")


def generate_users():
    users = []
    usernames = read_usernames()

    for i in range(USERS_COUNT):
        timeGenerator.next()
        usernameIndex = random.randrange(len(usernames))
        user = User(i + USERS_START_INDEX, usernames[usernameIndex], f"{usernames[usernameIndex]}@email.com", 1, DEFAULT_PASSWORD, 0, 'Active', timeGenerator.last(), i, timeGenerator.last(), i)

        usernames.remove(usernames[usernameIndex])

        users.append(user)

    return users


def generate_fuel_stations():
    fuel_stations = []

    for i in range(FUEL_STATION_COUNT):
        timeGenerator.next()
        city = random_from_list(cities)
        street = random_from_list(streets)
        latitude, longitude = city.random_point()
        station_chain = random_from_list(station_chains)

        station = FuelStation(i + 1, "", city.name, street, city.randomStreetNumber(), city.randomPostCode(), latitude,
                              longitude, 2, timeGenerator.last(), 2, timeGenerator.last(), station_chain.id)
        fuel_stations.append(station)

    return fuel_stations


def generate_services_at_station(fuel_stations):
    services_at_station = []

    for i in range(len(fuel_stations)):
        timeGenerator.next()
        num = random.randrange(len(services))
        random.shuffle(services)

        for j in range(num):
            service = ServiceAtStations(services[j].id, fuel_stations[i].id, timeGenerator.last(), 2)
            services_at_station.append(service)

    return services_at_station


def generate_fuel_types_at_station(fuel_stations):
    fuel_types_at_station = []
    fuel_prices = []

    for i in range(len(fuel_stations)):
        timeGenerator.next()
        num = random.randrange(2, len(fuel_types))
        random.shuffle(services)

        for j in range(num):
            fuel_type = FuelAtStation(fuel_types[j].id, fuel_stations[i].id, timeGenerator.last(), 2)
            fuel_types_at_station.append(fuel_type)
            fuel_prices.extend(generate_fuel_prices(fuel_types[j], fuel_stations[i]))

    return fuel_types_at_station, fuel_prices


def generate_fuel_prices(fuel_type, fuel_station):
    num_of_entries = random.randrange(MIN_FUEL_PRICE_COUNT, MAX_FUEL_PRICE_COUNT)
    step = (fuel_type.max_price - fuel_type.min_price) / num_of_entries
    min_price = fuel_type.min_price

    time_step = (datetime.now() - datetime(2018, 1, 1)) / num_of_entries
    time = datetime(2018, 1, 1)

    start_id = fuel_station.id * 100000 + fuel_type.id * 10000

    fuel_prices = []

    for i in range(num_of_entries):
        user_id = random.randrange(USERS_START_INDEX, USERS_COUNT + USERS_START_INDEX)
        price = round(random.uniform(min_price, min_price + step), 2)
        available = 0 if random.randrange(100) == 1 else 1

        if random.randrange(5) == 0:
            min_price -= step
        else:
            min_price += step

        fuel_price = FuelPrice(start_id + i, price, available, 'Accepted', 0, fuel_station.id, fuel_type.id, user_id, user_id, time, user_id, time)
        fuel_prices.append(fuel_price)
        time += time_step

    return fuel_prices

