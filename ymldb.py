import yaml
import glob
import os


def fetchUser(id):
    print(id)
    for file in glob.glob("*.yml"):
        print(file,file.replace(".yml", ''))
        if file.replace(".yml", '') == id:
            print(file, 'found')
            return file

    return None


def fetchUserData(id):
    fn = fetchUser(id)
    print(fn)
    if fn != None:
        with open(fn) as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
            name = doc["name"]
            pronouns = doc["pronouns"]
            stuffie = doc["stuffie"]

            return (name, pronouns, stuffie)

    else:
        return "User not found, must be configured first"
    


def createUser(id, name, pronoun_dict):
    fn = id+".yml"
    user_dict = {
        "name": name,
        "pronouns": pronoun_dict,
        "stuffie":
        {
            'name': 'null',
            'pronouns':
                    {'sps': 'null', 'spo': 'null', 'sp': 'null', 'sr': 'null'}}
    }
    with open(fn, 'w') as f:
        yaml.dump(user_dict, f)


def createStuffie(id, stuffie_name, stuffe_pronun_dict):
    pass


# print(fetchUser("Alicia#9680"))
# print(fetchUser("K"))
#print(fetchUserData("Alicia#9680"))
#createUser("test#123", "TestGal", {
#           'sps': 'she', 'spo': 'her', 'sp': 'hers', 'sr': 'herself'})
