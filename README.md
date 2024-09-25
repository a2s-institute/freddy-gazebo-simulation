# ss24-gazebo-simulation-freddy

## Simulation of the Freddy robot in Gazebo Harmonic

This repository provides a simulation of the mobile dual-manipulator robot Freddy in the Gazebo Harmonic simulator. The simulation offers independent control of the Robile base, left Kinova arm, and right Kinova arm components of the robot.

https://github.com/user-attachments/assets/9719dc71-e8f2-4259-aa2a-4f2d219f52aa

### Features
- Position, velocity, and effort control for each of the two driven wheels of each Kelo drive of the Robile base
- Position and velocity trajectory control, and effort joint control, for each Kinova arm
- Selectable controllers for the Robile base and Kinova arms using launch arguments

### Launching the Simulation

>### Prerequisites
>The simulation requires `ros2_control` and `ros2_controllers`. Install these packages using the following command:
>```bash
>sudo apt install ros-${ROS_DISTRO}-ros2-control ros-${ROS_DISTRO}-ros2-controllers
>```
>
>If you are using ROS2 Humble, install Gazebo Harmonic using the following command. Note that Gazebo Harmonic and ROS2 Humble is a 'non-default Gazebo/ROS2 pairing'.
>```bash
>sudo apt-get install ros-humble-ros-gzharmonic
>```
>Create and build the workspace
>```bash
>mkdir freddy_ws
>cd mkdir && mkdir src
>cd src
>git clone https://github.com/a2s-institute/freddy-gazebo-simulation.git
>cd .. && colcon build
>source install/setup.bash
>```
>The package's dependencies can be installed with the following command:
>```bash
>cd src
>vcs import < freddy-gazebo-simulation/dep.repos
>```
>
>
> When building the workspace, ensure that the environment variable `GZ_VERSION` is set to `harmonic`. This can be done with the following command:
>```bash
>export GZ_VERSION=harmonic
>```

The simulation can be launched using the following command:
```bash
ros2 launch freddy_gazebo freddy_gazebo.launch.py
```

By default, the `base_controller` for controlling the Robile base is a velocity controller and the `arm_controller` for controlling the Kinova arms is a `trajectory_controller`. You can customize the base_controller and arm_controller by providing launch arguments, for example:
```bash
ros2 launch freddy_gazebo freddy_gazebo.launch.py arm_controller:=joint_trajectory base_controller:=position
```
Valid values for `arm_controller` are `joint_trajectory` and `effort`. Valid values for `base_controller` are `position`, `velocity`, and `effort`. The `joint_trajectory` controller can accept position as well as velocity commands.

### Commanding the Robot's Joints
For purposes of demonstration, commands can be given to each joint of each component of the robot through keyboard input. The executable for commanding the robot's joints can be launched using the following command:
```bash
ros2 run freddy_gazebo freddy_gazebo
```

The behaviour of this executable can be changed to match the controllers used when launching `freddy_gazebo.launch.py`. This can be done by providing `arm_controller` and `base_controller` arguments as follows:
```bash
ros2 run freddy_gazebo freddy_gazebo --ros-args -p arm_controller:=joint_trajectory_velocity -p base_controller:=velocity
```
Valid values for `arm_controller` are `joint_trajectory_position`, `joint_trajectory_velocity`, and `effort`. Valid values for `base_controller` are `position`, `velocity`, and `effort`. When using a `joint_trajectory_velocity` command scheme, joint positions are additionally rolled out (or integrated) using the commanded velocity.

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

### Switching the Controllers
The default controllers are loaded automatically, and additional controllers can be loaded using ROS arguments as mentioned above. Alternatively, you can use rqt_controller_manager to switch controllers without restarting the simulation. To switch controllers, first unload the current controller through the UI, then load the desired one, please follow these steps to make sure the correct hardware interfaces are "claimed" and commands run smoothly.

To download rqt_controller_manager, use the following command:
```bash
apt install ros-humble-rqt-controller-manager
```
To run the controller_manager UI, use the following command:
```bash
ros2 run rqt_controller_manager rqt_controller_manager --force-discover
```
In the UI, if controller_manager is not already selected, choose it from the dropdown menu.
![Select the namespace(controller_manager)](/doc/images/namespace.png)

To unload a controller, right-click on the desired controller and select "De-activate and Unload".
![Unload the controller for left arm/right arm/base](/doc/images/unload.png)

To load the desired controller, right-click on it and select 'Load, Configure and activate'.
![Load the controller for left arm/right arm/base](/doc/images/load.png)

### System Requirements
The package has the following environment requirements and dependencies:

- ROS2 Humble
- Gazebo Harmonic (tested on Gazebo Sim version 8.3.0 and 8.6.0)
- Python (tested on Python >=3.10)
- `ros2_control` framwork for real-time control of robots using ROS2
- `gz_ros2_control` package for integrating the `ros2_control` controller architecture with the Gazebo simulator
- `freddy_description` package for the Freddy description files
- `ros2_kortex` package for the Kinowa Gen3 7DoF arm description

Note that the Robotiq gripper has not been integrated or tested for the simulation.

### References

- https://automaticaddison.com/how-to-control-a-robotic-arm-using-ros-2-control-and-gazebo/#Gazebo_new_version

- https://automaticaddison.com/how-to-simulate-a-robotic-arm-in-gazebo-ros-2/

- https://github.com/ros-controls/gz_ros2_control/tree/master/gz_ros2_control_demos

- https://control.ros.org/rolling/doc/ros2_control/doc/index.html

- https://github.com/gazebosim/gz-sim/tree/gz-sim7

- https://github.com/Kinovarobotics/ros2_kortex/tree/main
