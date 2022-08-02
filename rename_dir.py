import os
path = os.chdir("light_backgrounds/")
i = 0 
for file in os.listdir(path):
    new_name ="pic{}.jpg".format(i)
    os.rename(file, new_name)
    i = i+1
