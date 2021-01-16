class Room:

    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.guests = []
        self.playlist = []
        # extensions
        self.capacity = capacity
    
    def check_in_guest(self, guest):
        self.guests.append(guest)
    
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