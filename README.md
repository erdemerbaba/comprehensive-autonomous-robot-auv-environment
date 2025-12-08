# Comprehensive Autonomous Robot AUV Environment

<img width="665" alt="image" src="https://github.com/erdemerbaba/Remotelly-Operated-Underwater-Vehicle/assets/57148700/e0f71155-0ea4-4cf7-9797-852286262ef0">

## Outline / Table of Contents

1. Abstract  
2. Introduction  
  2.1 Problem Statement  
  2.2 Motivation  
3. Literature Review  
4. Methodology  
  4.1 Remotely Operated Underwater Vehicle — Mechanical Works  
  4.2 System Modelling  
    4.2.1 Circuit Algorithm  
    4.2 Electronical Design  
  4.3 Electrical Design  
  4.4 Communication  
    4.4.1 Sensors and Applications  
  4.5 Calculations  
  4.6 Control Algorithm  
    4.6.1 Motor Controller Using Arduino  
    4.6.2 PID Control  
    4.6.3 Simulations  
      4.6.3.1 Simulation
  4.7 Operating System Settings  
    4.7.1 Windows 10 Settings  
      4.7.1.1 Connection over network switch  
      4.7.1.2 Python Script that is used in Windows OS as Controller  
    4.7.2 Raspbian Settings  
      4.7.2.1 Network Setting on Raspbian  
      4.7.2.2 Python Script on Raspberry Pi  
5. Future Suggestions  
6. Results and Discussion  
7. Conclusion  
8. References  
9. Appendix

---

## 1. Abstract

Remotely operated underwater vehicles (ROVs) are underwater robots used for research in science, military and offshore oil industries. Their main function is to interact with the underwater environment in various ways. ROVs are complex systems that provide critical capabilities in rescue missions, surveillance, scientific research, underwater filmmaking, and monitoring underwater industrial structures and network devices.

This project develops an ROV equipped with a surveillance system to record underwater video and stream selected footage to rescuers or operators. The design focuses on a low-cost, portable, safe and reliable ROV suitable for student use and for applications across civil, scientific and industrial domains.

<img width="601" height="312" alt="image" src="https://github.com/user-attachments/assets/4e334a0a-024f-469b-a031-8ac42e6dbb50" />

---

## 2. Introduction

This report presents models and methods for design methodology, design limitations, engineering calculations, algorithms, simulations, hardware and software for an ROV. The goal was to design and build a low-cost, easy-to-use, portable, safe and reliable ROV capable of supporting scientific research and student operation. Information and consultation were gathered from local companies.

---

### 2.1 Problem Statement

When diving deeper, challenges increase: hydrostatic pressure rises, temperature drops and human access becomes limited (narrow corridors and caves). Industrial divers face safety and operational limitations that increase cost and mission duration.

#### 2.1.1 Solution Offers

Offer 1 — Cable laying and inspection automation:
- Small maritime companies that regularly lay undersea cables rely on boats, divers and compressed air supplies. An ROV can reduce time and cost while improving safety.
- A low-cost ROV with a robotic gripper can assist divers and extend capability without replacing employment; it augments operations and access to hard-to-reach areas.

Main purposes:
1. Enable the underwater vehicle to obtain underwater images.
2. Provide a simple gripper arm for interventions in hazardous or constrained environments.
3. Implement autonomous routine functions (image processing with OpenCV) to detect geometric shapes, moving objects or specific colors for routine monitoring tasks.

Example applications:
- Underwater cable tracking
- Locating and parking in marked areas (geometric shapes) without an operator
- Monitoring painted surfaces or structures that need regular checks

Offer 2 — Emphasis on remote observation with lower-cost gripper:
- Aim for a cost-effective gripper that can perform simple grab-and-release tasks with autonomous capabilities for routine operations.

Offer 3 (Chosen approach) — Data-focused modular ROV:
- Main objective is to collect underwater data (routes, temperature, water flow properties and contents) with a modular design that can be upgraded later.
- Provide processed data to relevant sectors and educational institutions, and enable future development for niche applications.

Main purposes:
1. Enable underwater data acquisition.
2. Design subsequent vehicle iterations modularly.

Main targets:
1. Interpret and deliver data to relevant sectors and educational institutions.
2. Enable faculty and students to reproduce and improve the system in future iterations.

---

### 2.2 Motivation

Machines enable work in environments unsafe for humans. The designed ROV operates under high pressure and low temperatures, with smaller dimensions than humans enabling access to caves and narrow passages. The ROV is energy-efficient, resilient to environmental damage and suitable for exploration and monitoring.

---

## 3. Literature Review

The literature shows two prevalent ROV study categories: mini (low-cost) ROVs and platforms for dynamics/control research. Examples include:
- "Problem Identification for Underwater Remotely Operated Vehicle (ROV): A Case Study" — highlights low-cost mini ROVs.
- "A New Remotely Operated Underwater Vehicle for Dynamics and Control Research" (Johns Hopkins University) — presents a cost-effective research platform.

<img width="592" height="335" alt="image" src="https://github.com/user-attachments/assets/8623ad7f-c765-4ebf-adb7-4abf70dda5c7" />

---

## 4. Methodology

### 4.1 Mechanical Works

Early designs used plastic molds, which increase hydrodynamic drag. The team designed a skeleton from aluminum profiles to reduce drag and improve maneuverability. The aluminum frame was optimized to reduce weight by removing unnecessary profiles.

<img width="396" height="238" alt="image" src="https://github.com/user-attachments/assets/00f1b17d-87e4-4af5-9e3f-2c56f9032eb0" />

Electronics are housed in a Plexiglas cylindrical tube (inner diameter 14.5 cm, outer diameter 15.5 cm, length 50 cm) with flanged endcaps and O-ring seals. A transparent Plexiglas window in the forward flange allows the camera to view the environment.

<img width="390" height="239" alt="image" src="https://github.com/user-attachments/assets/d97d3992-26a6-49aa-9fe1-bdd1f6daa135" />

Cuffs (26 cm × 9.5 cm) support the tube within the frame. Thruster mounts were machined from aluminum and their positions validated via Unity simulations. The vehicle uses six thrusters: four for horizontal plane motion and two for vertical control. Horizontal thrusters are arranged to allow translation and yaw control.

Waterproofing materials considered: marine glue, silicone, grouting, epoxy. Marine glue provided the best combination of waterproofing and structural adhesion. Epoxy was used for transparent camera windows to avoid foaming.

---

### 4.2 System Modelling

<img width="601" height="312" alt="image" src="https://github.com/user-attachments/assets/4e334a0a-024f-469b-a031-8ac42e6dbb50" />

Electronics: Raspberry Pi 3 for high-level operations (ROS, image processing, path planning), an Arduino (for low-level motor control), IMU (accelerometer/gyro), pressure sensor and camera. The on-board system applies Kalman filtering to sensor inputs and a PID controller for stable motion. A thrust allocation matrix maps desired forces to motor PWM outputs, which are sent to ESCs.

---

#### 4.2.1 Circuit Algorithm

- Raspberry Pi handles communication with ground station, camera streaming, image processing and autonomous mission planning (ROS-based).
- Arduino Mega handles motor ESC PWM outputs and reads IMU (MPU-6050) via I2C.
- Kalman filter fuses IMU and sensor data; PID controllers stabilize the vehicle.
- ESCs are driven using PWM signals generated by the microcontroller.

<img width="832" height="1248" alt="image" src="https://github.com/user-attachments/assets/fe2b9e32-253c-4645-9e9d-b640b1d85341" />

---

### 4.3 Electronical Design

Six ESCs are needed for six thrusters. The electronics layout was designed to be compact and serviceable, with power distribution to ESCs, single-board computer, microcontroller, IMU and sensors.

<img width="694" height="425" alt="image" src="https://github.com/user-attachments/assets/7c90225f-d558-423e-a003-a2666eb11f7a" />

---

### 4.4 Electrical Design

Power is supplied from surface via a floating tether: 220VAC → 12V AC-DC converter at the ground station. The vehicle receives 12V, which is regulated onboard to 5V and 3.3V rails for electronics. A Power Distribution Board (PDB) supplies the ESCs and onboard electronics.

<img width="420" height="408" alt="image" src="https://github.com/user-attachments/assets/d2de8418-2335-4abb-a302-bb13f8185ba6" />

---

### 4.5 Communication

The communication architecture includes:
- Surface system (ground station)
- Surface core control system
- Vehicle control computer (Raspberry Pi)
- Vehicle on-board core control system (Arduino + sensors)
  
<img width="772" height="676" alt="image" src="https://github.com/user-attachments/assets/cea49283-1270-429c-b8d0-d0e6651b3530" />

#### 4.5.1 Sensors and Applications

- IMU: MPU-6050 selected for its documentation, calibration and performance.
- Temperature and humidity sensor inside the electronics tube to monitor internal conditions.
- Camera for environmental sensing and vision-based tasks.

<img width="385" height="248" alt="image" src="https://github.com/user-attachments/assets/0497f622-ae96-4500-9648-52c0870a8949" />

---

### 4.6 Calculations

Mass budget (selected items):
- Enclosure with electronics: 1,564 g
- Aluminium profiles (shorts & longs): ~5,742 g
- Thrusters (6): 1,722 g
- Flanges (2): 5,000 g
- Total mass: 14,445.3 g

<img width="713" height="261" alt="image" src="https://github.com/user-attachments/assets/f609fa2c-eabe-49d7-8d67-848e4e17e6ea" />

Center of gravity (X, Y, Z): (27.097 , 1.222 , 4.415)

<img width="443" height="397" alt="image" src="https://github.com/user-attachments/assets/25b1907a-0044-4733-95c1-af31f2b2e3cc" />

Weight: FG = m · g = 14.4453 kg · 9.81 m/s² = 141.71 N

Thruster performance:
- Straight thrust: 3.8 kgf
- Reverse thrust (some thrusters): 2.4–2.7 kgf
- 
<img width="521" height="116" alt="image" src="https://github.com/user-attachments/assets/f0da0a83-8dd0-4f7c-bab1-ea3824525dfa" />

Linear acceleration and terminal velocity calculations use standard drag equation:

<img width="294" height="240" alt="image" src="https://github.com/user-attachments/assets/7cab3dfa-b017-41fe-8f8f-61040e6b2d8d" />

Rotational dynamics:
- Turning torque computed from thruster forces and distances; moment of inertia values obtained from SolidWorks models used to compute angular accelerations.
<img width="261" height="245" alt="image" src="https://github.com/user-attachments/assets/13c36f5c-db7c-4f93-9dd1-60735d901a8a" />

<img width="259" height="63" alt="image" src="https://github.com/user-attachments/assets/e1e3cb63-27cf-470c-9544-14f98dff1a97" />

<img width="381" height="50" alt="image" src="https://github.com/user-attachments/assets/3fbbccfc-6017-4147-bf87-8570d9971477" />

<img width="289" height="97" alt="image" src="https://github.com/user-attachments/assets/3a19d8ca-b38d-4864-83bf-faa55d47470b" />

<img width="265" height="143" alt="image" src="https://github.com/user-attachments/assets/772610ee-cf0f-46b6-ad5b-ee4833c9851a" />

---

### 4.7 Control Algorithms

#### 4.7.1 Motor Controller Using Arduino

- Arduino Mega selected for many PWM outputs (14 PWM) and abundant I/O for ESCs and I2C.
- Communication between Raspberry Pi and Arduino via serial over USB (also provides 5V power).
- MPU-6050 interfaced via I2C (SDA/SCL). Gyro sensitivity set to ±500 dps, accelerometer to ±8g. Sampling set to 200 Hz.
- BTS-7960 motor drivers (12V DC, 40A) are used; they accept LPWM and RPWM inputs to control direction and speed.
  
<img width="641" height="221" alt="image" src="https://github.com/user-attachments/assets/e2ea688f-eee9-4296-9550-0773d0b8eab0" />

- The Arduino firmware:
  - Calibrates IMU (offset averaging at setup)
  - Reads sensor data (combining high/low bytes)
  - Runs sensor fusion (accelerometer + gyro adjustments)
  - Maintains finite-state loop, accepts commands from ground station, runs PID controllers and outputs PWM to ESCs
  - Manual controller (keyboard-driven) and PID-based autopilot modes are implemented
    
 <img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/2831b060-29a3-4a31-8c12-a8f9361178f5" />
 
- Control keys and movements (examples):
  - W: Forward
  - S: Backward
  - E: Up
  - Q: Down
  - D: Right
  - A: Left

#### 4.7.2 PID Control

<img width="1920" height="544" alt="image" src="https://github.com/user-attachments/assets/01c7ef88-00c6-48dc-a357-da13324ee15a" />

- PID controllers are implemented per axis (angular: roll/pitch/yaw, linear: velocities).
- PID tuning performed in simulations and on hardware.
- Implementations and examples (roll PID, Z-axis PID) are included in the Appendix (Figures 43–46).

<img width="1696" height="608" alt="image" src="https://github.com/user-attachments/assets/f4b0a003-def9-48eb-9238-4dddb761ed14" />

#### 4.7.3 Simulations

- Unity used for dynamic simulation (physics engine) and PID testing. FixedJoints are used to connect thruster rigidbodies to frame to ensure forces transfer correctly. PID controllers in Unity mimic PWM by applying impulse forces.
  
<img width="679" height="331" alt="image" src="https://github.com/user-attachments/assets/23bf7e61-7a3e-4ca7-8245-0a0e11f612b0" />

- Several motor placements tested to minimize rotational distortion and improve forward motion.
- ANSYS used for CFD and pressure visualization; identifies high-pressure regions (nose/front). Velocity/pressure fields and drag/resistance data were recorded for power-vs-velocity analysis.

<img width="694" height="432" alt="image" src="https://github.com/user-attachments/assets/43fd71ff-4160-4def-bf97-ea9175de5a3d" />

<img width="675" height="428" alt="image" src="https://github.com/user-attachments/assets/da7940cb-e7bc-471e-a76e-ed278c6a3436" />

<img width="676" height="436" alt="image" src="https://github.com/user-attachments/assets/6972bb13-e437-49ed-9a06-86dc888bdc25" />

<img width="691" height="417" alt="image" src="https://github.com/user-attachments/assets/2c7a5ff8-1106-4a29-95c5-ef068bb2f5b7" />

---

### 4.8 Operating System Settings

System networking uses IPv4 and static IPs for robust connection over RJ45 Ethernet. Recommended settings are provided for Windows 10 and Raspbian.

#### 4.8.1 Windows 10 Settings

- Static IPv4 configuration for Ethernet (matching Raspberry Pi network with unique final octet).
  
<img width="523" height="372" alt="image" src="https://github.com/user-attachments/assets/c4e063a8-4075-4fd5-9ebd-ccce61215c6d" />

- Connection via an 8-port Cnet CGS-800 network switch; CAT-6 cables recommended to transport high-bandwidth camera streams.
  
<img width="582" height="372" alt="image" src="https://github.com/user-attachments/assets/fd3c3c4f-9058-4855-ae8c-955fc0b980b1" />

#### 4.8.1.2 Python Script (Windows Controller)

- Python script reads keyboard input, sends commands to ROV, and receives camera frames using OpenCV.
- Communication uses ZMQ with REQ-REP pattern. The script continuously exchanges frames and control messages with the Raspberry Pi.

<img width="251" height="345" alt="image" src="https://github.com/user-attachments/assets/9be99fe6-9840-4106-b1aa-51adc10a97d1" />

#### 4.8.2 Raspbian Settings

- Static network configuration matching Windows settings (same first three octets).
- Raspberry Pi runs a Python server that:
  1. Establishes network communication.
  2. Receives control commands.
  3. Streams camera frames to the controller.
  4. Sends serial commands to Arduino.

---

## 5. Autonomy, Path Planning and Deep Learning Steps

- Improve SLAM and mapping using Gazebo/ROS and map-saving/navigation workflows (AMCL, 2D Nav Goal).
  
<img width="309" height="575" alt="image" src="https://github.com/user-attachments/assets/2fc7cb76-0927-4d9c-b77b-663b4a576675" />

- Explore topological mapping for global consistency with Gazebo in ROS.

<img width="305" height="265" alt="image" src="https://github.com/user-attachments/assets/db98cdee-724a-4c11-9d4f-08768888fba9" />

<img width="305" height="313" alt="image" src="https://github.com/user-attachments/assets/6947e109-0ede-4441-a0a0-74bdd2287074" />

- Enhance sensing and sensor fusion for robust obstacle avoidance.
- Implement reinforcement learning (DDPG) in Simulink/Matlab to learn navigation policies.
  
  <img width="319" height="294" alt="image" src="https://github.com/user-attachments/assets/02b846a7-cbc2-4e20-bff3-2c2b78a41672" />
  
- Integrate deeper image processing and deep learning models for object recognition and autonomous missions as reinforcement learning.
  
<img width="669" height="186" alt="image" src="https://github.com/user-attachments/assets/dc21d9a9-afc3-4023-9ee4-28bc23fb421b" />

<img width="644" height="219" alt="image" src="https://github.com/user-attachments/assets/38c81ae4-3114-44e2-a793-2f52ff3ec20c" />

- Add a functional gripper and tune control for competition

---

## 6. Results and Discussion

- Achieved watertight enclosure with robust flange sealing (marine glue + rosin reinforcement).
- Completed SolidWorks prototype, dynamic/kinematic modeling, Unity and ANSYS simulations.
- Achieved basic autonomous control with IMU-gyro-stabilized thruster control and basic image processing.
- The ROV is operational in water and can be further enhanced for competitions and higher autonomy.

---

## 7. Conclusion

The project progressed from literature review and design to a working prototype with thrusters, watertight enclosure, sensors and control systems. The ROV can maintain balance using onboard sensors and demonstrates autonomous control capabilities, simulations, and testing.

### 7.1 Achievements

- The "ROV Design" project received funding from TÜBİTAK 2209-b Industry Oriented Undergraduate Research Projects Support Program.

---

## 8. References
[1]- Muhammad Azhar B Abd Aziz, S. Mohamad Shazali B S. Abdul Hamid, M. Shahrieel M. 
Aras, Development of Wireless System For Data Transfer On Underwater Vehicles Application, 
UTeRG, Department of Mechatronics University Technical Malaysia Melaka, 2011.

[2]- David Smallwood, Ralf Bachmayer and Louis Whitcomb (1999). A New Remotely Operated 
Underwater Vehicle for Dynamics and Control Research. Johns Hopkins University, Department 
of Mechanical Engineering, Durham NH. (1999)

[3]- Sabiha Wadoo, Pushkin Kachroo Autonomous Underwater Vehicles, Modeling, Control 
Design and Simulation 2011 by Taylor and Francis Group, LLC

[4]- Sabiha Wadoo, Pushkin Kachroo Autonomous Underwater Vehicles, Modeling, Control

[5] Muhammad Azhar B Abd Aziz, S. Mohamad Shazali B S. Abdul Hamid, M. Shahrieel M. Aras, 
Development of Wireless System For Data Transfer On Underwater Vehicles Application, UTeRG, 
Department of Mechatronics University Technical Malaysia Melaka, 2011.

[6] David Smallwood, Ralf Bachmayer and Louis Whitcomb (1999). A New Remotely Operated 
Underwater Vehicle for Dynamics and Control Research. Johns Hopkins University, Department of 
Mechanical Engineering, Durham NH. (1999)

[7] SAGA Underwater Observation Vehicle. Retrieved from, 
https://videoray.com/accessoriesoptions/options/sonar/blueview-sonar.html#!m900_2250_
screenshot__2_ (Accessed: 19 November 2020).

[8] GMK – C ROV. Retrieved from, https://www.defenceturk.net/gmk-c (Accessed: 19 November 2020).

[9] Mission Specialist Defender ROV. Mission Specialist Defender ROV. Retrieved from, 
https://videoray.com/rovs/mss-rov/mission-specialist-defender.html#!Joshua_Vela_Fonseca_1 (Accessed: 
20 November 2020).

[10] National AUV-ROV. Retrieved from, https://www.defenceturk.net/auv (Accessed: 20 August 2020).

[11] HOYTEK ROV. Retrieved from, https://hoytek.com.tr/ (Accessed: 20 November 2020)

[12] BTS 7960 Wiring Schema https://www.youtube.com/watch?v=hny6wNhY1uU
