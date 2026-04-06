#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    mode_arg = DeclareLaunchArgument(
        'mode',
        default_value='None',
        description='Режим работы узла публикации'
    )
    
    freq_arg = DeclareLaunchArgument(
        'publish_frequency',
        default_value='8.0',
        description='Частота публикации чётных чисел (Гц)'
    )

    threshold_arg = DeclareLaunchArgument(
        'overflow_threshold',
        default_value='80',
        description='Порог, после которого происходит переполнение'
    )
    
    topic_arg = DeclareLaunchArgument(
        'topic_name',
        default_value='even_numbers',
        description='Название топика для публикации',
    )
    
    overflow_topic_arg = DeclareLaunchArgument(
        'overflow_topic_name',
        default_value='overflow',
        description='Название топика для предупреждений',
    )
    
    publisher_node_arg = DeclareLaunchArgument(
        'publisher_node_name',
        default_value='even_pub',
        description='Название узла для публикации',
    )
    
    listener_node_arg = DeclareLaunchArgument(
        'listener_node_name',
        default_value='overflow_listener',
        description='Название узла для прослушивания',
    )
    
    mode = LaunchConfiguration('mode')

    frequency = LaunchConfiguration('publish_frequency')
    threshold = LaunchConfiguration('overflow_threshold')
    
    topic = LaunchConfiguration('topic_name')
    overflow_topic = LaunchConfiguration('overflow_topic_name')
    
    publisher_node = LaunchConfiguration('publisher_node_name')
    listener_node = LaunchConfiguration('listener_node_name')
    
    return LaunchDescription([
        freq_arg,
        threshold_arg,
        topic_arg,
        overflow_topic_arg,
        publisher_node_arg,
        listener_node_arg,
        mode_arg,
        
        Node(
            package='super_motorikin_study_pkg',
            executable='even_number_publisher',
            name=publisher_node,
            parameters=[
                {'mode': mode},
                {'publish_frequency': frequency},
                {'overflow_threshold': threshold},
                {'topic_name': topic},
                {'overflow_topic_name': overflow_topic},
            ],
            output='screen',
        ),
        Node(
            package='super_motorikin_study_pkg',
            executable='overflow_listener',
            name=listener_node,
            parameters=[
                {'overflow_topic_name': overflow_topic},
            ],
            output='screen',
        ),
    ])
