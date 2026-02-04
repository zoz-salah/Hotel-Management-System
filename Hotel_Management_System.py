class Room:
    def __init__(self):
        self.room_number = 0
        self.guest_name = ""
        self.room_type = ""
        self.price_per_night = 0.0
        self.is_booked = False

    def setRoomNumber(self, number):
        self.room_number = number

    def setGuestName(self, name):
        self.guest_name = name

    def setRoomType(self, room_type):
        self.room_type = room_type

    def setPrice(self, price):
        self.price_per_night = price

    def bookRoom(self):
        self.is_booked = True

    def checkoutRoom(self):
        self.is_booked = False
        self.guest_name = ""

    def getRoomNumber(self):
        return self.room_number

    def isBooked(self):
        return self.is_booked

    def display(self):
        print("Room Number :", self.room_number)
        print("Room Type   :", self.room_type)
        print("Price/Night:", self.price_per_night)
        print("Status      :", "Booked" if self.is_booked else "Available")
        if self.is_booked:
            print("Guest Name  :", self.guest_name)
        print("-----------------------------")


allRooms = []


def roomExists(number):
    for room in allRooms:
        if room.getRoomNumber() == number:
            return True
    return False


def addRoom():
    room = Room()
    number = int(input("Enter room number: "))

    if roomExists(number):
        print("Room already exists!")
        return

    room.setRoomNumber(number)
    room.setRoomType(input("Enter room type: "))
    room.setPrice(float(input("Enter price per night: ")))

    allRooms.append(room)
    print("Room added successfully.")


def bookRoom():
    number = int(input("Enter room number to book: "))

    for room in allRooms:
        if room.getRoomNumber() == number:
            if room.isBooked():
                print("Room already booked.")
                return
            room.setGuestName(input("Enter guest name: "))
            room.bookRoom()
            print("Room booked successfully.")
            return

    print("Room not found.")


def checkoutRoom():
    number = int(input("Enter room number to checkout: "))

    for room in allRooms:
        if room.getRoomNumber() == number:
            if not room.isBooked():
                print("Room is not booked.")
                return
            room.checkoutRoom()
            print("Checkout completed successfully.")
            return

    print("Room not found.")


def displayRooms():
    if not allRooms:
        print("No rooms available.")
        return

    for room in allRooms:
        room.display()


def main():
    while True:
        print("\n===== Hotel Management System =====")
        print("1. Add Room")
        print("2. Book Room")
        print("3. Checkout Room")
        print("4. Display All Rooms")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            addRoom()
        elif choice == 2:
            bookRoom()
        elif choice == 3:
            checkoutRoom()
        elif choice == 4:
            displayRooms()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


main()
