class VideoPlayerMixin:
    def playVideo(self, videoName):
        print(f'Мы проигрываем видео {videoName}')

class MusicPlayerMixin:
    def playMusic(self, songName):
        print(f'Мы проигрываем музыку {songName}')

class  PrintSomething:
    def printSomething(self, text):
        print(f'Мы печатаем {text}')

class PlugHeadPhonejackMixin:
    def headPhoneJack(self, headphoneName):
        print(f'{headphoneName}')

class Computer(VideoPlayerMixin,MusicPlayerMixin,PrintSomething,PlugHeadPhonejackMixin):
    pass

class Tablet:
    def __init__(self, modelTablet):
        pass

    def tabletDisplay(self):
        pass

class Phone(Tablet, VideoPlayerMixin ,MusicPlayerMixin,PrintSomething):
    def __init__(self, sizePhone, modelTablet):
        self.sphone = sizePhone
        super().__init__(modelTablet)

class TvStation(VideoPlayerMixin,MusicPlayerMixin):
    pass

class RadioStation(MusicPlayerMixin):
    pass

iphone  = Phone()
samsungTv = TvStation()
appleMacbook = Computer()
sonyWalkman = RadioStation()

iphone.printSomething('adsasd')
samsungTv.playMusic('Eminem')
sonyWalkman.playMusic('E Presley')

