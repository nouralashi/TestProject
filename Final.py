
import random


class Client:

    def __int__(self, full_name, age, id_no, phone_number):
        self.id = random.randint(1, 100)
        self._full_name = full_name
        self._age = age
        self._id = id_no
        self._phone_number = phone_number


    def get_full_name(self):
        return self._full_name
    def get_age(self):
        return self._age
    def get_id_no(self):
        return self._id
    def get_phone_number(self):
        return self._phone_number

    def display(self):
        return {
            "full_name": self._full_name,
            "age": self._age,
            "id": self._id,
            "phone_number": self._phone_number

        }


class Librarian(Client):
    def salary(self, salar):
        self._salary = 0.0

    def get_salary(self):
        return self._salary



class Book:
    def __int__(self, title, description, author, status):
        self.id = random.random()
        self.title = title
        self.description = description
        self.author = author
        self.status = status


    #def status(self):
        #if self.status:
            #return "Active"
        #else:
            #return "Inactive"

    #def status(self,status):
        #if status in books:
            #return "Active"
         #else:
          #   return "Inactive"




class Borrowing_order:
    def __int__(self, start_date, end_date, book_id, client_id, status):
        self.id = random.random()
        self.start_date = start_date
        self.end_date = end_date
        self.book_id = book_id
        self.client_id = client_id
        self.status = status



clients = []
books = []
borrowing_orders = []
total_borrowed_books = 0
total_available_books = 0
total_borrowed_orders = 0
clients.append(clients(random.randint(1, 100), str(input("Client name :")), str(input("age :")), 1, str(input("id_no:")), str(input("phone_number:"))))
books.append(books(random.randint(1, 100), str(input("title :")), str(input("description:")), 1, str(input("author:")), str(input("status:"))))

for i in clients:
    print(i.display())