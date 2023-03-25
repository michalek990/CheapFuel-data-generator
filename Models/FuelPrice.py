class FuelPrice:

    def __init__(self, id, price, available, status, priority, fuel_station_id, fuel_type_id, user_id, created_by, created_at, updated_by, updated_at):
        self.id = id
        self.price = price
        self.available = available
        self.status = status
        self.priority = priority
        self.fuel_station_id = fuel_station_id
        self.fuel_type_id = fuel_type_id
        self.user_id = user_id
        self.created_by = created_by
        self.created_at = created_at
        self.updated_by = updated_by
        self.updated_at = updated_at

    def __str__(self):
        return f"INSERT INTO FuelPrices (Id, Price, Available, Status, Priority, FuelStationId, FuelTypeId, UserId, CreatedBy, CreatedAt, UpdatedBy, UpdatedAt, Deleted, DeletedBy, DeletedAt) " \
               f"VALUES ({self.id}, {self.price}, {self.available}, '{self.status}', {self.priority}, {self.fuel_station_id}, {self.fuel_type_id}, {self.user_id}, {self.created_by}, '{self.created_at}', {self.updated_by}, '{self.updated_at}', 0, NULL, NULL);"
