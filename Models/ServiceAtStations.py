class ServiceAtStations:

    def __init__(self, service_id, fuel_station_id, created_at, created_by):
        self.service_id = service_id
        self.fuel_station_id = fuel_station_id
        self.created_at = created_at
        self.created_by = created_by

    def __str__(self):
        return f"INSERT INTO ServiceAtStations (ServiceId, FuelStationId, CreatedAt, CreatedBy) " \
               f"VALUES ({self.service_id}, {self.fuel_station_id}, '{self.created_at}', {self.created_by});"
