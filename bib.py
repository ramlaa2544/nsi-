import jsonpickle
class Book:
    global_id = 0

    def __init__(self, title, author, content, id=None):
        if id is None:
            self.__id = Book.global_id
            Book.global_id += 1
        else:
            self.__id = id
        self.__title = title
        self.__author = author
        self.__content = content

    # Property methods omitted for brevity

    def __str__(self) -> str:
        return f"{self.__title}, {self.__author}"

    def __eq__(self, other):
        return self.__id == other.__id


class MyLibrary:
    def __init__(self):
        self.__library = []
        self.__load()

    def add_book(self, book):
        self.__library.append(book)

    def delete_book(self, id):
        self.__library = [book for book in self.__library if book.id != id]

    def update_book(self, book):
        for book_in_lib in self.__library:
            if book.id == book_in_lib.id:
                book_in_lib.title = book.title
                book_in_lib.author = book.author
                book_in_lib.content = book.content

    def list_books(self):
        for book in self.__library:
            print(book)

    def __load(self):
        try:
            with open('save.json', 'r') as f:
                strjson = f.read()
                self.__library = jsonpickle.decode(strjson)._MyLibrary__library
        except FileNotFoundError:
            self.__library = []
        except Exception as e:
            print(f"Error loading data: {e}")

    def save(self):
        with open('save.json', 'w') as f:
            f.write(jsonpickle.encode(self))


def input_book():
    title = input("title: ")
    author = input("author: ")
    content = input("content: ")
    return title, author, content


if __name__ == "__main__":
    mylib = MyLibrary()
    action = ""
    while action != "q":
        mylib.save()
        action = input("Choisissez une action (new/update/delete/list/q) : ").strip().lower()
        if action not in ["list", "q"]:
            print(f"Action déclenchée : {action}")
        match action:
            case "update":
                id = int(input("ID : "))
                title, author, content = input_book()
                book = Book(title=title, author=author, content=content, id=id)
                mylib.update_book(book)
            case "new":
                title, author, content = input_book()
                book = Book(title=title, author=author, content=content)
                mylib.add_book(book)
            case "delete":
                id = int(input("ID : "))
                mylib.delete_book(id)
            case "list":
                mylib.list_books()
            case "q":
                print("Sortie...")
            case _:
                if action not in ["list", "q"]:
                    print("Action invalide. Veuillez choisir parmi new, update, delete ou q (pour quitter).")