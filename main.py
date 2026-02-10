class file_handling():

  def select(self):
    user_intention = input("1. Organize a folder\n2. Preview changes\n3. Exit\n\nEnter your choice: ")
    return user_intention


def main():
  print("Welcome to File Organizer CLI\n-----------------------------------------------")
  f_h = file_handling()
  user_decision = f_h.select()
  print(user_decision)



main()