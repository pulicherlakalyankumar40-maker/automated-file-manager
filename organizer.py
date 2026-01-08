import os
import shutil
from datetime import datetime
filetypes ={
    'pdf':['.pdf'],
    'images':['.jpg', '.jpeg', '.png', '.gif', '.bmp',],
    'data':['.csv', '.xls', '.xlsx', '.json', '.xml']
}
def organize_files(directory):
    file_details = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            name, ext = os.path.splitext(file)
            ext = ext.lower()
            for folder, extensions in filetypes.items():
                if ext in extensions:
                    dest_folder = os.path.join(directory, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    date =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_name = f"{name}_{date}{ext}"
                    new_path = os.path.join(dest_folder, new_name)
                    new_file_path = os.path.join(dest_folder, file)
                    shutil.move(file_path, new_file_path)
                    size = os.path.getsize(new_file_path)
                    file_details.append([name, ext, size, date, dest_folder])
    return file_details