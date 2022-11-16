 RESEARCH TRACK 1  ASSIGNMENT 1
================================

## Goal Of The Assignment

The aim of this assignment is create a python node that: 

1. Give ability to robot **distinguish between silver** and **golden tokens**.
2. Find the **closest silver token** and **grab** it.
3. After grabing silver token, **find closest golden token** and **release** the silver token near to golden one.
4. Repeat these prosesses **whitout using same silver and golden tokens** until there are no silver tokens left.

----------------------------------

## Installation

The simulator requires a **Python 2.7** installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

---------------------------------

## How To Run

The solutions of the assignment can be found in the **solutions (python_simulator/robot-sim/solutions)** file. In this directory, there are three different solutions of the assignment:

+ Not_autonomous_solution.py
+ Semi_autonomous_solution.py
+ Full_autonomous_solution.py

To run these solutions in the simulator **cd** to **robot-sim** directory, use `run.py`, passing it the file names.

 Not autonomous &rarr; ``` $ python run.py solutions/Not_autonomous_solution.py ```.
 Semi autonomous &rarr; ``` $ python run.py solutions/Semi_autonomous_solution.py ```.
 Full autonomous &rarr; ``` $ python run.py solutions/Full_autonomous_solution.py ```.










## SOLUTIONS 
-----------------------------

To run one or more scripts in the simulator, use `run.py`, passing it the file names. 

I am proposing you three solutions(non-autonomous, semi-autonomous and full-autonomous), with an increasing level of difficulty.
The instruction for the three exercises can be found inside the .py files (NOT.py, semi.py, FULL.py).

When done, you can run the programs with:

## 1) NON AUTONOMOUS SOLUTION

```bash
$ python run.py NOT.py
```
## 2) SEMI AUTONOMOUS SOLUTION
```bash
$ python run.py semi.py
```
## 3)FULL AUTONOMOUS SOLUTION

```bash
$ python FULL.py NOT.py
```
## FLOW CHART FULL-AUTONOMOUS

![Ekran Görüntüsü - 2022-11-15 11-50-39](https://user-images.githubusercontent.com/117012520/201902114-55ff5ecb-5398-48e1-a9e5-1c3c8627db7c.png)
![Ekran Görüntüsü - 2022-11-15 11-50-10](https://user-images.githubusercontent.com/117012520/201902122-87af2adc-5e84-4b44-afb8-71c7a1292f28.png)
![Ekran Görüntüsü - 2022-11-15 11-47-32](https://user-images.githubusercontent.com/117012520/201902137-189651ee-0d67-4424-9af2-ea4c32dfd821.png)
![Ekran Görüntüsü - 2022-11-15 11-48-46](https://user-images.githubusercontent.com/117012520/201902143-391aa100-951a-41f4-8305-c6d2640ce4bc.png)




### Robot API

---------



The API for controlling a simulated robot is designed to be as similar as possible to the [SR API][sr-api].



### Motors ###



The simulated robot has two motors configured for skid steering, connected to a two-output [Motor Board](https://studentrobotics.org/docs/kit/motor_board). The left motor is connected to output `0` and the right motor to output `1`.



The Motor Board API is identical to [that of the SR API](https://studentrobotics.org/docs/programming/sr/motors/), except that motor boards cannot be addressed by serial number. So, to turn on the spot at one quarter of full power, one might write the following:



```python
R.motors[0].m0.power = 25
R.motors[0].m1.power = -25
```



### The Grabber ###



The robot is equipped with a grabber, capable of picking up a token which is in front of the robot and within 0.4 metres of the robot's centre. To pick up a token, call the `R.grab` method:



```python
success = R.grab()
```



The `R.grab` function returns `True` if a token was successfully picked up, or `False` otherwise. If the robot is already holding a token, it will throw an `AlreadyHoldingSomethingException`.



To drop the token, call the `R.release` method.



Cable-tie flails are not implemented.



### Vision ###



To help the robot find tokens and navigate, each token has markers stuck to it, as does each wall. The `R.see` method returns a list of all the markers the robot can see, as `Marker` objects. The robot can only see markers which it is facing towards.



Each `Marker` object has the following attributes:



* `info`: a `MarkerInfo` object describing the marker itself. Has the following attributes:

  * `code`: the numeric code of the marker.

  * `marker_type`: the type of object the marker is attached to (either `MARKER_TOKEN_GOLD`, `MARKER_TOKEN_SILVER` or `MARKER_ARENA`).

  * `offset`: offset of the numeric code of the marker from the lowest numbered marker of its type. For example, token number 3 has the code 43, but offset 3.

  * `size`: the size that the marker would be in the real game, for compatibility with the SR API.

* `centre`: the location of the marker in polar coordinates, as a `PolarCoord` object. Has the following attributes:

  * `length`: the distance from the centre of the robot to the object (in metres).

  * `rot_y`: rotation about the Y axis in degrees.

* `dist`: an alias for `centre.length`

* `res`: the value of the `res` parameter of `R.see`, for compatibility with the SR API.

* `rot_y`: an alias for `centre.rot_y`

* `timestamp`: the time at which the marker was seen (when `R.see` was called).



For example, the following code lists all of the markers the robot can see:



```python
markers = R.see()
print "I can see", len(markers), "markers:"
for m in markers:
    if m.info.marker_type in (MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER):
        print " - Token {0} is {1} metres away".format( m.info.offset, m.dist )
    elif m.info.marker_type == MARKER_ARENA:
        print " - Arena marker {0} is {1} metres away".format( m.info.offset, m.dist )
```



[sr-api]: https://studentrobotics.org/docs/programming/sr/
