import webbrowser
import time
class Video:
    def __init__(self,title="",link=""):
        self.title = title
        self.link = link
class Playlist:
    def __init__(self,name, description,rating,video):
        self.name = name
        self.description = description
        self.rating = rating
        self.video = video
def make_video():
    title = input("Enter title: ")
    link = input("Enter link: ")
    video = Video(title,link)
    return video
def make_videos(total):
    list_videos=[]
    for i in range(total):
        print("Enter video " + str(i+1) + ": ")
        list_videos.append(make_video())
    return list_videos
def write_to_file(f,list_video):
    for i in range (len(list_video)):
        f.write(list_video[i].title + "\n")
        f.write(list_video[i].link + "\n")
def export_list_videos(f):
    list_videos = []
    while True:
        line = f.readline()
        if not line:
            break
        else:
            title = line.strip()
            link = f.readline().strip()
            list_videos.append(Video(title,link))
    return list_videos
def print_file_videos(list_videos):
    print("List video: ")
    for i in range(len(list_videos)):
        print("Video "+ str(i+1) + ": ")
        print("Video title: " + list_videos[i].title)
        print("Video link: " + list_videos[i].link)
        
# Play lits {Name, description, video inf}
def make_playlist(total):
    name = input("Enter name playlist: ")
    des = input("Enter description: ")
    rating = input("Rating (1-5): ")
    video = make_videos(total)
    playlist = Playlist(name,des,rating,video)
    return playlist 

def write_playlist_to_file(playlist):
    with open("data.txt","w") as f:
        f.write(playlist.name + "\n")
        f.write(playlist.description + "\n")
        f.write(playlist.rating + "\n")
        write_to_file(f,playlist.video)
def export_playlist():
    with open("data.txt","r") as f:
        name = f.readline().strip()
        des = f.readline().strip()
        rating = f.readline().strip()
        video = export_list_videos(f)
        playlist = Playlist(name,des,rating,video)
    return playlist
def print_playlist(playlist):
            print("Name playlist: " + playlist.name)
            print("Description playlist: " + playlist.description)
            print("Rating playlist: " + playlist.rating)
            print_file_videos(playlist.video)
def add_video(playlist):
    num_add = int(input("Enter numbers video want to add: "))
    try:
        playlist.video.extend(make_videos(num_add))
        print("Add videos successful")
    except:
        print("Error")
def delete_video(playlist):
    num_del = int(input("Enter position video want to delete: "))
    try:
        playlist.video.pop(num_del - 1)
        print("Delete successful")
    except:
        print("Error")

def menu():
    print("___________________________")
    print("1. Create playlist.")
    print("2. Show playlist.")
    print("3. Play a video.")
    print("4. Add a video.")
    print("5. Delete video")
    print("6. Save and Exit")
    print("___________________________")
    
def selection(form, min, max):
    choice = input(form)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(form)
    choice = int(choice)
    return choice
def play_video(playlist):
    # chọn bài
    print_file_videos(playlist.video)
    total = len(playlist.video)
    choice = selection("Select a video (1, " + str(total) + "): ", 1, total )
    # Mở link
    webbrowser.open(playlist.video[choice - 1].link)
def main():
    while True:
        menu()
        choice = selection("Select an option (1-7): ", 1, 6)
        if choice == 1:
            total = int(input("Enter the number videos: "))
            playlist = make_playlist(total)
            write_playlist_to_file(playlist)
        elif choice == 2:
            try:
                print_playlist(playlist.video)
            except:
                print_playlist(export_playlist())
            
        elif choice == 3:
            try:# kiểm tra playlist có được khởi tạo không
                play_video(playlist)
            except:
                # chép video sang 1 list
                playlist = export_playlist()
                # Chạy như bth
                play_video(playlist)
        elif choice == 4:
            add_video(playlist)
        elif choice == 5:
            delete_video(playlist)
        elif choice == 6:
            write_playlist_to_file(export_playlist())
            print("Successful")
            break
main()