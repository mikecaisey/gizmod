    /**
  *********************************************************************
*************************************************************************
*** 
*** \file  stringconverter.hpp
*** \brief stringconverter class header
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

#ifndef __stringconverter_h
#define __stringconverter_h

#if HAVE_CONFIG_H
#include "config.h"
#endif

#include <string>

//////////////////////////////////////////////////////////////////////////////
// Namespace
///////////////////////////////////////

namespace H {

//////////////////////////////////////////////////////////////////////////////
// Class Definition
///////////////////////////////////////

/**
 * \class stringconverter
 * \brief Generic stringconverter class
 *
 * Converts various datatypes to string
 */
class stringconverter : public std::string {
public:	
	// public functions
	
	// construction / deconstruction
	stringconverter(int Value);
	virtual ~stringconverter() throw() ;
	
	// static public functions
	static std::string			toLower(std::string const & convertee);	///< Convert a string to lower case
	static std::string			toUpper(std::string const & convertee);	///< Convert a string to upper case

	/// Helper for ToLower case conversions
	struct ToLower { /** Conver to Lower */ char operator() (char c) const  { return std::tolower(c); } };
	
	///< Helper for ToUpper case conversions
	struct ToUpper { /** Conver to Upper */ char operator() (char c) const  { return std::toupper(c); } };
};

//////////////////////////////////////////////////////////////////////////////

}

#endif // __stringconverter_h
