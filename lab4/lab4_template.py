import random

def read_songs_from_file(filename):
    try:
        with open(filename, "r") as file:
            songs = file.read().splitlines()
            return songs
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. \
              Are you sure you saved it in the correct spot?"
        )
        return []
    
def choose_random_song(songs):
        return random.choice(songs)


songs = read_songs_from_file("song_list.txt")
selected_songs = set() # set will automatically remove duplicates.
attempts = 12
 
# write some code selecting 12 songs for a set
# if a song is already chosen, it choses another one

while attempts > 0:
    setlist_song = choose_random_song(songs)
    print("song chosen: ", setlist_song)
    if setlist_song not in selected_songs:
        selected_songs.add(setlist_song)
        print ("adding song", attempts, setlist_song)
        attempts-= 1
    else:
        print("You already picked that song.")


if attempts == 0:
    print ("setlist complete")
    for i, song in enumerate(selected_songs):
        print(f"song # {i+1}: {song}")
  
