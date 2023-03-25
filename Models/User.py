class User:

    def __init__(self, id, username, email, email_confirmed, password, multi_factor, status, updated_at, updated_by, created_at, created_by):
        self.id = id
        self.username = username
        self.email = email
        self.email_confirmed = email_confirmed
        self.password = password
        self.multi_factor = multi_factor
        self.status = status
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.created_at = created_at
        self.created_by = created_by

    def __str__(self):
        return f"INSERT INTO Users (Id, Username, Email, EmailConfirmed, Password, MultiFactorAuthEnabled, ROLE, Status, UpdatedAt, CreatedAt, CreatedBy, Deleted, DeletedAt, DeletedBy, UpdatedBy)" \
               f"VALUES ({self.id}, '{self.username}', '{self.email}', {self.email_confirmed}, '{self.password}', {self.multi_factor}, 'User', 'Active', '{self.updated_at}', '{self.created_at}', {self.id}, 0, NULL, NULL, {self.id});"