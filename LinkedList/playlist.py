# Basic Song playlist using LinkedList
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Node:
    def __init__(self, song, prev=None, next=None):
        self.song = song
        self.prev = prev
        self.next = next


class Playlist:
    def __init__(self):
        self.start = None

    def add_song(self, title, artist, duration):
        new_song = Song(title, artist, duration)
        new_node = Node(new_song)
        if self.start:
            new_node.prev = self.start.prev
            new_node.next = self.start
            self.start.prev.next = new_node
            self.start.prev = new_node
            self.start = new_node
        else:
            new_node.next = new_node
            new_node.prev = new_node
            self.start = new_node

    def play_song(self):
        if self.start:
            print(
                f"\n>> Now Playing: '{self.start.song.title}' by {self.start.song.artist}")
        else:
            print("Playlist is empty!")

    def prev_song(self):
        if self.start:
            print(f"\n>> Skipping: {self.start.song.title}!")
            self.start = self.start.prev
            self.play_song()
        else:
            print("No song to skip!")

    def next_song(self):
        if self.start:
            print(f"\n>> Skipping: {self.start.song.title}!")
            self.start = self.start.next
            self.play_song()
        else:
            print("No song to skip!")

    def show_playlist(self):
        current = self.start
        while current:
            print(f"SONG NAME: {current.song.title}")
            print(f"ARTIST: {current.song.artist}")
            print(f"DURATION: {current.song.duration}\n")
            current = current.next
            if current == self.start:
                break


def inbuilt_playlist(my_playlist):
    my_playlist.add_song("It's You", "Ali Gatie", "3:32")
    my_playlist.add_song("Lie to me", "Ali Gatie", "2:57")
    my_playlist.add_song("Moonlight", "Ali Gatie", "3:48")
    my_playlist.add_song("Let It Go", "Fotty Seven", "2:22")
    my_playlist.add_song("I Don't Miss That Life", "Seedhe Maut", "2:54")
    my_playlist.add_song("Strangers Again", "Ali Gatie", "2:44")


def menu():
    print("\n---------------------------------------------------")
    print("Welcome to my Song Playlist!\n")
    print("Please select an action --> [1/2/3/4/5/6]\n")
    print("1. Play Song \t\t[1]")
    print("2. Add Song \t\t[2]")
    print("3. Previous Song \t[3]")
    print("4. Next Song \t\t[4]")
    print("5. Show Playlist \t[5]")
    print("6. Exit \t\t[6]\n")


if __name__ == "__main__":
    import time
    import sys
    my_playlist = Playlist()
    inbuilt_playlist(my_playlist)

    while True:
        menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                my_playlist.play_song()
            elif choice == 2:
                song_title = input("\nEnter Song Title: ").title()
                song_artist = input("Enter Song Artist: ").title()
                song_duration = input("Enter Song Duration (0:00): ")
                my_playlist.add_song(song_title, song_artist, song_duration)
                print("\n---------------------------")
                print("Song Added successfully!")
                print("---------------------------\n\n")
            elif choice == 3:
                my_playlist.prev_song()
            elif choice == 4:
                my_playlist.next_song()
            elif choice == 5:
                print("\n---------------------------")
                print("\tYour Playlist")
                print("---------------------------")
                my_playlist.show_playlist()
                print("---------------------------\n\n")
                time.sleep(1)
            elif choice == 6:
                print("Exiting. . .")
                time.sleep(1)
                sys.exit()
            else:
                raise ValueError("Please enter a valid input [1/2/3/4/5/6]")

        except Exception as err:
            print(f"\nSomething unexpected occurred: {str(err)}\n")
