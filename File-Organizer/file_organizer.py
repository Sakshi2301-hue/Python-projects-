import os
import shutil


def organize_files(folder_path):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".mkv", ".avi"]
    }

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            extension = os.path.splitext(item)[1].lower()

            folder_name = "Others"

            for category, extensions in file_types.items():
                if extension in extensions:
                    folder_name = category
                    break

            destination_folder = os.path.join(folder_path, folder_name)

            os.makedirs(destination_folder, exist_ok=True)

            shutil.move(
                item_path,
                os.path.join(destination_folder, item)
            )


def main():
    folder_path = input("Enter folder path: ")

    try:
        organize_files(folder_path)
        print("Files organized successfully!")
    except FileNotFoundError:
        print("Folder not found!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
