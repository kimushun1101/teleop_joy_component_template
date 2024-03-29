# Copyright 2023 Shunsuke Kimura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

param_file = os.path.join(
    get_package_share_directory('teleop_joy_component'), 'config', 'param.yaml')


def generate_launch_description():
    container = ComposableNodeContainer(
        name='joy_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='joy',
                plugin='joy::Joy',
                name='joy'),
            ComposableNode(
                package='teleop_joy_component',
                plugin='teleop_joy_component::TeleopJoy',
                name='teleop_joy_component',
                parameters=[param_file]),
        ],
        output='screen',
    )

    return LaunchDescription([
        container,
    ])
