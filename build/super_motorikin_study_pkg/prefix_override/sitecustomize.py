import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bar1s/ros2_ws/src/install/super_motorikin_study_pkg'
