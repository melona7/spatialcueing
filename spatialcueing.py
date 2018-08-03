# -*- coding: utf-8 -*-
"""
Posner cueing task
Modeled with PsychoPy 3.0.0 beta

Annie Nie
"""
from psychopy.visual import Window, TextStim, ShapeStim, Rect
from psychopy.event import waitKeys
from psychopy.core import wait
from random import shuffle
import matplotlib.pyplot as plt
import numpy

LOGFILE_NAME = input('Participant name: ')
LOGFILE = LOGFILE_NAME
# monitor resolution, adjust if necessary
DISPLAY_SIZE = (1280, 720)

# foreground and background colours
# black
BACKGROUND = (-1, -1, -1)
# gray
FOREGROUND = (0, 0, 0)

"""
monitor name for monitor calibration,
Import this information by simply specifying monitor
so that name in the script matches the name given in
the Monitor Center. Or, without standalone psychopy,
set monitor with the following:

from psychopy import monitors
my_monitor = monitors.Monitor(name="MONITOR_NAME")
my_monitor.setSizePix((1920, 1080))
my_monitor.setWidth(20)
my_monitor.setDistance(100)
my_monitor.saveMon()

"""
MONITOR_NAME = "testMonitor"

# fixation time
FIXATION_TIME = 1.5
# duration of the cue
CUE_TIME = 0.05
# stimulus onset asynchrony
SOA = 0.7
# duration of the feedback Screen
FEEDBACK_TIME = 2.0
# instructions
INSTRUCTIONS = """In this task you will see a '*' appear in a box
on the left or right. You will be shown a cue prior.
Your task is to respond as quickly as possible when
you see the '*' appear. Press key 'N' for left and
press 'M' for right. Press any key to continue."""
# box size
BOXSIZE = 200
# define the boxes' centre coordinates
BOX_LEFT = (DISPLAY_SIZE[0]*-0.25, 0)
BOX_RIGHT = (DISPLAY_SIZE[0]*0.25, 0)

# define the window
win = Window(size=DISPLAY_SIZE,
             monitor=MONITOR_NAME,
             units='pix',
             color=BACKGROUND,
             fullscr=False)

# draw instructions
instructionsStim = TextStim(win,
                            text=INSTRUCTIONS,
                            font="Arial",
                            pos=(0.0, 0.0),
                            color=FOREGROUND,
                            height=24)

# creating a fixation cross
fixStim = ShapeStim(win,
                    vertices=((0, -10), (0, 10),
                              (0, 0), (-10, 0), (10, 0)),
                    lineWidth=3,
                    closeShape=False,
                    lineColor=FOREGROUND)

# create the left box
leftboxStim = Rect(win,
                   pos=BOX_LEFT,
                   width=BOXSIZE,
                   height=BOXSIZE,
                   lineColor=FOREGROUND,
                   lineWidth=3,
                   fillColor=None)
# create the right box
rightboxStim = Rect(win,
                    pos=BOX_RIGHT,
                    width=BOXSIZE,
                    height=BOXSIZE,
                    lineColor=FOREGROUND,
                    lineWidth=3,
                    fillColor=None)
# create left cue
cueleftStim = Rect(win,
                   pos=BOX_LEFT,
                   width=BOXSIZE,
                   height=BOXSIZE,
                   lineColor=FOREGROUND,
                   lineWidth=9,
                   fillColor=None)
# create right cue
cuerightStim = Rect(win,
                    pos=BOX_RIGHT,
                    width=BOXSIZE,
                    height=BOXSIZE,
                    lineColor=FOREGROUND,
                    lineWidth=9,
                    fillColor=None)

# create list of cues
cues = ['cueleft', 'cueright']

# create left and right target
targetleftStim = (TextStim(win,
                           text='*',
                           pos=BOX_LEFT,
                           height=100,
                           color=FOREGROUND))

targetrightStim = (TextStim(win,
                            text='*',
                            pos=BOX_RIGHT,
                            height=100,
                            color=FOREGROUND))

# list of trials possible where 80% are valid trials (64)
trialsPossible = ['valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'valid', 'valid', 'valid', 'valid',
                  'invalid', 'invalid', 'invalid', 'invalid', 'invalid',
                  'invalid', 'invalid', 'invalid', 'invalid', 'invalid',
                  'invalid', 'invalid']
# demo version
"""
trialsPossible = ['valid', 'valid', 'valid', 'valid', 'valid', 'valid',
                  'invalid', 'invalid', 'invalid', 'invalid', 'invalid',
                  'invalid', 'invalid']
"""

# create a dict of feedback
fbstim = {}
# draw the correct feedback
fbstim['correct'] = (TextStim(win,
                              text='Correct!',
                              height=24,
                              color=(-1, 1, -1)))
# draw the incorrect feedback
fbstim['incorrect'] = (TextStim(win,
                                text='Your response was incorrect.',
                                height=24,
                                color=(1, -1, -1)))

# open a log for values
log = open(LOGFILE + '.tsv', 'w')
header = ['trial ', 'target ', 'response ', 'RT ']
headerstr = '\t'.join(header)
headerstr += '\n'
log.write(headerstr)

# show instructions
instructionsStim.draw()
win.flip()
# wait for any key
waitKeys(maxWait=float('inf'), keyList=None, timeStamped=True)

# 64 trials, randomly selected that are valid
# 12 trials that are not valid
validData = []
invalidData = []
shuffle(trialsPossible)

for trial in trialsPossible:
    # show initial screen
    fixStim.draw()
    leftboxStim.draw()
    rightboxStim.draw()
    win.flip()
    wait(FIXATION_TIME)

    # show the cue
    fixStim.draw()
    leftboxStim.draw()
    rightboxStim.draw()

    shuffle(cues)
    currentCue = cues[0]

    if currentCue == 'cueleft':
        cueleftStim.draw()

    elif currentCue == 'cueright':
        cuerightStim.draw()

    win.flip()
    wait(CUE_TIME)

    # time to wait
    fixStim.draw()
    leftboxStim.draw()
    rightboxStim.draw()
    win.flip()
    wait(SOA - CUE_TIME)

    # show target
    fixStim.draw()
    leftboxStim.draw()
    rightboxStim.draw()

    # show valid trial
    if trial == 'valid':
        if currentCue == 'cueleft':
            target = 'left'
            targetleftStim.draw()
        elif currentCue == 'cueright':
            target = 'right'
            targetrightStim.draw()

    # show invalid trial
    elif trial == 'invalid':
        if currentCue == 'cueleft':
            target = 'right'
            targetrightStim.draw()
        elif currentCue == 'cueright':
            target = 'left'
            targetleftStim.draw()

    targetime = win.flip()

    # check response
    resplist = waitKeys(maxWait=float('inf'), keyList=['n', 'm'],
                        timeStamped=True)
    response, presstime = resplist[0]

    if response == 'n' and target == 'left':
        correct = 'correct'
    elif response == 'm' and target == 'right':
        correct = 'correct'
    else:
        correct = 'incorrect'

    # give RT in ms and show feedback
    RT = (presstime - targetime)*1000
    
    fbstim[correct].draw()
    win.flip()
    wait(FEEDBACK_TIME)

    # log response
    logLine = [trial, target, response, str(RT)]
    logLineStr = '\t'.join(logLine)
    logLineStr += '\n'
    log.write(logLineStr)

    if correct == 'correct' and trial == 'valid':
        validData.append(RT)
    elif correct == 'correct' and trial == 'invalid':
        invalidData.append(RT)

# calculate means for bar graph
validMean = (sum(validData) / float(len(validData)))
invalidMean = (sum(invalidData) / float(len(invalidData)))

# create bar graph
font = {'family': 'serif',
        'color': 'black',
        'weight': 'normal',
        'size': 'small',
        }

objects = ('Valid', 'Invalid')
means = [validMean, invalidMean]
y_pos = numpy.arange(len(objects))
plt.xticks(y_pos, objects)
plt.xlabel('Trial type', font)
plt.ylabel('RT (ms)', font)
plt.bar(y_pos, means, alpha=0.5, align='center')
plt.show()

log.close()
win.close()






