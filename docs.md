<a id="scratchXML.scratchXML"></a>

# scratchXML.scratchXML

<a id="scratchXML.scratchXML.Lineage"></a>

## Lineage Objects

```python
class Lineage()
```

Simple container to name our 3 items and make sure that _lineage is properly defined

<a id="scratchXML.scratchXML.ScratchElementList"></a>

## ScratchElementList Objects

```python
class ScratchElementList(list)
```

ScratchElementList is a list subclass that only allows ScratchElement instances to be added.
i.e. you can only add a Slot to the Slots list, etc.  Ultimatelly, this will support a new() method
which will automatically add the correct element type.

<a id="scratchXML.scratchXML.ScratchElement"></a>

## ScratchElement Objects

```python
class ScratchElement()
```

The superclass for Scratch.  Provides a dictionary and attribute lookups of the XML dictionary.
Most importantly, it defines parsechildren() and unparsechildren(), which takes a dict structure like
constructs{construct: [list of constructs]} and replaces them with a list of [construct()] instances

<a id="scratchXML.scratchXML.ScratchElement.parsechildren"></a>

#### parsechildren

```python
def parsechildren(lineage: Lineage)
```

This method converts a collective dict to an array of element instances.  It returns
a dict that can be used to update the xmldict of the object.

For example, in the XML you have <slots> <slot>...</slot> <slot>...</slot> </slots>.  This 
get converted to the dictionary {slots: [{slot: {...}}]}.
parsechildren() will convert that to {'slots': [Slot(...), Slot(...)]}.

It is called at the top from Scratch during the XML read phase, converts its children,
and asks each in turn to convert their children.

This is done through the constructors, when they are fed xmldict's, they go and parse

<a id="scratchXML.scratchXML.ScratchElement.unparsechildren"></a>

#### unparsechildren

```python
def unparsechildren()
```

This is called recursively to undo the objectification of the element array

<a id="scratchXML.scratchXML.ScratchElement.parsemeta"></a>

#### parsemeta

```python
def parsemeta()
```

the metadata is another special case, it's a dict of dataitems that we want to convert to a simple dict

<a id="scratchXML.scratchXML.ScratchElement.unparsemeta"></a>

#### unparsemeta

```python
def unparsemeta()
```

undo the metadata dict to dataitem array

<a id="scratchXML.scratchXML.Scratch"></a>

## Scratch Objects

```python
class Scratch(ScratchElement)
```

The root class for Scratch, the only one that needs to be explicitly imported.  This class
has the XML reader and writer, and then everything expands from there.

