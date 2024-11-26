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
