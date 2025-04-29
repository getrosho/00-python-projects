import json

my_file = 'Youtube.txt'
def load_data():
  try:
    with open(my_file, 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_helper_func(videos):
  with open(my_file, 'w') as file:
    json.dump(videos, file)

def list_all_videos(videos):
  print("\n")
  print("*" * 50)
  for index, video in enumerate(videos, start = 1):
    print(f"{index}. {video['name']}, Duration: {video['time']} ")
  print("*" * 50)
  print("\n")

def add_new_video(videos):
  video_name = input("Enter video name: ")
  video_time = input("Enter video time: ")
  videos.append({'name':video_name, 'time':video_time})
  save_helper_func(videos)

def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to update: "))
  if 1 <= index <= len(videos):
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[index-1] = {'name': name, "time": time }
    save_helper_func(videos)
  else:
    print("Invalid video number")

def delete_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to delete: "))
  if 1 <= index <= len(videos):
    del videos[index-1]
    save_helper_func(videos)
  else:
    print("Invalid video number")

def main():
  videos = load_data()
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
        list_all_videos(videos)

      case '2':
        add_new_video(videos)

      case '3':
        update_video(videos)
      
      case '4':
        delete_video(videos)
      
      case '5':
        break

      case _:
        print("Invalid choice")

if __name__ == "__main__":
  main()