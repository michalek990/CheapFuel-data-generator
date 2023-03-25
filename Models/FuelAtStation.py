class FuelAtStation:

    def __init__(self, fuel_type_id, fuel_station_id, created_at, created_by):
        self.fuel_type_id = fuel_type_id
        self.fuel_station_id = fuel_station_id
        self.created_at = created_at
        self.created_by = created_by

    def __str__(self):
        return f"INSERT INTO FuelAtStations (FuelTypeId, FuelStationId, CreatedAt, CreatedBy) " \
               f"VALUES ({self.fuel_type_id}, {self.fuel_station_id}, '{self.created_at}', {self.created_by});"
