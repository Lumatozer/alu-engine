import argparse
from material import *
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector
from color import Color
from engine import RenderEngine
from light import Light

WIDTH=320
HEIGHT=200
RENDERED_IMG="output.ppm"
CAMERA = Vector(0,-0.35,-1)
OBJECTS = [
    Sphere(Point(0,10000.5,1),10000,ChequeredMaterial(color1=Color.from_hex("#420500"),color2=Color.from_hex("#e6b87d"),ambient=0.2,reflection=0.2)),
    Sphere(Point(0.75,-0.1, 1), 0.6, Material(Color.from_hex("#0000FF"))),
    Sphere(Point(-0.5,-0.1, 0.5), 0.6, Material(Color.from_hex("#803980")))
]
LIGHTS = [
    Light(Point(0,-4.5,-17),Color.from_hex("#FFFFFF")),
    Light(Point(10,-10,-5),Color.from_hex("#E6E6E6"))
]