
current_anime = {'One Piece': '11:00am',
                 'Naruto': '1:00pm',
                 'Bleach': '3:00pm',
                 'JJK': '5:00pm'}

print("We're showing the following movies")
for key in current_anime:
    print(key)
anime = input('What anime would you like the showtime for?\n')

showtime = current_anime.get(anime)

if showtime == None:
    print("Requested anime isn't playing")
else:
    print(anime, 'is playing at', showtime)