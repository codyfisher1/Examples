

def ComparePlayer(player, players):
        #Iterates through list players
    
    ComparePlayer.StatList = []  
    #StatList.extend([player.position, player.first_name,  player.last_name])
            
        #Prints primary player comparison
        #print('Comparing ' + player.first_name + ' ' + player.last_name + '(' + player.position + ')' + ' on team ' + player.team  )
    for p in players:
        
            #sorts through players whos team doesnt equal to the primary players
        if player.team != p.team:
             
            #prints the list players information before exceuting comparison functions
            #print(p.position, p.first_name, p.last_name, p.team)
            
            #defines comparison functions
            off_adv = round(player.offense - p.offense,2)
            def_adv = round(player.defense - p.defense,2)
            overall_adv = round(player.overall - p.overall,2)
            commonstats_adv = round(player.commonstats - p.commonstats,2)
            shootingArea_adv = round(player.shootingArea - p.shootingArea,2)
            driving_adv = round(player.driving - p.driving,2)
            passing_adv = round(player.passing - p.passing,2)
            rebounds_adv = round(player.rebounds - p.rebounds,2)
            ballhandling_adv = round(player.ballhandling -p.ballhandling,2)
            MiscShooting_adv = round(player.MiscShooting - p.MiscShooting,2)
            Intelligence_adv = round(player.Intelligence - p.Intelligence,2)
            endurance_adv = round(player.endurance - p.endurance,2)
            speed_adv = round(player.speed - p.speed,2)
            Misc_adv = round(player.Misc - p.Misc,2)
            Experience_adv = round(player.Experience - p.Experience,2)
            Foulrating_adv = round(player.FoulRating - p.FoulRating,2)
            Total_Player_Adv = round(shootingArea_adv + driving_adv + passing_adv + rebounds_adv
            + ballhandling_adv + MiscShooting_adv + Intelligence_adv + endurance_adv
            + speed_adv + Misc_adv + Experience_adv + Foulrating_adv,2)

            ComparePlayer.StatList.extend([off_adv, def_adv, overall_adv, commonstats_adv, shootingArea_adv,
            driving_adv, passing_adv, rebounds_adv, ballhandling_adv, MiscShooting_adv, Intelligence_adv
            ,endurance_adv,speed_adv,Misc_adv,Experience_adv, Foulrating_adv,Total_Player_Adv])

            
            
            #prints out the values of the comparison funtions for the UI
            #print('     Total Player Advantage: '+ str(round(Total_Player_Adv,2)))
            #print('     Overall Advantage: ' + str(round(overall_adv,2)))
            #print('     Offenisive Advantage: ' + str(round(off_adv,2)))
            #print('     Defensive Advantage: ' + str(round(def_adv,2)))
            #print('     Common Statistics Advantage: '+ str(round(commonstats_adv,2)))
            #print('     Shooting Area Advantage: '+ str(round(shootingArea_adv,2)))
            #print('     Driving Advantage: '+ str(round(driving_adv,2)))
            #print('     Rebounds Advantage: '+ str(round(rebounds_adv,2)))
            #print('     Ball Handling Advantage: '+ str(round(ballhandling_adv,2)))
            #print('     Misc Shooting Advantage: '+ str(round(MiscShooting_adv,2)))
            #print('     Intelligence Advantage: '+ str(round(Intelligence_adv,2)))
            #print('     Endurance Advantage: '+ str(round(endurance_adv,2)))
            #print('     Misc Advantage: '+ str(round(Misc_adv,2)))
            #print('     Experience Advantage: '+ str(round(Experience_adv,2)))
            #print('     Foul Rating Advantage: '+ str(round(Foulrating_adv,2)))
        


def CompareTeams(Team_1, players):
    
    CompareTeams.PlayerStats = []
    for q in Team_1:
        
        
        ComparePlayer(q, players)
        StatAdd = ComparePlayer.StatList
        CompareTeams.PlayerStats.extend([StatAdd])
        