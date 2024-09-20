from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, Float, Date
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the association table for many-to-many relationship between Books and Genres
book_genre_association = Table('book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

# Define Author model
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")

# Define Book model
class Book(Base):
    __tablename__= 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    stock = Column(Integer)
    price = Column(Float)
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary=book_genre_association, back_populates="books")

# Define Genre model
class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary=book_genre_association, back_populates="genres")

# Define Sale model
class Sale(Base):
    __tablename__= 'sales'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer)
    total_price = Column(Float)
    date = Column(Date)

# Function to create the database and tables
def init_db():
    # Create an engine that stores data in the local file bookstore.db
    engine = create_engine('sqlite:///bookstore.db', echo=False)
    # Set echo=True to show SQL statements for debugging
    Base.metadata.create_all(engine)  # Create all tables if they don't exist
    Session = sessionmaker(bind=engine)
    return Session  # Return the session class

if __name__ == "__main__":
    init_db()