import pyglet
import os
from colorama import Fore

while True:
    i = os.listdir()

    # удаление по индексу
    e = i.index('main.py')
    ii = i.pop(e)

    for o in i:
        print(Fore.GREEN + o)

    a = input(Fore.BLUE + 'name:')
    if a + '.mp3' in i:
        index = i.index(a + '.mp3')

        song = pyglet.media.load(i[index])
        player = pyglet.media.Player()
        player.queue(song)

        # Воспроизведите песню
        player.play()

        is_paused = False  # Флаг, который показывает, находится ли песня на паузе

        while True:
            pause = input('command:')
            if pause.lower() == 'yes':
                if not is_paused:
                    player.pause()
                    is_paused = True
            elif pause.lower() == 'no':
                if is_paused:
                    player.play()
                    is_paused = False
            elif pause == 'music':
                break
        continue
    else:
        print(Fore.RED + 'Песня не найдена.')
