class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.guests = []
    
    def check_in_guest(self, guest):
        self.guests.append(guest)
