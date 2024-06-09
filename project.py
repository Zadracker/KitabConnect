import csv
import sys

CSV_FILE = 'books.csv'
COURSE_TYPES = ("Engineering", "Arts", "Law", "Medicine", "Business", "Architecture")

def main():
    while True:
        option = str(input("Buying / Selling / Searching / Exit: ")).lower().strip()
        select_user(option)

def select_user(option):
    try:
        if option in ["buying", "buy"]:
            buy_page()
        elif option in ["selling", "sell"]:
            sell_page()
        elif option in ["searching", "search"]:
            search_books()
        elif option == "exit":
            sys.exit("Exiting")
        else:
            raise ValueError
    except ValueError:
        print("Invalid input, please enter 'Buying', 'Selling', 'Searching', or 'Exit'.")

def buy_page():
    while True:
        try:
            with open(CSV_FILE, mode='r', newline='') as file:
                csv_reader = csv.DictReader(file)
                books = list(csv_reader)

                if not books:
                    print("No books listed yet. Please try selling first.")
                    return

                print(f"{'Serial No.':<10}{'Book Name':<20}{'Course Name':<20}{'Price':<10}")
                print('-' * 60)
                for row in books:
                    print(f"{row['Serial No.']:<10}{row['Book Name']:<20}{row['Course Name']:<20}{row['Price']:<10}")

                serial_to_buy = input("Enter the serial number of the book you want to buy (or type 'cancel' to return): ").strip()

                if serial_to_buy.lower() == 'cancel':
                    return

                try:
                    serial_to_buy = int(serial_to_buy)
                except ValueError:
                    print("Invalid serial number. Please try again.")
                    continue

                for book in books:
                    if int(book['Serial No.']) == serial_to_buy:
                        confirm = input(f"Do you want to purchase '{book['Book Name']}' for {book['Price']}? (yes/no): ").lower()
                        if confirm == 'yes':
                            print(f"Purchase of '{book['Book Name']}' successful for {book['Price']}.")
                            books.remove(book)
                            with open(CSV_FILE, mode='w', newline='') as file:
                                fieldnames = ['Serial No.', 'Book Name', 'Course Name', 'Price']
                                csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
                                csv_writer.writeheader()
                                csv_writer.writerows(books)
                            return
                        else:
                            print("Purchase cancelled.")
                            return
                print("Book not found. Please try again.")
        except FileNotFoundError:
            print("No books listed yet. Please try selling first.")
            return

def sell_page():
    while True:
        book_name = input("Enter the name of the book (or type 'cancel' to go back): ").strip()
        if book_name.lower() == 'cancel':
            return

        print("Select a course type:")
        for i, course in enumerate(COURSE_TYPES, 1):
            print(f"{i}. {course}")

        try:
            course_index = int(input("Enter the number corresponding to the course: ").strip())
            if course_index < 1 or course_index > len(COURSE_TYPES):
                raise ValueError
            course_name = COURSE_TYPES[course_index - 1]
        except ValueError:
            print("Invalid input. Please enter a valid number corresponding to the course.")
            continue

        try:
            book_price = int(input("Enter price: ").strip())
        except ValueError:
            print("Invalid input. Price must be a number.")
            continue

        try:
            with open(CSV_FILE, mode='r', newline='') as file:
                csv_reader = csv.DictReader(file)
                books = list(csv_reader)
                last_serial = int(books[-1]['Serial No.']) if books else 0
        except FileNotFoundError:
            last_serial = 0

        serial_no = last_serial + 1

        with open(CSV_FILE, mode='a', newline='') as file:
            fieldnames = ['Serial No.', 'Book Name', 'Course Name', 'Price']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                csv_writer.writeheader()
            csv_writer.writerow({'Serial No.': serial_no, 'Book Name': book_name, 'Course Name': course_name, 'Price': book_price})

        print(f"Book '{book_name}' for course '{course_name}' listed at price '{book_price}' with serial number '{serial_no}'.")
        return

def search_books():
    while True:
        search_option = input("Search by (1) Course, (2) Price Range, or type 'cancel' to return: ").strip().lower()
        if search_option == 'cancel':
            return

        try:
            with open(CSV_FILE, mode='r', newline='') as file:
                csv_reader = csv.DictReader(file)
                books = list(csv_reader)

                if not books:
                    print("No books listed yet.")
                    return

                results = []
                if search_option == '1':
                    print("Select a course type:")
                    for i, course in enumerate(COURSE_TYPES, 1):
                        print(f"{i}. {course}")

                    try:
                        course_index = int(input("Enter the number corresponding to the course: ").strip())
                        if course_index < 1 or course_index > len(COURSE_TYPES):
                            raise ValueError
                        course_name = COURSE_TYPES[course_index - 1]
                        results = [book for book in books if book['Course Name'] == course_name]
                    except ValueError:
                        print("Invalid input. Please enter a valid number corresponding to the course.")
                        continue

                elif search_option == '2':
                    try:
                        min_price = float(input("Enter the minimum price: ").strip())
                        max_price = float(input("Enter the maximum price: ").strip())
                        results = [book for book in books if min_price <= float(book['Price']) <= max_price]
                    except ValueError:
                        print("Invalid input. Please enter valid numbers for price range.")
                        continue

                else:
                    print("Invalid option. Please try again.")
                    continue

                if not results:
                    print("No books found matching your criteria.")
                else:
                    print(f"{'Serial No.':<10}{'Book Name':<20}{'Course Name':<20}{'Price':<10}")
                    print('-' * 60)
                    for row in results:
                        print(f"{row['Serial No.']:<10}{row['Book Name']:<20}{row['Course Name']:<20}{row['Price']:<10}")

        except FileNotFoundError:
            print("No books listed yet.")
            return

def initialize_csv():
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            if not csv_reader.fieldnames or 'Serial No.' not in csv_reader.fieldnames:
                raise FileNotFoundError
    except FileNotFoundError:
        with open(CSV_FILE, mode='w', newline='') as file:
            fieldnames = ['Serial No.', 'Book Name', 'Course Name', 'Price']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()

if __name__ == "__main__":
    initialize_csv()
    main()
