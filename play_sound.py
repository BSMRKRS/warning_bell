import sys
import os
import time

def play(file = 'AirHorn-SoundBiblecom-964603082.mp3', mute = True, unmute = True):
  if mute:
    os.system('amixer sset PCM mute')
  os.system('omxplayer --vol 100 -o local /home/pi/warning_bell/' + file) 
  if unmute:
    os.system('amixer sset PCM unmute')

if len(sys.argv) > 1:
  play('requests/door_bell.mp3', True, False)
  time.sleep(1)
  play('requests/' + sys.argv[1] + '.mp3', False, False)
  time.sleep(1)
  play('requests/' + sys.argv[1] + '.mp3', False, True)
  time.sleep(1)
