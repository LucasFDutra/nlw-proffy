import os
from dotenv import load_dotenv


def run_dev():
    os.system('python3 backend/server.py')


def up_migration():
    load_dotenv()
    list_migrations = os.listdir('backend/src/database')
    list_migrations.sort()
    for migration in list_migrations:
        if ('migration' in migration and not ('_up' in migration)):
            os.system('python backend/src/database/'+migration+' --up')
            os.rename('backend/src/database/'+migration,
                      'backend/src/database/'+migration+'_up')


def down_migration():
    load_dotenv()
    list_migrations = os.listdir('backend/src/database')
    list_migrations.sort()
    for migration in list_migrations:
        if ('migration' in migration and '_up' in migration):
            os.system('python backend/src/database/'+migration+' --down')
            migration_ = migration.replace('_up', '')
            os.rename('backend/src/database/'+migration,
                      'backend/src/database/'+migration_)
