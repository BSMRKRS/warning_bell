import sys
import os
import time

def play(file = 'AirHorn-SoundBiblecom-964603082.mp3', mute = False, unmute = False, vol = '100'):
  if mute:
    os.system('amixer sset Headphone mute')
  os.system('omxplayer --vol ' + str(vol) + ' -o local /home/pi/warning_bell/' + file) 
  if unmute:
    os.system('amixer sset Headphone unmute')
  return(1)

if len(sys.argv) > 1:
  play('requests/door_bell.mp3', True, False)
  time.sleep(1)
  play('requests/' + sys.argv[1] + '.mp3', False, False, 1000)
  time.sleep(1)
  play('requests/' + sys.argv[1] + '.mp3', False, True, 1000)
  time.sleep(1)
