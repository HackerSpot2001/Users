from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
import os



class Command(BaseCommand):
    help = "Migrate  all data from base_data folder to databse"

    def handle(self, *args, **options):
        self.folder_path = os.path.join(settings.BASE_DIR ,'Users','sqls')
        file_lists  = [ x for x in sorted(os.listdir(self.folder_path)) ]
        for file in file_lists:
            file_obj = open(os.path.join(self.folder_path, file),'r')
            with connection.cursor() as cursor:
                sql = file_obj.read()
                sql = sql.replace("hrms",'hms')
                cursor.execute(sql)

            file_obj.close()
                    
            self.stdout.write(
                self.style.SUCCESS('Successfully write file "{}"'.format( file) )
            )

