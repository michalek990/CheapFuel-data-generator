class FuelType:

    def __init__(self, id, name, created_at, created_by, updated_at, updated_by, min_price, max_price):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.min_price = min_price
        self.max_price = max_price

    def __str__(self):
        return f"INSERT INTO FuelTypes (Id, Name, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy) VALUES ({self.id}, '{self.name}', '{self.created_at}', {self.created_by}, '{self.updated_at}', {self.updated_by});"
