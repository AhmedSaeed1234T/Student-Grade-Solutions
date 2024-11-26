print("Enter the borrowed books in the format 'Book Title - Days Borrowed', separated by commas:")
bookRecords = []
while True:
    record = input()
    if not record:
        break
    bookRecords.append(record.strip())

bookDict = {}

for record in bookRecords:
    title, daysBorrowed = record.split(" - ")
    daysBorrowed = int(daysBorrowed)
    bookDict[title] = bookDict.get(title, 0) + daysBorrowed


def findMaxBooks(dictionary):
    max_key = None
    max_value = float("-inf")
    for key, value in dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

most_borrowed_book = findMaxBooks(bookDict)

def findMinBooks(dictionary):
    min_key = None
    min_value = float("inf")
    for key, value in dictionary.items():
        if value < min_value:
            min_key = key
            min_value = value
    return min_key, min_value

least_borrowed_book = findMinBooks(bookDict)

totalDays = sum(bookDict.values())
totalBooks = len(bookDict)

average_days = totalDays / totalBooks

unique_titles = set(bookDict.keys())

sorted_books = list(bookDict.items())

for i in range(len(sorted_books)):
    for j in range(i + 1, len(sorted_books)):
        if sorted_books[i][1] < sorted_books[j][1]:
            sorted_books[i], sorted_books[j] = sorted_books[j], sorted_books[i]

 # Display results
print("\nLibrary Borrowing Analysis:")
print(f"Most borrowed book: {most_borrowed_book[0]} ({most_borrowed_book[1]} days)")
print(f"Least borrowed book: {least_borrowed_book[0]} ({least_borrowed_book[1]} days)")
print(f"Average borrowing duration: {average_days:.2f} days")
print(f"Unique titles of borrowed books: {unique_titles}")
print(f"Books sorted by borrowing duration:")
for title, days in sorted_books:
    print(f"{title}: {days} days")














# # Program to analyze library book borrowing records

# def main():
#     # Accept the list of borrowed books
#     borrowed_books_input = input("Enter the borrowed books in the format 'Book Title - Days Borrowed', separated by commas: ")

#     # Split the input and process each record
#     borrowed_books_list = borrowed_books_input.split(",")
#     borrowed_books = {}

#     try:
#         for record in borrowed_books_list:
#             # Split the record into title and days
#             title, days = map(str.strip, record.split("-"))
#             days = int(days)  # Convert days to an integer

#             # Update the dictionary with total borrowed days
#             borrowed_books[title] = borrowed_books.get(title, 0) + days
#     except ValueError:
#         print("Invalid input format. Ensure each record is 'Book Title - Days Borrowed'.")
#         return

#     # Calculate the most and least borrowed book
#     most_borrowed = max(borrowed_books.items(), key=lambda x: x[1])
#     least_borrowed = min(borrowed_books.items(), key=lambda x: x[1])

#     # Calculate the average borrowing duration
#     total_days = sum(borrowed_books.values())
#     total_books = len(borrowed_books)
#     average_days = total_days / total_books

#     # Find unique book titles
#     unique_titles = set(borrowed_books.keys())

#     # Sort books by the number of days borrowed in descending order
#     sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)

#     # Display results
#     print("\nLibrary Borrowing Analysis:")
#     print(f"Most borrowed book: {most_borrowed[0]} ({most_borrowed[1]} days)")
#     print(f"Least borrowed book: {least_borrowed[0]} ({least_borrowed[1]} days)")
#     print(f"Average borrowing duration: {average_days:.2f} days")
#     print("Unique titles of borrowed books:")
#     print(", ".join(unique_titles))
#     print("\nBooks sorted by borrowing duration:")
#     for title, days in sorted_books:
#         print(f"{title}: {days} days")

# # Run the program
# if __name__ == "__main__":
#     main()