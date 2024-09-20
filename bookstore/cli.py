from models import init_db, Author, Book, Genre, Sale
from datetime import datetime

# Initialize the database session
SessionLocal = init_db()

def main():
    while True:
        print("\nBookstore Management System")
        print("1. Add Author")
        print("2. Add Book")
        print("3. Add Genre")
        print("4. Record Sale")
        print("5. Search Books")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter author name: ")
            add_author(name)
        elif choice == '2':
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            stock = int(input("Enter stock quantity: "))
            price = float(input("Enter price: "))
            genres = input("Enter genres (comma-separated): ")
            add_book(title, author_name, stock, price, genres)
        elif choice == '3':
            name = input("Enter genre name: ")
            add_genre(name)
        elif choice == '4':
            book_title = input("Enter book title: ")
            quantity = int(input("Enter quantity sold: "))
            total_price = float(input("Enter total price: "))
            add_sale(book_title, quantity, total_price)
        elif choice == '5':
            title = input("Enter book title (leave blank for any): ")
            genre = input("Enter genre (leave blank for any): ")
            available = input("Available only? (yes/no): ").lower() == 'yes'
            search_books(title=title or None, genre=genre or None, available=available)
        elif choice == '6':
            print("Exiting the Bookstore Management System.")
            break
        else:
            print("Invalid option. Please choose a number from the menu.")

def add_author(name):
    session = SessionLocal()  # Create a session
    try:
        author = Author(name=name)
        session.add(author)
        session.commit()
        print(f'Added author: {name}')
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def add_book(title, author_name, stock, price, genres):
    session = SessionLocal()  # Create a session
    try:
        # Find or create the author
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            print(f'Author {author_name} not found. Please add the author first.')
            return

        # Find or create genres
        genre_names = [genre.strip() for genre in genres.split(',')]
        genres_list = []
        for name in genre_names:
            genre = session.query(Genre).filter_by(name=name).first()
            if not genre:
                genre = Genre(name=name)
                session.add(genre)
            genres_list.append(genre)

        # Create the book
        book = Book(title=title, author=author, stock=stock, price=price, genres=genres_list)
        session.add(book)
        session.commit()
        print(f'Added book: {title} by {author_name}')
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def add_genre(name):
    session = SessionLocal()  # Create a session
    try:
        genre = Genre(name=name)
        session.add(genre)
        session.commit()
        print(f'Added genre: {name}')
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def add_sale(book_title, quantity, total_price):
    session = SessionLocal()  # Create a session
    try:
        # Find the book
        book = session.query(Book).filter_by(title=book_title).first()
        if not book:
            print(f'Book {book_title} not found.')
            return

        # Record the sale
        sale = Sale(book_id=book.id, quantity=quantity, total_price=total_price, date=datetime.now())
        session.add(sale)
        session.commit()
        print(f'Recorded sale for: {book_title} (Quantity: {quantity}, Total Price: {total_price})')
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def search_books(title=None, genre=None, available=False):
    session = SessionLocal()  # Create a session
    try:
        query = session.query(Book)
        if title:
            query = query.filter(Book.title.ilike(f'%{title}%'))
        if genre:
            query = query.join(Book.genres).filter(Genre.name.ilike(f'%{genre}%'))
        if available:
            query = query.filter(Book.stock > 0)
        
        results = query.all()

        if results:
            print("Search Results:")
            for book in results:
                print(f' - {book.title} by {book.author.name} (Stock: {book.stock}, Price: {book.price})')
        else:
            print("No results found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()