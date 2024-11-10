import sys
def moviesList():
    return {
        "1":
                    {"title":"Sitaramam", "seating_chart":[['-'for row in range(5)]for col in range(5)],"price":90} ,
        "2":
                    {"title":"Rockstar", "seating_chart":[['-'for row in range(5)]for col in range(5)],"price":100}}
    

def display_movies(movies):
    for i in movies:
        seating= sum(row.count('-')for row in movies[i]["seating_chart"])
        print(f"movie-id= {i},title= {movies[i]["title"]}, no_of seats={seating}, price={movies[i]["price"]}")

# display_movies(d)

def book_ticket(movies, cart):
    display_movies(movies)
    # for i in movies:

    while True:
        a=input("enter a movie-id:")
        if a in movies:
            print(movies[a]["title"])
            break
        else:
            print("Invalid movie-id ")
    for rows in movies[a]["seating_chart"]:
        print(''.join(rows))
    # print()
    seating= sum(row.count('-')for row in movies[a]["seating_chart"])
    while True:
        b= int(input("enter no of tickets:"))

        if b<=seating and b > 0:
            break
        else:
            print("enter valid no of seats! ")
    c=[]
    d=[]
    seat_nos=[]
    for i in range(b):
        
        while True:
            row = int(input("enter row: "))
            col = int(input("enter col: "))
            if 0<= row <=4 and 0<=col<=4 and movies[a]["seating_chart"][row][col]=='-':
                # movies[a]["seating_chart"][row][col]='X'
                c.append(row)
                d.append(col)
                seat_nos.append((row,col))
                break
            else:
                print("invalid!")
    print(c)
    print(d)
    print(seat_nos)
    print(f"PAY:{movies[a]["price"]*b}")
    confirm = input("Confirm booking (y/n)?:")
    if confirm == "y":
        print("Confirmed")
        for i in range(b):
            movies[a]["seating_chart"][c[i]][d[i]]='X'
        cart.append({"movie_name":movies[a]["title"],"No.of seats":b,"seat_no":seat_nos, "total_price":movies[a]["price"]*b})
        for rows in movies[a]["seating_chart"]:
            print(''.join(rows))
    else:
        print("thankyou! see you soon")
    
    
    # for rows in movies[a]["seating_chart"]:
    #     print(''.join(rows))

def view_cart(cart):
    if cart == []:
        print("No items in cart")
    else:
        print(cart)
        checkout= input("Do you want to checkout y/n:")
        if checkout == "y":
            while True:
                payment = input("payment done? y/n:")
                if payment == "y":
                    print("Booking is Successfull!")
                    cart.clear()
                    break
                else:
                    print("retry the payment")
        else:
            print("Checkout cancelled")

def bookmyShow():
    movies = moviesList()
    cart = []
    print("Welcome to BookMyShow!")
    
    while True:
        print("\n1. Book Ticket\n2. View Cart\n3. Exit")
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            book_ticket(movies, cart)
        elif choice == 2:
            view_cart(cart)
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

bookmyShow()