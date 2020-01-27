from playhouse.migrate import *

my_db = SqliteDatabase('buses.db')
migrator = SqliteMigrator(my_db)

title_field = IntegerField(null=True)

migrate(
    migrator.add_column('stopdata', 'coordinates', IntegerField),
)

migrate(
    migrator.rename_table('routedata', 'buses'),
)