class CityExperience:
    def __init__(self):
        self.city = ["Delhi", "Lakshadweep", "Leh", "Gokharna", "Srinagar", "Havelock", "Pondicherry", "Goa", "Manali", "Amritsar", "Ujjain", "Auli", "Pondicherry", "Mount Abu"]

    def welcome_to_city(self, user_city):
        if user_city in self.city:
            print("Welcome to", user_city)
            return True
        else:
            print("Sorry, we don't have information about this city.")
            return False

class CityPlace:
    def __init__(self):
        self.places = ["Hotel", "Park", "Club"]

    def choose_place(self, user_place):
        if user_place in self.places:
            print("Welcome to", user_place)
            return True
        else:
            print("Sorry, we don't have information about this place.")
            return False

class Hotel:
    def __init__(self):
        self.rooms = ["Hollywood Twin Room", "Suite / Executive Suite", "Murphy Room", "Cabana", "Villa"]

    def choose_room(self, user_room):
        if user_room in self.rooms:
            print("Welcome to", user_room)
            return True
        else:
            print("Sorry, this room is not available.")
            return False

    def choose_colors(self):
        hollywood_room_colors = ["Red", "Yellow", "Blue"]
        suite_colors = ["Blue", "Yellow", "Black"]
        murphy_room_colors = ["Pink", "Red", "Brown"]

        user_choice1 = input("Enter your first color choice: ")
        user_choice2 = input("Enter your second color choice: ")

        if user_choice1 in hollywood_room_colors and user_choice2 in suite_colors:
            if user_choice1 == user_choice2:
                print("You win!")
            else:
                print("Sorry, try again.")
        else:
            print("Invalid color choices. Please choose again.")

class Park:
    def __init__(self):
        self.areas = ["Gardens", "Ponds or Lakes", "Shaded Areas", "Picnic Area", "Walking/Jogging Trails"]

    def choose_area(self, user_area):
        if user_area in self.areas:
            print("Welcome to", user_area)
            return True
        else:
            print("Sorry, this area is not available.")
            return False

    def choose_colors(self):
        park_area_colors = ["Red", "Yellow", "Blue"]
        pond_area_colors = ["Blue", "Yellow", "Black"]
        shaded_area_colors = ["Pink", "Red", "Brown"]

        user_choice1 = input("Enter your first color choice: ")
        user_choice2 = input("Enter your second color choice: ")

        if user_choice1 in park_area_colors and user_choice2 in pond_area_colors:
            if user_choice1 == user_choice2:
                print("You win!")
            else:
                print("Sorry, try again.")
        else:
            print("Invalid color choices. Please choose again.")

class Club:
    def __init__(self):
        self.rooms = ["Main Dance Floor", "VIP Lounge", "Bar Area", "Outdoor Patio", "Private Rooms"]

    def choose_room(self, user_room):
        if user_room in self.rooms:
            print("Welcome to", user_room)
            return True
        else:
            print("Sorry, this room is not available.")
            return False

    def choose_colors(self):
        dance_floor_colors = ["Red", "Yellow", "Blue"]
        vip_lounge_colors = ["Blue", "Yellow", "Black"]
        bar_area_colors = ["Pink", "Red", "Brown"]

        user_choice1 = input("Enter your first color choice: ")
        user_choice2 = input("Enter your second color choice: ")

        if user_choice1 in dance_floor_colors and user_choice2 in vip_lounge_colors:
            if user_choice1 == user_choice2:
                print("You win!")
            else:
                print("Sorry, try again.")
        else:
            print("Invalid color choices. Please choose again.")

def main():
    user_city = input("Enter a city: ")
    city_exp = CityExperience()

    if city_exp.welcome_to_city(user_city):
        user_place = input("Enter a place (Hotel/Park/Club): ")
        city_place = CityPlace()

        if city_place.choose_place(user_place):
            if user_place == "Hotel":
                user_room = input("Enter a room: ")
                hotel = Hotel()

                if hotel.choose_room(user_room):
                    hotel.choose_colors()

            elif user_place == "Park":
                user_area = input("Enter an area: ")
                park = Park()

                if park.choose_area(user_area):
                    park.choose_colors()

            elif user_place == "Club":
                user_room = input("Enter a room: ")
                club = Club()

                if club.choose_room(user_room):
                    club.choose_colors()

if __name__ == "__main__":
    main()
