from player import Player

if __name__ == "__main__":

    corbin = Player("Corbin", 10)
    cody = Player("Cody", 0)
    alex = Player("Alex", -100)

    players = [corbin, cody, alex]

    #Iterate through player and print out their names
    for p in players:
        print (p.name)