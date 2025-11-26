
computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

posortowane = sorted(computer_games)
liczba = 1
for gra in posortowane:
    print(f"{liczba} {gra}")
    liczba += 1