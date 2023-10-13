# Triangle

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Github CI](https://github.com/qtenebrae/triangle-python-app/actions/workflows/python-app.yml/badge.svg)](https://github.com/qtenebrae/triangle-python-app/actions/workflows/python-app.yml)

Triangle is an application designed to show the motion of a perfectly elastic ball in a triangular region. The ball
bounces elastically off the walls and there are no gravitational or frictional forces.

## Content

- [Intro](#intro)
- [Getting started](#getting-started)
    - [Installation](#installation)
- [Running the app](#running-the-app)
- [Project usage](#project-usage)

## Intro

The project was written as part of the Computer Graphics laboratory work.

Below is the interface of the application.

<p align="center">
  <img src="https://github.com/qtenebrae/triangle-python-app/blob/main/img/interface.jpg" width="600" height="400">
</p>

You can see the app in action in the gif below.

<p align="center">
  <img src="https://github.com/qtenebrae/triangle-python-app/blob/main/img/into.gif" width="600" height="400">
</p>

## Getting started

### Installation

Clone the repository

    git clone https://github.com/qtenebrae/triangle-python-app.git

Switch to the repo folder

    cd triangle-python-app

Installing dependencies

    pip install pytest

## Running the app

To run the application, you need to write a script:

    python .\src\__init__.py

To run the tests, it is sufficient to write the following:

    pytest

## Project usage

When you start the application, the coordinates of the triangle vertices, the centre of the ball and its speed are given
by default.

These values can be changed by the user.

When the `Старт` button is pressed, a triangle and a ball are drawn according to the parameters entered. The ball will
start moving at the appropriate speed.

`Стоп` button clears the canvas.

The same actions are available from the `Окно` menu item, the `Старт` and `Стоп` sub-menus.

The `Значения по умолчанию` button resets all values to their original values.

The `Справка` and `О программе` sub-menus allow you to open a modal window with help text and programme information
respectively.


