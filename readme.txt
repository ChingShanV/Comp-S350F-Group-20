1.MySQL database(If the MySQL workbench and configurator has already been downloaded and setup due to other groups' project, jump to 1d)
	1a. Download MySQL Workbench
	https://dev.mysql.com/downloads/workbench/
	
	1b. Download MySQL Configurator
	https://dev.mysql.com/downloads/installer/
	
	1c. Run MySQL Configurator and setup the server
	host name = local host
	user = root
	password = 2002531vex

	1d. Open MySQL Workbench and click 'File' button, then 'open SQL Script'. Open the file 'MySQL database'
	
	1e. Click on any space of the first line, click the button with lightning and cursor(not only lightning) to execute the code of the first line to 	create a database
	
	1f. Click on second line of the code and execute
	
	1g. Execute the code on line 7, 17, 30, 53, 60, 82, 90 and 112.

2.Image for graphic user interface
	2a. Download the whole file with all the codes and images. Images should include "my ioh_banner 1 (1).png", "HKMU-logo-mb (1).png" and 	"HKMU_homepage.png" in the file group with the program code.

3.Python code (Use any platform that can run Python)
	3a. Before running the py files, MySQL connector needs to be installed through typing 'pip install MySQL-python' or 'pip install mysql', 'pip 	install mysql-connector', 'pip install mysql-connector-python'. Different platforms may have different ways to install it. If already installed, 	ignore this step

	3b. Library tkinter also needs to be installed through typing 'pip install tkinter' or 'pip install tk'. It may already be installed together with 	the Python language. If already installed, ignore this step

	3c. If the MySQL Configurator and Workbench has been setup due to other groups' project, the Python code of 'MySQL Create course table.py' and 	'MySQL Copy data to course table.py' has to be modified. Line 3, 4 and 5 needs to be modified according to the setting in MySQL configurator.

	3d. Open and run the code of 'MySQL Create course tables.py'. One table will be created named by the courseid for each course saved inside the 	courselist table.

	3e. Open and run the code of 'MySQL Copy data to course table.py'

4.Checking the database
	4a. For students' login id and password, click on line 3 and execute the code in MySQL workbench. The id(login_id) and password(pw) were saved 	inside 	the MySQL table
	
	4b. For instructors' login id and password, click on line 4 and execute the code in MySQL workbench

	4c. For line 5 of the MySQL code, different courses can be seen inside the courselist table after executing this line of code

	4d. For line 6, it is an example of checking data stored inside different course tables. Replace the course id to check other course tables.

5.Running the system
	5a. Open the file 'Academic Record Project.py'
		
	5b. If the MySQL Configurator and Workbench has been setup due to other groups' project, the Python code of 'Academic Record Project.py' has to be 	modified. Line 9, 10 and 11 needs to be modified according to the setting in MySQL configurator.

	5c. Run the file 'Academic Record Project.py'
