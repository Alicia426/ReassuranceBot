import yaml
import glob
import os

def ensureDir():
    if os.getcwd().split("/")[-1] != 'user_data':
        os.chdir('user_data')

def fetchUser(id):
    ensureDir()
    for file in glob.glob("*.yml"):
        if file.replace(".yml",'') == id:
            #print(file, 'found')
            return file
    return None

def createUser(id,name,pronoun_dict):
    ensureDir()

def createStuffie(id,stuffie_name, stuffe_pronun_dict):
    ensureDir()


print(fetchUser("Alicia#9680"))
print(fetchUser("K"))