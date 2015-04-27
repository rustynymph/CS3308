# CS3308 -- Fireproof
Software Engineering Methods and Tools

##Organization of Repository:
We sorted our files into the following folders:
* The autodoc_html_files folder contains the html for all the autodocumentor output
* The code folder contains all the code for the app
* The images folder contains the logo for the app
* The project writeups folder contains all the .pdf documents for the checkpoints
* The tests folder contains the Python testing scripts for the project

##Setup:
For first time users:
* Launch MySQL by running "mysql -u root -p"
* Login using your MySQL password
* Type into the prompt $CREATE DATABASE Fireproof;
* In the MySQL prompt run $CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testAnnie';
* Next run $GRANT ALL PRIVILEGES ON `%`.* TO 'testuser'@'localhost' IDENTIFIED BY 'testAnnie' WITH GRANT OPTION;

If this is not your first time setting up the app, please skip all the above steps.

##Running the App:
Simply type $python Fireproof.py
* Developed and tested for use on Unix
