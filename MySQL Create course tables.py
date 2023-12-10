import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "2002531vex",
    database = "comp350F_project"
    )
mycursor = mydb.cursor()

# Loop through course_id values from courselist table
mycursor.execute("SELECT course_id FROM courselist")
courseid = mycursor.fetchall()

for row in courseid:
    row = str(row)
    newstr = row[2:-3]
    table_name = "`" + newstr + "`"
    check_name = "'" + newstr + "'" 

    # Check if the table already exists
    mycursor.execute(f"SHOW TABLES LIKE {check_name}")
    table_exists = mycursor.fetchone()

    if table_exists:
        print(f"Table {check_name} already exists. Skipping table creation.")
    else:
        # Create a new table with the primary key value as the table name
        create_table_query = f"CREATE TABLE {table_name} (name VARCHAR(50),sid INT(20),grade VARCHAR(20),\
            major VARCHAR(50),`year` INT(1),semester VARCHAR(20))"
        try:
            mycursor.execute(create_table_query)
            print(f"Created table: {newstr}")
        except mysql.connector.Error as err:
            print(f"Failed to create table: {newstr}. Error: {err}")

mydb.commit()
