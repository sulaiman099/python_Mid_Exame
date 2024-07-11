class Star_Cinema:
    hall_list = []

    def entry_hall(self, Hall):
        self.hall_list.append(Hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hol_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hol_no = hol_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        tempTuple = (id, movie_name, time)
        self.__show_list.append(tempTuple)

        seatAvailable = [['$' for i in range(self.cols)] for i in range(self.rows)]
        self.__seats[id] = seatAvailable

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print("Invalid show id")
            return

        for row, col in seat_list:
            if row >= self.rows or col >= self.cols or row < 0 or col < 0:
                print(f'Invalid seat: {row}, {col}')
                return
            if self.__seats[id][row][col] == 1:
                print(f"Seat {row}, {col} is already booked")
                return
            self.__seats[id][row][col] = 1

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid show id")
            return 
        return self.__seats[id]


cinema = Hall(5, 5, 'NO-1')
cinema.entry_show('101', 'artugol', '10:30 am')
cinema.entry_show('102', 'sulttan', '2:30 pm')
cinema.entry_show('103', 'usmanbe', '8:30 pm')
cinema.book_seats('101', [(1, 1)])#vip person

while True:
    print("1. View all shows today:")
    print("2. View available seats:")
    print("3. Book Ticket")
    print("4. Exit")
    choice = int(input("Enter option: "))

    if choice == 1:
        print(cinema.view_show_list())

    elif choice == 2:
        id = input("Enter Show ID: ")
        available_seats = cinema.view_available_seats(id)
        if available_seats is not None:
            for row in available_seats:
                print(row)

    elif choice == 3:
        id = input("Enter Show ID: ")
        
        row=int(input("Enter row:"))
        col=int(input("Enter col:"))
        cinema.book_seats(id,[(row,col)])

    elif choice == 4:
        break

    else:
        print("Invalid option")

    