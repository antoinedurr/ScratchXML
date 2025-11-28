<!-- markdownlint-disable -->

<a href="../scratchXML/scratchXML.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `scratchXML`






---

<a href="../scratchXML/scratchXML.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Lineage`
Simple container to name our 3 items and make sure that _lineage is properly defined 

<a href="../scratchXML/scratchXML.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(collective: str, child: str, childclass: type['ScratchElement'])
```









---

<a href="../scratchXML/scratchXML.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ScratchElementList`
ScratchElementList is a list subclass that only allows ScratchElement instances to be added. i.e. you can only add a Slot to the Slots list, etc.  Ultimatelly, this will support a new() method which will automatically add the correct element type. 

<a href="../scratchXML/scratchXML.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(initial_elements=None)
```








---

<a href="../scratchXML/scratchXML.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `append`

```python
append(item)
```





---

<a href="../scratchXML/scratchXML.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `extend`

```python
extend(iterable)
```





---

<a href="../scratchXML/scratchXML.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `insert`

```python
insert(index, item)
```






---

<a href="../scratchXML/scratchXML.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ScratchElement`
The superclass for Scratch.  Provides a dictionary and attribute lookups of the XML dictionary. Most importantly, it defines parsechildren() and unparsechildren(), which takes a dict structure like constructs{construct: [list of constructs]} and replaces them with a list of [construct()] instances 

<a href="../scratchXML/scratchXML.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xmldict=None, lineage=None, parsemeta=False)
```








---

<a href="../scratchXML/scratchXML.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key, default=None)
```





---

<a href="../scratchXML/scratchXML.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys()
```





---

<a href="../scratchXML/scratchXML.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsechildren`

```python
parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns a dict that can be used to update the xmldict of the object. 

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This  get converted to the dictionary {slots: [{slot: {...}}]}. parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}. 

It is called at the top from Scratch during the XML read phase, converts its children, and asks each in turn to convert their children. 

This is done through the constructors, when they are fed xmldict's, they go and parse  

---

<a href="../scratchXML/scratchXML.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsemeta`

```python
parsemeta()
```

Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value 

---

<a href="../scratchXML/scratchXML.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsechildren`

```python
unparsechildren()
```

This is called recursively to undo the objectification of the element array 

---

<a href="../scratchXML/scratchXML.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsemeta`

```python
unparsemeta()
```

Undo the metadata dict back to a dataitem array 


---

<a href="../scratchXML/scratchXML.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Scratch`
The root class for Scratch, the only one that needs to be explicitly imported.  This class has the XML reader and writer, and then everything expands from there. 

<a href="../scratchXML/scratchXML.py#L183"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xml=None)
```








---

<a href="../scratchXML/scratchXML.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key, default=None)
```





---

<a href="../scratchXML/scratchXML.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys()
```





---

<a href="../scratchXML/scratchXML.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsechildren`

```python
parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns a dict that can be used to update the xmldict of the object. 

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This  get converted to the dictionary {slots: [{slot: {...}}]}. parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}. 

It is called at the top from Scratch during the XML read phase, converts its children, and asks each in turn to convert their children. 

This is done through the constructors, when they are fed xmldict's, they go and parse  

---

<a href="../scratchXML/scratchXML.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsemeta`

```python
parsemeta()
```

Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value 

---

<a href="../scratchXML/scratchXML.py#L193"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read(xml=None)
```

Read an XML file and return the parsed dictionary. 

:param xml: Filepath of XML file. 

---

<a href="../scratchXML/scratchXML.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsechildren`

```python
unparsechildren()
```

This is called recursively to undo the objectification of the element array 

---

<a href="../scratchXML/scratchXML.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsemeta`

```python
unparsemeta()
```

Undo the metadata dict back to a dataitem array 

---

<a href="../scratchXML/scratchXML.py#L207"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write`

```python
write(xml=None)
```

Write the current dictionary to an XML file. 

:param xml: Filepath of XML file. 


---

<a href="../scratchXML/scratchXML.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Group`




<a href="../scratchXML/scratchXML.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xmldict=None, lineage=None, parsemeta=False)
```








---

<a href="../scratchXML/scratchXML.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key, default=None)
```





---

<a href="../scratchXML/scratchXML.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys()
```





---

<a href="../scratchXML/scratchXML.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsechildren`

```python
parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns a dict that can be used to update the xmldict of the object. 

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This  get converted to the dictionary {slots: [{slot: {...}}]}. parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}. 

It is called at the top from Scratch during the XML read phase, converts its children, and asks each in turn to convert their children. 

This is done through the constructors, when they are fed xmldict's, they go and parse  

---

<a href="../scratchXML/scratchXML.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsemeta`

```python
parsemeta()
```

Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value 

---

<a href="../scratchXML/scratchXML.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsechildren`

```python
unparsechildren()
```

This is called recursively to undo the objectification of the element array 

---

<a href="../scratchXML/scratchXML.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsemeta`

```python
unparsemeta()
```

Undo the metadata dict back to a dataitem array 


---

<a href="../scratchXML/scratchXML.py#L229"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Construct`
Object representation of a Scratch Construct, which contains Slots 

<a href="../scratchXML/scratchXML.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xmldict=None)
```








---

<a href="../scratchXML/scratchXML.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key, default=None)
```





---

<a href="../scratchXML/scratchXML.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys()
```





---

<a href="../scratchXML/scratchXML.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsechildren`

```python
parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns a dict that can be used to update the xmldict of the object. 

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This  get converted to the dictionary {slots: [{slot: {...}}]}. parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}. 

It is called at the top from Scratch during the XML read phase, converts its children, and asks each in turn to convert their children. 

This is done through the constructors, when they are fed xmldict's, they go and parse  

---

<a href="../scratchXML/scratchXML.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsemeta`

```python
parsemeta()
```

Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value 

---

<a href="../scratchXML/scratchXML.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsechildren`

```python
unparsechildren()
```

This is called recursively to undo the objectification of the element array 

---

<a href="../scratchXML/scratchXML.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsemeta`

```python
unparsemeta()
```

Undo the metadata dict back to a dataitem array 


---

<a href="../scratchXML/scratchXML.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Slot`
Object representation of a Scratch Slot, which contains Shots 

<a href="../scratchXML/scratchXML.py#L243"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xmldict=None)
```






---

#### <kbd>property</kbd> index







---

<a href="../scratchXML/scratchXML.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key, default=None)
```





---

<a href="../scratchXML/scratchXML.py#L262"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `insertshot`

```python
insertshot(index, shot)
```

Insert a shot at a specific index in the slot. 

:param index: Position to insert the shot. :param shot: Shot instance to insert. 

---

<a href="../scratchXML/scratchXML.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys()
```





---

<a href="../scratchXML/scratchXML.py#L282"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `listshots`

```python
listshots(prefix='')
```

List the shots in this slot. 

:param prefix: Often sets of spaces for indentation. 

---

<a href="../scratchXML/scratchXML.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsechildren`

```python
parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns a dict that can be used to update the xmldict of the object. 

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This  get converted to the dictionary {slots: [{slot: {...}}]}. parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}. 

It is called at the top from Scratch during the XML read phase, converts its children, and asks each in turn to convert their children. 

This is done through the constructors, when they are fed xmldict's, they go and parse  

---

<a href="../scratchXML/scratchXML.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsemeta`

```python
parsemeta()
```

Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value 

---

<a href="../scratchXML/scratchXML.py#L252"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `removeshot`

```python
removeshot(removeshot)
```

Remove shot from the slot.  Expects a Shot instance, from which it will match the UUID. 

:param removeshot: Shot() instance to remove 

---

<a href="../scratchXML/scratchXML.py#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renumbershots`

```python
renumbershots()
```

Renumber the @layer attributes of all shots in the slot.  This is called automatically after an insertshot  or removeshot operation, so that the @layer attributes remain consistent. 

---

<a href="../scratchXML/scratchXML.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsechildren`

```python
unparsechildren()
```

This is called recursively to undo the objectification of the element array 

---

<a href="../scratchXML/scratchXML.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsemeta`

```python
unparsemeta()
```

Undo the metadata dict back to a dataitem array 


---

<a href="../scratchXML/scratchXML.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Shot`
Object representation of a Scratch Shot.  This is also known as a version in the Scratch UI. 

<a href="../scratchXML/scratchXML.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xmldict=None)
```






---

#### <kbd>property</kbd> layer





---

#### <kbd>property</kbd> slot







---

<a href="../scratchXML/scratchXML.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(key, default=None)
```





---

<a href="../scratchXML/scratchXML.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `keys`

```python
keys()
```





---

<a href="../scratchXML/scratchXML.py#L314"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `move`

```python
move(sourceslot: Slot, destslot: Slot, destlayer: int)
```

Move this shot from one slot to another at the specified layer. 

:param sourceslot: Source slot :type sourceslot: Slot :param destslot: Destination slot :type destslot: Slot :param destlayer: The index in the destination slot where the shot should be inserted :type destlayer: int 

---

<a href="../scratchXML/scratchXML.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsechildren`

```python
parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns a dict that can be used to update the xmldict of the object. 

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This  get converted to the dictionary {slots: [{slot: {...}}]}. parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}. 

It is called at the top from Scratch during the XML read phase, converts its children, and asks each in turn to convert their children. 

This is done through the constructors, when they are fed xmldict's, they go and parse  

---

<a href="../scratchXML/scratchXML.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `parsemeta`

```python
parsemeta()
```

Refactor the dict of dataitems into a simple key:value dictionary of metadata name, metadata value 

---

<a href="../scratchXML/scratchXML.py#L330"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `shotname`

```python
shotname()
```

Convenience method to get the name of the shot. 

---

<a href="../scratchXML/scratchXML.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsechildren`

```python
unparsechildren()
```

This is called recursively to undo the objectification of the element array 

---

<a href="../scratchXML/scratchXML.py#L170"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unparsemeta`

```python
unparsemeta()
```

Undo the metadata dict back to a dataitem array 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
