from .base import *

DEBUG = False
DEBUG_TOOLBAR_PATCH_SETTINGS = False 

try:
	from .local import *
except ImportError:
	pass
