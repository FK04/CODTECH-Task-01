# CODTECH-Task-01
**Name** : SYED ABDUL QADER FAIZAN KHUNDMIRY
**Company** : CODTECH IT SOLUTIONS
**ID** : CT6WDS1928
**Domain** : Python Programming
**Duration** : September to November 2024
**Mentor** : Neela Santhosh Kumar

## Overview Of The Project

### Project : LIBRARY MANAGEMENT SYSTEM

### Overview
The Library Management System is a user-friendly desktop application built with Python and MySQL. It provides an intuitive GUI for managing library operations, such as adding, updating, searching, and viewing book records. This project is ideal for small to medium-sized libraries aiming to streamline their inventory and borrowing processes.

### Features
- **Add Books**: Easily add new book entries with title, author, category, and availability status.
- **Search Books**: Search for books based on title, author, or category.
- **Update Records**: Update book details, such as title, author, or category.
- **View All Records**: Display a complete list of all books in the library's inventory.
- **Checkout and Return**: Manage the borrowing and returning of books.

### Technologies Used
- Programming Language: Python (Tkinter for GUI development)
- Database: MySQL (for storing book records and transaction details)
- Libraries:
- tkinter: For creating the GUI.
- mysql.connector: For database connectivity.

### Setup Instructions
Clone the repository:
git clone <repository_url>
cd library-management-system

Install the required dependencies:
pip install mysql-connector-python


Create a database named library_db.
Import the provided SQL file (sql_query.sql) to set up the required tables.
Update the database connection details in the script (host, user, and password).
Run the application:

bash
python library_management_system.py

### How It Works
The application launches a GUI where users can manage the library records.
Books can be added, searched, updated, or deleted using the respective modules.
A Treeview widget is used to display book data in a structured format.
The database ensures data persistence and allows for scalable management.

### Future Enhancements

Add user authentication for secure access.
Implement advanced search filters.
Include support for borrowing history tracking.
Optimize the GUI for larger datasets.

### Contribution

Feel free to contribute to this project by creating issues, submitting pull requests, or suggesting features.
