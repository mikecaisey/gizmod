    /**
  *********************************************************************
*************************************************************************
*** 
*** \file  GizmoEventPowermate.cpp
*** \brief GizmoEventPowermate class body
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

#include "GizmoEventPowermate.hpp"
#include "GizmoLinuxInputDevice.hpp"
#include "../libH/Debug.hpp"
#include "../libH/Exception.hpp"
#include "../libH/Util.hpp"
#include <boost/bind.hpp>

using namespace std;
using namespace boost;
using namespace H;
using namespace Gizmod;

////////////////////////////////////////////////////////////////////////////
// Type Defs
///////////////////////////////////////

////////////////////////////////////////////////////////////////////////////
// Construction
///////////////////////////////////////

/**
 * \brief GizmoEventPowermate Default Constructor
**/
GizmoEventPowermate::GizmoEventPowermate() : GizmoEvent(GIZMO_EVENTCLASS_POWERMATE, false) {
	ClickTime = 0.0f;
}

/**
 * \brief GizmoEventPowermate Init Constructor
**/
GizmoEventPowermate::GizmoEventPowermate(struct input_event const & InputEvent, bool IsRemote) : GizmoEvent(GIZMO_EVENTCLASS_POWERMATE, IsRemote), GizmoLinuxInputEvent(InputEvent) {
	ClickTime = 0.0f;
}

/**
 * \brief GizmoEventPowermate Destructor
**/
GizmoEventPowermate::~GizmoEventPowermate() {
	ClickTime = 0.0f;
}

////////////////////////////////////////////////////////////////////////////
// Class Body
///////////////////////////////////////

/**
 * \brief  Build an event vector from a read buffer
 * \param  EventVector Reference to a vector which will contain the results
 * \param  Buffer The bufer to convert into events
 * \param  SendNullEvents Signals if NULL events should be passed onto the config script
**/
void GizmoEventPowermate::buildEventsVectorFromBuffer(std::vector< boost::shared_ptr<GizmoEventPowermate> > & EventVector, H::DynamicBuffer<char> const & Buffer, bool SendNullEvents) {
	std::vector<struct input_event> InputEvents;
	GizmoLinuxInputDevice::buildInputEventsVectorFromBuffer(InputEvents, Buffer);
	apply_static_func_args(InputEvents, GizmoEventPowermate::buildEventsVectorFromBufferFunctor, &EventVector, SendNullEvents);
}

/**
 * \brief  Functor for building events from Linnux input_events
**/
void GizmoEventPowermate::buildEventsVectorFromBufferFunctor(struct input_event & InputEvent, std::vector< boost::shared_ptr<GizmoEventPowermate> > * pEventVector, bool SendNullEvents) {
	if ( (!SendNullEvents) && (InputEvent.type == 0) && (InputEvent.code == 0) && (InputEvent.value == 0) )
		return;
	pEventVector->push_back(boost::shared_ptr<GizmoEventPowermate>(new GizmoEventPowermate(InputEvent)));
}
