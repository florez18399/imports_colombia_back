import re
import csv
import pandas as pd
from unidecode import unidecode
from sqlalchemy import create_engine


def change_headers(data_frame_p):
    return data_frame_p.rename(columns=lambda header: unidecode(header.lower().replace(' ', '_')))


def convert_encoding(file):
    pattern = "&#(\d+);"
    regex = re.compile(pattern)

    csv_rows = []
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            for index, word in enumerate(row):
                match = regex.search(word)
                if match:
                    number = match.group(1)
                    row[index] = regex.sub(chr(int(number)), word)
            csv_rows.append(row)
    return change_headers(pd.DataFrame(csv_rows[1:], columns=csv_rows[0]))


print("Cleaning CSV file ...")
data_frame = convert_encoding('C:\\Users\\AndresFlorezC\\Downloads\\Enero.csv')
print("CSV data successfully cleaned. Loading into the database...")

table_name = "dashboard_imports_importprocess"
sql_engine = create_engine(
    'postgresql+psycopg2://postgres:admin@localhost/db_imp_colom', pool_recycle=3600)
db_connection = sql_engine.connect()

try:
    columns_to_insert = ['fech', 'adua', 'paisgen', 'paispro', 'paiscom', 'deptodes', 'regimen', 'naban', 'vafodo',
                         'flete', 'vacid', 'vacip', 'imp1', 'cuidaimp', 'cuidaexp', 'actecon', 'codadad', 'vadua',
                         'vrajus', 'baseiva', 'totalivayo', 'seguros', 'otrosg', 'luin', 'codluin', 'depim', 'copaex',
                         'tipoim', 'porara', 'derel']
    frame = data_frame[columns_to_insert].to_sql(table_name, db_connection, index=True, if_exists='append', index_label='id')
    pass
except ValueError as value_error:
    print(value_error)
except Exception as exception:
    print(exception)
else:
    print(f'Data successfully charged to table {table_name}.')
finally:
    db_connection.close()


