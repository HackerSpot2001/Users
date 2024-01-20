from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os



class Command(BaseCommand):
    help = "Migrate  all data from base_data folder to databse"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.folder_path = os.path.join(settings.BASE_DIR , 'base_data')
        file_lists  = [ x for x in os.listdir(self.folder_path)]
        for file in file_lists:
            sqlFile = self.convertSqls(file)
        
            self.stdout.write(
                self.style.SUCCESS('Successfully write file "{}" from "{}"'.format( file, sqlFile) )
            )


    def convertSqls(self,file):
        sql_statement  = "begin work;\n"
        with open(os.path.join(self.folder_path,file),'r') as f:
            lines = f.readlines()
        table_name = file.split('.')[0]
        cols = []
        for x in lines[0].rstrip().split(';') :
            if str(x) == 'last_updated_stamp':
                x= 'updated_stamp'
            cols.append(x)

        lines.pop(0)
        for line in lines:
            myArgs  = []
            for x in line.rstrip().split(';'):
                if x == "":
                    myArgs.append('NULL')
                else:
                    myArgs.append("'{}'".format(x))
            # myArgs = [ f'{x}' for x in line.rstrip().split(';') if (x == "")  x = 'NULL'  else x = f"{x}" ]
            sql_statement += "INSERT INTO hrms.{} ({}) values({});\n".format(table_name, ','.join(cols), ','.join(myArgs))
            
        sql_statement += 'commit;\n'
        sqlFile = os.path.join(self.folder_path,table_name+'.sql')
        with open(sqlFile, 'w') as f:
            f.write(sql_statement)

        return sqlFile

            
        