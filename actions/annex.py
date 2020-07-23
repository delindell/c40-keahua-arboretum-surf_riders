import os
from environments import River
def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Mountain")
    print("2. Swamp")
    print("3. Grassland")
    print("4. Forest")
    print("5. River")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass

## Expected output

# 1. Mountain
# 2. Swamp
# 3. Grassland
# 4. Forest
# 5. River

# Choose what you want to annex.
# > _