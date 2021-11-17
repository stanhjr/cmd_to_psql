from sys import argv
import psycopg2
from tools import get_production_id, get_order_description_id, get_project_id, get_constructor_id

barcode_number, project_number, project_description, order_number, order_description, \
    production_area, file_path, constructor_name, deadline, priority = argv[1:]

try:
    connection = psycopg2.connect(user="cmd",
                                  password="cmd",
                                  host="192.168.77.138",
                                  port="5432",
                                  database="promdesign_db",
                                  )

    cursor = connection.cursor()

    production_area_id = get_production_id(production_area, cursor, connection)
    constructor_id = get_constructor_id(constructor_name, cursor, connection)
    order_description_id = get_order_description_id(order_description, cursor, connection)
    project_number_id = get_project_id(project_number, project_description, cursor, connection)

    cursor.execute("INSERT INTO order_base_pd (barcode_number, project_number, order_number, order_description, "
                   "production_area, file_path, constructor_name, deadline, priority) VALUES (%s, %s, %s, %s, %s, %s, "
                   "%s, %s, %s);", (barcode_number, project_number_id, order_number, order_description_id,
                                    production_area_id, file_path, constructor_id, deadline, priority))

    connection.commit()

except ValueError:
    print('Неправильное количество аргументов или присутствуют кавычки в описании проекта или заказа')

