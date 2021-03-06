    #***
  #*********************************************************************
#*************************************************************************
#*** 
#*** GizmoDaemon Config Script
#*** 	Powermate Firefox config
#***
#*****************************************
  #*****************************************
    #***

"""

  Copyright (c) 2007, Gizmo Daemon Team
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at 

	http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and 
  limitations under the License. 
  
"""

############################
# Imports
##########################

from GizmoDaemon import *
from GizmoScriptActiveApplication import *

ENABLED = True
VERSION_NEEDED = 3.2
INTERESTED_CLASSES = [GizmoEventClass.Powermate]
INTERESTED_WINDOWS = ["firefox", "swiftfox", "iceweasel"]

############################
# PowermateFirefox Class definition
##########################

class PowermateFirefox(GizmoScriptActiveApplication):
	"""
	Firefox Powermate Event Mapping
	"""
	
	############################
	# Public Functions
	##########################
			
	def onDeviceEvent(self, Event, Gizmo = None):
		"""
		Called from Base Class' onEvent method.
		See GizmodDispatcher.onEvent documention for an explanation of this function
		"""
		
	   	# Only interact with Firefox if it's the first Powermate
	  	if Gizmo.DeviceClassID == 0:
		   	# Check for rotations
			if Event.Type == GizmoEventType.EV_REL:
				# scroll the window slowly if the button isn't pressed
				# and fast if the button is down
				if not Gizmo.getKeyState(GizmoKey.BTN_0):
					# scroll slowly (create a mouse wheel event)
					Gizmod.Mice[0].createEventRaw(GizmoEventType.EV_REL, GizmoMouseAxis.WHEEL, -Event.Value)
				else:
					# scroll quickly (by pages using the page up / page down keys)
					if Event.Value > 0:
						for repeat in range(abs(Event.Value)):
							Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_PAGEDOWN)
					else:
						for repeat in range(abs(Event.Value)):
							Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_PAGEUP)
				return True
			# check for button press
			elif Event.Type == GizmoEventType.EV_KEY:
				if Event.Value == 0 and not Gizmo.Rotated:
					# issue a close tab if the button is pressed
					Gizmod.Keyboards[0].createEvent(GizmoEventType.EV_KEY, GizmoKey.KEY_W, [GizmoKey.KEY_LEFTCTRL])
					return True
			else:
				return False
		else:
			return False
	
	############################
	# Private Functions
	##########################

	def __init__(self):
		""" 
		Default Constructor
		"""
		
		GizmoScriptActiveApplication.__init__(self, ENABLED, VERSION_NEEDED, INTERESTED_CLASSES, INTERESTED_WINDOWS)

############################
# PowermateFirefox class end
##########################

# register the user script
PowermateFirefox()
