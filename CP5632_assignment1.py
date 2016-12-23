__author__ = jc458517

# Initialize the constants

def main():
	print("Reading List 1.0 - by sukhdeep")
	book_list=[]
	load_books(book_list)
	display_menu()

choice=input('>>>').upper()

while choice != 'Q':
    if choice == 'R':
     # list_required_books(book_list)
      print("required")
	elif choice == 'C':
	  print("required")
        # list_completed_books(book_list)
    elif choice == 'A':
        # add_new_books(book_list)
    elif choice == 'M':
          # mark_books_completed()
    else:
        print('Please enter R,C,A,M or Q(Q(uit')
    display_menu()
    choice=input('>>>').upper()
	print('Have a nice day:')')



# end of main()
def display_Menu():
	print('Menu:')
	print('R - List required books')
    print('C - List completed books')
    print('A - Add new book')
    print('M - Mark a book as completed')
print('Q - Quit')

def load_books():
"""

"""
	print("load books")

# end of load_books()

def complete_a_book():
"""

"""
	print("complete a book")

# end of complete_a_book()

# Start the program
main()