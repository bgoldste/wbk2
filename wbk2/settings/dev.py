from .base import *

DEBUG = True

try:
	from .local import *
	print "using local settings"
except ImportError:
	print "not using local settings"
	pass
