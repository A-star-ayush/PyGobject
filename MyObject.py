#!/usr/bin/python3

# Here we will create our own object having its own properties and signals by inherting the base class GObject.GObject
# For theory and additional operations refer to the book

import gi
from gi.repository import GObject

class MyObj(GObject.GObject):
	# Note that the dicts are maintained globally and not inside the init function
	__gsignals__ = {
			'customSignal' : (GObject.SIGNAL_RUN_FIRST, None, 
							  (int, ))
		}

	prop1 = GObject.property(type=str, default='default_text', flags=GObject.PARAM_READWRITE) # (1)

	# __gproperties__ = {  # (3)
	# 	"prop3" : (int, # type
	# 			   "integer property", # nick name used by programs with strong introspection abilites (eg Glade)
	# 			   "A property that contains an integer", # blurb- long description. Also used by Glade and such progs
	# 			   1, #min
	# 			   5, #max
	# 			   2, #default
	# 			   GObject.PARAM_READWRITE #flags
	# 			   )
	# }

	@GObject.property # (2)
	def prop2(this):
		print("This is read-only")

	def __init__(this):
		GObject.GObject.__init__(this) # Initialising the inheritance realtionship
		this.prop3 = 2  # needed for way (3) to work
		
	def do_customSignal(this, arg): # the format of the associated func wid the signal: do_signalname(this, ...)
		print("class method for customSignal called with argument %d" %(arg))

	# def do_get_property(this, prop):
	# 	if prop.name == "prop3":
	# 		return this.prop3
	# 	else:
	# 		raise AttributeError("unknown property %s" %(prop.name))

	# def do_set_property(this, prop, value):
	# 	if prop.name == 'prop3':
	# 		this.prop3 = value
	# 	else:
	# 		raise AttributeError("unknown property %s" %(prop.name))

# Whenever a property is modified, a signal is emitted, whose name is notify:property_name
# This signal need not be created manually. 

def on_notify_prop1(obj, gparamstring): # format: on_notify_propertyName(obj, gparamstring)
	print("prop1 changed") # where gparamstring is the parameter string

def main():
	obj = MyObj()
	obj.emit("customSignal", 19)

	obj.connect("notify::prop1", on_notify_prop1)
	print(obj.get_property("prop1"))
	obj.set_property("prop1", "fooBar")
	print(obj.get_property("prop1"))

	print(obj.prop2)
	print(obj.get_property("prop2"))

	# print(obj.get_property("prop3"))


if __name__ == '__main__':
	main()



# for an entry in __gsignals__:
	# 1st arg- GObject.SIGNAL_RUN_FIRST|LAST|CLEANUP - (1st emmision stage| third stage | last stage)
	# 2nd arg- return type of the signal (usually None)
	# 3rd arg - expected arguments with their types defined (even for a dynamic language like python)

# The three ways to define a property have been marked as (1), (2), and (3)
# (2) can define only readonly properties
# (3) is a more verbose form and can be used to introduce more features like minimum and maximum value of the property
# Using (3), u cannot use simaltaneously (1) or (2) since (3) requires you to override the do_get/set property methods
# flags can be GObject.PARAM_READABLE|WRITEABLE|READWRITE. The last one is also called public.
# type needs to be defined beforehand. default is optional.