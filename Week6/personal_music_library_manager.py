# Exercise 1: Music Library Manager

# 1. Initialize Data Structures
# TODO: Create an empty list or dictionary to store your music library.

songs = []
genre_count = {}

print ("Welcome to Music Library Manager! Run by Giovanni Bouzari.")


# 2. Function to Add Music (5 songs) collect song name and genre using input()
# TODO: Define a function that takes music details (title, artist, genre, duration)

for i in range(1, 6):
    print(f"\nEnter Song {i}:")
    name = input(" Song Name: ")
    genre = input("  Genre: ")
    print()

# Store song as Tuple
    song_tuple = (name, genre)
    songs.append(song_tuple)

    # count genres
    genre_count[genre] = genre_count.get(genre, 0) + 1

# 3. Function to Display Music Library
# TODO: Define a function that prints all songs in the library in a formatted way.

print("\n=== YOUR MUSIC LIBRARY ===")
for i, (name, genre) in enumerate(songs, start = 1):
    print(f"{i}. {name} ({genre})")



# 4. Main Program Loop
# TODO: Implement a loop that allows the user to:

print("\n=== GENRE STATISTICS ===")
for g, count in genre_count.items():
    print(f"{g}: {count} songs")

    # Determine most popular genre
    most_popular = max(genre_count, key=genre_count.get)
    print(f"Most popular genre: {most_popular}")