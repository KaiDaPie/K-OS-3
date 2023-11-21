import requests
import hashlib
import os

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        buffer = file.read(65536)  # 64 KB chunks
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(65536)
    return hasher.hexdigest()

def main():
    os.system('clear')
    file_url = "https://raw.githubusercontent.com/KaiDaPie/K-OS-3/main/Files/main.py"
    local_file_path = "main.py"

    if not os.path.exists(local_file_path):
        print("File is missing. Downloading file...")
        download_file(file_url, local_file_path)
        print("File downloaded successfully.")
    else:
        remote_hash = requests.get(file_url).headers['ETag'].replace('"', '')
        local_hash = calculate_file_hash(local_file_path)

        if remote_hash != local_hash:
            print("File is outdated. Downloading updated version...")
            download_file(file_url, local_file_path)
            print("File updated successfully.")
        else:
            print("File is up to date.")

if __name__ == "__main__":
    main()
