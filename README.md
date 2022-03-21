# Alu Engine

Alu Engine is a Python based meshless 3d ray tracer made without any external libraries.\
The Engine supports 3d spheres, materials, ambience lighting, high resolution reflections, depth, specular reflections,\
 diffusion etc.

## Installation

Use the git command-line program to clone the alu-engine repo.
```bash
git clone https://github.com/Lumatozer/alu-engine
```

Then go into the source folder of the project using
```bash
cd alu-engine
```

## Requirements
The project does not need any outside libraries to process but to make the rendering procedure faster we can use pypy3 to execute our engine files.

To install pypy3
```bash
sudo apt-get -y install pypy3
```

## Usage using Example Scene
I have packaged an example scene with the engine called example_scene.\
To make any changes to the scene make sure to make a backup.
To render the example scene u can use the following command.
```bash
pypy3 main.py example_scene
```
## How to view the output?
The engine outputs the scene into a ppm file which cannot be viewed on a windows machine.
To view the output u can go to 
```bash
https://www.cs.rhodes.edu/welshc/COMP141_F16/ppmReader.html
```
On the page you can upload the ppm file and the website will be able to preview the image for you.

## How do I make my own scene?
Making your own scene might seem a bit complicated but is pretty easy.

1st import the following modules
```python
import argparse
from material import *
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector
from color import Color
from engine import RenderEngine
from light import Light
```
Then define the parameters for our image file.
```python
WIDTH=320
HEIGHT=200
RENDERED_IMG="output.ppm"
```
Now we define the props in our scene one by one:

First we define our Camera using the following command:\
```python
CAMERA = Vector(0,-0.35,-1)
```
This defines the camera's vector location in our 3d space

Next we define the objects in the scene\
Objects are added to our scene in an array using the following way
```python
OBJECTS = [
    Sphere(Point(-0.5,-0.1, 0.5), 0.6, Material(Color.from_hex("#803980")))
]
```
The same way we can add lights
```python
LIGHTS = [
    Light(Point(0,-4.5,-17),Color.from_hex("#FFFFFF")),
    Light(Point(10,-10,-5),Color.from_hex("#E6E6E6"))
]
```
And now u can simple execute the following command to render the scene :
```bash
pypy3 main.py {"scene_name"}
```
## Issues
```
1.  My engine does not support 3d meshes.
2.  Images are outputted as PPM files instead of a more commonly used extension like JPEG or PNG.
3.  The engine processes everything one a single CPU core.
4.  The engine runs on a CPU instead of a GPU.
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\
Please make sure to update tests as appropriate.

