    #***
  #*********************************************************************
#*************************************************************************
#*** 
#*** GizmoDaemon Config Script v3:0
#*** 	LIRCHauppauge Mplayer config
#***
#*****************************************
  #*****************************************
    #***

############################
# Imports
##########################

from GizmoDaemon import *
from Hauppauge import *
import subprocess

ENABLED = True
INTERESTED_CLASSES = [GizmoEventClass.LIRC]
INTERESTED_WINDOWS = ["mplayer"]

############################
# LIRCHauppaugeMplayer Class definition
##########################

class LIRCHauppaugeMplayer(Hauppauge):
	"""
	Event mapping for LIRC when using Mplayer with the Hauppauge remote
	"""
	
	############################
	# Public Functions
	##########################
			
	def onEvent(self, Event, Gizmo = None):
		"""
		See GizmodDispatcher.onEvent documention for an explanation of this function
		"""
		
		# if the event class is in INTERESTED_CLASSES and the active window is
		# one of INTERESTED_WINDOWS and there is a keyboard and mouse attached 
		# then process the event
		if Event.Class in INTERESTED_CLASSES and \
		   [i for i in INTERESTED_WINDOWS if Gizmod.CurrentFocus.WindowName.lower().find(i) > -1] and \
		   len(Gizmod.Mice) and len(Gizmod.Keyboards):
			# process the key
		   	KeyString = self.getKeyString(Event)
		   	if KeyString == "Go":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_A)
		   		return True
		   	elif KeyString == "Power":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_ESC)
		   		return True
		   	elif KeyString == "TV":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_B)
		   		return True
		   	elif KeyString == "Videos":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_V)
		   		return True
		   	elif KeyString == "Music":		   	
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHTSHIFT, 1)
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_SLASH)
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHTSHIFT, 0)
		   		return True
		   	elif KeyString == "Pictures":
		   		return False
		   	elif KeyString == "Guide":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_S)
		   		return True
		   	elif KeyString == "Up":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_UP)
		   		return True
		   	elif KeyString == "Radio":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_N)
		   		return True
		   	elif KeyString == "Left":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_LEFT)
		   		return True
		   	elif KeyString == "OK":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_ENTER)
		   		return True
		   	elif KeyString == "Right":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHT)
		   		return True
		   	elif KeyString == "Back/Exit":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_ESC)
		   		return True
		   	elif KeyString == "Down":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_DOWN)
		   		return True
		   	elif KeyString == "Menu":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_O)
		   		return True
		   	elif KeyString == "VolUp":
		   		return False
		   	elif KeyString == "VolDown":
		   		return False
		   	elif KeyString == "Prev.Ch":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_H)
		   		return True
		   	elif KeyString == "Mute":
		   		return False
		   	elif KeyString == "ChUp":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_UP)
		   		return True
		   	elif KeyString == "ChDown":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_DOWN)
		   		return True
		   	elif KeyString == "Rec":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_R)
		   		return True
		   	elif KeyString == "Stop":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_S)
		   		return True
		   	elif KeyString == "Rewind":
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHTSHIFT, 1)
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_COMMA)
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHTSHIFT, 0)
		   		return True
		   	elif KeyString == "Play":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_SPACE)
		   		return True
		   	elif KeyString == "FastForward":
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHTSHIFT, 1)
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_DOT)
				Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_RIGHTSHIFT, 0)
		   		return True
		   	elif KeyString == "Replay":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_PAGEDOWN)
		   		return True
		   	elif KeyString == "Pause":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_SPACE)
		   		return True
		   	elif KeyString == "Skip":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_PAGEUP)
		   		return True
		   	elif KeyString == "1":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_1)
		   		return True
		   	elif KeyString == "2":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_2)
		   		return True
		   	elif KeyString == "3":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_3)
		   		return True
		   	elif KeyString == "4":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_4)
		   		return True
		   	elif KeyString == "5":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_5)
		   		return True
		   	elif KeyString == "6":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_6)
		   		return True
		   	elif KeyString == "7":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_7)
		   		return True
		   	elif KeyString == "8":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_8)
		   		return True
		   	elif KeyString == "9":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_9)
		   		return True
		   	elif KeyString == "*":
		   		return False
		   	elif KeyString == "0":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_0)
		   		return True
		   	elif KeyString == "#":
		   		return False
		   	elif KeyString == "Red":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_END)
		   		return True
		   	elif KeyString == "Green":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_HOME)
		   		return True
		   	elif KeyString == "Yellow":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_C)
		   		return True
		   	elif KeyString == "Blue":
				Gizmod.Keyboards[0].createEventPress(GizmoEventType.EV_KEY, GizmoKey.KEY_I)
		   		return True
		   	else:
		   		# unmatched event, keep processing
				return False				
		# event not of interest
		return False
	
	############################
	# Private Functions
	##########################

	def __init__(self):
		""" 
		Default Constructor
		"""
		
		Hauppauge.__init__(self)
		print "Loaded User Script: " + self.__class__.__name__

############################
# LIRCHauppaugeMplayer class end
##########################

# register the user script
if ENABLED:
	Gizmod.Dispatcher.userScripts.append(LIRCHauppaugeMplayer())
