# Social Media Content Downloader
import instaloader as il
import pyttsx3
import os
from pytube import YouTube
import youtube_dl
os.system("cls")
engine = pyttsx3.init()
sound = engine.getProperty('voices')
engine.setProperty('voice', sound[0].id)
# --------------------------------------
# Instagram Profile Picture Downloader
# --------------------------------------
def Instagram():
    try:
        _extracted_from_Instagram_3()
    except il.ProfileNotExistsException as e:
        print("\033[01;31m Username does not exist :x:")
        engine.say("Username does not exist ")
        engine.runAndWait()
    except il.ConnectionException as e:
        print("\033[01;31m Connection Error :fire:")
def _extracted_from_Instagram_3():
    ig = il.Instaloader()
    user = input("\033[01;36m Enter Username :bust_in_silhouette:: ").strip()
    ig.download_profile(user, profile_pic_only=True)
    engine.say("Profile Picture Downloaded")
    engine.runAndWait()
    print("\033[01;32m Downloaded Profile Picture :heavy_check_mark:")
# ----------------------------------------
# Instagram Photos and Videos Downloader
# ----------------------------------------
def Instagram_Reels():
    try:
        _extracted_from_Instagram_4()
    except il.ProfileNotExistsException as e:
        print("\033[01;31m Username does not exist :x:")
        engine.say("Username does not exist ")
        engine.runAndWait()
    except il.ConnectionException as e:
        print("\033[01;31m Connection Error :fire:")
def _extracted_from_Instagram_4():
    ig = il.Instaloader()
    user = input("\033[01;36m Enter Username :bust_in_silhouette:: ").strip()
    ig.download_profile(user, profile_pic_only=False)
    engine.say(f"{user} - All Photos and Videos Downloaded")
    engine.runAndWait()
    print("\033[01;32m All Photos and Videos Downloaded :heavy_check_mark:")
# -----------------------------------
# Youtube Videos Downloader
# -----------------------------------
def Youtube_Video():  # sourcery skip: extract-duplicate-method
    url = input("\033[01;32mEnter Youtube Video URL: ").strip()
    try:
        yt = YouTube(url)
        print(f"YouTube Video Title::point_right: {yt.title}")
        print(f"YouTube Video Thumbnail Image Link::point_right: {yt.thumbnail_url}")
    except Exception:
        print("\033[01;31m Invalid URL :x:")
        engine.say("Invalid URL ")
        engine.runAndWait()
    try:
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("\033[01;32m Video was Downloaded successfully  :heavy_check_mark:")
    except Exception:
        print("\033[01;31mDownload Failed :x:")
        engine.say("Download Failed ")
        engine.runAndWait()
def main():
    print("""\033[01;36mChoose Options, Like Type '1' and then hit enter!
          \033[01;36m \n1::point_right: Download Instagram Profile
          \033[01;35m \n2::point_right: Download Instagram Photos and Videos
          \033[01;33m \n3::point_right: Download Instagram Stories
          \033[01;31m \n4::point_right: Download Youtube Videos, Title and Thumbnail
          \033[01;35m \nq::point_right: Quit\n""")
    options = {
        '1': Instagram,
        '2': Instagram_Reels,
        '3': Instagram,
        '4': Youtube_Video
    }
    while True:
        try:
            User = input('\033[01;36mChoose Options and Hit enter: ').strip()
            if User in options:
                options[User]()
            elif User.lower() in ['q', 'qq', 'exit']:
                engine.say("Thanks for using! ")
                engine.runAndWait()
                print("\n \033[01;36m Thanks! :wink:")
                break
            else:
                print(
                    "\n \033[01;31m Thanks! But Sorry Please try again another command\n")
        except KeyboardInterrupt:
            print("\n \033[01;31m Exit!\n")
            break
if __name__ == "__main__":
    main()
