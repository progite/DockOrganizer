import shutil
import read_folder
import os
import sys
from bertopic import BERTopic

model = BERTopic.load("Model\Cluster_documents.h5")
model_labels = model.get_topic_info().Name

def topic_clustering(folder_path):
    #files contains filenames 
    #text cotains the file contents in the form of a list
    files, text = read_folder.read_folder_content(folder_path)
    
    #clustering files in input folder
    topic, _ = model.transform(text)

    #clustering files in new folders
    folder_path_tf = []
    for _ in range(len(files)):
        folder_path_tf.append([])

    for idx, file in enumerate(files):
        folder_path_tf[int(topic[idx])].append(file)

    print(model_labels)
    print(list(folder_path_tf))
    group_folder(folder_path, folder_path_tf)

def group_folder(folder_path_old, folder_path_tf):

    #if label has any element then move the files from current folder to a new folder
    for idx, fileList in enumerate(folder_path_tf):
        
        if fileList == []:
            continue

        #create new folder to move the documents according to clustering
        folder_path_new = os.path.join(folder_path_old, model_labels[idx])
        if not os.path.exists(folder_path_new):
            os.makedirs(folder_path_new)

        #move files in a cluster from current folder to new folder
        for file_name in fileList:
            old_path = os.path.join(folder_path_old, file_name)
            new_path = os.path.join(folder_path_new, file_name)
            # folder_path_new =  + cluster_folder
            shutil.move(old_path, new_path)

def main():
    folder_name = sys.argv[1]
    print(folder_name)
    topic_clustering(folder_name)
    # test()

if __name__ == '__main__':
    main()