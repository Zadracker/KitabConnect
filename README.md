
# Kitab Connect


It is a Python-based application designed to facilitate the buying, selling, and searching of books for a college bookstore. The system utilizes CSV files to manage book data, allowing users to list books for sale, purchase books, and search for books based on course or price range.

## Key Features



>Sell Books: Allows users to list books for sale by entering book details.

>Buy Books: Enables users to purchase listed books.

>Search Books: Provides functionality to search for books by course name or price range.
## Main Functions
>sell_page
This function allows users to list a book for sale. Users will be prompted to enter the book name, course name, and price. The entered details are then stored in the CSV file. Here is how it works:

Prompts the user to enter the book name.
Prompts the user to enter the course name (represented by a number).
Prompts the user to enter the price of the book.
Saves the details to the CSV file

>buy_page

This function enables users to purchase a book. Users need to enter the serial number of the book they wish to purchase. The function performs the following steps:

Prompts the user to enter the serial number of the book they want to buy.
Confirms the purchase with the user.
Updates the CSV file to remove the purchased book or mark it as sold.
>search_books
This function allows users to search for books based on specific criteria. Users can search by course name or price range. The search function works as follows:

Prompts the user to choose the search criteria (course name or price range).
If searching by course name, the user enters the course name, and the function displays matching books.
If searching by price range, the user enters the minimum and maximum price, and the function displays books within that range.
Displays the search results to the user.
