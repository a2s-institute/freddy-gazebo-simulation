import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import AppendEnvironmentVariable, IncludeLaunchDescription, ExecuteProcess, RegisterEventHandler, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue
from launch.event_handlers import OnProcessExit
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    # Package directories
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_freddy_gazebo = get_package_share_directory('freddy_gazebo')
    pkg_freddy_description = get_package_share_directory('freddy_description')

    # Resource paths
    resource_paths = [
        pkg_freddy_description,
        os.path.join(pkg_freddy_description, 'freddy_base_description', 'meshes'),
        os.path.join(pkg_freddy_description, 'freddy_base_description', 'meshes', 'sensors'),
        os.path.join(pkg_freddy_description, 'freddy_torso_description', 'meshes'),
    ]
    resource_paths_str = os.pathsep.join(resource_paths)
    set_env_vars_resources = AppendEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=resource_paths_str,
    )

    # World and robot files
    world_file = os.path.join(pkg_freddy_gazebo, 'worlds', 'my_world.sdf')
    robot_description_content = Command(
        [
            PathJoinSubstitution(
                [
                    FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("freddy_description"),
                    "robots",
                    # "freddy_gz.urdf.xacro"
                    "freddy_gz_torso.urdf.xacro"
                ]
            ),
            " ",
            "sim_gz:=true",
        ]
    )

    declare_joint_state_gui = DeclareLaunchArgument(
        "joint_state_gui",
        default_value="true",
        description="Launch joint state gui publisher",
    )
  
    zero_positions_config = os.path.join(
        get_package_share_directory("freddy_description"),
        "config",
        "initial_positions.yaml",
    )
   

 
    # Gazebo simulation
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': ['-r -v4 ', world_file], 'on_exit_shutdown': 'true'}.items(),
    )

    # Robot state publisher
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': ParameterValue(robot_description_content, value_type=str),
        }]
    )

    # Spawn entity
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'freddy', '-topic', 'robot_description'],
        output='screen'
    )

    return LaunchDescription([
        set_env_vars_resources,
        declare_joint_state_gui,
            
        # joint_state_publisher_gui_node,
        # joint_state_publisher_node,
        gz_sim,
        node_robot_state_publisher,
        spawn_entity,
    ])
