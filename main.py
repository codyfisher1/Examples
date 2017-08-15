from player import Player

def comparePlayerToOthers(player, players):
    
    print("Comparing " + player.name + " on team " + player.team + " to others")
    for p in players:
        if player.team != p.team:
            print(p.name, p.skill, p.team)

if __name__ == "__main__":

    corbin = Player("Corbin", 10, "A")
    cody = Player("Cody", 0, "A")
    alex = Player("Alex", -100, "B")
    kyle = Player("Kyle", 0, "B")

    players = [corbin, cody, alex, kyle]

    comparePlayerToOthers(corbin, players)


