# NBodySimulator-2020-USTC: a 3D multibody simulator made for CPII 2020

[![Build Status](https://travis-ci.com/BC-Li/NbodySimulator-2020-USTC.svg?token=Yyg3baLESvJZxgyG1jBY&branch=master)](https://travis-ci.com/BC-Li/NbodySimulator-2020-USTC)  ![CI](https://github.com/BC-Li/NbodySimulator-2020-USTC/workflows/CI/badge.svg)  ![Python application](https://github.com/BC-Li/NbodySimulator-2020-USTC/workflows/Python%20application/badge.svg)

This is my mini project for n-body problem for Computer Programming II 2020 Spring in USTC.   

Source: https://introcs.cs.princeton.edu/python/34nbody/  

Princeton used their own API based on a 2D toolkit "pygame". So I used numpy instead to meet current needs.

## Directory Structure
├─.travis.yml  // Travis CI config  
├─my_project   // my project and testcase.  
└─Princeton_sample   // samples given by Princeton    

## Getting Started
Clone this repo, move directly into `my_project` directory and run `nbodysimulator.py.`

### Dependencies
* Matplotlib
* Numpy
### Run the project

* Install all the dependencies before you start running this demo

* Run `cd path_to_the_file_you_cloned` in Windows Terminal
* Run `python nbodysimulator.py` 
* Input the parameters following the instruction given. 
  For example: 
  * Input the number of material points you want to simulate and their mass (KG) , velocity and position. 
  * Among them, the velocity and position needs to be in the form of numpy vector like `[x,y,z]`.
* See the results.
## Commit History & Changes
May 21, 2020: Sample given by princeton updated. Test ok.  

Jul 24, 2020: Finish adding runnable 3 & 2 body simulators. Test OK. 

Jul 27, 2020: Finish the project.

