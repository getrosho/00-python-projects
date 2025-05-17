import sqlite3

con = sqlite3.connect('youtube_video.db')

cur = con.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
            ''')

def list_all_videos():
   cur.execute("SELECT * FROM videos")
   for row in cur.fetchall():
      print(row)

def add_video(name, time):
   cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
   con.commit()

def update_video(id, name, time):
   cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
   con.commit()

def delete_video(id):
   cur.execute("DELETE FROM videos WHERE id = ? ", (id,))
   con.commit()

def main():
    while True:
        print("\n Youtube Video Manager | Choose an option")
        print("1. List all saved YouTube videos")
        print("2. Add a new YouTube video")
        print("3. Update an existing YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
    
        match choice:
            case '1':
                list_all_videos()

            case '2':
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                add_video(name, time)


            case '3':
                id = input('Enter video ID: ')
                name = input('Enter video name: ')
                time = input('Enter video time: ')
                update_video(id, name, time)

            case '4':
                id = input('Enter video ID: ')
                delete_video(id) 
                
            case '5':
                break
            
            case _:
                print('Invalid input')
    con.close()

if __name__ == "__main__":
   main()
