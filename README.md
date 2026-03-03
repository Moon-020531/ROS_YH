#  ROS development 
- Ubuntu 20.04 
- ROS neotic

# ROS install 
1. source list  
```bash 
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. Set up your keys
```bash 
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
3. Installation 
```bash
sudo apt update
```
```bash
sudo apt install ros-noetic-desktop-full
```

4. Environment setup
```bash 
source /opt/ros/noetic/setup.bash
```
```bash 
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
5. Create a ROS Workspace

```bash 
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
```bash
source devel/setup.bash
```
```bash
echo $ROS_PACKAGE_PATH
```

# setting
6. rosdep install
```bash
sudo apt install python3-rosdep
rosdep --version
sudo rosdep init
```

7. Creating a catkin Package

```bash
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```

7. Building a catkin workspace and sourcing the setup file

```bash
. ~/catkin_ws/devel/setup.bash
```

8. turtle keyboard teleoperation
```bash
rosrun turtlesim turtle_teleop_key
```


## /turtle1/pose 필드 분석

X: 거북이가 x좌표가 늘어나는 방향으로 가면 증가합니다
Y: 거북이가 y좌표가 늘어가는 방향으로 가면 증가합니다

theta: 거북이가 12시를 기준으로 반시계 방향회전 할때 3.~ 까지 늘어나다가 줄어듭니다

linear_velocity: 전진키를 누르면 2.0까지 올라가고 거북이가 멈추면 0이 됩니다
angular_velocity: 회전할떄 2.0까지 올라고 거북이가 회전을 멈추면 0이 됩니다

## turtlesim 토픽 정리

### /turtle1/cmd_vel (geometry_msgs/Twist)

linear X,Y,Z = float64 형태로 들어있음
angular X,Y,Z = float64 형태로 들어있음


### /turtle1/color_sensor (turtlesim/Color)

R,G,B = uint8 형태로 되어있음

### /turtle1/pose (turtlesim/Pose)
X,Y, theta,linear_velocity,angular_velocity =float32 형태로 들어있음



# 정사각형

  '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]' 2번 실행

  '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.5708]' 1번 실행

  '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]' 2번 실행

  '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.5708]' 1번 실행

  '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]' 2번 실행

  '[0.0, 0.0, 0.0]' '[0.0, 0.0, 1.5708]' 1번 실행

  '[2.0, 0.0, 0.0]' '[0.0, 0.0, 0.0]' 2번 실행


# turtlesim 2개 동시 실행 관찰

하나만 움직입니다
Subscribers: 
 * /turtlesim (http://ubuntu:36201/)
 * /my_turtle (http://ubuntu:42981/)

주소가 다르기 때문입니다

