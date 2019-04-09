![yapps_logo.svg](Resources/images/logos/yapps_logo.svg)
# Yahtzee Advanced Pick &amp; Place System

[![Build Status](https://travis-ci.org/coe-ssm-integrated-systems-and-robotics/YAPPS.svg?branch=master)](https://travis-ci.org/coe-ssm-integrated-systems-and-robotics/YAPPS) &nbsp;
[![Coverage Status](https://coveralls.io/repos/github/coe-ssm-integrated-systems-and-robotics/YAPPS/badge.svg?branch=master)](https://coveralls.io/github/coe-ssm-integrated-systems-and-robotics/YAPPS?branch=master)&nbsp;
[![CodeFactor](https://www.codefactor.io/repository/github/coe-ssm-integrated-systems-and-robotics/yapps/badge)](https://www.codefactor.io/repository/github/coe-ssm-integrated-systems-and-robotics/yapps) &nbsp;
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE) &nbsp;
![Python versions](https://img.shields.io/badge/python%20versions-2.6%7C2.7%7C3.3%7C3.4%7C3.5%7C3.6-brightgreen.svg) &nbsp;
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/coe-ssm-integrated-systems-and-robotics/Yapps.svg)


[TOC]: # " "

- [Yahtzee Advanced Pick &amp; Place System](#yahtzee-advanced-pick--place-system)
    - [About The Project](#about-the-project)
    - [The Aim Of The Project](#the-aim-of-the-project)
    - [About This Repository](#about-this-repository)
    - [Documentation](#documentation)
    - [Project Details](#project-details)
        - [Get started](#get-started)
            - [Clone the project](#clone-the-project)
            - [install dev](#install-dev)
            - [tests](#tests)
    - [About us & Contact](#about-us--contact)
    - [Links](#links)
    - [APA Reference List](#apa-reference-list)

## About The Project
The Netherlands is undergoing a powerful development in the area of High-tech Systems and
Materials. The sector High-tech Systems and Materials develops and produces top quality materials, products, components and offers services for customers around the world. The initiative taker for this project is Mark van der Staaij, his goal is to develop a system in which a robot can differentiate between different balls based on colour.

The aim of the Centre is to create and share knowledge. The lecturer makes a connection between the training, the business community and other lecturers, such as the lecturer Pre (Sustainable plastics) and Vision. But also, the research around sensory and production technology takes place in Lingen / Hochschule Osnabruck. A landing site with regional and cross-border appearance. The Centre gives a ' face ' to Northern Netherlands and the position of NHL Stenden, especially in this field.

The Centre has two main points: ' Smart Production Technology ' and ' Digital Factory '. Smart Production Technology is about designing and producing SMART. Topics within Smart Production Technology are ' Added manufacturing ' and ' Robotics & End of Arm Tooling’. Topics inside Digital Factory are ‘Smart Industrial Control and ‘Sensor Applications’.

## The Aim Of The Project
The project group will have to research, develop and implement an advanced Pick & Place system on the universal Robot UR10 with a vision system. The system provides the recognition of the number on a number of dices, the calculation of the total score according to rules of ‘Yahtzee’, the determination of the follow-up steps, and the movement of the dice. The system consists of the robot manipulator, the Controller/master, a Raspberry Pi, a vision system and a gripper. There has already been some research already done and development on this topic by a TI2 group in the 2018-2019 school year. The architecture is built up in accordance with the vision document ‘control of a Kuka Robot’. Some cooperation with students of Mechanical Engineering education could be necessary.
The robot should be able to tell a score of one round of a Yahtzee game. After the 5 dice are thrown, they will be put manually to concrete positions in a matrix. Then the robot using gripper should move all the dice into a line, based on their values in an ascending/ descending order using relative positioning and computer vision.

Perform research for the already delivered result and the vision document. Redefine the starting points. Investigate the results of earlier research and the vision document. Redefine the starting points.

Research, develop and implement a controlled ETHERCARD IO module on an embedded controller. Choose one or more sensor principles in addition to Vision.

Program the embedded software of the vision system and the control logic of the controller.
Investigate, develop and implement an advanced Pick & Place system on the UR10 fitted with a vision system.

Research, develop and implement a controlled ETHERCAD system with one master (PLC) and various slaves. These slaves can be both sensors, actors, IO-link master/slave of embedded controllers.

Investigate, develop and implement a controlled ETHERCAD system with one master (PLC) and several slaves. These slaves can be both sensors, actors, IO-link master/slave or embedded controller.

Research, develop and implement an advanced Pick & Place system with a controlled ETHERCAD system with one master (UR10). Set up control logic possibly together with the mechanical engineering students.

## About This Repository
This repository contains the design and implementation of the Yahtzee Advanced Pick & Place System. The aim of this repository is to create a program that is able to detect and manipulate dices with the UR10 ([Universal Robot 10](https://www.universal-robots.com/nl/producten/ur10-robot/)). The software will be developed in [URScript]() (The default programming language available on the UR10) and [Python 3](https://docs.python.org/3/). To detect the dice we use [OpenCV]() and its python bindings to process the data and send commands to the UR10 over ethernet.

## Documentation
[**Yapps Design**](Documentation/Design)
   - [Design Document](Documentation/Design/design_document_v1.0.1.md)  ([pdf](Documentation/Design/Design%20Document%20v1.0.0.pdf))
- [Use_Case](Documentation/Design/Use_Case.md)

[**Yapps Scheme's**](Documentation/Schemes)
[**URScript**](Documentation/Schemes)

## Project Details

| Details for    | Details                                                                                                                                            |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| Python support | Python 2.7, >= 3.3                                                                                                                                 |
| Source         | [https://github.com/coe-ssm-integrated-systems-and-robotics/YAPPS]()                                                                               |
| Docs           | [http://YAPPS.rtfd.org](http://YAPPS.rtfd.org)                                                                                                                          |
| Changelog      | [http://YAPPS.readthedocs.org/en/latest/history.html](http://YAPPS.readthedocs.org/en/latest/history.html)                                         |
| API            | [http://YAPPS.readthedocs.org/en/latest/api.html](http://YAPPS.readthedocs.org/en/latest/api.html)                                                 |
| Issues         | [https://github.com/coe-ssm-integrated-systems-and-robotics/YAPPS/issues](https://github.com/coe-ssm-integrated-systems-and-robotics/YAPPS/issues) |
| Travis         | [http://travis-ci.org/coe-ssm-integrated-systems-and-robotics/YAPPS](http://travis-ci.org/coe-ssm-integrated-systems-and-robotics/YAPPS)           |
| Test coverage  | [https://coveralls.io/r/coe-ssm-integrated-systems-and-robotics/YAPPS](https://coveralls.io/r/coe-ssm-integrated-systems-and-robotics/YAPPS)       |
| pypi           | [https://pypi.python.org/pypi/YAPPS](https://pypi.python.org/pypi/YAPPS)                                                                           |
| License        | [GPLv3 - General Public Licence Version 3](LICENCE)                                                                                                |
| git repo       | https://github.com/coe-ssm-integrated-systems-and-robotics/YAPPS.git                                                                               |

### Get started
#### Clone the project
```console
$ git clone https://github.com/jorisrietveld/YAPPS.git
```
#### install dev
```console
$ git clone https://github.com/jorisrietveld/YAPPS.git YAPPS
$ cd ./YAPPS
$ virtualenv .env
$ source .env/bin/activate
$ pip install -e
~~~
#### tests
```console
$ python setup.py test
~~~
## About us & Contact

- [Joris Rietveld](https://github.com/jorisrietveld) :netherlands: - Embedded Software Developer
- [Romandy Richardson](mailto:romandy.richardson@student.stenden.com) (Saint-Martin):netherlands:  - Team Member
- [Danylo Znamerovskyi](mailto:danylo.znamerovskyi@student.stenden.com) :ukraine: - Project Leader
- [Tarik Arrindell](mailto:tarik.arrindell@student.stenden.com) - Team member


## Links

## APA Reference List
- Programming with Mosh. (2018, October 22). Python Tutorial for Programmers - Python Crash Course \[Video file\]. Retrieved April 7, 2019, from https://www.youtube.com/watch?v=f79MRyMsjrQ
- R. Audrey (2016) Cookiecutter - Read The Docs. Retrieved April 7, 2019, from https://cookiecutter.readthedocs.io/en/latest/readme.md
- T. Narlock (2016) Cookiecutter pyhonic - Readme. Retrieved 7 April, 2019, from https://github.com/tony/cookiecutter-pypackage-pythonic
- Forgac, D. (2015, August 8). Python Packaging from Init to Deploy \[Video file\]. Retrieved April 7, 2019, from https://www.youtube.com/watch?v=4fzAMdLKC5k


![nhlstendenMadeByStudents.png](Resources/images/logos/nhlstendenMadeByStudents.png)

<hr>
This page (the documentation) is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

