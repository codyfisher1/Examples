class player:
    def __init__(self,first_name,last_name,position,team,offense,defense,overall,
    commonstats,shootingArea,driving,passing, rebounds,ballhandling, MiscShooting,
     Intelligence,speed, endurance, Misc, Experience, FoulRating ):
        
        #list of parameters that define a player
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team
        self.offense = offense
        self.defense = defense
        self.overall = overall
        self.commonstats = commonstats
        self.shootingArea = shootingArea
        self.driving = driving
        self.passing = passing
        self.rebounds = rebounds
        self.ballhandling = ballhandling
        self.MiscShooting = MiscShooting
        self.Intelligence = Intelligence
        self.endurance = endurance
        self.speed = speed
        self.Misc = Misc
        self.Experience = Experience
        self.FoulRating = FoulRating