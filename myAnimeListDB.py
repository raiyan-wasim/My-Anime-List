import sqlite3
import time

conn = sqlite3.connect("animes.db")

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS animes (
               id INTEGER PRIMARY KEY,
               anime TEXT NOT NULL,
               rating TEXT NOT NULL
    )
''')

def list_all_anime():
    print("\n")
    print("*" * 100)
    print("\n")
    print("Your Current ANIME List: \n")
    time.sleep(1)
    cursor.execute("SELECT * FROM animes")
    rows = cursor.fetchall()
    for row in rows:
        anime_id, anime_name, anime_rating = row
        print(f"{anime_id}. {anime_name}   {float(anime_rating)}")
        
    time.sleep(1)
    print("\n")
    print("^" * 20,"Feel Free To Edit ", "^" * 20)
    print("\n")

def add_anime(anime, rating):
    print("\nAdding anime to list...")
    time.sleep(0.4)
    cursor.execute("INSERT INTO animes (anime,rating) VALUES (?,?)", (anime, rating))
    print("\n")
    print("^" * 20,"Anime added Sucessfully","^" * 20)
    print("\n")
    conn.commit()

def update_anime(anime_id, new_anime, new_rating):
    time.sleep(0.4)
    print("Updating...")
    cursor.execute("UPDATE animes SET anime = ?, rating = ? WHERE id = ?", (new_anime,new_rating, int(anime_id)))
    print("\nAnime Updated Sucessfully\n")
    conn.commit()

def update_anime_rating(anime_id, new_rating):
    time.sleep(0.4)
    print("Updating...")
    cursor.execute("UPDATE animes SET rating = ? WHERE id = ?", (new_rating, int(anime_id)))
    print("\nRating Updated Sucessfully\n")
    conn.commit()

def delete_anime(anime_id):
    print("Deleting...")
    time.sleep(0.4)
    cursor.execute("DELETE FROM animes WHERE id = ?", (int(anime_id),))
    print("\nDeleted Sucessfully\n")
    conn.commit()


def main():
    while True:

        print("My Anime List\n")
        print("1. List all your Animes")
        print("2. Add an Anime")
        print("3. Update Anime")
        print("4. Update Anime Rating")
        print("5. Delete an Anime")
        print("6. Exit the app")
        choice = input("\nEnter your choice: ")

    
        match choice:
                case "1":
                    list_all_anime()

                case "2":
                    anime = input("Enter Anime: ")
                    rating = input("Enter Rating: ")
                    add_anime(anime,rating)

                case "3":
                    list_all_anime()
                    anime_id = input("Enter anime ID: ")
                    anime = input("Enter Anime: ")
                    rating = input("Enter Rating: ")
                    update_anime(anime_id,anime,rating)

                case "4":
                    list_all_anime()
                    anime_id = input("Enter anime ID: ")
                    new_rating = input("Enter Rating: ")
                    update_anime_rating(anime_id, new_rating)

                case "5":
                    list_all_anime()
                    anime_id = input("Enter anime ID: ")
                    delete_anime(anime_id)

                case "6":
                    break
            
                case _:
                    print("INVALID CHOICE")

    conn.close()

if __name__ == "__main__":
    main()