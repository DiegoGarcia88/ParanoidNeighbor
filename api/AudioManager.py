import pygame
import random

class AudioManager(object):
    
    mInstance = None
    mInitialized = False
    mChannels = 8

    def __new__(self,*args,**kargs):
        if(AudioManager.mInstance is None):
            AudioManager.mInstance = object.__new__(self,*args,**kargs)
            self.init(AudioManager.mInstance)
        else:
            print("Careful, AudioManager() shouldnt be instance more than once, please use AudioManager.inst()")
        return AudioManager.mInstance

    @classmethod

    def inst(cls):
        if(not cls.mInstance):
            return cls()
        return cls.mInstance

    def init(self):
        if (AudioManager.mInitialized):
            return
        else:
            AudioManager.mInitialized = True
            AudioManager.mChannels = pygame.mixer.get_num_channels()
        self.mArray = []
        self.SONG_END = pygame.USEREVENT + 1

    def play(self, aSound, aLoop = 0, aMaxTime = 0, aFadeMs = 0):
        AudioManager.inst().get_channel().play(aSound, aLoop, aMaxTime, aFadeMs)

    def setSongEnd(self):
        pygame.mixer.music.set_endevent(self.SONG_END)

    def playRandom(self):
        pygame.mixer.music.load(self.mArray[random.randint(0, 1)])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(1)

    def loadSongs(self, aArray):
        self.mArray = aArray

    def get_channel(self):
        c = pygame.mixer.find_channel(True)
        while (c is None):
            AudioManager.mChannels += 1
            pygame.mixer.set_num_channels(AudioManager.mChannels)
            c = pygame.mixer.find_channel()
        return c

    def destroy(self):
        AudioManager.mInstance = None
            
