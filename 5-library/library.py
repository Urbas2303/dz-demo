import sys

books = {
    "Скотный двор": "Джордж Оруэлл",
    "Мастер и Маргарита": "Михаил Булгаков",
    "1984": "Джордж Оруэлл",
    "Преступление и наказание": "Фёдор Достоевский",
    "Война и мир": "Лев Толстой",
    "Собачье сердце": "Михаил Булгаков",
    "Идиот": "Фёдор Достоевский"
}

func = sys.argv[1]
arg = sys.argv[2]

if func == "sort":
    sort_by = sys.argv[2] if len(sys.argv) > 2 else "book"

    formatted_list = list(
        map(lambda item: f"{item[0]} — {item[1]}", books.items()))

    if sort_by == "author":
        formatted_list.sort(key=lambda x: x.split(" — ")[1])
    else:
        formatted_list.sort()

    print(*formatted_list, sep="\n")

if func == "filter":
    author_name = sys.argv[2]

    filtered_books = filter(lambda item: item[1] == author_name, books.items())

    result = map(lambda item: f"{item[0]} — {item[1]}", filtered_books)
    print(*result, sep="\n")
