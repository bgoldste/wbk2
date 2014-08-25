from .base import *

DEBUG = False
DEBUG_TOOLBAR_PATCH_SETTINGS = False 
print "using production settings"

try:
	from .local import *
except ImportError:
	pass
