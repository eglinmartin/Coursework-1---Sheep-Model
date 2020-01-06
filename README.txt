
-----------------README-----------------

CONTENTS

1. Model outline
2. Instructions for running
3. Directory contents
4. Licences


------------1. MODEL OUTLINE------------

This model assumes the role of
measuring sheep movement through a
field.  These sheep move at a constant
rate in random x and y directions.

Environment data is imported from
'in.txt' in the same directory.  Sheep
traverse this, and alter it through
feeding on it and excreting on it.  If
close to another sheep, that sheep's
food will be shared with the other in a
1:1 ratio.  Sheep are shown using a
white circle.

Wolves patrol the area, at a variable
speed in random directions.  If close to
a sheep, the sheep will be eaten and
shown using a black 'x' as dead.  Wolves
are shown using a grey circle.

Farmers stay inside the fence in the
centre of the map's extent, and will
shoot the wolves if they come too close.
The wolves are then represented using
a red 'x', showing that they have been
shot.  Farmers are shown using a blue
circle.

The fence in the centre of the model
restricts movement of both the sheep
and the farmers, but not the wolves.
The farmer will always spawn inside the
fence, and cannot move beyond it.  If a
sheep moves inside the boundaries of
the fence, it will be 'sheared', turning
it pink, and it will be 'captured' inside
the fence and will not be able to move
beyond it.  Wolves can still leap over
the fence, but will likely be shot by the
farmers.

Once the model has finished, results are
written to 'out.txt', which displays the
most recent results from the model.



-----2. INSTRUCTIONS FOR RUNNING--------

This model was designed to be run in
the Spyder IDE, available at
https://www.spyder-ide.org/.  No extra
steps need to be taken, however if the
model does not run immediately, typing
'matplotlib qt' into the console
(without inverted commas) should rectify
this.

Upon running, two windows should appear.
Neither should be closed, however the
only one required for using the model
is the one entitled 'Sheep Model'.

"Menu -> Run model with current
parameters" is used to run the model at
the default parameters (10 sheep, 3
wolves, 1 farmer, and 10 animation
frames.

To edit parameters, select "Edit
Parameters" and select the option being
changed.  Type into the Spyder console
the number that you wish to change it
to, and press Return to save.  When
'Run model with current parameters' is
then selected, the model will run
using the changes that have been made.

Upon navigating to 'out.txt', the
results of the most recent test can
be viewed in writing.



--------3. DIRECTORY CONTENTS-----------

The downloaded directory includes:

- 'sheep_model.py' - the main file, to
	be opened in Spyder IDE.

- 'agentframework.py' - auxiliary file
	containing class data.  No
	need to open to run the model.

- 'in.txt' - ASCII file containing the
	environment data.

- 'out.txt' - text file containing the
	results of the most recent
	test.  Overwritten on model
	reset.

- 'README' - this file.
     


-------------4. LICENCES----------------

This model was created using the
tutorials from the GEOG5990M
'Programming for Geographical
Information Analysts: Core Skills'
module at the University of Leeds. The
concept and much of the code, including 
the 'in.txt' data, was created and
supplied for this project from them.