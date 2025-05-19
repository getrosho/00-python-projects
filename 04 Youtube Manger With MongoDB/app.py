from pymongo import MongoClient
from bson.objectid import ObjectId

# Bad practice: hardcoding sensitive information in the code. Use environment variables or a config file instead.
client = MongoClient("mongodb+srv://youtubewithmongo:youtubewithmongo@cluster0.hpvpj1m.mongodb.net/?retryWrites=true&w=majority")

db = client["youtube"]
video_collection = db["videos"]

# This is a simple YouTube video manager that allows you to list videos using MongoDB as the database.
def list_all_videos():
    videos = video_collection.find()
    print("\nSaved YouTube Videos:")
    for video in videos:
        print(f"ID: {video.get('_id')} | Name: {video.get('name')} | Time: {video.get('time')}")

# This function adds a new video to the database.
# It takes the video name and time as parameters.
def add_video(name, time):
    video = {"name": name, "time": time}
    result = video_collection.insert_one(video)
    print(f"Added video with id: {result.inserted_id}")

# This function updates an existing video in the database.
# It takes the video ID, name, and time as parameters.
def update_video(id, name, time):
    try:
        object_id = ObjectId(id)
    except Exception:
        print("Invalid ID format.")
        return
    result = video_collection.update_one(
        {"_id": object_id},
        {"$set": {"name": name, "time": time}}
    )
    if result.modified_count > 0:
        print("Video updated successfully.")
    else:
        print("No video found with the given ID or no changes made.")

# This function deletes a video from the database.
# It takes the video ID as a parameter.
def delete_video(id):
    try:
        object_id = ObjectId(id)
    except Exception:
        print("Invalid ID format.")
        return
    result = video_collection.delete_one({"_id": object_id})
    if result.deleted_count > 0:
        print("Video deleted successfully.")
    else:
        print("No video found with the given ID.")


# This is the main function that runs the app.
# It provides a menu for the user to choose an action.
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


if __name__ == "__main__":
  main()