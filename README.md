# Bookstore Managment System
# Bookstore Management System

## Overview

The Bookstore Management System is a command-line application built with Python that allows users to manage a bookstore's inventory, including authors, books, genres, and sales. It utilizes SQLAlchemy as an ORM for database management and provides a simple CLI interface for interacting with the application.

## Features

- Manage authors, books, and genres
- Record sales and update stock automatically
- View and list all entities
- Simple command-line interface using Click
- Database schema defined with SQLAlchemy

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Getting Started

### Step 1: Setup Your Development Environment

1. **Install Python**: Ensure Python is installed on your machine. 

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv bookstore_env
   source bookstore_env/bin/activate  
   ```

3. **Install Required Packages**:
   ```bash
   pip install sqlalchemy click
   ```

### Step 2: Design the Database Schema

The application defines the following models:
- **Authors**: Contains `id` and `name`.
- **Books**: Contains `id`, `title`, `author_id`, and `stock`.
- **Genres**: Contains `id` and `name`.
- **Sales**: Contains `id`, `book_id`, `quantity`, and `sale_date`.
- **BookGenres**: A many-to-many relationship table between books and genres.

### Step 3: Implement the ORM Models.

The models are defined using SQLAlchemy as shown below:

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    stock = Column(Integer)
    author = relationship("Author")

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)

book_genre_table = Table('book_genres', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer)
    sale_date = Column(String)  
```

### Step 4: Create the CLI Interface.


### Step 5: Implement CRUD Operations

Functions are implemented for creating, reading, updating, and deleting (CRUD) authors, books, and genres.

### Step 6: Sales Management

- **Record Sales**: Functionality to record sales and update book stock.
- **Sales Reporting**: Optionally create reports for sales data.

### Step 7: Testing

- **Unit Tests**: Write tests for CRUD operations and CLI commands using unittest or pytest.
- **Integration Tests**: Ensure that all parts of the application work together seamlessly.

### Step 8: Documentation

- Write comments and docstrings to document your code.
- Create user documentation for instructions on using the CLI.

### Step 9: Refine and Expand

- Enhance features with advanced search options, data validation, and error handling.
- Gather user feedback to improve the application.

### Step 10: Deployment (Optional)

- Package your application using setuptools or pyinstaller for distribution.

## Conclusion

This Bookstore Management System serves as a foundation for managing a bookstore's inventory and sales. 
