# Taichi DEM Tutorial
This repository contains a minimal DEM simulation demo written in Taichi, and a series of practices for
beginners to get started with the DEM algorithm. 

<img src="https://raw.githubusercontent.com/taichi-dev/public_files/master/taichi_dem/demo.gif" height="270px">

There are four practices in the `tutorial` folder.
```bash
./tutorial/dem-step-1q.py  # Practice 1. Implement the Grain dataclass.
./tutorial/dem-step-1q.py  # Practice 2. Implement the brute-force collision-detection.
./tutorial/dem-step-1q.py  # Practice 3. Calculate the grain_count and prefix_sum for fast collision-detection.
./tutorial/dem-step-1q.py  # Practice 4. Implement a fast collision-detection based on grid.
```

You can find the corresponding answers in the `answer` folder.

> To implement your own version, click the "Use this template" button on this page and simply modify the `dem.py` script.

## Installation
Make sure your `pip` is up-to-date:

```bash
$ pip3 install pip --upgrade
```

Assume you have a Python 3 environment, to install Taichi:

```bash
$ pip3 install -U taichi
```

To run the demo:

```bash
$ python dem.py
```

## Assumptions
The `dem.py` implements a minimal DEM solver with the following assumptions:

- All paricles are round circles with variable radius.
- Only the normal force between particles is considered - the tangential force is not included.
- The deformation of the particles is not included.
- Ignore the angular momentum of the particle and only consider the translation of the particle.

## Open missions
There are plenty of room for hacking! We suggest a few of them for you to start with:
- Reduce the neighborhood search region from the 3x3 grid cells to only 5 grid cells
- Support more particle geometries
- Implement angular momentum of the particles
- Include tangential forces
- ...

## Show your work!
We encourage you to continue developing on this repo and share your work with our community members. To notify us about your work, make sure you use this repo as a template.
