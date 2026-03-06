# Day 4

## action
1. 서비스에서 응답이 너무 오랜 시간이 걸려 사용
2. 실행중인 요청을 선점하고  예상대로 요청이 제시간에 완료되지 않은 경우 다른 요청을 보낼 수 있는 통신

## 방법
1. package. xml 추가 
<build_depend>actionlib</build_depend>
<build_depend>actionlib_msgs</build_depend>
<exec_depend>actionlib</exec_depend>
<exec_depend>actionlib_msgs</exec_depend>

2. CMakeList.txt에  actionlib 추가

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib              # 추가
  actionlib_msgs         # 추가
)

add_action_files(
  FILES
  Timer.action
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs         # 추가
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs   # 추가
)

3. action 파일 추가
4. Timer.action 작성
```bash
# Goal
int32 target_seconds   
---
# Result
bool success
int32 elapsed_seconds
---
# Feedback
int32 current_seconds
float32 progress_percent
```

# Ros 디버깅 방법 

1. 통신 관찰 : rostopic echo           ex:rostopic/echo/timer/cancel
2. 수동 주입 : rostopoc pub            ex:rostopic pub/timer/cancel actionlib_msg/GoalID --{} 
3. 로그 디버깅: rospy.loginfo
