import unittest
from booklover import BookLover
import pandas as pd


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        booklover1 = BookLover("Mark Tuan", "mtuan7@gmail.com", "sci-fi")
        booklover1.add_book("Caravel",4)
        self.assertEqual(booklover1.book_list.iloc[0]['book_name'], "Caravel")
        self.assertEqual(booklover1.book_list.iloc[0]['book_rating'], 4)
        #self.assertEqual(booklover1.book_list.iloc[0]['book_name'],"Harry Potter and the Sorcerer's Stone")

    def test_2_add_book(self):
        booklover1 = BookLover("Mark Tuan", "mtuan7@gmail.com", "sci-fi")
        booklover1.add_book("Animal Farm", 3)
        booklover1.add_book("Animal Farm", 3)
        self.assertEqual(len(booklover1.book_list), 1)
        #self.assertEqual(booklover1.book_list.iloc[0]['book_name'], "Animal Farm")

    def test_3_has_read(self):
        booklover1 = BookLover("Mark Tuan","mtuan7@gmail.com","sci-fi")
        booklover1.add_book("Caravel", 4)
        booklover1.add_book("Animal Farm", 3)
        actual = booklover1.has_read('Caravel')
        self.assertTrue(actual)

    def test_4_has_read(self):
        booklover1 = BookLover("Mark Tuan","mtuan7@gmail.com","sci-fi")
        booklover1.add_book("Caravel", 4)
        booklover1.add_book("Animal Farm", 3)
        actual = booklover1.has_read("Brave New World")
        self.assertFalse(actual)

    def test_5_num_books_read(self):
       booklover1 = BookLover("Mark Tuan","mtuan7@gmail.com","sci-fi")
       booklover1.add_book("Caravel", 4)
       booklover1.add_book("Animal Farm", 3)
       booklover1.add_book("Brave New World",2)
       booklover1.add_book("Evelyn Hugo and Her seven husbands",5) 
       actual = booklover1.num_books_read()
       expected = 4
       self.assertEqual(actual, expected)

    def test_6_fav_books(self):
        booklover1 = BookLover("Mark Tuan","mtuan7@gmail.com","sci-fi")
        booklover1.add_book("Caravel", 4)
        booklover1.add_book("Animal Farm", 3)
        booklover1.add_book("Brave New World",2)
        booklover1.add_book("Evelyn Hugo and Her seven husbands",5) 
        booklover1.add_book("1984", 4)
        fav_rating = booklover1.fav_books()['book_rating']
        self.assertTrue(all(rating > 3 for rating in fav_rating))
        




if __name__ == "__main__":
    unittest.main(verbosity=3)