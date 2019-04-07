![yapps_logo.svg](Resources/images/logos/yapps_logo.svg)
# Yahtzee Advanced Pick &amp; Place System

[TOC]: # " "

- [Yahtzee Advanced Pick &amp; Place System](#yahtzee-advanced-pick--place-system)
    - [About The Project](#about-the-project)
    - [The Aim Of The Project](#the-aim-of-the-project)
    - [About This Repository](#about-this-repository)
    - [About us & Contact](#about-us--contact)
    - [Links](#links)
    - [Reference List](#reference-list)

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

## About us & Contact

[Joris Rietveld ](https://github.com/jorisrietveld) - :penguin: Enthusiast & Embedded Software Developer

## Links

## Reference List

![nhlstendenMadeByStudents.png](Resources/images/logos/nhlstendenMadeByStudents.png)

<hr>
This page (the documentation) is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

