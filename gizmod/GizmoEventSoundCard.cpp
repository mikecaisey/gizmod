    /**
  *********************************************************************
*************************************************************************
*** 
*** \file  GizmoEventSoundCard.cpp
*** \brief GizmoEventSoundCard class body
***
*****************************************
  *****************************************
    **/

/*
  
  Copyright (c) 2007, Tim Burrell
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at 

	http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and 
  limitations under the License. 
  
*/

#include "GizmoEventSoundCard.hpp"
#include "../libH/Debug.hpp"
#include "../libH/Exception.hpp"
#include <boost/shared_ptr.hpp>

using namespace std;
using namespace boost;
using namespace H;

////////////////////////////////////////////////////////////////////////////
// Type Defs
///////////////////////////////////////

/**
 * \def   GIZMO_EVENT_SOUNDCARD_TYPE
 * \brief String type of this event
 */
#define GIZMO_EVENT_SOUNDCARD_TYPE	"SoundCard"

////////////////////////////////////////////////////////////////////////////
// Construction
///////////////////////////////////////

/**
 * \brief GizmoEventSoundCard Default Constructor
 */
GizmoEventSoundCard::GizmoEventSoundCard() : GizmoEvent(GIZMO_EVENTCLASS_SOUNDCARD) {
}

/**
 * \brief GizmoEventSoundCard Destructor
 */
GizmoEventSoundCard::~GizmoEventSoundCard() {
}

////////////////////////////////////////////////////////////////////////////
// Class Body
///////////////////////////////////////

/**
 * \brief  Get the type of this Gizmo
 * \return Type of the Gizmo
 */
std::string GizmoEventSoundCard::getEventType() {
	return GIZMO_EVENT_SOUNDCARD_TYPE;
}
