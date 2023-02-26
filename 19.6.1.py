violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
time_songs =[]
number_songs = int(input('Введите колличество песен:'))
for i in range(number_songs):
    song = input('Введите название песни:')
    time = violator_songs[song]
    time_songs.append(time)
print(round(sum(time_songs),2))