#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

###########################
### About #################
###########################

__author__ = "Lindsay Gelle (gellel)"

###########################
### Exports ###############
###########################

__all__ = [
	"ADAPTABILITY",
	"AERILATE",
	"AFTERMATH",
	"AIR_LOCK",
	"ANALYTIC",
	"ANGER_POINT",
	"ANTICIPATION",
	"ARENA_TRAP",
	"AROMA_VEIL",
	"AURA_BREAK",
	"BAD_DREAMS",
	"BATTERY",
	"BATTLE_ARMOR",
	"BATTLE_BOND",
	"BEAST_BOOST",
	"BERSERK",
	"BIG_PECKS",
	"BLAZE",
	"BULLETPROOF",
	"CHEEK_POUCH",
	"CHLOROPHYLL",
	"CLEAR_BODY",
	"CLOUD_NINE",
	"COLOR_CHANGE",
	"COMATOSE",
	"COMPETITIVE",
	"COMPOUND_EYES",
	"CONTRARY",
	"CORROSION",
	"CURSED_BODY",
	"CUTE_CHARM",
	"DAMP",
	"DANCER",
	"DARK_AURA",
	"DAZZLING",
	"DEFEATIST",
	"DEFIANT",
	"DELTA_STREAM",
	"DESOLATE_LAND",
	"DISGUISE",
	"DOWNLOAD",
	"DRIZZLE",
	"DROUGHT",
	"DRY_SKIN",
	"EARLY_BIRD",
	"EFFECT_SPORE",
	"ELECTRIC_SURGE",
	"EMERGENCY_EXIT",
	"FAIRY_AURA",
	"FILTER",
	"FLAME_BODY",
	"FLARE_BOOST",
	"FLASH_FIRE",
	"FLOWER_GIFT",
	"FLOWER_VEIL",
	"FLUFFY",
	"FORECAST",
	"FOREWARN",
	"FRIEND_GUARD",
	"FRISK",
	"FUR_COAT",
	"GALE_WINGS",
	"GALVANIZE",
	"GLUTTONY",
	"GOOEY",
	"GRASS_PELT",
	"GRASSY_SURGE",
	"GUTS",
	"HARVEST",
	"HEALER",
	"HEATPROOF",
	"HEAVY_METAL",
	"HONEY_GATHER",
	"HUGE_POWER",
	"HUSTLE",
	"HYDRATION",
	"HYPER_CUTTER",
	"ICE_BODY",
	"ILLUMINATE",
	"ILLUSION",
	"IMMUNITY",
	"IMPOSTER",
	"INFILTRATOR",
	"INNARDS_OUT",
	"INNER_FOCUS",
	"INSOMNIA",
	"INTIMIDATE",
	"IRON_BARBS",
	"IRON_FIST",
	"JUSTIFIED",
	"KEEN_EYE",
	"KLUTZ",
	"LEAF_GUARD",
	"LEVITATE",
	"LIGHT_METAL",
	"LIGHTNING_ROD",
	"LIMBER",
	"LIQUID_OOZE",
	"LIQUID_VOICE",
	"LONG_REACH",
	"MAGIC_BOUNCE",
	"MAGIC_GUARD",
	"MAGICIAN",
	"MAGMA_ARMOR",
	"MAGNET_PULL",
	"MARVEL_SCALE",
	"MEGA_LAUNCHER",
	"MERCILESS",
	"MINUS",
	"MISTY_SURGE",
	"MOLD_BREAKER",
	"MOODY",
	"MOTOR_DRIVE",
	"MOXIE",
	"MULTISCALE",
	"MULTITYPE",
	"MUMMY",
	"NATURAL_CURE",
	"NO_GUARD",
	"NORMALIZE",
	"OBLIVIOUS",
	"OVERCOAT",
	"OVERGROW",
	"OWN_TEMPO",
	"PARENTAL_BOND",
	"PICKPOCKET",
	"PICKUP",
	"PIXILATE",
	"PLUS",
	"POISON_HEAL",
	"POISON_POINT",
	"POISON_TOUCH",
	"POWER_CONSTRUCT",
	"PRANKSTER",
	"PRESSURE",
	"PRIMORDIAL_SEA",
	"PRISM_ARMOR",
	"PROTEAN",
	"PSYCHIC_SURGE",
	"PURE_POWER",
	"QUEENLY_MAJESTY",
	"QUICK_FEET",
	"RAIN_DISH",
	"RATTLED",
	"RECEIVER",
	"RECKLESS",
	"REFRIGERATE",
	"REGENERATOR",
	"RIVALRY",
	"RKS_SYSTEM",
	"ROCK_HEAD",
	"ROUGH_SKIN",
	"RUN_AWAY",
	"SAND_FORCE",
	"SAND_RUSH",
	"SAND_STREAM",
	"SAND_VEIL",
	"SAP_SIPPER",
	"SCHOOLING",
	"SCRAPPY",
	"SERENE_GRACE",
	"SHADOW_SHIELD",
	"SHADOW_TAG",
	"SHED_SKIN",
	"SHEER_FORCE",
	"SHELL_ARMOR",
	"SHIELD_DUST",
	"SHIELDS_DOWN",
	"SIMPLE",
	"SKILL_LINK",
	"SLOW_START",
	"SLUSH_RUSH",
	"SNIPER",
	"SNOW_CLOAK",
	"SNOW_WARNING",
	"SOLAR_POWER",
	"SOLID_ROCK",
	"SOUL_HEART",
	"SOUNDPROOF",
	"SPEED_BOOST",
	"STAKEOUT",
	"STALL",
	"STAMINA",
	"STANCE_CHANGE",
	"STATIC",
	"STEADFAST",
	"STEELWORKER",
	"STENCH",
	"STICKY_HOLD",
	"STORM_DRAIN",
	"STRONG_JAW",
	"STURDY",
	"SUCTION_CUPS",
	"SUPER_LUCK",
	"SURGE_SURFER",
	"SWARM",
	"SWEET_VEIL",
	"SWIFT_SWIM",
	"SYMBIOSIS",
	"SYNCHRONIZE",
	"TANGLED_FEET",
	"TANGLING_HAIR",
	"TECHNICIAN",
	"TELEPATHY",
	"TERAVOLT",
	"THICK_FAT",
	"TINTED_LENS",
	"TORRENT",
	"TOUGH_CLAWS",
	"TOXIC_BOOST",
	"TRACE",
	"TRIAGE",
	"TRUANT",
	"TURBOBLAZE",
	"UNAWARE",
	"UNBURDEN",
	"UNNERVE",
	"VICTORY_STAR",
	"VITAL_SPIRIT",
	"VOLT_ABSORB",
	"WATER_ABSORB",
	"WATER_BUBBLE",
	"WATER_COMPACTION",
	"WATER_VEIL",
	"WEAK_ARMOR",
	"WHITE_SMOKE",
	"WIMP_OUT",
	"WONDER_GUARD",
	"WONDER_SKIN",
	"ZEN_MODE"]

###########################
### Constants #############
###########################

ADAPTABILITY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

AERILATE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

AFTERMATH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

AIR_LOCK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ANALYTIC = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ANGER_POINT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ANTICIPATION = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ARENA_TRAP = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

AROMA_VEIL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

AURA_BREAK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BAD_DREAMS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BATTERY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BATTLE_ARMOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BATTLE_BOND = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BEAST_BOOST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BERSERK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BIG_PECKS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BLAZE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

BULLETPROOF = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CHEEK_POUCH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CHLOROPHYLL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CLEAR_BODY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CLOUD_NINE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

COLOR_CHANGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

COMATOSE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

COMPETITIVE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

COMPOUND_EYES = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CONTRARY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CORROSION = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CURSED_BODY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

CUTE_CHARM = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DAMP = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DANCER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DARK_AURA = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DAZZLING = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DEFEATIST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DEFIANT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DELTA_STREAM = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DESOLATE_LAND = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DISGUISE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DOWNLOAD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DRIZZLE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DROUGHT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

DRY_SKIN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

EARLY_BIRD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

EFFECT_SPORE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ELECTRIC_SURGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

EMERGENCY_EXIT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FAIRY_AURA = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FILTER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FLAME_BODY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FLARE_BOOST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FLASH_FIRE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FLOWER_GIFT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FLOWER_VEIL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FLUFFY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FORECAST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FOREWARN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FRIEND_GUARD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FRISK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FULL_METAL_BODY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

FUR_COAT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GALE_WINGS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GALVANIZE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GLUTTONY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GOOEY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GRASS_PELT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GRASSY_SURGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

GUTS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HARVEST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HEALER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HEATPROOF = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HEAVY_METAL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HONEY_GATHER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HUGE_POWER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HUSTLE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HYDRATION = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

HYPER_CUTTER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ICE_BODY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ILLUMINATE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ILLUSION = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

IMMUNITY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

IMPOSTER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

INFILTRATOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

INNARDS_OUT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

INNER_FOCUS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

INSOMNIA = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

INTIMIDATE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

IRON_BARBS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

IRON_FIST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

JUSTIFIED = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

KEEN_EYE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

KLUTZ = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LEAF_GUARD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LEVITATE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LIGHT_METAL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LIGHTNING_ROD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LIMBER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LIQUID_OOZE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LIQUID_VOICE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

LONG_REACH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MAGIC_BOUNCE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MAGIC_GUARD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MAGICIAN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MAGMA_ARMOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MAGNET_PULL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MARVEL_SCALE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MEGA_LAUNCHER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MERCILESS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MINUS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MISTY_SURGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MOLD_BREAKER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MOODY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MOTOR_DRIVE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MOXIE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MULTISCALE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MULTITYPE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

MUMMY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

NATURAL_CURE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

NO_GUARD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

NORMALIZE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

OBLIVIOUS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

OVERCOAT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

OVERGROW = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

OWN_TEMPO = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PARENTAL_BOND = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PICKPOCKET = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PICKUP = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PIXILATE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PLUS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

POISON_HEAL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

POISON_POINT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

POISON_TOUCH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

POWER_CONSTRUCT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

POWER_OF_ALCHEMY = dict(
	ABOUT = dict(
		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PRANKSTER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PRESSURE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PRIMORDIAL_SEA = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PRISM_ARMOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PROTEAN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PSYCHIC_SURGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

PURE_POWER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

QUEENLY_MAJESTY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

QUICK_FEET = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RAIN_DISH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RATTLED = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RECEIVER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RECKLESS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

REFRIGERATE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

REGENERATOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RIVALRY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RKS_SYSTEM = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ROCK_HEAD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ROUGH_SKIN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

RUN_AWAY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SAND_FORCE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SAND_RUSH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SAND_STREAM = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SAND_VEIL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SAP_SIPPER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SCHOOLING = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SCRAPPY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SERENE_GRACE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHADOW_SHIELD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHADOW_TAG = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHED_SKIN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHEER_FORCE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHELL_ARMOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHIELD_DUST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SHIELDS_DOWN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SIMPLE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SKILL_LINK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SLOW_START = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SLUSH_RUSH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SNIPER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SNOW_CLOAK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SNOW_WARNING = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SOLAR_POWER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SOLID_ROCK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SOUL_HEART = dict(
	ABOUT = dict(
		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SOUNDPROOF = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SPEED_BOOST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STAKEOUT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STALL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STAMINA = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STANCE_CHANGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STATIC = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STEADFAST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STEELWORKER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STENCH = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STICKY_HOLD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STORM_DRAIN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STRONG_JAW = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

STURDY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SUCTION_CUPS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SUPER_LUCK = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SURGE_SURFER = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SWARM = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SWEET_VEIL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SWIFT_SWIM = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SYMBIOSIS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

SYNCHRONIZE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TANGLED_FEET = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TANGLING_HAIR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TECHNICIAN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TELEPATHY = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TERAVOLT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

THICK_FAT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TINTED_LENS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TORRENT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TOUGH_CLAWS = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TOXIC_BOOST = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TRACE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TRIAGE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TRUANT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

TURBOBLAZE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

UNAWARE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

UNBURDEN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

UNNERVE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

VICTORY_STAR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

VITAL_SPIRIT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

VOLT_ABSORB = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WATER_ABSORB = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WATER_BUBBLE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WATER_COMPACTION = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WATER_VEIL = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WEAK_ARMOR = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WHITE_SMOKE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WIMP_OUT = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WONDER_GUARD = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

WONDER_SKIN = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))

ZEN_MODE = dict(
	ABOUT = dict(
 		DIAMOND = None, 
 		PEARL = None,
 		PLATINUM = None, 
 		HEART_GOLD = None,
 		SOUL_SILVER = None,
 		BLACK = None,
 		WHITE = None,
 		X = None,
 		Y = None,
 		OMEGA_RUBY = None,
 		OMEGA_SAPPHIRE = None,
 		SUN = None,
 		MOON = None))
