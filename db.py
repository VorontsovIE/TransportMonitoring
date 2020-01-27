from playhouse.migrate import *

my_db = SqliteDatabase('buses.db')
migrator = SqliteMigrator(my_db)

migrate(
    migrator.add_column('stopdata', 'coordinates', IntegerField(null=True)),
)

migrate(
    migrator.rename_table('routedata', 'buses'),
)