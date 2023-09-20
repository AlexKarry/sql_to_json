import sqlite3
import json

db_filenem = "../session_2.db"

json_file = "../revenue.json"

conn = sqlite3.connect(db_filenem)

cursor = conn.cursor()

outer_dict = {}

data_from_sql = "SELECT * FROM revenue"
cursor.execute(data_from_sql)

# counter = 1

for row in cursor:
    name = row[0]
    state = row[1]
    cost = row[2]

    inner_dict = {
        "name": name,
        "state": state,
        "cost": cost
    }

    outer_dict[name] = inner_dict

    # outer_dict[counter] = inner_dict
    # counter += 1

    wfh = open(json_file, 'w', newline='')
    json.dump(outer_dict, wfh, indent=5)

conn.close()
print(outer_dict)
