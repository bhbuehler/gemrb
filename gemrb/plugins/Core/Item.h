/* GemRB - Infinity Engine Emulator
 * Copyright (C) 2003 The GemRB Project
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 * $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/plugins/Core/Item.h,v 1.6 2004/11/07 19:19:12 edheldil Exp $
 *
 */

#ifndef ITEM_H
#define ITEM_H

#include <vector>
#include "../../includes/ie_types.h"

#include "AnimationMgr.h"


#ifdef WIN32

#ifdef GEM_BUILD_DLL
#define GEM_EXPORT __declspec(dllexport)
#else
#define GEM_EXPORT __declspec(dllimport)
#endif

#else
#define GEM_EXPORT
#endif

// Item Flags bits
// !!! Keep these synchronized with GUIDefines.h !!!
#define IE_ITEM_CRITICAL     0x00000001
#define IE_ITEM_TWO_HANDED   0x00000002
#define IE_ITEM_MOVABLE      0x00000004
#define IE_ITEM_DIITMAYABLE  0x00000008
#define IE_ITEM_CURSED       0x00000010
#define IE_ITEM_NOT_COPYABLE 0x00000020
#define IE_ITEM_MAGICAL      0x00000040
#define IE_ITEM_BOW          0x00000080
#define IE_ITEM_SILVER       0x00000100
#define IE_ITEM_COLD_IRON    0x00000200
#define IE_ITEM_STOLEN       0x00000400
#define IE_ITEM_CONVERSABLE  0x00000800
#define IE_ITEM_PULSATING    0x00001000
#define IE_ITEM_UNSELLABLE   ( IE_ITEM_CRITICAL | IE_ITEM_STOLEN )


// the same as ITMFeature
typedef struct ITMFeature {
	ieWord Opcode;
	ieByte Target;
	ieByte Power;
	ieDword Parameter1;
	ieDword Parameter2;
	ieByte TimingMode;
	ieByte Resistance;
	ieDword Duration;
	ieByte Probability1;
	ieByte Probability2;
	ieResRef Resource;
	ieDword DiceThrown;
	ieDword DiceSides;
	ieDword SavingThrowType;
	ieDword SavingThrowBonus;
	ieDword unknown;
} ITMFeature;

class GEM_EXPORT ITMExtHeader {
public:
        ITMExtHeader();
        ~ITMExtHeader();
	ieByte AttackType;
	ieByte IDReq;
	ieByte Location;
	ieByte unknown1;
	ieResRef UseIcon;
	ieByte Target;
	ieByte TargetNumber;
	ieWord Range;
	ieWord ProjectileType;
	ieWord Speed;
	ieWord THAC0Bonus;
	ieWord DiceSides;
	ieWord DiceThrown;
	ieWord DamageBonus;
	ieWord DamageType;
	ieWord FeatureCount;
	ieWord FeatureOffset;
	ieWord Charges;
	ieWord ChargeDepletion;
	ieByte UseStrengthBonus;
	ieByte Recharge;
	ieWord unknown2;
	ieWord ProjectileAnimation;
	ieWord MeleeAnimation[3];
	ieWord BowArrowQualifier;
	ieWord CrossbowBoltQualifier;
	ieWord MiscProjectileQualifier;
	std::vector< ITMFeature*> features;
};


class GEM_EXPORT Item {
public:
	Item();
	~Item();

	std::vector< ITMExtHeader*> ext_headers;
	std::vector< ITMFeature*> equipping_features;

	ieStrRef ItemName;
	ieStrRef ItemNameIdentified;
	ieResRef ReplacementItem;
	ieDword Flags;
	ieWord ItemType;
	ieDword UsabilityBitmask;
	char InventoryIconType[2];
	ieWord MinLevel;
	ieWord MinStrength;
	ieWord MinStrengthBonus;
	ieWord MinIntelligence;
	ieWord MinDexterity;
	ieWord MinWisdom;
	ieWord MinConstitution;
	ieWord MinCharisma;
	ieDword Price;
	ieWord StackAmount;
	ieResRef ItemIcon;
	ieWord LoreToID;
	ieResRef GroundIcon;
	ieDword Weight;
	ieStrRef ItemDesc;
	ieStrRef ItemDescIdentified;
	ieResRef CarriedIcon;
	ieDword Enchantment;
	ieDword ExtHeaderOffset;
	ieWord ExtHeaderCount;
	ieDword FeatureBlockOffset;
	ieWord EquippingFeatureOffset;
	ieWord EquippingFeatureCount;

	// PST only
	ieResRef Dialog;
	ieStrRef DialogName;
	ieWord WieldColor;

	// PST and IWD2 only
	char unknown[26];

	AnimationMgr* ItemIconBAM;
	AnimationMgr* GroundIconBAM;
	AnimationMgr* CarriedIconBAM;
};

#endif  // ! ITEM_H
