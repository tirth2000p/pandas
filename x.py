import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM()
from java.util import ArrayList

myList = ArrayList()
myList.add(1)
myList.add(2)

print('length:', len(myList))

jpype.shutdownJVM()