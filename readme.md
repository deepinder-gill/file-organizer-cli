# 📂 File Organizer CLI

A simple command-line tool built with Python that automatically organizes files in a directory into categorized folders based on their extensions.

---

## 🚀 Features

- Organizes files into categories:
  - Documents
  - Images
  - Audio
  - Video
  - Archives
  - Code
  - Executables
  - Unknown
- Automatically creates folders if they don’t exist
- Skips non-file entries
- Simple interactive CLI interface

---

## 🛠️ Tech Used

- Python
- `os` module
- `shutil` module

---

## 📌 How It Works

1. User provides the path to a folder.
2. The program scans all files in the directory.
3. Files are moved into categorized subfolders based on file extension.

---

## ▶️ How To Run

```bash
python main.py
```

(Ensure Python 3.x is installed.)

---

## ⚠️ Project Status

This project is built for learning purposes and can be further improved with:

- Duplicate file handling
- Logging system
- Custom organization rules
- Dry-run mode
- Error handling improvements

---

## 📚 What I Learned

- Working with file systems using `os`
- Moving files using `shutil`
- Handling user input in CLI applications
- Writing cleaner and more maintainable code