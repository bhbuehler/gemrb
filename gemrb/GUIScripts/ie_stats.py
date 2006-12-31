# -*-python-*-
# GemRB - Infinity Engine Emulator
# Copyright (C) 2003 The GemRB Project
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# $Header: /data/gemrb/cvs2svn/gemrb/gemrb/gemrb/GUIScripts/ie_stats.py,v 1.11 2006/12/31 15:09:35 avenger_teambg Exp $

# ie_stats.py - definitions of creature stats codes

# !!! NOTE: Keep this file synchronized with gemrb/includes/ie_stats.h !!!

# EA values
INANIMATE     = 1
PC            = 2
FAMILIAR      = 3
ALLY          = 4
CONTROLLED    = 5
CHARMED       = 6
GOODBUTRED    = 28
GOODBUTBLUE   = 29
GOODCUTOFF    = 30
NOTGOOD       = 31
ANYTHING      = 126
NEUTRAL       = 128
NOTEVIL       = 199
EVILCUTOFF    = 200
EVILBUTGREEN  = 201
EVILBUTBLUE   = 202
ENEMY         = 255

# state bits (IE_STATE)
STATE_DEAD    = 2048

MC_FALLEN_PALADIN = 0x200
MC_FALLEN_RANGER = 0x400
MC_EXPORTABLE = 0x800

# stats
IE_HITPOINTS 			= 0
IE_MAXHITPOINTS			= 1
IE_ARMORCLASS 			= 2
IE_ACCRUSHINGMOD 		= 3
IE_ACMISSILEMOD 		= 4
IE_ACPIERCINGMOD 		= 5
IE_ACSLASHINGMOD 		= 6
IE_THAC0 			= 7
IE_NUMBEROFATTACKS 		= 8
IE_SAVEVSDEATH 			= 9
IE_SAVEVSWANDS 			= 10
IE_SAVEVSPOLY 			= 11
IE_SAVEVSBREATH 		= 12
IE_SAVEVSSPELL 			= 13
IE_RESISTFIRE 			= 14
IE_RESISTCOLD 			= 15
IE_RESISTELECTRICITY 		= 16
IE_RESISTACID 			= 17
IE_RESISTMAGIC 			= 18
IE_RESISTMAGICFIRE 		= 19
IE_RESISTMAGICCOLD 		= 20
IE_RESISTSLASHING 		= 21
IE_RESISTCRUSHING 		= 22
IE_RESISTPIERCING 		= 23
IE_RESISTMISSILE 		= 24
IE_LORE 			= 25
IE_LOCKPICKING 			= 26
IE_STEALTH 			= 27
IE_TRAPS 			= 28
IE_PICKPOCKET 			= 29
IE_FATIGUE 			= 30
IE_INTOXICATION 		= 31
IE_LUCK 			= 32
IE_TRACKING 			= 33
IE_LEVEL 			= 34
IE_SEX 				= 35
IE_STR 				= 36
IE_STREXTRA 			= 37
IE_INT 				= 38
IE_WIS 				= 39
IE_DEX 				= 40
IE_CON 				= 41
IE_CHR 				= 42
IE_XPVALUE 			= 43
IE_XP 				= 44
IE_GOLD 			= 45
IE_MORALEBREAK 			= 46
IE_MORALERECOVERYTIME 		= 47
IE_REPUTATION 			= 48
IE_HATEDRACE 			= 49
IE_DAMAGEBONUS 			= 50
IE_SPELLFAILUREMAGE 		= 51
IE_SPELLFAILUREPRIEST 		= 52
IE_SPELLDURATIONMODMAGE 	= 53
IE_SPELLDURATIONMODPRIEST 	= 54
IE_TURNUNDEADLEVEL 		= 55
IE_BACKSTABDAMAGEMULTIPLIER 	= 56
IE_LAYONHANDSAMOUNT 		= 57
IE_HELD 			= 58
IE_POLYMORPHED 			= 59
IE_TRANSLUCENT 			= 60
IE_IDENTIFYMODE 		= 61
IE_ENTANGLE 			= 62
IE_SANCTUARY 			= 63
IE_MINORGLOBE 			= 64
IE_SHIELDGLOBE 			= 65
IE_GREASE 			= 66
IE_WEB 				= 67
IE_LEVEL2 			= 68
IE_LEVEL3 			= 69
IE_CasterHold 			= 70
IE_ENCUMBRANCE                  = 71
IE_MISSILETHAC0BONUS 		= 72  
IE_MAGICDAMAGERESISTANCE 	= 73
IE_RESISTPOISON 		= 74
IE_DONOTJUMP 			= 75
IE_AURACLEANSING 		= 76
IE_MENTALSPEED 			= 77
IE_PHYSICALSPEED 		= 78
IE_CASTINGLEVELBONUSMAGE 	= 79
IE_CASTINGLEVELBONUSCLERIC 	= 80
IE_SEEINVISIBLE 		= 81
IE_IGNOREDIALOGPAUSE 		= 82
IE_MINHITPOINTS 		= 83
IE_THAC0BONUSRIGHT 		= 84
IE_THAC0BONUSLEFT 		= 85
IE_DAMAGEBONUSRIGHT 		= 86
IE_DAMAGEBONUSLEFT 		= 87
IE_STONESKINS 			= 88
IE_PROFICIENCYBASTARDSWORD 	= 89
IE_PROFICIENCYLONGSWORD 	= 90
IE_PROFICIENCYSHORTSWORD 	= 91
IE_PROFICIENCYAXE 		= 92			
IE_PROFICIENCYTWOHANDEDSWORD 	= 93
IE_PROFICIENCYKATANA 		= 94
IE_PROFICIENCYSCIMITARWAKISASHININJATO = 95
IE_PROFICIENCYDAGGER 		= 96
IE_PROFICIENCYWARHAMMER 	= 97
IE_PROFICIENCYSPEAR 		= 98
IE_PROFICIENCYHALBERD 		= 99			
IE_PROFICIENCYFLAILMORNINGSTAR 	= 100
IE_PROFICIENCYMACE 		= 101			
IE_PROFICIENCYQUARTERSTAFF 	= 102		
IE_PROFICIENCYCROSSBOW 		= 103		
IE_PROFICIENCYLONGBOW 		= 104		
IE_PROFICIENCYSHORTBOW 		= 105		
IE_PROFICIENCYDART 		= 106
IE_PROFICIENCYSLING 		= 107	
IE_PROFICIENCYBLACKJACK 	= 108	
IE_PROFICIENCYGUN 		= 109		
IE_PROFICIENCYMARTIALARTS 	= 110	
IE_PROFICIENCY2HANDED 		= 111 
IE_PROFICIENCYSWORDANDSHIELD 	= 112
IE_PROFICIENCYSINGLEWEAPON 	= 113	
IE_PROFICIENCY2WEAPON 		= 114  			
IE_EXTRAPROFICIENCY1 		= 115
IE_EXTRAPROFICIENCY2 		= 116
IE_EXTRAPROFICIENCY3 		= 117
IE_EXTRAPROFICIENCY4 		= 118
IE_EXTRAPROFICIENCY5 		= 119
IE_EXTRAPROFICIENCY6 		= 120
IE_EXTRAPROFICIENCY7 		= 121
IE_EXTRAPROFICIENCY8 		= 122
IE_EXTRAPROFICIENCY9 		= 123
IE_EXTRAPROFICIENCY10 		= 124
IE_EXTRAPROFICIENCY11 		= 125
IE_EXTRAPROFICIENCY12 		= 126
IE_EXTRAPROFICIENCY13 		= 127
IE_EXTRAPROFICIENCY14 		= 128
IE_EXTRAPROFICIENCY15 		= 129
IE_EXTRAPROFICIENCY16 		= 130
IE_EXTRAPROFICIENCY17 		= 131
IE_EXTRAPROFICIENCY18 		= 132
IE_EXTRAPROFICIENCY19 		= 133
IE_EXTRAPROFICIENCY20 		= 134
IE_FREESLOTS			= 134 #not an error (PST)
IE_HIDEINSHADOWS		= 135
IE_DETECTILLUSIONS  		= 136
IE_SETTRAPS 			= 137
IE_PUPPETMASTERID   		= 138
IE_PUPPETMASTERTYPE 		= 139
IE_PUPPETTYPE   		= 140
IE_PUPPETID 			= 141
IE_CHECKFORBERSERK  		= 142
IE_BERSERKSTAGE1		= 143
IE_BERSERKSTAGE2		= 144
IE_DAMAGELUCK   		= 145
IE_CRITICALHITBONUS 		= 146
IE_VISUALRANGE  		= 147
IE_EXPLORE  			= 148
IE_THRULLCHARM  		= 149
IE_SUMMONDISABLE		= 150
IE_HITBONUS 			= 151    
IE_KIT  			= 152 
IE_FORCESURGE   		= 153
IE_SURGEMOD 			= 154
IE_IMPROVEDHASTE		= 155
IE_SCRIPTINGSTATE1  		= 156
IE_SCRIPTINGSTATE2  		= 157
IE_SCRIPTINGSTATE3  		= 158
IE_SCRIPTINGSTATE4  		= 159
IE_SCRIPTINGSTATE5  		= 160
IE_SCRIPTINGSTATE6  		= 161
IE_SCRIPTINGSTATE7  		= 162   
IE_SCRIPTINGSTATE8  		= 163
IE_SCRIPTINGSTATE9  		= 164
IE_SCRIPTINGSTATE10 		= 165
IE_MELEETHAC0			= 166
IE_MELEEDAMAGE			= 167
IE_MISSILEDAMAGE		= 168
IE_NOCIRCLE			= 169
IE_FISTTHAC0			= 170
IE_FISTDAMAGE			= 171
IE_TITLE1			= 172
IE_TITLE2			= 173
IE_DISABLEOVERLAY		= 174
IE_DISABLEBACKSTAB		= 175
IE_XP_MAGE	 		= 176 # In PST this stores secondary level exp
IE_XP_THIEF	 		= 177 # In PST this stores tertiary level exp
IE_DIALOGRANGE                  = 178 # distance for dialogue
#179-198 unused
IE_STONESKINSGOLEM		= 199
IE_LEVELDRAIN			= 200
IE_AVATARREMOVAL                = 201
# GemRB Specific Defines
IE_ANIMATION_ID			= 205
IE_STATE_ID			= 206
IE_EXTSTATE_ID                  = 207
IE_METAL_COLOR			= 208
IE_MINOR_COLOR			= 209
IE_MAJOR_COLOR			= 210
IE_SKIN_COLOR			= 211
IE_LEATHER_COLOR		= 212
IE_ARMOR_COLOR			= 213
IE_HAIR_COLOR			= 214
IE_MC_FLAGS			= 215
IE_TALKCOUNT			= 216
IE_ALIGNMENT			= 217
IE_UNSELECTABLE			= 218
IE_ARMOR_TYPE			= 219
IE_TEAM				= 220
IE_FACTION			= 221
IE_SUBRACE			= 222
IE_SPECIES                      = 223 #pst specific
IE_HATEDRACE2                   = 224
IE_HATEDRACE3                   = 225
IE_HATEDRACE4                   = 226
IE_HATEDRACE5                   = 227
IE_HATEDRACE6                   = 228
IE_HATEDRACE7                   = 229
IE_HATEDRACE8                   = 230
# These are in original PST, IWD, IWD2, but not as stats
IE_RACE				= 231
IE_CLASS			= 232
IE_GENERAL			= 233
IE_EA				= 234
IE_SPECIFIC			= 235
#
IE_LEVELBARBARIAN               = 240
IE_LEVELBARD                    = 241
IE_LEVELCLERIC                  = 242
IE_LEVELDRUID                   = 243
IE_LEVELMONK                    = 244
IE_LEVELPALADIN                 = 245
IE_LEVELRANGER                  = 246
IE_LEVELSORCEROR                = 247
#place for more classes
IE_SAVEDXPOS                    = 253
IE_SAVEDYPOS                    = 254
IE_SAVEDFACE                    = 255

# End of file ie_stats.py
