import csv
from datetime import datetime as dt
import random

FILENAME = "books.csv"
OUTPUT_FILENAME = "random.txt"
DATE_STR = "Дата поступления"
AUTHOR_STR = "Автор"
TITLE_STR = "Название"

# changes arg dictionary
def find_col_numbers(names_dict):
    with open(FILENAME, newline="") as file:
        csvr = csv.reader(file, delimiter=";")
        i = 0
        for name in next(csvr):
            if name in names_dict:
                names_dict[name] = i
            i += 1


def get_csv_size(filename=FILENAME):
    with open(FILENAME, newline="") as file:
        csvr = csv.reader(file, delimiter=";")
        next(csvr)
        N = sum(1 for row in csvr)
        return N


def number_of_long_entries(n=30, column_name=TITLE_STR):
    counter = 0
    columns = {
        column_name: 0,
    }
    find_col_numbers(columns)

    with open(FILENAME, newline="") as file:
        books_reader = csv.reader(file, delimiter=";")

        for row in books_reader:
            if len(row[columns[column_name]]) > name_size:
                counter += 1
    return counter


def find_by_author(
    author,
    start_date,
    end_date,
    date_str=DATE_STR,
    author_str=AUTHOR_STR,
    title_str=TITLE_STR,
):
    author_books = []
    columns = {date_str: 0, author_str: 0, title_str: 0}
    find_col_numbers(columns)

    with open(FILENAME, newline="") as file:
        csvr = csv.reader(file, delimiter=";")
        next(csvr)
        for entry in csvr:
            entry_date = dt.strptime(entry[columns[date_str]], "%d.%m.%Y %H:%M")
            if (
                entry[columns[author_str]] == author
                and entry_date >= start_date
                and entry_date <= end_date
            ):
                author_books.append(entry[columns[title_str]])
    return author_books


def write_random_entries(n=20, filename=OUTPUT_FILENAME):
    date_str = "Дата поступления"
    author_str = "Автор"
    title_str = "Название"
    columns = {date_str: 0, author_str: 0, title_str: 0}
    find_col_numbers(columns)

    with open(FILENAME, newline="") as file:
        csvr = csv.reader(file, delimiter=";")
        next(csvr)
        N = get_csv_size()
        row_numbers = [random.randint(1, N) for _ in range(n)]
        with open(OUTPUT_FILENAME, "w") as output_file:
            i, j = 1, 1
            for entry in csvr:
                if i in row_numbers:
                    output_file.write(
                        str(j)
                        + ". "
                        + entry[columns[author_str]]
                        + ". "
                        + entry[columns[title_str]]
                        + " - "
                        + str(dt.strptime(entry[columns[date_str]], "%d.%m.%Y %H:%M").year)
                        + "\n"
                    )
                    j += 1
                i += 1


def main():
    start_date = dt(2016, 1, 1)
    end_date = dt(2018, 12, 31, hour=23, minute=59, second=59)
    print(find_by_author("Джей Эшер", start_date, end_date))
    write_random_entries()


if __name__ == "__main__":
    main()
    