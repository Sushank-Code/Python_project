import os,shutil

path = input ("Enter the path :")
files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]


    create = os.path.join(path,extension)     # C:\Users\namss\OneDrive\Desktop\Photo\jpg 

    if os.path.exists(create):
        shutil.move(os.path.join(path, file), os.path.join(create,file))
    else:
        os.makedirs(create)
        shutil.move(os.path.join(path, file), os.path.join(create,file))

        
