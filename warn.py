### Definition of default schedules
###################################

regular_schedule = ['9:30','10:15','11:00','11:45','13:05','13:55','14:40']
block_schedule = ['9:20','10:45','13:03','14:30']
event_block_schedule = ['9:05','11:45','13:25','14:40']
late_block_schedule = ['10:05','11:15','13:25','14:40']
no_schedule = []

### Set the Schedule Here
#########################

## The schedule is an array of military times as strings
## You can set a custom schedule by defining this array. For example custom_schedule = ['8:40','9:30','10:15','11:00','11:45','13:05','13:55','14:40']
## leave custom_schedule = False if you want to use the normal schedules
## You can also set custom_schedule to one of the following: [default_schedule, block_schedule, event_block_schedule, late_block_schedule, no_schedule

### Below this is the code, which doesn't need to be touched.
#############################################################

import os
import time
import datetime
import play_sound

def check_for_warning_time(dt):
  secs = dt.hour * 3600 + dt.minute * 60 + dt.second
  current = datetime.datetime.now()
  diff = secs - (current.hour * 3600 + current.minute * 60 + current.second)
  print(diff)
  if(diff < 120 and diff > 80):
    print("Warning")
    play_sound.play()
    return(1)

def check_schedule():
  schedule = determine_schedule()
  for t in schedule:
    dt = datetime.datetime.now()
    dt = dt.replace(hour=int(t.split(':')[0]), minute=int(t.split(':')[1]), second=0)
    check_for_warning_time(dt)
  return(1)

def default_schedule():
  return [block_schedule, block_schedule, block_schedule, block_schedule, block_schedule, no_schedule, no_schedule][datetime.datetime.today().weekday()]

def determine_schedule():
  f = open('/home/pi/warning_bell/schedule.txt','r')
  schedule_command = f.read().strip()
  if ':' in schedule_command:
    schedule = schedule_command.split(',')
  elif schedule_command == 'auto':
    schedule = default_schedule()
  else:
    schedule = {'regular': regular_schedule, 'block': block_schedule, 'event_block': event_block_schedule, 'late_block': late_block_schedule, 'none': no_schedule}[schedule_command]
  f.close()
  return schedule

print("Example Sound from Warning Bell")
play_sound.play('OldCarStarting.mp3')
while True:
  check_schedule()
  time.sleep(10)
