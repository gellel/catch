import os

###########################
### Paths #################
###########################

os.chdir(os.path.realpath(os.path.dirname(sys.argv[0])))

sys.path.append("../../../lib")

###########################
### Supports ##############
###########################

from constructors.attributes.attributes import ATTRIBUTES
