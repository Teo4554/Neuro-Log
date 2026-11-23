#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.2.4),
    on Sun 22 Nov 2026 06:23:34 PM -04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import psychopy.hardware.speaker

# set audio backend
sound.Sound.backend = prefs.hardware['audioLib']
hardware.speaker.SpeakerDevice.backend = prefs.hardware['audioLib']
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.2.4'
expName = 'MODULO2'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = 'data/' + expInfo['participant'] + '_' + expName + '_' + expInfo['date']
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='datos/MODULO2.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "WELCOME1" ---
    RESPUESTAWELCOME_2 = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    Welcome_2 = visual.TextStim(win=win, name='Welcome_2',
        text='Saludos, bievenido a la tarea de medicion de tiempos de reaccion comparativa, a continuacion, vera una pantalla en blanco, en la cual periodicamente aparecera un o escuchara un sonido claro, cuando lo haga, debera presionar la tecla espacio, ¡Suerte!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    SEÑALGRAFICA = visual.TextStim(win=win, name='SEÑALGRAFICA',
        text='¡YA!\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=0.0);
    SEÑALAUDITIVA = sound.Sound(
        'A', 
        secs=1.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='SEÑALAUDITIVA'
    )
    SEÑALAUDITIVA.setVolume(1.0)
    RESPUESTASEÑAL = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    FIJACION = visual.TextStim(win=win, name='FIJACION',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "DESPEDIDA" ---
    DESPEDIDA1 = visual.TextStim(win=win, name='DESPEDIDA1',
        text='¡Gracias por participar!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    RESPUESTADESPEDIDA = keyboard.Keyboard(deviceName='defaultKeyboard', backend='PsychToolbox')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "WELCOME1" ---
    # create an object to store info about Routine WELCOME1
    WELCOME1 = data.Routine(
        name='WELCOME1',
        components=[RESPUESTAWELCOME_2, Welcome_2],
    )
    WELCOME1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for RESPUESTAWELCOME_2
    RESPUESTAWELCOME_2.keys = []
    RESPUESTAWELCOME_2.rt = []
    _RESPUESTAWELCOME_2_allKeys = []
    Welcome_2.setOpacity(None)
    # store start times for WELCOME1
    WELCOME1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    WELCOME1.tStart = globalClock.getTime(format='float')
    WELCOME1.status = STARTED
    thisExp.addData('WELCOME1.started', WELCOME1.tStart)
    WELCOME1.maxDuration = None
    # keep track of which components have finished
    WELCOME1Components = WELCOME1.components
    for thisComponent in WELCOME1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WELCOME1" ---
    thisExp.currentRoutine = WELCOME1
    WELCOME1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RESPUESTAWELCOME_2* updates
        waitOnFlip = False
        
        # if RESPUESTAWELCOME_2 is starting this frame...
        if RESPUESTAWELCOME_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RESPUESTAWELCOME_2.frameNStart = frameN  # exact frame index
            RESPUESTAWELCOME_2.tStart = t  # local t and not account for scr refresh
            RESPUESTAWELCOME_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RESPUESTAWELCOME_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RESPUESTAWELCOME_2.started')
            # update status
            RESPUESTAWELCOME_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RESPUESTAWELCOME_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RESPUESTAWELCOME_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RESPUESTAWELCOME_2.status == STARTED and not waitOnFlip:
            theseKeys = RESPUESTAWELCOME_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _RESPUESTAWELCOME_2_allKeys.extend(theseKeys)
            if len(_RESPUESTAWELCOME_2_allKeys):
                RESPUESTAWELCOME_2.keys = _RESPUESTAWELCOME_2_allKeys[-1].name  # just the last key pressed
                RESPUESTAWELCOME_2.rt = _RESPUESTAWELCOME_2_allKeys[-1].rt
                RESPUESTAWELCOME_2.duration = _RESPUESTAWELCOME_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *Welcome_2* updates
        
        # if Welcome_2 is starting this frame...
        if Welcome_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome_2.frameNStart = frameN  # exact frame index
            Welcome_2.tStart = t  # local t and not account for scr refresh
            Welcome_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Welcome_2.started')
            # update status
            Welcome_2.status = STARTED
            Welcome_2.setAutoDraw(True)
        
        # if Welcome_2 is active this frame...
        if Welcome_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=WELCOME1,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            WELCOME1.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if WELCOME1.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in WELCOME1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WELCOME1" ---
    for thisComponent in WELCOME1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for WELCOME1
    WELCOME1.tStop = globalClock.getTime(format='float')
    WELCOME1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('WELCOME1.stopped', WELCOME1.tStop)
    # check responses
    if RESPUESTAWELCOME_2.keys in ['', [], None]:  # No response was made
        RESPUESTAWELCOME_2.keys = None
    thisExp.addData('RESPUESTAWELCOME_2.keys',RESPUESTAWELCOME_2.keys)
    if RESPUESTAWELCOME_2.keys != None:  # we had a response
        thisExp.addData('RESPUESTAWELCOME_2.rt', RESPUESTAWELCOME_2.rt)
        thisExp.addData('RESPUESTAWELCOME_2.duration', RESPUESTAWELCOME_2.duration)
    thisExp.nextEntry()
    # the Routine "WELCOME1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ENSAYO = data.TrialHandler2(
        name='ENSAYO',
        nReps=10, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('CONDICIONES.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(ENSAYO)  # add the loop to the experiment
    thisENSAYO = ENSAYO.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisENSAYO.rgb)
    if thisENSAYO != None:
        for paramName in thisENSAYO:
            globals()[paramName] = thisENSAYO[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisENSAYO in ENSAYO:
        ENSAYO.status = STARTED
        if hasattr(thisENSAYO, 'status'):
            thisENSAYO.status = STARTED
        currentLoop = ENSAYO
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisENSAYO.rgb)
        if thisENSAYO != None:
            for paramName in thisENSAYO:
                globals()[paramName] = thisENSAYO[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[SEÑALGRAFICA, SEÑALAUDITIVA, RESPUESTASEÑAL, FIJACION],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        SEÑALGRAFICA.setOpacity(opacidad_texto)
        SEÑALAUDITIVA.setSound('datos/AUDIOREACCIOn.mp3', secs=1.0, hamming=True)
        SEÑALAUDITIVA.setVolume(volumen_audio, log=False)
        SEÑALAUDITIVA.seek(0)
        # create starting attributes for RESPUESTASEÑAL
        RESPUESTASEÑAL.keys = []
        RESPUESTASEÑAL.rt = []
        _RESPUESTASEÑAL_allKeys = []
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        thisExp.currentRoutine = trial
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisENSAYO, 'status') and thisENSAYO.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *SEÑALGRAFICA* updates
            
            # if SEÑALGRAFICA is starting this frame...
            if SEÑALGRAFICA.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                SEÑALGRAFICA.frameNStart = frameN  # exact frame index
                SEÑALGRAFICA.tStart = t  # local t and not account for scr refresh
                SEÑALGRAFICA.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SEÑALGRAFICA, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SEÑALGRAFICA.started')
                # update status
                SEÑALGRAFICA.status = STARTED
                SEÑALGRAFICA.setAutoDraw(True)
            
            # if SEÑALGRAFICA is active this frame...
            if SEÑALGRAFICA.status == STARTED:
                # update params
                pass
            
            # if SEÑALGRAFICA is stopping this frame...
            if SEÑALGRAFICA.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SEÑALGRAFICA.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    SEÑALGRAFICA.tStop = t  # not accounting for scr refresh
                    SEÑALGRAFICA.tStopRefresh = tThisFlipGlobal  # on global time
                    SEÑALGRAFICA.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SEÑALGRAFICA.stopped')
                    # update status
                    SEÑALGRAFICA.status = FINISHED
                    SEÑALGRAFICA.setAutoDraw(False)
            
            # *SEÑALAUDITIVA* updates
            
            # if SEÑALAUDITIVA is starting this frame...
            if SEÑALAUDITIVA.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                SEÑALAUDITIVA.frameNStart = frameN  # exact frame index
                SEÑALAUDITIVA.tStart = t  # local t and not account for scr refresh
                SEÑALAUDITIVA.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('SEÑALAUDITIVA.started', tThisFlipGlobal)
                # update status
                SEÑALAUDITIVA.status = STARTED
                SEÑALAUDITIVA.play(when=win)  # sync with win flip
            
            # if SEÑALAUDITIVA is stopping this frame...
            if SEÑALAUDITIVA.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SEÑALAUDITIVA.tStartRefresh + 1.0-frameTolerance or SEÑALAUDITIVA.isFinished:
                    # keep track of stop time/frame for later
                    SEÑALAUDITIVA.tStop = t  # not accounting for scr refresh
                    SEÑALAUDITIVA.tStopRefresh = tThisFlipGlobal  # on global time
                    SEÑALAUDITIVA.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'SEÑALAUDITIVA.stopped')
                    # update status
                    SEÑALAUDITIVA.status = FINISHED
                    SEÑALAUDITIVA.stop()
            
            # *RESPUESTASEÑAL* updates
            waitOnFlip = False
            
            # if RESPUESTASEÑAL is starting this frame...
            if RESPUESTASEÑAL.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                RESPUESTASEÑAL.frameNStart = frameN  # exact frame index
                RESPUESTASEÑAL.tStart = t  # local t and not account for scr refresh
                RESPUESTASEÑAL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RESPUESTASEÑAL, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RESPUESTASEÑAL.started')
                # update status
                RESPUESTASEÑAL.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(RESPUESTASEÑAL.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(RESPUESTASEÑAL.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if RESPUESTASEÑAL.status == STARTED and not waitOnFlip:
                theseKeys = RESPUESTASEÑAL.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _RESPUESTASEÑAL_allKeys.extend(theseKeys)
                if len(_RESPUESTASEÑAL_allKeys):
                    RESPUESTASEÑAL.keys = _RESPUESTASEÑAL_allKeys[-1].name  # just the last key pressed
                    RESPUESTASEÑAL.rt = _RESPUESTASEÑAL_allKeys[-1].rt
                    RESPUESTASEÑAL.duration = _RESPUESTASEÑAL_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *FIJACION* updates
            
            # if FIJACION is starting this frame...
            if FIJACION.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FIJACION.frameNStart = frameN  # exact frame index
                FIJACION.tStart = t  # local t and not account for scr refresh
                FIJACION.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FIJACION, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FIJACION.started')
                # update status
                FIJACION.status = STARTED
                FIJACION.setAutoDraw(True)
            
            # if FIJACION is active this frame...
            if FIJACION.status == STARTED:
                # update params
                pass
            
            # if FIJACION is stopping this frame...
            if FIJACION.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FIJACION.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    FIJACION.tStop = t  # not accounting for scr refresh
                    FIJACION.tStopRefresh = tThisFlipGlobal  # on global time
                    FIJACION.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'FIJACION.stopped')
                    # update status
                    FIJACION.status = FINISHED
                    FIJACION.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        SEÑALAUDITIVA.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if RESPUESTASEÑAL.keys in ['', [], None]:  # No response was made
            RESPUESTASEÑAL.keys = None
        ENSAYO.addData('RESPUESTASEÑAL.keys',RESPUESTASEÑAL.keys)
        if RESPUESTASEÑAL.keys != None:  # we had a response
            ENSAYO.addData('RESPUESTASEÑAL.rt', RESPUESTASEÑAL.rt)
            ENSAYO.addData('RESPUESTASEÑAL.duration', RESPUESTASEÑAL.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisENSAYO as finished
        if hasattr(thisENSAYO, 'status'):
            thisENSAYO.status = FINISHED
        # if awaiting a pause, pause now
        if ENSAYO.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            ENSAYO.status = STARTED
        thisExp.nextEntry()
        
    # completed 3 repeats of 'ENSAYO'
    ENSAYO.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "DESPEDIDA" ---
    # create an object to store info about Routine DESPEDIDA
    DESPEDIDA = data.Routine(
        name='DESPEDIDA',
        components=[DESPEDIDA1, RESPUESTADESPEDIDA],
    )
    DESPEDIDA.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for RESPUESTADESPEDIDA
    RESPUESTADESPEDIDA.keys = []
    RESPUESTADESPEDIDA.rt = []
    _RESPUESTADESPEDIDA_allKeys = []
    # store start times for DESPEDIDA
    DESPEDIDA.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    DESPEDIDA.tStart = globalClock.getTime(format='float')
    DESPEDIDA.status = STARTED
    thisExp.addData('DESPEDIDA.started', DESPEDIDA.tStart)
    DESPEDIDA.maxDuration = None
    # keep track of which components have finished
    DESPEDIDAComponents = DESPEDIDA.components
    for thisComponent in DESPEDIDA.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "DESPEDIDA" ---
    thisExp.currentRoutine = DESPEDIDA
    DESPEDIDA.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DESPEDIDA1* updates
        
        # if DESPEDIDA1 is starting this frame...
        if DESPEDIDA1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DESPEDIDA1.frameNStart = frameN  # exact frame index
            DESPEDIDA1.tStart = t  # local t and not account for scr refresh
            DESPEDIDA1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DESPEDIDA1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DESPEDIDA1.started')
            # update status
            DESPEDIDA1.status = STARTED
            DESPEDIDA1.setAutoDraw(True)
        
        # if DESPEDIDA1 is active this frame...
        if DESPEDIDA1.status == STARTED:
            # update params
            pass
        
        # *RESPUESTADESPEDIDA* updates
        waitOnFlip = False
        
        # if RESPUESTADESPEDIDA is starting this frame...
        if RESPUESTADESPEDIDA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RESPUESTADESPEDIDA.frameNStart = frameN  # exact frame index
            RESPUESTADESPEDIDA.tStart = t  # local t and not account for scr refresh
            RESPUESTADESPEDIDA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RESPUESTADESPEDIDA, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'RESPUESTADESPEDIDA.started')
            # update status
            RESPUESTADESPEDIDA.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RESPUESTADESPEDIDA.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RESPUESTADESPEDIDA.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RESPUESTADESPEDIDA.status == STARTED and not waitOnFlip:
            theseKeys = RESPUESTADESPEDIDA.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _RESPUESTADESPEDIDA_allKeys.extend(theseKeys)
            if len(_RESPUESTADESPEDIDA_allKeys):
                RESPUESTADESPEDIDA.keys = _RESPUESTADESPEDIDA_allKeys[-1].name  # just the last key pressed
                RESPUESTADESPEDIDA.rt = _RESPUESTADESPEDIDA_allKeys[-1].rt
                RESPUESTADESPEDIDA.duration = _RESPUESTADESPEDIDA_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=DESPEDIDA,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            DESPEDIDA.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if DESPEDIDA.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in DESPEDIDA.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "DESPEDIDA" ---
    for thisComponent in DESPEDIDA.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for DESPEDIDA
    DESPEDIDA.tStop = globalClock.getTime(format='float')
    DESPEDIDA.tStopRefresh = tThisFlipGlobal
    thisExp.addData('DESPEDIDA.stopped', DESPEDIDA.tStop)
    # check responses
    if RESPUESTADESPEDIDA.keys in ['', [], None]:  # No response was made
        RESPUESTADESPEDIDA.keys = None
    thisExp.addData('RESPUESTADESPEDIDA.keys',RESPUESTADESPEDIDA.keys)
    if RESPUESTADESPEDIDA.keys != None:  # we had a response
        thisExp.addData('RESPUESTADESPEDIDA.rt', RESPUESTADESPEDIDA.rt)
        thisExp.addData('RESPUESTADESPEDIDA.duration', RESPUESTADESPEDIDA.duration)
    thisExp.nextEntry()
    # the Routine "DESPEDIDA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
