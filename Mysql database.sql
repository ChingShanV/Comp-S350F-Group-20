CREATE DATABASE `comp350F_project`;
USE `comp350F_project`;
select * from `student_info`;
SELECT * FROM `instructor_info`;
select * from `courselist`;
select * from `ABCDEF`;
CREATE TABLE `student_info` (
    `sid` INT PRIMARY KEY,
    `name` VARCHAR(50),
    `gender` ENUM('Male', 'Female') ,
    `tel` VARCHAR(20),
    `login_id` VARCHAR(50),
    `pw` VARCHAR(50),
    `major` VARCHAR(50),
    `year` INT(1)
);	
INSERT INTO `student_info` (sid, `name`, gender, tel, login_id, pw, major, `year`)
VALUES	
	(12668421, 'Young Ching Shan', 'Male', 12345678, 's12668421', 'p12668421', 'Mechanical Engineering', 1),
	(12668422, 'Lee Ho Chit', 'Male', 12345679, 's12668422', 'p12668422', 'Chemistry', 3),
	(12668423, 'Chau Ka Chun', 'Male', 12345680,  's12668423', 'p12668423', 'History', 4),
	(12668424, 'Lau Kit Wing', 'Female', 12345681, 's12668424', 'p12668424', 'Mechanical Engineering', 2),
	(12668425, 'AAA', 'Female', 12345682, 's12668425', 'p12668425', 'History', 1),
	(12668426, 'BBB', 'Male', 12345683, 's12668426', 'p12668426', 'Mechanical Engineering', 4),
	(12668427, 'CCC', 'Male', 12345684, 's12668427', 'p12668427', 'Computer Science', 3),
	(12668428, 'DDD', 'Female', 12345685, 's12668428', 'p12668428', 'Psychology', 2),
	(12668429, 'EEE', 'Female', 12345686, 's12668429', 'p12668429', 'Chemistry', 1),
	(12668430, 'FFF', 'Male', 12345687, 's12668430', 'p12668430', 'Chemistry', 2)
;
INSERT INTO `student_info` (sid, `name`, gender, tel, login_id, pw, major, `year`)
VALUES	
	(12668431, 'GGG', 'Male', 12345688, 's12668431', 'p12668431', 'Mechanical Engineering', 3),
	(12668432, 'HHH', 'Female', 12345689, 's12668432', 'p12668432', 'Computer Science', 2),
	(12668433, 'III', 'Male', 12345690, 's12668433', 'p12668433', 'Chemistry', 1),
	(12668434, 'JJJ', 'Female', 12345691, 's12668434', 'p12668434', 'Psychology', 4),
	(12668435, 'KKK', 'Male', 12345692, 's12668435', 'p12668435', 'Mechanical Engineering', 3),
	(12668436, 'LLL', 'Female', 12345693, 's12668436', 'p12668436', 'History', 2),
	(12668437, 'MMM', 'Male', 12345694, 's12668437', 'p12668437', 'Computer Science', 1),
	(12668438, 'NNN', 'Female', 12345695, 's12668438', 'p12668438', 'Chemistry', 4),
	(12668439, 'OOO', 'Male', 12345696, 's12668439', 'p12668439', 'Psychology', 3),
	(12668440, 'PPP', 'Female', 12345697, 's12668440', 'p12668440', 'Mechanical Engineering', 2),
	(12668441, 'QQQ', 'Male', 12345698, 's12668441', 'p12668441', 'Computer Science', 1),
	(12668442, 'RRR', 'Female', 12345699, 's12668442', 'p12668442', 'Chemistry', 4),
	(12668443, 'SSS', 'Male', 12345700, 's12668443', 'p12668443', 'Psychology', 3),
	(12668444, 'TTT', 'Female', 12345701, 's12668444', 'p12668444', 'Mechanical Engineering', 2),
	(12668445, 'UUU', 'Male', 12345702, 's12668445', 'p12668445', 'History', 1),
	(12668446, 'VVV', 'Female', 12345703, 's12668446', 'p12668446', 'Computer Science', 4),
	(12668447, 'WWW', 'Male', 12345704, 's12668447', 'p12668447', 'Psychology', 3),
	(12668448, 'XXX', 'Female', 12345705, 's12668448', 'p12668448', 'Chemistry', 2),
	(12668449, 'YYY', 'Male', 12345706, 's12668449', 'p12668449', 'Mechanical Engineering', 1),
	(12668450, 'ZZZ', 'Female', 12345707, 's12668450', 'p12668450', 'Computer Science', 4)
;
CREATE TABLE `instructor_info` (
	`name` VARCHAR(50),
    `gender` ENUM('Male', 'Female') ,
    `tel` VARCHAR(20),
    `login_id` VARCHAR(50),
    `pw` VARCHAR(50)
);
INSERT INTO `instructor_info` (`name`, gender, tel, login_id, pw)
VALUES
	('John Smith','Male','12345678','i12345678','p12345678'),
    ('Jennifer Lee','Female','12345679','i12345679','p12345679'),
    ('Michael Davis','Male','12345679','i12345679','p12345679'),
	('Sarah Thompson','Female','12345681','i12345681','p12345681'),
    ('Matthew Clark','Male','12345682','i12345682','p12345682'),
    ('Megan Thompson','Male','12345683','i12345683','p12345683'),
    ('Stephanie Adams','Female','12345684','i12345684','p12345684'),
    ('Laura Miller','Female','12345685','i12345685','p12345685'),
    ('Samantha Turner','Female','12345686','i12345686','p12345686'),
    ('Benjamin Harris','Male','123456807','i123456807','p123456807'),
    ('David Anderson','Male','12345688','i12345688','p12345688'),
    ('Christopher Hall','Male','12345689','i12345689','p12345689'),
    ('Andrew White','Male','12345690','i12345690','p12345690'),
    ('Natalie Walker','Female','12345691','i12345691','p12345691'),
    ('Jessica Brown','Female','12345692','i12345692','p12345692'),
    ('Daniel Roberts','Male','12345693','i12345693','p12345693'),
    ('Robert Johnson','Male','12345694','i12345694','p12345694'),
    ('Olivia Johnson','Female','12345695','i12345695','p12345695'),
    ('Emily Johnson','Female','12345696','i12345696','p12345696'),
    ('Ryan Wilson','Male','12345697','i12345697','p12345697');
CREATE TABLE `courselist` (
    `course_id` VARCHAR(20) PRIMARY KEY,
    `course_name` VARCHAR(100),	
    `major` VARCHAR(50) ,
    `instructor` VARCHAR(50),
    `year` INT(1),
    `semester` VARCHAR(20)
);
INSERT INTO courselist (course_id, course_name, major, instructor, `year`, semester)
VALUES
    ('ABCDER', 'Introduction to Physics', 'Mechanical Engineering', 'John Smith', 1, 'Spring'),
    ('XVJPHD', 'Data Structures', 'Computer Science', 'Emily Johnson', 4, 'Autumn'),
    ('PSYSAO', 'Introduction to Psychology', 'Psychology', 'David Anderson', 2, 'Summer'),
    ('GZIGFI', 'Organic Chemistry', 'Chemistry', 'Sarah Thompson', 5, 'Autumn'),
    ('BZYVOY', 'English Literature', 'English', 'Michael Davis', 3, 'Spring'),
    ('SUYGCM', 'Algorithms and Complexity', 'Computer Science', 'Jessica Brown', 1, 'Summer'),
    ('ZJQDMQ', 'Thermodynamics', 'Mechanical Engineering', 'Ryan Wilson', 4, 'Autumn'),
    ('KXOJYU', 'Inorganic Chemistry', 'Chemistry', 'Laura Miller', 2, 'Spring'),
    ('SXZDNY', 'World History', 'History', 'Daniel Roberts', 3, 'Summer'),
    ('UJXNME', 'Materials Science', 'Mechanical Engineering', 'Olivia Johnson', 5, 'Autumn'),
    ('POXHJO', 'Cognitive Psychology', 'Psychology', 'Benjamin Harris', 1, 'Summer'),
    ('NBJDQH', 'British Literature', 'English', 'Samantha Turner', 4, 'Autumn'),
    ('JGTJAH', 'Artificial Intelligence', 'Computer Science', 'Matthew Clark', 2, 'Spring'),
    ('JZSFLP', 'Mechanical Design', 'Mechanical Engineering', 'Megan Thompson', 3, 'Summer'),
    ('QHPLLW', 'Analytical Chemistry', 'Chemistry', 'Christopher Hall', 5, 'Autumn'),
    ('KPYZAB', 'American Literature', 'English', 'Stephanie Adams', 1, 'Spring'),
    ('QZIBOQ', 'European History', 'History', 'Andrew White', 4, 'Autumn'),
    ('SMTQSV', 'Database Systems', 'Computer Science', 'Natalie Walker', 2, 'Spring'),
    ('TZGFWG', 'Physical Chemistry', 'Chemistry', 'Robert Johnson', 3, 'Summer'),
    ('ATZVXJ', 'Fluid Mechanics', 'Mechanical Engineering', 'Jennifer Lee', 5, 'Autumn');
INSERT INTO courselist (course_id, course_name, major, instructor, `year`, semester)
VALUES
    ('ABCDEF', 'Introduction to Physics', 'Mechanical Engineering', 'John Smith', 1, 'Spring'),
    ('XVJPHV', 'Data Structures', 'Computer Science', 'Emily Johnson', 4, 'Autumn'),
    ('PSYSAP', 'Introduction to Psychology', 'Psychology', 'David Anderson', 2, 'Summer'),
    ('GZIGFQ', 'Organic Chemistry', 'Chemistry', 'Sarah Thompson', 3, 'Autumn'),
    ('SUYGCF', 'Algorithms and Complexity', 'Computer Science', 'Jessica Brown', 4, 'Summer'),
    ('ZJQDMA', 'Thermodynamics', 'Mechanical Engineering', 'Ryan Wilson', 2, 'Autumn'),
    ('KXOJYS', 'Inorganic Chemistry', 'Chemistry', 'Laura Miller', 3, 'Spring'),
    ('SXZDNF', 'World History', 'History', 'Daniel Roberts', 1, 'Summer'),
    ('UJXNMN', 'Materials Science', 'Mechanical Engineering', 'Olivia Johnson', 4, 'Autumn'),
    ('POXHJH', 'Artificial Intelligence', 'Computer Science', 'Matthew Clark', 1, 'Spring'),
    ('JZSFLL', 'Mechanical Design', 'Mechanical Engineering', 'Megan Thompson', 4, 'Summer'),
    ('QHPLLL', 'Analytical Chemistry', 'Chemistry', 'Christopher Hall', 2, 'Autumn'),
    ('QZIBOH', 'European History', 'History', 'Andrew White', 1, 'Autumn'),
    ('SMTQEV', 'Database Systems', 'Computer Science', 'Natalie Walker', 4, 'Spring'),
    ('TZGFGG', 'Physical Chemistry', 'Chemistry', 'Robert Johnson', 2, 'Summer'),
    ('ATZVXH', 'Fluid Mechanics', 'Mechanical Engineering', 'Jennifer Lee', 3, 'Autumn');