# Exercise 36: Designing and Debugging

# A Day in the Life: By Tricia Decker

# This 'game' is a walkthrough of my typical morning routine.
# As of 8/31/2015, I have coded up the rooms, so you can move around, but
# you can't really interact with much yet.

import random as rand 

def init_game():
	init_flags = {
		'teeth': 0,
		'shower': 0,
		'walks': 0,
		'fed': 0,
		'dressed': 0,
		'wash face': 0,
		'breakfast': 0,
		'bike prep': 0,
		'pack lunch': 0,
		'pack bag':	0,
	}
	return init_flags

def score(final_flags):
	final_score = 0
	for flag in flags:
		final_score += flags[flag]
	if final_score == 10:
		print "\nScore = 10. You are SO ready for work! Get it!"
	elif final_score > 7:
		print "\nScore = %d. You are a bit disheveled but can survive the day." % final_score
	else:
		print "\nScore = %d. ... Maybe you should just go back to bed." % final_score
	print "\nGAME OVER.\n"

# ROOMS

# Bring up current room after action.
def current_room(room):
	if room == 'bedroom':
		bedroom()
	elif room == 'bath':
		bathroom()
	elif room == 'closet':
		closet()
	elif room == 'living':
		living_room()
	elif room == 'kitchen':
		kitchen()
	elif room == 'outside':
		outside()
	#elif room == 'outside':
	#	outside()
	else:
		print "ERROR: I do not understand where you are."

def eval_action(action, room):
	if "bath" in action:
		room = 'bathroom'
		bathroom()
	elif "sleep" in action or "snooze" in action or "alarm" in action:
		bed()
	elif "wake" in action or "get up" in action:
		bedroom()
	elif "closet" in action or "clothes" in action or "dressed" in action:
		room = 'closet'
		closet()
	elif "living" in action or "den" in action:
		room = 'living'
		living_room()
	elif "bed" in action:
		bedroom()
	elif "kitchen" in action or "inside" in action or "home" in action:
		kitchen()
	elif "out" in action:
		outside()
	elif "where" in action or "look" in action:
		current_room(room)
	elif "quit" in action:
		score(flags)
		exit(0)
	else:
		print "You cannot do that right now."
		action = raw_input("> ")
		eval_action(action, room)

def eval_action_bath(action, room):
	if "teeth" in action or "tooth" in action:
		brush_teeth(flags)
		room = 'bath'
		action = raw_input("> ")
		eval_action_bath(action, room)
	elif "shower" in action:
		shower(flags)
		room = 'bath'
		action = raw_input("> ")
		eval_action_bath(action,room)
	elif "bed" in action:
		bedroom()
	elif "where" in action or "look" in action:
		current_room(room)
	elif "quit" in action:
		score(flags)
		exit(0)
	else:
		print "You cannot do that right now."
		room = 'bath'
		action = raw_input("> ")
		eval_action_bath(action, room)



# in bed
def bed():
	"""Location: In Bed"""
	room = 'cama'
	print """
ROOM: BED, BEDROOM
You are lying in bed. You are snuggled up under your down duvet, with your head
propped comfortably against a feather pillow. Unfortunately, your boyfriend, who
is asleep next to you, is making quite the racket with his snoring. Your phone
is on the side of the bed frame, and your headphones are on the headboard.

So is it time to get up?"""
	
	user_action = raw_input("> ")
	eval_action(user_action, room)


# in the bedroom
def bedroom():
	"""Location: Bedroom"""
	room = 'bedroom'

	print """
ROOM: %s
You are in the bedroom. There is a queen-size bed, a dresser, a computer 
workstation, and a filing cabinet. There are also two bicycle racks. Paintings
and pictures hang on the walls. There is a window on the north wall.

There is a door to the bathroom, a door to the walk-in closet, and a door to
the living room. """ % room
	
	# dog_room = dog_status()

	# set action flag to 0 and prompt user for action until flag == 1
	# action_status = 0
	
	# prompt user for action
	user_action = raw_input("> ")
	eval_action(user_action, room)

	#while room == 'bedroom':
		#if "dog" or "dogs" in action:
		#	pet_dogs(dog_room) 
		#	dog_room = dog_status()
		#	action = raw_input("> ")

	

# Walk-in-closet
def closet():
	"""Location: Walk-in-closet"""
	room = 'closet'
	print """
ROOM: %s
You are in the closet. Your street clothes are hanging on the rack to your
right. Your cycling clothes are in a metal organizer on the floor. Your shoes
are hanging on the back of the door.

There is a door to the bedroom. """ % room
	
	user_action = raw_input("> ")
	eval_action(user_action, room)


# Bathroom
def bathroom():
	"""Location: Bathroom"""
	room = 'bathroom'
	print """
ROOM: %s
You are in the bathroom. There is a shower, a toilet, and a vanity sink. A
mirror on the wall lets you see your reflection, and there is a scale on the
floor.

There is a door to the bedroom. """ % room
	
	user_action = raw_input("> ")
	eval_action_bath(user_action, room)


# Living Room
def living_room():
	"""Location: Living Room"""
	room = 'living'
	print """
ROOM: %s
You are in the living room. A long sectional couch lines one wall directly
across from the flat-screen TV, which is flanked by bookshelves lined with
photographs. A vintage Braun radio sits atop a low bookshelf. 

There is a door to the bedroom. You can see the kitchen from here.""" % room

	user_action = raw_input("> ")
	eval_action(user_action, room)
	

# Kitchen
def kitchen():
	"""Location: Kitchen"""
	room = 'kitchen'
	print """
ROOM: %s
You are in the kitchen. There is a refrigerator, a stove, a sink, and a dish-
washer. Several bar stools line the island counter in the center of the room.

There is a door to outside. You can see the living room from here.""" % room
	
	user_action = raw_input("> ")
	eval_action(user_action, room)


# Outside
def outside():
	"""Location: Outisde"""
	room = 'outside'
	print """
ROOM: %s
You are outside of your apartment, standing on the fourth floor breezeway that
looks out onto the common courtyard. You hear the whoosh of the Muni street-
car on Ocean Avenue. 

There is a door to your apartment. In the distance, you can see the elevators.
""" % room

	user_action = raw_input("> ")
	eval_action(user_action, room)


# DOG INTERACTIONS

# Use a random variable to control whether Calvin and Hobbes are in the room
# with you. This should be weighted to favor them being there.

	user_action = raw_input("> ")
	eval_action(user_action)
	
def dog_status():
		dogs_in_room = rand.randint(0,1)
		#print "dog room: %d" % dog_room
		if dogs_in_room == 1:
			print """
Calvin and Hobbes are here with you. They are SUPER cute! Look at those
sad, sad eyes. 'Won't you pet us mommy?'
			"""

		else:
			print """
Calvin and Hobbes are in another room, probably licking their butts.
			"""
		return dogs_in_room	

		

def pet_dogs(dogs_in_room):
		#print "in 'pet_dogs' dog_room: %d" %
		if dogs_in_room == 1:
			print """
You bend down and scratch Calvin's ears. Hobbes walks over and interrupts you
to get his share of pets. You could do this all day.
			"""
		else:
			print """
Calvin and Hobbes are in another room, probably licking their butts.
			"""	
		#current_room()


# TASKS

def brush_teeth(flag):
	if flag['teeth'] == 0:
		print """
Looking at your reflection in the mirror, you open your mouth wide. Your teeth
could use a bit of TLC.

You pick up your toothbrush, squeeze a pea-sized dot of toothpaste onto the
bristles, and begin scrubbing away. ... Brush-a-brush-a-bruuuuuuuush-a ...
	"""
		flag['teeth'] = 1 # indicate teeth have already been brushed
	else:
		print "You have already brushed your teeth this morning! Get moving!"

def shower(flag):
	if flag['shower'] == 0:
		print """
You turn on the shower and fling your pajamas into the hamper while the water
warms up. You do the things that people do when taking a shower and emerge
feeling ready to face the world! 

You wrap yourself and your dripping hair in some towels.
	"""
		flag['shower'] = 1 # indicate showered
	else:
		print """
You have already showered this morning! What are you, a clean freak?! """


## Ideas to implement
# -- inventory
# -- other interactions
# -- time of day / environmental cues (sunrise, sunset ...)

# ------------------------------------------------------------------------- #
# Start a new game
flags = init_game()
print flags
bed()
