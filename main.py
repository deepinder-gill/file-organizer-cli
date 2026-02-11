import os
import shutil

class file_handling():

  def select(self):
    try:
      user_intention = int(input("1. Organize a folder\n2. Exit\n\nEnter your choice: [1/2]"))
      if user_intention in (1, 2):
        return user_intention
      else:
        print("please choose between [1/2]:")
    except ValueError:
      print("PLEASE CHOOSE BETWEEN [1/2] FOR PROGRAM TO EXECUTE")
  
  def exit(self):
    while True:
      _exit = input("are you sure you want to exit?[y/n]")
      if _exit in ("y", "n"):
        return _exit
      else:
        print("INVALID CHOICE!!")

  def organize_a_folder(self):
    while True:
      try:
        file_type = { "DOCUMENTS": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"], "IMAGES": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"], "AUDIO": [".mp3", ".wav", ".aac", ".flac"], "VIDEO": [".mp4", ".mkv", ".avi", ".mov"], "ARCHIVE": [".zip", ".rar", ".7z", ".tar", ".gz"], "CODE": [".py", ".js", ".java", ".cpp", ".html", ".css", ".json"], "EXECUTABLES": [".exe", ".msi", ".apk", ".sh"] }
        organize_mode = int(input("Select Mode:\n1. Proceed with Organization\n2. Exit()\n[1 or 2]"))
        if organize_mode == 1:
          folder_path = input("Enter The Directory's Path: ")
          if  os.path.isdir(folder_path):
            files = os.listdir(folder_path)
            for file in files:
              moved = False
              extension = os.path.splitext(file)[1].lower()
              for folder_name, extensions in file_type.items():
                if extension in extensions:
                  file_to_move = file
                  file_path = os.path.join(folder_path, file_to_move)
                  if not os.path.isfile(file_path):
                    continue
                  move_to = os.path.join(folder_path, folder_name)
                  os.makedirs(move_to, exist_ok=True)
                  shutil.move(file_path, move_to)
                  print(f"{file_path} moved to {move_to}")
                  moved = True
                  break
                
              if not moved :
                move_to = os.path.join(folder_path, "UNKNOWN")
                os.makedirs(move_to, exist_ok=True)
                shutil.move(file_path, move_to)

          elif os.path.isfile(folder_path):
            print("Please enter the path to a folder or directory!")

          else:
            print("invalid folde_path !!")

        if organize_mode == 2:
          ask = input("sure? [y/n]")
          if ask in ("y",  "n") and ask == "y":
            break

          elif ask in ("y",  "n") and ask == "n":
            continue

          else:
            print("INVALID CHOICE")

      except ValueError:
        print("Please choose between [1/2]")
         

def main():
  print("Welcome to File Organizer CLI\n-----------------------------------------------")
  f_h = file_handling()
  while True:
    user_decision = f_h.select()
    if user_decision == 1:
      f_h.organize_a_folder()
    
    if user_decision == 2:
      end = f_h.exit()
      if end == "y":
        print("THANKYOU FOR USING OUR SERVICE\n------------------------------------------------------")
        break
if __name__ == "__main__":
  main()
