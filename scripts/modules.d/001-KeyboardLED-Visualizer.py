    #***
  #*********************************************************************
#*************************************************************************
#*** 
#*** GizmoDaemon Config Script
#*** 	Keyboard Visualization config
#***
#*****************************************
  #*****************************************
    #***

############################
# Imports
##########################

from GizmoDaemon import *
from GizmoDeviceStrings import *
from VisualizerDefault import *
import sys

ENABLED = True
VERSION_NEEDED = 3.1

############################
# KeyboardVisualizer Class definition
##########################

class KeyboardVisualizer(VisualizerDefault):
	"""
	Keyboard Visualization Handler
	"""
	
	############################
	# Public Functions
	##########################
	
	def applyVisualizationCPUUsage(self, Event):
		"""
		Set the Keyboards' LEDs to the current system CPU Usage
		"""
		
		self.__setLEDsPercent(Event.getCPUUsageAvg(0))
		
	def applyVisualizationVolume(self):
		"""
		Set the Keyboards' LEDs to the Default playback volume mixer's level
		"""

		# make sure there's a mixer available		
		if not Gizmod.DefaultMixerVolume:
			return
			
		# update the Keyboards' LEDs
		if Gizmod.DefaultMixerSwitch.SwitchPlayback:
			# if not muted set LED to volume level
			self.__setLEDsPercent(Gizmod.DefaultMixerVolume.VolumePlaybackPercent)
		else:
			# if muted pulse the led
			for i in range(len(LEDS)):
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_LED, i, 0)
			
	def applyVisualizationSound(self, Event):
		"""
		Set the Keyboards' LEDs to the sound level
		"""
		
		self.__setLEDsPercent(Event.VUCombined * 100.0)

	############################
	# Private Functions
	##########################
	
	def __setLEDsPercent(self, Percent):
		"""
		Set the keyboard LEDs to a percentage
		"""
		
		CurVal = 0
		for i in range(len(KEYBOARD_LEDS)):
			if Percent >= CurVal and Percent >= 7.5:
				if self.LEDs[i] != 1:
					Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_LED, KEYBOARD_LEDS[i], 1)
					self.LEDs[i] = 1
			else:
				if self.LEDs[i] != 0:
					Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_LED, KEYBOARD_LEDS[i], 0)
					self.LEDs[i] = 0
			CurVal += self.RangePerLED	
	
	def __init__(self):
		""" 
		Default Constructor
		"""

		# call base constructor
		VisualizerDefault.__init__(self)
		
		# print informative text		
		Gizmod.printNiceScriptInit(1, self.__class__.__name__, self.__class__.__doc__, str(len(Gizmod.Keyboards)) + " Keyboards")

		# initialize member variables
		self.RangePerLED = 100.0 / float(len(KEYBOARD_LEDS))
		
		# so we only set LED states when neccessery
		self.LEDs = []
		for i in range(len(KEYBOARD_LEDS)):
			self.LEDs.append(0)
			Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_LED, i, 0)

############################
# KeyboardVisualization class end
##########################

# register the user script
if ENABLED:
	if not Gizmod.checkVersion(VERSION_NEEDED, False):
		Gizmod.printNiceScriptInit(1, " * KeyboardVisualizer", "NOT LOADED", "Version Needed: " + str(VERSION_NEEDED))
	else:
		Gizmod.Dispatcher.userScripts.append(KeyboardVisualizer())
