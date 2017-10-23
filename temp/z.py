import random

class Common (object):

	def __str__ (self):
		pass

	def __init__ (self, 
		abilities,
		attribute_types,
		catch_rate,
		effort_yield_name,
		effort_yield_number,
		evolve_next_name,
		evolve_next_number,
		evolve_previous_name,
		evolve_previous_number,
		experience,
		growth_rate,
		happiness_name,
		happiness_number,
		height_imperial,
		height_metric,
		hitpoints,
		name_english,
		name_japanese,
		name_species,
		pokeball,
		pokemon_number,
		series_number,
		weight_imperial,
		weight_metric):

		self.abilities = abilities
		self.attribute_types = attribute_types
		self.catch_rate = catch_rate
		self.effort_yield_name = effort_yield_name
		self.effort_yield_number = effort_yield_number
		self.evolve_next_name = evolve_next_name
		self.evolve_next_number = evolve_next_number
		self.evolve_previous_name = evolve_previous_name
		self.evolve_previous_number = evolve_previous_number
		self.experience = experience
		self.growth_rate = growth_rate
		self.happiness_name = happiness_name
		self.happiness_number = happiness_number
		self.height_imperial = height_imperial
		self.height_metric = height_metric
		self.hitpoints = hitpoints
		self.name_english = name_english
		self.name_japanese = name_japanese
		self.name_species = name_species
		self.pokeball = pokeball
		self.pokemon_number = pokemon_number
		self.series_number = series_number
		self.weight_imperial = weight_imperial
		self.weight_metric = weight_metric


class Breed (object):

	def __str__ (self):
		pass

	def __init__ (self,
		egg_cycles,
		egg_cycles_steps,
		egg_groups,
		female_ratio,
		male_ratio):

		self.egg_cycles = egg_cycles
		self.egg_cycles_steps = egg_cycles_steps
		self.egg_groups = egg_groups
		self.female_ratio = female_ratio
		self.male_ratio = male_ratio


class Stats (object):

	def __str__ (self):
		pass

	def __init__ (self,
		attack_base,
		attack_max,
		attack_min,
		defence_base,
		defence_max,
		defence_min,
		hitpoints_base,
		hitpoints_max,
		hitpoints_min,
		special_attack_base,
		special_attack_max,
		special_attack_min,
		special_defence_base,
		special_defence_max,
		special_defence_min,
		speed_base,
		speed_max,
		speed_min):

		self.attack_base = attack_base
		self.attack_max = attack_max
		self.attack_min = attack_min
		self.defence_base = defence_base
		self.defence_max = defence_max
		self.defence_min = defence_min
		self.hitpoints_base = hitpoints_base
		self.hitpoints_max = hitpoints_max 
		self.hitpoints_min = hitpoints_min
		self.special_attack_base = special_attack_base
		self.special_attack_max = special_attack_max
		self.special_attack_min = special_attack_min
		self.special_defence_base = special_defence_base
		self.special_defence_max = special_defence_max
		self.special_defence_min = special_defence_min
		self.speed_base = speed_base
		self.speed_max = speed_max
		self.speed_min = speed_min
		self.stats_total = sum([self.attack_base, self.defence_base, self.hitpoints_base, 
			self.special_attack_base, self.special_defence_base, self.speed_base])



class Pokemon (Common, Breed, Stats):


	def __init__ (self, **kwargs):

		Common.__init__(self,

			abilities = kwargs.get(
				"abilities", [(None, None)]),

			attribute_types = kwargs.get(
				"attribute_types", ((None, None))),

			catch_rate = kwargs.get(
				"catch_rate", 0.0),

			effort_yield_name = kwargs.get(
				"effort_yield_name", None),

			effort_yield_number = kwargs.get(
				"effort_yield_number", 0),

			evolve_next_name = kwargs.get(
				"evolve_next_name", None),

			evolve_next_number = kwargs.get(
				"evolve_next_number", -1),

			evolve_previous_name = kwargs.get(
				"evolve_previous_name", None),

			evolve_previous_number = kwargs.get(
				"evolve_previous_number", -1),

			experience = kwargs.get(
				"experience", 0),

			growth_rate = kwargs.get(
				"growth_rate", 0.0),

			happiness_name = kwargs.get(
				"happiness_name", None),

			happiness_number = kwargs.get(
				"happiness_number", 0),

			height_imperial = kwargs.get(
				"height_imperial", 0.0),

			height_metric = kwargs.get(
				"height_metric", 0.0),

			hitpoints = kwargs.get(
				"hitpoints", 0),

			name_english = kwargs.get(
				"name_english", None),

			name_japanese = kwargs.get(
				"name_japanese", None),

			name_species = kwargs.get(
				"name_species", None),

			pokeball = kwargs.get(
				"pokeball", None),

			pokemon_number = kwargs.get(
				"pokemon_number", -1),

			series_number = kwargs.get(
				"series_number", -1),

			weight_imperial = kwargs.get(
				"weight_imperial", 0.0),

			weight_metric = kwargs.get(
				"weight_metric", 0.0))


		Breed.__init__(self,

			egg_cycles = kwargs.get(
				"egg_cycles", 0),

			egg_cycles_steps = kwargs.get(
				"egg_cycles_steps", 0),

			egg_groups = kwargs.get(
				"egg_groups", ((None, 0))),

			female_ratio = kwargs.get(
				"female_ratio", 50.0),

			male_ratio = kwargs.get(
				"male_ratio", 50.0))


		Stats.__init__(self,

			attack_base = kwargs.get(
				"attack_base", 0),

			attack_max = kwargs.get(
				"attack_max", 0),
			
			attack_min = kwargs.get(
				"attack_min", 0),
			
			defence_base = kwargs.get(
				"defence_base", 0),
			
			defence_max = kwargs.get(
				"defence_max", 0),
			
			defence_min = kwargs.get(
				"defence_min", 0),
			
			hitpoints_base = kwargs.get(
				"hitpoints_base", self.hitpoints),
			
			hitpoints_max = kwargs.get(
				"hitpoints_max", 0),
			
			hitpoints_min = kwargs.get(
				"hitpoints_min", 0),
			
			special_attack_base = kwargs.get(
				"special_attack_base", 0),
			
			special_attack_max = kwargs.get(
				"special_attack_max", 0),
			
			special_attack_min = kwargs.get(
				"special_attack_min", 0),
			
			special_defence_base = kwargs.get(
				"special_defence_base", 0),
			
			special_defence_max = kwargs.get(
				"special_defence_max", 0),
			
			special_defence_min = kwargs.get(
				"special_defence_min", 0),
			
			speed_base = kwargs.get(
				"speed_base", 0),
			
			speed_max = kwargs.get(
				"speed_max", 0),
			
			speed_min = kwargs.get(
				"speed_min", 0))


p = Pokemon()

print(dir(p))

