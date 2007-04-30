    /**
  *********************************************************************
*************************************************************************
*** 
*** \file  GizmoEventCPU.cpp
*** \brief GizmoEventCPU class body
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

#include "GizmoEventCPU.hpp"
#include "../libH/Debug.hpp"
#include "../libH/Exception.hpp"
#include <boost/shared_ptr.hpp>

using namespace std;
using namespace boost;
using namespace H;

////////////////////////////////////////////////////////////////////////////
// Type Defs
///////////////////////////////////////

////////////////////////////////////////////////////////////////////////////
// Construction
///////////////////////////////////////

/**
 * \brief GizmoEventCPU Default Constructor
 */
GizmoEventCPU::GizmoEventCPU() : GizmoEvent(GIZMO_EVENTCLASS_CPU) {
}

/**
 * \brief GizmoEventCPU Destructor
 */
GizmoEventCPU::~GizmoEventCPU() {
}

////////////////////////////////////////////////////////////////////////////
// Class Body
///////////////////////////////////////
