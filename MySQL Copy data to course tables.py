import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "2002531vex",
    database = "comp350F_project"
    )
mycursor = mydb.cursor()

mycursor.execute("SELECT sid, name, major, year FROM student_info")
student_info_rows = mycursor.fetchall()

for row in student_info_rows:
    sid, name, major, year = row
    # Check if major and year match in courselist table
    mycursor.execute("SELECT course_id FROM courselist WHERE major = %s AND year = %s", (major, year))
    courselist_rows = mycursor.fetchall()
    # Loop through the courselist rows
    for courselist_row in courselist_rows:
        course_id = courselist_row[0]
        # Check if the student already exists in the course table
        select_query = "SELECT COUNT(*) FROM `" + course_id + "` WHERE sid = %s"
        mycursor.execute(select_query, (sid,))
        count = mycursor.fetchone()[0]
        if count == 0:  # Student does not exist in the course table
            insert_query = "INSERT INTO `" + course_id + "` (sid, name, major, year) VALUES (%s, %s, %s, %s)"
            mycursor.execute(insert_query, (sid, name, major, year))
            mydb.commit()
        
# Copy and insert data from courselist table to relevant course tables
mycursor.execute("SELECT course_id, semester FROM courselist")
courselist_rows = mycursor.fetchall()
# Loop through the courselist rows
for row in courselist_rows:
    course_id, semester = row
    # Update semester column in the course table
    update_query = "UPDATE `" + course_id + "` SET semester = %s WHERE semester IS NULL"
    mycursor.execute(update_query, (semester,))
    mydb.commit()