computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games_sorting = sorted(computer_games)
for i in range(len(computer_games_sorting)):
    print(f"{i}. {computer_games_sorting[i]}")
