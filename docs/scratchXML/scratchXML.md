



Contents
========

* [**Lineage**](#lineage)
	* [line: 13 - `__init__`](#line-13---__init__)
* [**ScratchElementList**](#scratchelementlist)
	* [line: 25 - `__init__`](#line-25---__init__)
	* [line: 36 - `_validate_item`](#line-36---_validate_item)
	* [line: 40 - `append`](#line-40---append)
	* [line: 44 - `insert`](#line-44---insert)
	* [line: 48 - `__setitem__`](#line-48---__setitem__)
	* [line: 57 - `extend`](#line-57---extend)
* [**ScratchElement**](#scratchelement)
	* [line: 70 - `__init__`](#line-70---__init__)
	* [line: 83 - `__getitem__`](#line-83---__getitem__)
	* [line: 86 - `__setitem__`](#line-86---__setitem__)
	* [line: 89 - `get`](#line-89---get)
	* [line: 92 - `keys`](#line-92---keys)
	* [line: 96 - `__getattr__`](#line-96---__getattr__)
	* [line: 104 - `__setattr__`](#line-104---__setattr__)
	* [line: 107 - `__repr__`](#line-107---__repr__)
	* [line: 127 - `parsechildren`](#line-127---parsechildren)
	* [line: 151 - `unparsechildren`](#line-151---unparsechildren)
	* [line: 161 - `parsemeta`](#line-161---parsemeta)
	* [line: 171 - `unparsemeta`](#line-171---unparsemeta)
* [**Scratch**](#scratch)
	* [line: 184 - `__init__`](#line-184---__init__)
	* [line: 194 - `read`](#line-194---read)
	* [line: 203 - `write`](#line-203---write)
* [**Group**](#group)
* [**Construct**](#construct)
	* [line: 221 - `__init__`](#line-221---__init__)
* [**Slot**](#slot)
	* [line: 228 - `__init__`](#line-228---__init__)
	* [line: 233 - `index`](#line-233---index)
	* [line: 237 - `removeshot`](#line-237---removeshot)
	* [line: 242 - `insertshot`](#line-242---insertshot)
	* [line: 247 - `renumbershots`](#line-247---renumbershots)
	* [line: 252 - `listshots`](#line-252---listshots)
* [**Shot**](#shot)
	* [line: 259 - `__init__`](#line-259---__init__)
	* [line: 269 - `layer`](#line-269---layer)
	* [line: 273 - `slot`](#line-273---slot)
	* [line: 276 - `move`](#line-276---move)
	* [line: 282 - `shotname`](#line-282---shotname)


&nbsp;

--------

--------
# **Lineage**

```
Simple container to name our 3 items and make sure that _lineage is properly defined
```

--------
## line: 13 - `__init__`

```
def __init__(self, collective: str, child: str, childclass: type['ScratchElement']):
```


>  no docstring

&nbsp;

--------

--------
# **ScratchElementList**

```
ScratchElementList is a list subclass that only allows ScratchElement instances to be added.
i.e. you can only add a Slot to the Slots list, etc.  Ultimatelly, this will support a new() method
which will automatically add the correct element type.
```

--------
## line: 25 - `__init__`

```
def __init__(self, initial_elements=None):
```


>  no docstring

--------
## line: 36 - `_validate_item`

```
def _validate_item(self, item):
```


>  no docstring

--------
## line: 40 - `append`

```
def append(self, item):
```


>  no docstring

--------
## line: 44 - `insert`

```
def insert(self, index, item):
```


>  no docstring

--------
## line: 48 - `__setitem__`

```
def __setitem__(self, key, value):
```


>  no docstring

--------
## line: 57 - `extend`

```
def extend(self, iterable):
```


>  no docstring

&nbsp;

--------

--------
# **ScratchElement**

```
The superclass for Scratch.  Provides a dictionary and attribute lookups of the XML dictionary.
Most importantly, it defines parsechildren() and unparsechildren(), which takes a dict structure like
constructs{construct: [list of constructs]} and replaces them with a list of [construct()] instances
```

--------
## line: 70 - `__init__`

```
def __init__(self, xmldict=None, lineage=None, parsemeta=False):
```


>  no docstring

--------
## line: 83 - `__getitem__`

```
def __getitem__(self, key):
```


>  no docstring

--------
## line: 86 - `__setitem__`

```
def __setitem__(self, key, value):
```


>  no docstring

--------
## line: 89 - `get`

```
def get(self, key, default=None):
```


>  no docstring

--------
## line: 92 - `keys`

```
def keys(self):
```


>  no docstring

--------
## line: 96 - `__getattr__`

```
def __getattr__(self, key):
```


>  no docstring

--------
## line: 104 - `__setattr__`

```
def __setattr__(self, key, val):
```


>  no docstring

--------
## line: 107 - `__repr__`

```
def __repr__(self):
```


>  no docstring

--------
## line: 127 - `parsechildren`

```
def parsechildren(self, lineage: Lineage):
```
>This method converts a collective dict to an array of element instances.  It returnsa dict that can be used to update the xmldict of the object.For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This get converted to the dictionary {slots: [{slot: {...}}]}.parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}.It is called at the top from Scratch during the XML read phase, converts its children,and asks each in turn to convert their children.This is done through the constructors, when they are fed xmldict's, they go and parse 

--------
## line: 151 - `unparsechildren`

```
def unparsechildren(self):
```
>This is called recursively to undo the objectification of the element array

--------
## line: 161 - `parsemeta`

```
def parsemeta(self):
```
>the metadata is another special case, it's a dict of dataitems that we want to convert to a simple dict

--------
## line: 171 - `unparsemeta`

```
def unparsemeta(self):
```
>undo the metadata dict to dataitem array

&nbsp;

--------

--------
# **Scratch**

```
The root class for Scratch, the only one that needs to be explicitly imported.  This class
has the XML reader and writer, and then everything expands from there.
```

--------
## line: 184 - `__init__`

```
def __init__(self, xml=None):
```


>  no docstring

--------
## line: 194 - `read`

```
def read(self, xml=None):
```


>  no docstring

--------
## line: 203 - `write`

```
def write(self, xml=None):
```


>  no docstring

&nbsp;

--------

--------
# **Group**




&nbsp;

--------

--------
# **Construct**




--------
## line: 221 - `__init__`

```
def __init__(self, xmldict=None):
```


>  no docstring

&nbsp;

--------

--------
# **Slot**




--------
## line: 228 - `__init__`

```
def __init__(self, xmldict=None):
```


>  no docstring

--------
## line: 233 - `index`

```
def index(self):
```


>  no docstring

--------
## line: 237 - `removeshot`

```
def removeshot(self, removeshot):
```


>  no docstring

--------
## line: 242 - `insertshot`

```
def insertshot(self, index, shot):
```


>  no docstring

--------
## line: 247 - `renumbershots`

```
def renumbershots(self):
```


>  no docstring

--------
## line: 252 - `listshots`

```
def listshots(self, prefix=''):
```


>  no docstring

&nbsp;

--------

--------
# **Shot**




--------
## line: 259 - `__init__`

```
def __init__(self, xmldict=None):
```


>  no docstring

--------
## line: 269 - `layer`

```
def layer(self):
```


>  no docstring

--------
## line: 273 - `slot`

```
def slot(self):
```


>  no docstring

--------
## line: 276 - `move`

```
def move(self, sourceslot: Slot, destslot: Slot, destlayer: int):
```


>  no docstring

--------
## line: 282 - `shotname`

```
def shotname(self):
```


>  no docstring