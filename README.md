# Warning Bell

## How to setup WarningBell

Maker sure that `/etc/rc.local` contains the line `sh /home/pi/warning_bell/warn_on_schedule.py` (or whatever the path is)

## How to use WarningBell

It runs on a preset schedule, so you needn't do anything on days with normal schedules.

## Changing the bell schedule

The schedule can be changed in `warn.py`

Leave custom_schedule = False if you want to use the normal schedules

The schedule is an array of military times as strings.

You can set a custom schedule by defining this array. For example `custom_schedule = ['8:40','9:30','10:15','11:00','11:45','13:05','13:55','14:40']`

You can also set custom_schedule to one of the following: [default_schedule, block_schedule, event_block_schedule, late_block_schedule, no_schedule]. For example `custom_schedule = event_block_schedule`

