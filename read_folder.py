import os

def read_file(file_path):
    file = open(file_path, "r")
    content = file.read()
    return content

def read_folder_content(folder_path):
    dir_list = os.listdir(folder_path)
    
    content = []
    files = []
    
    for file_name in dir_list:
        if '.' not in file_name:
            continue
        files.append(file_name)
        file_path = folder_path + "/" + file_name
        #considering text based files for analysis and clustering
        if file_name[file_name.index('.'):] in ['.txt', 'pdf']:
            content.append(read_file(file_path))
    return files, content