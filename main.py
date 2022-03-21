import argparse
import importlib
import os
from material import Material
from point import Point
from scene import Scene
from sphere import Sphere
from vector import Vector
from color import Color
from engine import RenderEngine
from light import Light

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene without .py extension")
    args = parser.parse_args()
    mod=importlib.import_module(args.scene)
    scene = Scene(mod.CAMERA,mod.OBJECTS,mod.LIGHTS,mod.WIDTH,mod.HEIGHT)
    engine=RenderEngine()
    image=engine.render(scene)
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDERED_IMG, "w") as img_file:
        image.write_ppm(img_file)

main()