def take_magic_damage(health, resist, amp, spell_power):
	maximum_damage = spell_power * amp 
	damage = maximum_damage - resist
	new_health =  health - damage
	return new_health
