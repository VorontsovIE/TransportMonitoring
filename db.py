from playhouse.migrate import *

my_db = SqliteDatabase('buses.db')
migrator = SqliteMigrator(my_db)

title_field = CharField(default='')
status_field = IntegerField(null=True)

# migrate(
#     migrator.add_column('buses.db', 'title', title_field),
#     migrator.add_column('buses.db', 'status', status_field),
#     migrator.drop_column('buses.db', 'old_column'),
# )

migrate(
    migrator.rename_table('buses.db', 'routedata'),
)