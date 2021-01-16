class Room:

    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.guests = []
        self.playlist = []
        # extensions
        self.capacity = capacity
    
    def check_in_guest(self, guest):
        # extension
        if len(self.guests) <= self.capacity:
            self.guests.append(guest)
            return "Welcome! Enjoy your time."
        else:
            return f"Sorry, this room cannot accomodate more than {self.capacity} guests. Try another room."
            
    def check_out_guest(self, guest):
        self.guests.remove(guest)
    
    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)
    
    def check_capacity(self):
        return self.capacity
    
    def check_occupancy(self):
        return len(self.guests)