#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on February 11, 2021, at 00:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'TE_idea2-jy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\cat\\Desktop\\lab work\\Regina Lapate lab\\works\\Anorexia project\\Time estimates task\\modified psychopy\\TE_idea2-jy_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome!\n\nIn the next task, we are interested in understanding how we form our internal representations of time.',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press any key to continue',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "intro1_TE1"
intro1_TE1Clock = core.Clock()
intro_1 = visual.TextStim(win=win, name='intro_1',
    text='For this task, you will be asked to count in synchrony with the computer for a few seconds, and then to continue counting until you reach the specified number for each trial.\n\nAt the beginning of each trial, we will count with you until “10” by flashing numbers on the screen. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_intro_1 = keyboard.Keyboard()

# Initialize components for Routine "intro2"
intro2Clock = core.Clock()
introtext1 = visual.TextStim(win=win, name='introtext1',
    text='After we reach “10”, please continue to count silently in your head and press the spacebar whenever you reach the target number (indicated at the start of each trial). \n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Let’s practice this once\n\nFor this practice trial, you will count to 15.\n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "practicetrial"
practicetrialClock = core.Clock()
one_p = visual.TextStim(win=win, name='one_p',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
two_p = visual.TextStim(win=win, name='two_p',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
three_p = visual.TextStim(win=win, name='three_p',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
four_p = visual.TextStim(win=win, name='four_p',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
five_p = visual.TextStim(win=win, name='five_p',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
six_p = visual.TextStim(win=win, name='six_p',
    text='6',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
seven_p = visual.TextStim(win=win, name='seven_p',
    text='7',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
eight_p = visual.TextStim(win=win, name='eight_p',
    text='8',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
nine_p = visual.TextStim(win=win, name='nine_p',
    text='9',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ten_p = visual.TextStim(win=win, name='ten_p',
    text='10',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
blank_p = visual.TextStim(win=win, name='blank_p',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "starttrials"
starttrialsClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Okay, now we will begin the task. \n',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr_TE1"
instr_TE1Clock = core.Clock()
instrtext = visual.TextStim(win=win, name='instrtext',
    text='For this trial, you will count to \n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()
begintext = visual.TextStim(win=win, name='begintext',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
endnumber = visual.TextStim(win=win, name='endnumber',
    text='default text',
    font='Arial',
    pos=(0, 0.147), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "TE1"
TE1Clock = core.Clock()
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
two = visual.TextStim(win=win, name='two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
three = visual.TextStim(win=win, name='three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
four = visual.TextStim(win=win, name='four',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
five = visual.TextStim(win=win, name='five',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
six = visual.TextStim(win=win, name='six',
    text='6',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
seven = visual.TextStim(win=win, name='seven',
    text='7',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
eight = visual.TextStim(win=win, name='eight',
    text='8',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
nine = visual.TextStim(win=win, name='nine',
    text='9',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ten = visual.TextStim(win=win, name='ten',
    text='10',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0.5, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "intro_TE2"
intro_TE2Clock = core.Clock()
introforpt2 = visual.TextStim(win=win, name='introforpt2',
    text='Now we will begin part 2 of this task.\n\nYou will continue to count to a target number for each trial, but we will be counting at a slightly different pace.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press the spacebar to begin',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instr_TE2"
instr_TE2Clock = core.Clock()
instrtext2 = visual.TextStim(win=win, name='instrtext2',
    text='For this trial, you will count to \n\nWe will count with you until 10\n\nPlease continue counting in your head at the same pace and press the spacebar once you reach the target number.\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()
endnumber2 = visual.TextStim(win=win, name='endnumber2',
    text='default text',
    font='Arial',
    pos=(0, 0.147), height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
begintext2 = visual.TextStim(win=win, name='begintext2',
    text='Press the space bar to begin',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "TE2"
TE2Clock = core.Clock()
one_4 = visual.TextStim(win=win, name='one_4',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
two_4 = visual.TextStim(win=win, name='two_4',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
three_4 = visual.TextStim(win=win, name='three_4',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
four_4 = visual.TextStim(win=win, name='four_4',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
five_4 = visual.TextStim(win=win, name='five_4',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
six_4 = visual.TextStim(win=win, name='six_4',
    text='6',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
seven_4 = visual.TextStim(win=win, name='seven_4',
    text='7',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
eight_4 = visual.TextStim(win=win, name='eight_4',
    text='8',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
nine_4 = visual.TextStim(win=win, name='nine_4',
    text='9',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ten_4 = visual.TextStim(win=win, name='ten_4',
    text='10',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
blank_4 = visual.TextStim(win=win, name='blank_4',
    text=None,
    font='Arial',
    pos=(0.5, -0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_4 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
welcomeComponents = [text, key_resp_6, text_2]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro1_TE1"-------
continueRoutine = True
# update component parameters for each repeat
key_intro_1.keys = []
key_intro_1.rt = []
_key_intro_1_allKeys = []
# keep track of which components have finished
intro1_TE1Components = [intro_1, key_intro_1]
for thisComponent in intro1_TE1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro1_TE1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro1_TE1"-------
while continueRoutine:
    # get current time
    t = intro1_TE1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro1_TE1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_1* updates
    if intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_1.frameNStart = frameN  # exact frame index
        intro_1.tStart = t  # local t and not account for scr refresh
        intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_1, 'tStartRefresh')  # time at next scr refresh
        intro_1.setAutoDraw(True)
    
    # *key_intro_1* updates
    waitOnFlip = False
    if key_intro_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_intro_1.frameNStart = frameN  # exact frame index
        key_intro_1.tStart = t  # local t and not account for scr refresh
        key_intro_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_intro_1, 'tStartRefresh')  # time at next scr refresh
        key_intro_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_intro_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_intro_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_intro_1.status == STARTED and not waitOnFlip:
        theseKeys = key_intro_1.getKeys(keyList=None, waitRelease=False)
        _key_intro_1_allKeys.extend(theseKeys)
        if len(_key_intro_1_allKeys):
            key_intro_1.keys = _key_intro_1_allKeys[-1].name  # just the last key pressed
            key_intro_1.rt = _key_intro_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro1_TE1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro1_TE1"-------
for thisComponent in intro1_TE1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_1.started', intro_1.tStartRefresh)
thisExp.addData('intro_1.stopped', intro_1.tStopRefresh)
# the Routine "intro1_TE1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
intro2Components = [introtext1, key_resp_8]
for thisComponent in intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro2"-------
while continueRoutine:
    # get current time
    t = intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introtext1* updates
    if introtext1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introtext1.frameNStart = frameN  # exact frame index
        introtext1.tStart = t  # local t and not account for scr refresh
        introtext1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introtext1, 'tStartRefresh')  # time at next scr refresh
        introtext1.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=None, waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro2"-------
for thisComponent in intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introtext1.started', introtext1.tStartRefresh)
thisExp.addData('introtext1.stopped', introtext1.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
practiceComponents = [text_5, key_resp_10, text_6]
for thisComponent in practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice"-------
while continueRoutine:
    # get current time
    t = practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice"-------
for thisComponent in practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# the Routine "practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practicetrial"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
practicetrialComponents = [one_p, two_p, three_p, four_p, five_p, six_p, seven_p, eight_p, nine_p, ten_p, blank_p, key_resp_11]
for thisComponent in practicetrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practicetrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practicetrial"-------
while continueRoutine:
    # get current time
    t = practicetrialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practicetrialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_p* updates
    if one_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_p.frameNStart = frameN  # exact frame index
        one_p.tStart = t  # local t and not account for scr refresh
        one_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_p, 'tStartRefresh')  # time at next scr refresh
        one_p.setAutoDraw(True)
    if one_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > one_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            one_p.tStop = t  # not accounting for scr refresh
            one_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(one_p, 'tStopRefresh')  # time at next scr refresh
            one_p.setAutoDraw(False)
    
    # *two_p* updates
    if two_p.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        two_p.frameNStart = frameN  # exact frame index
        two_p.tStart = t  # local t and not account for scr refresh
        two_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_p, 'tStartRefresh')  # time at next scr refresh
        two_p.setAutoDraw(True)
    if two_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > two_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            two_p.tStop = t  # not accounting for scr refresh
            two_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(two_p, 'tStopRefresh')  # time at next scr refresh
            two_p.setAutoDraw(False)
    
    # *three_p* updates
    if three_p.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        three_p.frameNStart = frameN  # exact frame index
        three_p.tStart = t  # local t and not account for scr refresh
        three_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three_p, 'tStartRefresh')  # time at next scr refresh
        three_p.setAutoDraw(True)
    if three_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > three_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            three_p.tStop = t  # not accounting for scr refresh
            three_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(three_p, 'tStopRefresh')  # time at next scr refresh
            three_p.setAutoDraw(False)
    
    # *four_p* updates
    if four_p.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        four_p.frameNStart = frameN  # exact frame index
        four_p.tStart = t  # local t and not account for scr refresh
        four_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four_p, 'tStartRefresh')  # time at next scr refresh
        four_p.setAutoDraw(True)
    if four_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            four_p.tStop = t  # not accounting for scr refresh
            four_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(four_p, 'tStopRefresh')  # time at next scr refresh
            four_p.setAutoDraw(False)
    
    # *five_p* updates
    if five_p.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
        # keep track of start time/frame for later
        five_p.frameNStart = frameN  # exact frame index
        five_p.tStart = t  # local t and not account for scr refresh
        five_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five_p, 'tStartRefresh')  # time at next scr refresh
        five_p.setAutoDraw(True)
    if five_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > five_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            five_p.tStop = t  # not accounting for scr refresh
            five_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(five_p, 'tStopRefresh')  # time at next scr refresh
            five_p.setAutoDraw(False)
    
    # *six_p* updates
    if six_p.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:
        # keep track of start time/frame for later
        six_p.frameNStart = frameN  # exact frame index
        six_p.tStart = t  # local t and not account for scr refresh
        six_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(six_p, 'tStartRefresh')  # time at next scr refresh
        six_p.setAutoDraw(True)
    if six_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > six_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            six_p.tStop = t  # not accounting for scr refresh
            six_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(six_p, 'tStopRefresh')  # time at next scr refresh
            six_p.setAutoDraw(False)
    
    # *seven_p* updates
    if seven_p.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
        # keep track of start time/frame for later
        seven_p.frameNStart = frameN  # exact frame index
        seven_p.tStart = t  # local t and not account for scr refresh
        seven_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(seven_p, 'tStartRefresh')  # time at next scr refresh
        seven_p.setAutoDraw(True)
    if seven_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > seven_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            seven_p.tStop = t  # not accounting for scr refresh
            seven_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(seven_p, 'tStopRefresh')  # time at next scr refresh
            seven_p.setAutoDraw(False)
    
    # *eight_p* updates
    if eight_p.status == NOT_STARTED and tThisFlip >= 7.0-frameTolerance:
        # keep track of start time/frame for later
        eight_p.frameNStart = frameN  # exact frame index
        eight_p.tStart = t  # local t and not account for scr refresh
        eight_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eight_p, 'tStartRefresh')  # time at next scr refresh
        eight_p.setAutoDraw(True)
    if eight_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > eight_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            eight_p.tStop = t  # not accounting for scr refresh
            eight_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(eight_p, 'tStopRefresh')  # time at next scr refresh
            eight_p.setAutoDraw(False)
    
    # *nine_p* updates
    if nine_p.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        nine_p.frameNStart = frameN  # exact frame index
        nine_p.tStart = t  # local t and not account for scr refresh
        nine_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nine_p, 'tStartRefresh')  # time at next scr refresh
        nine_p.setAutoDraw(True)
    if nine_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > nine_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            nine_p.tStop = t  # not accounting for scr refresh
            nine_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(nine_p, 'tStopRefresh')  # time at next scr refresh
            nine_p.setAutoDraw(False)
    
    # *ten_p* updates
    if ten_p.status == NOT_STARTED and tThisFlip >= 9.0-frameTolerance:
        # keep track of start time/frame for later
        ten_p.frameNStart = frameN  # exact frame index
        ten_p.tStart = t  # local t and not account for scr refresh
        ten_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ten_p, 'tStartRefresh')  # time at next scr refresh
        ten_p.setAutoDraw(True)
    if ten_p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ten_p.tStartRefresh + 0.1-frameTolerance:
            # keep track of stop time/frame for later
            ten_p.tStop = t  # not accounting for scr refresh
            ten_p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ten_p, 'tStopRefresh')  # time at next scr refresh
            ten_p.setAutoDraw(False)
    
    # *blank_p* updates
    if blank_p.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        blank_p.frameNStart = frameN  # exact frame index
        blank_p.tStart = t  # local t and not account for scr refresh
        blank_p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blank_p, 'tStartRefresh')  # time at next scr refresh
        blank_p.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practicetrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practicetrial"-------
for thisComponent in practicetrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_p.started', one_p.tStartRefresh)
thisExp.addData('one_p.stopped', one_p.tStopRefresh)
thisExp.addData('two_p.started', two_p.tStartRefresh)
thisExp.addData('two_p.stopped', two_p.tStopRefresh)
thisExp.addData('three_p.started', three_p.tStartRefresh)
thisExp.addData('three_p.stopped', three_p.tStopRefresh)
thisExp.addData('four_p.started', four_p.tStartRefresh)
thisExp.addData('four_p.stopped', four_p.tStopRefresh)
thisExp.addData('five_p.started', five_p.tStartRefresh)
thisExp.addData('five_p.stopped', five_p.tStopRefresh)
thisExp.addData('six_p.started', six_p.tStartRefresh)
thisExp.addData('six_p.stopped', six_p.tStopRefresh)
thisExp.addData('seven_p.started', seven_p.tStartRefresh)
thisExp.addData('seven_p.stopped', seven_p.tStopRefresh)
thisExp.addData('eight_p.started', eight_p.tStartRefresh)
thisExp.addData('eight_p.stopped', eight_p.tStopRefresh)
thisExp.addData('nine_p.started', nine_p.tStartRefresh)
thisExp.addData('nine_p.stopped', nine_p.tStopRefresh)
thisExp.addData('ten_p.started', ten_p.tStartRefresh)
thisExp.addData('ten_p.stopped', ten_p.tStopRefresh)
thisExp.addData('blank_p.started', blank_p.tStartRefresh)
thisExp.addData('blank_p.stopped', blank_p.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
# the Routine "practicetrial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "starttrials"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
starttrialsComponents = [text_7, key_resp_12, text_8]
for thisComponent in starttrialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
starttrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "starttrials"-------
while continueRoutine:
    # get current time
    t = starttrialsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=starttrialsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in starttrialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "starttrials"-------
for thisComponent in starttrialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# the Routine "starttrials" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TE1_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimcon.xlsx'),
    seed=None, name='TE1_trials')
thisExp.addLoop(TE1_trials)  # add the loop to the experiment
thisTE1_trial = TE1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTE1_trial.rgb)
if thisTE1_trial != None:
    for paramName in thisTE1_trial:
        exec('{} = thisTE1_trial[paramName]'.format(paramName))

for thisTE1_trial in TE1_trials:
    currentLoop = TE1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTE1_trial.rgb)
    if thisTE1_trial != None:
        for paramName in thisTE1_trial:
            exec('{} = thisTE1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr_TE1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    endnumber.setText(s1)
    # keep track of which components have finished
    instr_TE1Components = [instrtext, key_resp_5, begintext, endnumber]
    for thisComponent in instr_TE1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr_TE1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr_TE1"-------
    while continueRoutine:
        # get current time
        t = instr_TE1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr_TE1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrtext* updates
        if instrtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrtext.frameNStart = frameN  # exact frame index
            instrtext.tStart = t  # local t and not account for scr refresh
            instrtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrtext, 'tStartRefresh')  # time at next scr refresh
            instrtext.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *begintext* updates
        if begintext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begintext.frameNStart = frameN  # exact frame index
            begintext.tStart = t  # local t and not account for scr refresh
            begintext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begintext, 'tStartRefresh')  # time at next scr refresh
            begintext.setAutoDraw(True)
        
        # *endnumber* updates
        if endnumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endnumber.frameNStart = frameN  # exact frame index
            endnumber.tStart = t  # local t and not account for scr refresh
            endnumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endnumber, 'tStartRefresh')  # time at next scr refresh
            endnumber.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_TE1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_TE1"-------
    for thisComponent in instr_TE1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TE1_trials.addData('instrtext.started', instrtext.tStartRefresh)
    TE1_trials.addData('instrtext.stopped', instrtext.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    TE1_trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        TE1_trials.addData('key_resp_5.rt', key_resp_5.rt)
    TE1_trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    TE1_trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    TE1_trials.addData('begintext.started', begintext.tStartRefresh)
    TE1_trials.addData('begintext.stopped', begintext.tStopRefresh)
    TE1_trials.addData('endnumber.started', endnumber.tStartRefresh)
    TE1_trials.addData('endnumber.stopped', endnumber.tStopRefresh)
    # the Routine "instr_TE1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TE1"-------
    continueRoutine = True
    # update component parameters for each repeat
    blank.setText('')
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    TE1Components = [one, two, three, four, five, six, seven, eight, nine, ten, blank, key_resp]
    for thisComponent in TE1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TE1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TE1"-------
    while continueRoutine:
        # get current time
        t = TE1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TE1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one* updates
        if one.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            one.setAutoDraw(True)
        if one.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                one.tStop = t  # not accounting for scr refresh
                one.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one, 'tStopRefresh')  # time at next scr refresh
                one.setAutoDraw(False)
        
        # *two* updates
        if two.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            two.frameNStart = frameN  # exact frame index
            two.tStart = t  # local t and not account for scr refresh
            two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
            two.setAutoDraw(True)
        if two.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                two.tStop = t  # not accounting for scr refresh
                two.frameNStop = frameN  # exact frame index
                win.timeOnFlip(two, 'tStopRefresh')  # time at next scr refresh
                two.setAutoDraw(False)
        
        # *three* updates
        if three.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            three.frameNStart = frameN  # exact frame index
            three.tStart = t  # local t and not account for scr refresh
            three.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
            three.setAutoDraw(True)
        if three.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                three.tStop = t  # not accounting for scr refresh
                three.frameNStop = frameN  # exact frame index
                win.timeOnFlip(three, 'tStopRefresh')  # time at next scr refresh
                three.setAutoDraw(False)
        
        # *four* updates
        if four.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            four.frameNStart = frameN  # exact frame index
            four.tStart = t  # local t and not account for scr refresh
            four.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
            four.setAutoDraw(True)
        if four.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                four.tStop = t  # not accounting for scr refresh
                four.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four, 'tStopRefresh')  # time at next scr refresh
                four.setAutoDraw(False)
        
        # *five* updates
        if five.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            five.frameNStart = frameN  # exact frame index
            five.tStart = t  # local t and not account for scr refresh
            five.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
            five.setAutoDraw(True)
        if five.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                five.tStop = t  # not accounting for scr refresh
                five.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five, 'tStopRefresh')  # time at next scr refresh
                five.setAutoDraw(False)
        
        # *six* updates
        if six.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            six.frameNStart = frameN  # exact frame index
            six.tStart = t  # local t and not account for scr refresh
            six.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six, 'tStartRefresh')  # time at next scr refresh
            six.setAutoDraw(True)
        if six.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                six.tStop = t  # not accounting for scr refresh
                six.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six, 'tStopRefresh')  # time at next scr refresh
                six.setAutoDraw(False)
        
        # *seven* updates
        if seven.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            seven.frameNStart = frameN  # exact frame index
            seven.tStart = t  # local t and not account for scr refresh
            seven.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven, 'tStartRefresh')  # time at next scr refresh
            seven.setAutoDraw(True)
        if seven.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                seven.tStop = t  # not accounting for scr refresh
                seven.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven, 'tStopRefresh')  # time at next scr refresh
                seven.setAutoDraw(False)
        
        # *eight* updates
        if eight.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
            # keep track of start time/frame for later
            eight.frameNStart = frameN  # exact frame index
            eight.tStart = t  # local t and not account for scr refresh
            eight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight, 'tStartRefresh')  # time at next scr refresh
            eight.setAutoDraw(True)
        if eight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                eight.tStop = t  # not accounting for scr refresh
                eight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight, 'tStopRefresh')  # time at next scr refresh
                eight.setAutoDraw(False)
        
        # *nine* updates
        if nine.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            nine.frameNStart = frameN  # exact frame index
            nine.tStart = t  # local t and not account for scr refresh
            nine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
            nine.setAutoDraw(True)
        if nine.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                nine.tStop = t  # not accounting for scr refresh
                nine.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine, 'tStopRefresh')  # time at next scr refresh
                nine.setAutoDraw(False)
        
        # *ten* updates
        if ten.status == NOT_STARTED and tThisFlip >= 9-frameTolerance:
            # keep track of start time/frame for later
            ten.frameNStart = frameN  # exact frame index
            ten.tStart = t  # local t and not account for scr refresh
            ten.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten, 'tStartRefresh')  # time at next scr refresh
            ten.setAutoDraw(True)
        if ten.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                ten.tStop = t  # not accounting for scr refresh
                ten.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten, 'tStopRefresh')  # time at next scr refresh
                ten.setAutoDraw(False)
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TE1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TE1"-------
    for thisComponent in TE1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TE1_trials.addData('one.started', one.tStartRefresh)
    TE1_trials.addData('one.stopped', one.tStopRefresh)
    TE1_trials.addData('two.started', two.tStartRefresh)
    TE1_trials.addData('two.stopped', two.tStopRefresh)
    TE1_trials.addData('three.started', three.tStartRefresh)
    TE1_trials.addData('three.stopped', three.tStopRefresh)
    TE1_trials.addData('four.started', four.tStartRefresh)
    TE1_trials.addData('four.stopped', four.tStopRefresh)
    TE1_trials.addData('five.started', five.tStartRefresh)
    TE1_trials.addData('five.stopped', five.tStopRefresh)
    TE1_trials.addData('six.started', six.tStartRefresh)
    TE1_trials.addData('six.stopped', six.tStopRefresh)
    TE1_trials.addData('seven.started', seven.tStartRefresh)
    TE1_trials.addData('seven.stopped', seven.tStopRefresh)
    TE1_trials.addData('eight.started', eight.tStartRefresh)
    TE1_trials.addData('eight.stopped', eight.tStopRefresh)
    TE1_trials.addData('nine.started', nine.tStartRefresh)
    TE1_trials.addData('nine.stopped', nine.tStopRefresh)
    TE1_trials.addData('ten.started', ten.tStartRefresh)
    TE1_trials.addData('ten.stopped', ten.tStopRefresh)
    TE1_trials.addData('blank.started', blank.tStartRefresh)
    TE1_trials.addData('blank.stopped', blank.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    TE1_trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        TE1_trials.addData('key_resp.rt', key_resp.rt)
    TE1_trials.addData('key_resp.started', key_resp.tStartRefresh)
    TE1_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "TE1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'TE1_trials'


# ------Prepare to start Routine "intro_TE2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
intro_TE2Components = [introforpt2, key_resp_9, text_4]
for thisComponent in intro_TE2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro_TE2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro_TE2"-------
while continueRoutine:
    # get current time
    t = intro_TE2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro_TE2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introforpt2* updates
    if introforpt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introforpt2.frameNStart = frameN  # exact frame index
        introforpt2.tStart = t  # local t and not account for scr refresh
        introforpt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introforpt2, 'tStartRefresh')  # time at next scr refresh
        introforpt2.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_TE2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro_TE2"-------
for thisComponent in intro_TE2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introforpt2.started', introforpt2.tStartRefresh)
thisExp.addData('introforpt2.stopped', introforpt2.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "intro_TE2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TE2_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimcon.xlsx'),
    seed=None, name='TE2_trials')
thisExp.addLoop(TE2_trials)  # add the loop to the experiment
thisTE2_trial = TE2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTE2_trial.rgb)
if thisTE2_trial != None:
    for paramName in thisTE2_trial:
        exec('{} = thisTE2_trial[paramName]'.format(paramName))

for thisTE2_trial in TE2_trials:
    currentLoop = TE2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTE2_trial.rgb)
    if thisTE2_trial != None:
        for paramName in thisTE2_trial:
            exec('{} = thisTE2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr_TE2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    endnumber2.setText(s2)
    # keep track of which components have finished
    instr_TE2Components = [instrtext2, key_resp_7, endnumber2, begintext2]
    for thisComponent in instr_TE2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr_TE2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr_TE2"-------
    while continueRoutine:
        # get current time
        t = instr_TE2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr_TE2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrtext2* updates
        if instrtext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrtext2.frameNStart = frameN  # exact frame index
            instrtext2.tStart = t  # local t and not account for scr refresh
            instrtext2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrtext2, 'tStartRefresh')  # time at next scr refresh
            instrtext2.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *endnumber2* updates
        if endnumber2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endnumber2.frameNStart = frameN  # exact frame index
            endnumber2.tStart = t  # local t and not account for scr refresh
            endnumber2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endnumber2, 'tStartRefresh')  # time at next scr refresh
            endnumber2.setAutoDraw(True)
        
        # *begintext2* updates
        if begintext2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begintext2.frameNStart = frameN  # exact frame index
            begintext2.tStart = t  # local t and not account for scr refresh
            begintext2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begintext2, 'tStartRefresh')  # time at next scr refresh
            begintext2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_TE2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_TE2"-------
    for thisComponent in instr_TE2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TE2_trials.addData('instrtext2.started', instrtext2.tStartRefresh)
    TE2_trials.addData('instrtext2.stopped', instrtext2.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    TE2_trials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        TE2_trials.addData('key_resp_7.rt', key_resp_7.rt)
    TE2_trials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    TE2_trials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    TE2_trials.addData('endnumber2.started', endnumber2.tStartRefresh)
    TE2_trials.addData('endnumber2.stopped', endnumber2.tStopRefresh)
    TE2_trials.addData('begintext2.started', begintext2.tStartRefresh)
    TE2_trials.addData('begintext2.stopped', begintext2.tStopRefresh)
    # the Routine "instr_TE2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "TE2"-------
    continueRoutine = True
    # update component parameters for each repeat
    blank_4.setText('')
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    TE2Components = [one_4, two_4, three_4, four_4, five_4, six_4, seven_4, eight_4, nine_4, ten_4, blank_4, key_resp_4]
    for thisComponent in TE2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TE2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TE2"-------
    while continueRoutine:
        # get current time
        t = TE2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TE2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *one_4* updates
        if one_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            one_4.frameNStart = frameN  # exact frame index
            one_4.tStart = t  # local t and not account for scr refresh
            one_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_4, 'tStartRefresh')  # time at next scr refresh
            one_4.setAutoDraw(True)
        if one_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > one_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                one_4.tStop = t  # not accounting for scr refresh
                one_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(one_4, 'tStopRefresh')  # time at next scr refresh
                one_4.setAutoDraw(False)
        
        # *two_4* updates
        if two_4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            two_4.frameNStart = frameN  # exact frame index
            two_4.tStart = t  # local t and not account for scr refresh
            two_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(two_4, 'tStartRefresh')  # time at next scr refresh
            two_4.setAutoDraw(True)
        if two_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > two_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                two_4.tStop = t  # not accounting for scr refresh
                two_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(two_4, 'tStopRefresh')  # time at next scr refresh
                two_4.setAutoDraw(False)
        
        # *three_4* updates
        if three_4.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            three_4.frameNStart = frameN  # exact frame index
            three_4.tStart = t  # local t and not account for scr refresh
            three_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(three_4, 'tStartRefresh')  # time at next scr refresh
            three_4.setAutoDraw(True)
        if three_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > three_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                three_4.tStop = t  # not accounting for scr refresh
                three_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(three_4, 'tStopRefresh')  # time at next scr refresh
                three_4.setAutoDraw(False)
        
        # *four_4* updates
        if four_4.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            four_4.frameNStart = frameN  # exact frame index
            four_4.tStart = t  # local t and not account for scr refresh
            four_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(four_4, 'tStartRefresh')  # time at next scr refresh
            four_4.setAutoDraw(True)
        if four_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > four_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                four_4.tStop = t  # not accounting for scr refresh
                four_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(four_4, 'tStopRefresh')  # time at next scr refresh
                four_4.setAutoDraw(False)
        
        # *five_4* updates
        if five_4.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            five_4.frameNStart = frameN  # exact frame index
            five_4.tStart = t  # local t and not account for scr refresh
            five_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(five_4, 'tStartRefresh')  # time at next scr refresh
            five_4.setAutoDraw(True)
        if five_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > five_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                five_4.tStop = t  # not accounting for scr refresh
                five_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(five_4, 'tStopRefresh')  # time at next scr refresh
                five_4.setAutoDraw(False)
        
        # *six_4* updates
        if six_4.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            six_4.frameNStart = frameN  # exact frame index
            six_4.tStart = t  # local t and not account for scr refresh
            six_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_4, 'tStartRefresh')  # time at next scr refresh
            six_4.setAutoDraw(True)
        if six_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > six_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                six_4.tStop = t  # not accounting for scr refresh
                six_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(six_4, 'tStopRefresh')  # time at next scr refresh
                six_4.setAutoDraw(False)
        
        # *seven_4* updates
        if seven_4.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
            # keep track of start time/frame for later
            seven_4.frameNStart = frameN  # exact frame index
            seven_4.tStart = t  # local t and not account for scr refresh
            seven_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(seven_4, 'tStartRefresh')  # time at next scr refresh
            seven_4.setAutoDraw(True)
        if seven_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > seven_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                seven_4.tStop = t  # not accounting for scr refresh
                seven_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(seven_4, 'tStopRefresh')  # time at next scr refresh
                seven_4.setAutoDraw(False)
        
        # *eight_4* updates
        if eight_4.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            eight_4.frameNStart = frameN  # exact frame index
            eight_4.tStart = t  # local t and not account for scr refresh
            eight_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eight_4, 'tStartRefresh')  # time at next scr refresh
            eight_4.setAutoDraw(True)
        if eight_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eight_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                eight_4.tStop = t  # not accounting for scr refresh
                eight_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(eight_4, 'tStopRefresh')  # time at next scr refresh
                eight_4.setAutoDraw(False)
        
        # *nine_4* updates
        if nine_4.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
            # keep track of start time/frame for later
            nine_4.frameNStart = frameN  # exact frame index
            nine_4.tStart = t  # local t and not account for scr refresh
            nine_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine_4, 'tStartRefresh')  # time at next scr refresh
            nine_4.setAutoDraw(True)
        if nine_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > nine_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                nine_4.tStop = t  # not accounting for scr refresh
                nine_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(nine_4, 'tStopRefresh')  # time at next scr refresh
                nine_4.setAutoDraw(False)
        
        # *ten_4* updates
        if ten_4.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
            # keep track of start time/frame for later
            ten_4.frameNStart = frameN  # exact frame index
            ten_4.tStart = t  # local t and not account for scr refresh
            ten_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ten_4, 'tStartRefresh')  # time at next scr refresh
            ten_4.setAutoDraw(True)
        if ten_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ten_4.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                ten_4.tStop = t  # not accounting for scr refresh
                ten_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ten_4, 'tStopRefresh')  # time at next scr refresh
                ten_4.setAutoDraw(False)
        
        # *blank_4* updates
        if blank_4.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            blank_4.frameNStart = frameN  # exact frame index
            blank_4.tStart = t  # local t and not account for scr refresh
            blank_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_4, 'tStartRefresh')  # time at next scr refresh
            blank_4.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TE2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TE2"-------
    for thisComponent in TE2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TE2_trials.addData('one_4.started', one_4.tStartRefresh)
    TE2_trials.addData('one_4.stopped', one_4.tStopRefresh)
    TE2_trials.addData('two_4.started', two_4.tStartRefresh)
    TE2_trials.addData('two_4.stopped', two_4.tStopRefresh)
    TE2_trials.addData('three_4.started', three_4.tStartRefresh)
    TE2_trials.addData('three_4.stopped', three_4.tStopRefresh)
    TE2_trials.addData('four_4.started', four_4.tStartRefresh)
    TE2_trials.addData('four_4.stopped', four_4.tStopRefresh)
    TE2_trials.addData('five_4.started', five_4.tStartRefresh)
    TE2_trials.addData('five_4.stopped', five_4.tStopRefresh)
    TE2_trials.addData('six_4.started', six_4.tStartRefresh)
    TE2_trials.addData('six_4.stopped', six_4.tStopRefresh)
    TE2_trials.addData('seven_4.started', seven_4.tStartRefresh)
    TE2_trials.addData('seven_4.stopped', seven_4.tStopRefresh)
    TE2_trials.addData('eight_4.started', eight_4.tStartRefresh)
    TE2_trials.addData('eight_4.stopped', eight_4.tStopRefresh)
    TE2_trials.addData('nine_4.started', nine_4.tStartRefresh)
    TE2_trials.addData('nine_4.stopped', nine_4.tStopRefresh)
    TE2_trials.addData('ten_4.started', ten_4.tStartRefresh)
    TE2_trials.addData('ten_4.stopped', ten_4.tStopRefresh)
    TE2_trials.addData('blank_4.started', blank_4.tStartRefresh)
    TE2_trials.addData('blank_4.stopped', blank_4.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    TE2_trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        TE2_trials.addData('key_resp_4.rt', key_resp_4.rt)
    TE2_trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    TE2_trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "TE2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'TE2_trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
