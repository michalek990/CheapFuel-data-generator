class FuelStation:

    def __init__(self, id, name, city, street, street_number, postcode, latitude, longitude, updated_by, updated_at, created_by, created_at, station_chain_id):
        self.id = id
        self.name = name
        self.city = city
        self.street = street
        self.street_number = street_number
        self.postcode = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.updated_by = updated_by
        self.updated_at = updated_at
        self.created_by = created_by
        self.created_at = created_at
        self.station_chain_id = station_chain_id

    def __str__(self):
        return f"INSERT INTO FuelStations (Id, City, Street, StreetNumber, PostalCode, Latitude, Longitude, UpdatedBy, UpdatedAt, CreatedBy, CreatedAt, StationChainId) " \
               f"VALUES ({self.id}, '{self.city}', '{self.street}', '{self.street_number}', '{self.postcode}', {self.latitude}, {self.longitude}, {self.updated_by}, '{self.updated_at}', {self.created_by}, '{self.created_at}', {self.station_chain_id});"
