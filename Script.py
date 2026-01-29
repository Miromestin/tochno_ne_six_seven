import time

def screen_setup():
    print('0' * 125)
    for _ in range(1, 50):
        print('')
    animation()

def animation():
    lyricNum = 1
    while True:
        for frameNum in range(1,51):
            with open('Frames/'+str(frameNum)+'.txt') as frame:
                print(frame.read())
            with open('Lyrics/'+str(lyricNum)+'.txt') as lyric:
                print(lyric.read())

            time.sleep(0.0417)

        if lyricNum < 7:
            lyricNum += 1
        else:
            lyricNum = 1

screen_setup()