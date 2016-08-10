import re

re_number = re.compile('[0-9]+')

def greet():
    print("welcome to stone of the hearth! choose a class!\n")
    print("1. Warrior    2. Shaman    3. Rogue")
    print("4. Paladin    5. Hunter    6. Druid")
    print("7. Warlock    8. Mage      9. Priest")

# blank choice = 0. choice
def prompt_action( themax ):
    while True:
        command = input("\n> ")
        anumber = re_number.search(command)
        a = None

        if anumber:
            a = anumber.group(0)
            if (int(a) < 1 or int(a) > themax):
                continue
        if not a:
            return 0
        return int(a) - 1
