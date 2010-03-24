/* GemRB - Infinity Engine Emulator
 * Copyright (C) 2003 The GemRB Project
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * $Id$
 *
 */

/**
 * @file MoviePlayer.h
 * Declares MoviePlayer class, abstract loader and player for videos
 * @author The GemRB Project
 */


#ifndef MOVIEPLAYER_H
#define MOVIEPLAYER_H

#include "../../includes/win32def.h"
#include "../../includes/globals.h"
#include "Resource.h"


/**
 * @class MoviePlayer
 * Abstract loader and player for videos
 */

class GEM_EXPORT MoviePlayer : public Resource {
public:
	static const TypeID ID;
	MoviePlayer(void);
	virtual ~MoviePlayer(void);
	virtual int Play() = 0;
	virtual void CallBackAtFrames(ieDword cnt, ieDword *frames, ieDword *strrefs) = 0;
};

#endif
