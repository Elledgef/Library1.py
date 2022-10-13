#Author: Faith Elledge
#Githubusername: Elledgef
#Date: 10/12/22
#Description: This project holds members, library items and makes it so they can be added to lists and removed.
# Makes it so patrons can be fined for late books and have items put on hold for them.


class LibraryItem:
        """ This is the library Item Object, this class will be inhereted by the Book, Author and Movie class"""

        def __init__(self,library_item_id,title):
            self._library_item_id = library_item_id
            self._title = title
            self._location = "ON_SHELF"
            self._checked_out_by = None
            self._requested_by = None
            self._date_checked_out = None

        def get_library_item_id (self):
            return self._library_item_id

        def get_title(self):
            return self._title

        def get_location(self):
            return self._location

        def set_location (self,location):
            self._location = location

        def get_checked_out(self):
            return self._checked_out_by

        def get_requested_by(self):
            return self._requested_by

        def set_requested_by(self,user):
            self._requested_by = user

        def get_date_checked_out(self):
            return self._date_checked_out

        def set_date_checked_out(self, current_day):
            self._date_checked_out = current_day

class Book(LibraryItem):
        """ Book is inhereted by the LibraryItem Class"""
        def __init__(self,library_item_id, title, author):
            super().__init__(library_item_id, title)
            self._author = author

        def get_author(self):
            return self._author

        def set_author(self, author):
            self._author = author

        def get_check_out_length(self):
            return 21
        """This is the check out time that the library allows for books"""
class Album(LibraryItem):
        """ Album inherits from Library Item Class"""
        def __init__(self, library_item_id, title, artist):
            super().__init__(library_item_id, title)
            self._artist = artist

        def get_arist(self):
            return self._artist

        def set_artist(self, artist):
            self._artist = artist

        def get_check_out_lenght(self):
            return 14
        """This is the check out time that the library allows for albums"""

class Movie(LibraryItem):
        """The Movie class is inherited from the Library Item Class"""
        def __init__(self, library_item_id, title, director):
            super().__init__(library_item_id, title)
            self._director = director

        def get_director(self):
            return self._director

        def set_director(self, director):
            self._director = director

        def get_check_out_length(self):
            return 7
        """This is the check out time that the library allows for Movies"""

class Patron:

        def __init__(self, patron_id, name):
            """ Patron object with an Id, a name, a list with items that have been checked out amd a fine amount if
                needed """
            self._patron_id = patron_id
            self._name = name
            self._checked_out_items = []
            self._fine_amount = 0

        def get_patron_id (self):
            return self._patron_id

        def get_name(self):
            return self._name

        def get_checked_out_items(self):
            return self._checked_out_items

        def add_library_item(self, item):
            """ Adds a specified libraryitem to checked out list"""
            self._checked_out_items.append(item)

        def remove_library_item(self, item):
            """Removes a specifiec LibraryItem from checked out list"""
            self._checked_out_items.remove(item)

        def amend_fine(self, amount):
            """ takes a postive amound to charge patron or a negative amount when patron pays"""
            self._fine_amount += amount

        def get_fine_amount(self):
            return self._fine_amount

class Library:
        """ A library that contains Items and has patrons. Makes it so patrons are able to check out items, return items,
        request/ hold items, and charges patrons fines """
        def __init__(self):
            self._current_date = 0
            self._holdings = []
            self._members = []

        def get_current_date(self):
            return self._current_date

        def get_holdings(self):
            self._holdings = []

        def get_members(self):
            self._members = []

        def add_library_item(self, libraryitem):
            self._holdings.append(libraryitem)

        def add_patron(self,user):
            self._members.append(user)


        def lookup_library_item_from_id(self, library_item_id):
            for libraryitem in self._holdings:
                if (libraryitem.lookup_library_item_id() == library_item_id):
                    return libraryitem
            return None

        def lookup_patron_from_id(self, patron_id):
            for patron in self._members:
                if (patron.lookup_patron_from_id()== patron_id):
                    return patron
            return None

        def check_out_library_item(self, patron_id, library_item_id, item):
            patron = self._lookup_patron_from_id = patron_id
            libraryitem = self._lookup_library_item_from_id = library_item_id
            if (patron == None):
                return "Library Member not found"
            elif (libraryitem == None):
                return "Item not found"
            elif item.get_location() == "CHECKED_OUT":
                return "item already checked out"
            elif item.get_location() == "ON_HOLD_SHELF":
                return "Item on hold from another library member"
            else:
                item.set_checked_out_by(patron)
                item.set_date_checked_out(self._current_date)
                item.set_location("CHECKED_OUT")
            if  item.get_requested_by() == patron:
                item.set_requested_by(None)
                patron.add_library_item(item)
                return "check out successful"

        def return_library_item(self,library_item_id,item):
            libraryitem = self._lookup_library_item_from_id = library_item_id
            if (libraryitem == None):
                return "item not found"
            else:

                if item.lookup_library_item_from_id() == "CHECKED_OUT":
                 return "item already in library"
                patron = item.get_checked_out_by()
                patron.remove_library_item(item)
                if item.get_requested_by () != None:
                    item.set_location("ON_HOLD_SHELF")
                item.set_location("ON_SHELF")
                item.set_checked_out_by(None)
                return "return Successful"

        def request_library_item(self, patron_id, library_item_id, item):
            patron = self._lookup_patron_from_id = patron_id
            libraryitem = self._lookup_library_item_from_id = library_item_id
            if (patron == None):
                return "Library member not found"
            elif (libraryitem == None):
                return "Item not found"
            if item.get_requested_by() != None:
                return "Item already on hold"
            item.set_requested_by(patron)
            if item.get_location() == "ON_SHELF":
                item.set_location("ON_HOLD_SHELF")
            return "Request Successful"

        def pay_fine(self, patron_id, fineamount):
            patron = self._lookup_patron_from_id = patron_id
            if (patron == None):
                return "Library member not found"
            else:
                    patron.amend_fine(-fineamount)
                    return "payment Successful"

        def increment_current_date(self):
            self._current_date +=1
            for i in range(len(self._members)):
                self._members[i].amend_fine(0.10)

def main():
    book1 = Book ("1357", "The Shining", "King")
    book2 = Book ("1490", "The Mist", "King")
    album1 = Album ("1567", "Vertigo", "Eden")
    movie1 = Movie ("3456","The grinch","Howard")
    patron1 = Patron ("234", "Faith")
    patron2 = Patron ("567", "Tanner")
    lib = Library()
    lib.add_library_item(book1)
    lib.add_library_item(book2)
    lib.add_library_item(album1)
    lib.add_library_item(movie1)
    lib.add_patron(patron1)
    lib.add_patron(patron2)
    lib.check_out_library_item("234", "1357")
    lib.check_out_library_item("567","1490")





























