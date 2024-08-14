# ss24-gazebo-simulation-freddy

## Simulation of the Freddy robot in Gazebo Harmonic

This repository provides a simulation of the mobile dual-manipulator robot Freddy in the Gazebo Harmonic simulator. The simulation offers independent control of the Robile base, left Kinova arm, and right Kinova arm components of the robot.

### Features
- Position, velocity, and effort control for each of the two driven wheels of each Kelo drive of the Robile base
- Position and velocity trajectory control, and effort joint control, for each Kinova arm
- Selectable controllers for the Robile base and Kinova arms using launch arguments

### Launching the Simulation
The simulation can be launched using the following command:

```bash
ros2 launch freddy_gazebo freddy_gazebo.launch.py
```

By default, the `base_controller` for controlling the Robile base is a velocity controller and the `arm_controller` for controlling the Kinova arms is a `trajectory_controller`. You can customize the base_controller and arm_controller by providing launch arguments, for example:
```bash
ros2 launch freddy_gazebo freddy_gazebo.launch.py arm_controller:=joint_trajectory base_controller:=position
```
Valid values for `arm_controller` are `joint_trajectory` and `effort`. Valid values for `base_controller` are `position`, `velocity`, and `effort`.

### Commanding the Robot's Joints
For purposes of demonstration, commands can be given to each joint of each component of the robot through keyboard input. The executable for commanding the robot's joints can be launched using the following command:
```bash
ros2 run freddy_gazebo freddy_gazebo
```

The behaviour of this executable can be changed to match the controllers used when launching `freddy_gazebo.launch.py`. This can be done by providing `arm_controller` and `base_controller` arguments as follows:
```bash
ros2 run freddy_gazebo freddy_gazebo --ros-args -p arm_controller:=joint_trajectory -p base_controller:=velocity
```

The robot can be controlled using the keyboard as follows:
```
Increment state using     w   e   r   t   y   u   i   o
                          ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑
                Joint     1   2   3   4   5   6   7   8
                          ↓   ↓   ↓   ↓   ↓   ↓   ↓   ↓
Decrement state using     s   d   f   g   h   j   k   l

Increment state increment step using    +
                                        ↑
                                        ↓
Decrement state decrement step using    -

Choose robot component to command using
                                        q : arm_left
                                        a : arm_right
                                        z : base
```

### References

- https://automaticaddison.com/how-to-control-a-robotic-arm-using-ros-2-control-and-gazebo/#Gazebo_new_version

- https://automaticaddison.com/how-to-simulate-a-robotic-arm-in-gazebo-ros-2/

- https://github.com/ros-controls/gz_ros2_control/tree/master/gz_ros2_control_demos

- https://control.ros.org/rolling/doc/ros2_control/doc/index.html

- https://github.com/gazebosim/gz-sim/tree/gz-sim7

- https://github.com/Kinovarobotics/ros2_kortex/tree/main
