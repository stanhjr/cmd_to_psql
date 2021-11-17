
def get_project_id(project_num: str, project_desc: str, cur, conn) -> str:
    cur.execute("SELECT id, project_number FROM project_number WHERE project_number=(%s);", (project_num,))
    query = cur.fetchone()
    if query:
        return query[0]
    else:
        cur.execute("INSERT INTO project_number (project_number, project_description) VALUES (%s, %s);",
                    (project_num, project_desc))
        conn.commit()
        cur.execute("SELECT id, project_number FROM project_number WHERE project_number=(%s);", (project_num,))
        query = cur.fetchone()
        return query[0]


def get_order_description_id(order_desc: str, cur, conn) -> str:
    cur.execute("SELECT id, order_description FROM order_description WHERE order_description=(%s);", (order_desc,))
    query = cur.fetchone()
    if query:
        return query[0]
    else:
        cur.execute("INSERT INTO order_description (order_description) VALUES (%s);", (order_desc,))
        conn.commit()
        cur.execute("SELECT id, order_description FROM order_description WHERE order_description=(%s);", (order_desc,))
        query = cur.fetchone()
        return query[0]


def get_constructor_id(name: str, cur, conn) -> str:
    cur.execute("SELECT id, constructor_name FROM constructor_name WHERE constructor_name=(%s);", (name,))
    query = cur.fetchone()
    if query:
        return query[0]
    else:
        cur.execute("INSERT INTO constructor_name (constructor_name) VALUES (%s);", (name,))
        conn.commit()
        cur.execute("SELECT id, constructor_name FROM constructor_name WHERE constructor_name=(%s);", (name,))
        query = cur.fetchone()
        return query[0]


def get_production_id(production_area_name: str, cur, conn) -> str:
    cur.execute("SELECT id, production_area FROM production_area WHERE production_area=(%s);", (production_area_name,))
    query = cur.fetchone()
    if query:
        return query[0]
    else:
        cur.execute("INSERT INTO production_area (production_area) VALUES (%s);", (production_area_name,))
        conn.commit()
        cur.execute("SELECT id, production_area FROM production_area WHERE production_area=(%s);", (production_area_name,))
        query = cur.fetchone()
        return query[0]


