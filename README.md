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

---

## 2. Introduction

This report presents models and methods for design methodology, design limitations, engineering calculations, algorithms, simulations, hardware and software for an ROV. The goal was to design and build a low-cost, easy-to-use, portable, safe and reliable ROV capable of supporting scientific research and student operation. Information and consultation were gathered from local companies.

Project tasks and timelines were allocated to team members and tracked with task and time tables (see Appendix).

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

(See Appendix: Table 3 — Searched ROV Studies.)

---

## 4. Methodology

### 4.1 Mechanical Works

Early designs used plastic molds, which increase hydrodynamic drag. The team designed a skeleton from aluminum profiles to reduce drag and improve maneuverability. The aluminum frame was optimized to reduce weight by removing unnecessary profiles.

Electronics are housed in a Plexiglas cylindrical tube (inner diameter 14.5 cm, outer diameter 15.5 cm, length 50 cm) with flanged endcaps and O-ring seals. A transparent Plexiglas window in the forward flange allows the camera to view the environment.

Cuffs (26 cm × 9.5 cm) support the tube within the frame. Thruster mounts were machined from aluminum and their positions validated via Unity simulations. The vehicle uses six thrusters: four for horizontal plane motion and two for vertical control. Horizontal thrusters are arranged to allow translation and yaw control.

Waterproofing materials considered: marine glue, silicone, grouting, epoxy. Marine glue provided the best combination of waterproofing and structural adhesion. Epoxy was used for transparent camera windows to avoid foaming.

(See Figures 1–12 in Appendix for designs, views and tests.)

---

### 4.2 System Modelling

Electronics: Raspberry Pi 3 for high-level operations (ROS, image processing, path planning), an Arduino (for low-level motor control), IMU (accelerometer/gyro), pressure sensor and camera. The on-board system applies Kalman filtering to sensor inputs and a PID controller for stable motion. A thrust allocation matrix maps desired forces to motor PWM outputs, which are sent to ESCs.

A general algorithm schema and electrical circuit schema are provided in the Appendix.

---

#### 4.2.1 Circuit Algorithm

- Raspberry Pi handles communication with ground station, camera streaming, image processing and autonomous mission planning (ROS-based).
- Arduino Mega handles motor ESC PWM outputs and reads IMU (MPU-6050) via I2C.
- Kalman filter fuses IMU and sensor data; PID controllers stabilize the vehicle.
- ESCs are driven using PWM signals generated by the microcontroller.

(See Schema 1 and Figure 13 in Appendix.)

---

### 4.3 Electronical Design

Six ESCs are needed for six thrusters. The electronics layout was designed to be compact and serviceable, with power distribution to ESCs, single-board computer, microcontroller, IMU and sensors.

(Material list and pricing are presented in Appendix Figure 14.)

---

### 4.4 Electrical Design

Power is supplied from surface via a floating tether: 220VAC → 12V AC-DC converter at the ground station. The vehicle receives 12V, which is regulated onboard to 5V and 3.3V rails for electronics. A Power Distribution Board (PDB) supplies the ESCs and onboard electronics.

---

### 4.5 Communication

The communication architecture includes:
- Surface system (ground station)
- Surface core control system
- Vehicle control computer (Raspberry Pi)
- Vehicle on-board core control system (Arduino + sensors)

(See Schema 2 in Appendix.)

#### 4.5.1 Sensors and Applications

- IMU: MPU-6050 selected for its documentation, calibration and performance.
- Temperature and humidity sensor inside the electronics tube to monitor internal conditions.
- Camera for environmental sensing and vision-based tasks.

(See Figure 17 in Appendix.)

---

### 4.6 Calculations

Mass budget (selected items):
- Enclosure with electronics: 1,564 g
- Aluminium profiles (shorts & longs): ~5,742 g
- Thrusters (6): 1,722 g
- Flanges (2): 5,000 g
- Total mass: 14,445.3 g

Center of gravity (X, Y, Z): (27.097 , 1.222 , 4.415)

Weight: FG = m · g = 14.4453 kg · 9.81 m/s² = 141.71 N

Thruster performance:
- Straight thrust: 3.8 kgf
- Reverse thrust (some thrusters): 2.4–2.7 kgf

Linear acceleration and terminal velocity calculations use standard drag equation:
Fd = 0.5 · ρ · A · v² · Cd

Example terminal velocities and drag calculations are presented in the report (see section 4.6 calculations).

Rotational dynamics:
- Turning torque computed from thruster forces and distances; moment of inertia values obtained from SolidWorks models used to compute angular accelerations.

(See Table 4 and calculations in full report and Appendix.)

---

### 4.7 Control Algorithms

#### 4.7.1 Motor Controller Using Arduino

- Arduino Mega selected for many PWM outputs (14 PWM) and abundant I/O for ESCs and I2C.
- Communication between Raspberry Pi and Arduino via serial over USB (also provides 5V power).
- MPU-6050 interfaced via I2C (SDA/SCL). Gyro sensitivity set to ±500 dps, accelerometer to ±8g. Sampling set to 200 Hz.
- BTS-7960 motor drivers (12V DC, 40A) are used; they accept LPWM and RPWM inputs to control direction and speed.
- The Arduino firmware:
  - Calibrates IMU (offset averaging at setup)
  - Reads sensor data (combining high/low bytes)
  - Runs sensor fusion (accelerometer + gyro adjustments)
  - Maintains finite-state loop, accepts commands from ground station, runs PID controllers and outputs PWM to ESCs
  - Manual controller (keyboard-driven) and PID-based autopilot modes are implemented
- Control keys and movements (examples):
  - W: Forward
  - S: Backward
  - E: Up
  - Q: Down
  - D: Right
  - A: Left

(Arduino code excerpts are in the Appendix Figures 29–42.)

#### 4.7.2 PID Control

- PID controllers are implemented per axis (angular: roll/pitch/yaw, linear: velocities).
- PID tuning performed in simulations and on hardware.
- Implementations and examples (roll PID, Z-axis PID) are included in the Appendix (Figures 43–46).

#### 4.7.3 Simulations

- Unity used for dynamic simulation (physics engine) and PID testing. FixedJoints are used to connect thruster rigidbodies to frame to ensure forces transfer correctly. PID controllers in Unity mimic PWM by applying impulse forces.
- Several motor placements tested to minimize rotational distortion and improve forward motion.
- ANSYS used for CFD and pressure visualization; identifies high-pressure regions (nose/front). Velocity/pressure fields and drag/resistance data were recorded for power-vs-velocity analysis.

(See Figures 47–63 in Appendix and ANSYS results.)

---

### 4.8 Operating System Settings

System networking uses IPv4 and static IPs for robust connection over RJ45 Ethernet. Recommended settings are provided for Windows 10 and Raspbian.

#### 4.8.1 Windows 10 Settings

- Static IPv4 configuration for Ethernet (matching Raspberry Pi network with unique final octet).
- Connection via an 8-port Cnet CGS-800 network switch; CAT-6 cables recommended to transport high-bandwidth camera streams.

#### 4.8.1.2 Python Script (Windows Controller)

- Python script reads keyboard input, sends commands to ROV, and receives camera frames using OpenCV.
- Communication uses ZMQ with REQ-REP pattern. The script continuously exchanges frames and control messages with the Raspberry Pi.

(See Appendix Figures 52–57 for Python script excerpts.)

#### 4.8.2 Raspbian Settings

- Static network configuration matching Windows settings (same first three octets).
- Raspberry Pi runs a Python server that:
  1. Establishes network communication.
  2. Receives control commands.
  3. Streams camera frames to the controller.
  4. Sends serial commands to Arduino.

(Python server code fragments are in Appendix Figures 52–55.)

---

## 5. Future Suggestions

- Improve SLAM and mapping using Gazebo/ROS and map-saving/navigation workflows (AMCL, 2D Nav Goal).
- Explore topological mapping for global consistency.
- Enhance sensing and sensor fusion for robust obstacle avoidance.
- Implement reinforcement learning (DDPG) in Simulink/Matlab to learn navigation policies.
- Integrate deeper image processing and deep learning models for object recognition and autonomous missions.
- Add a functional gripper and tune control for competition (e.g., Teknofest ROV tasks).

(See Figures 23–28 and reinforcement learning diagrams in Appendix.)

---

## 6. Results and Discussion

- Achieved watertight enclosure with robust flange sealing (marine glue + rosin reinforcement).
- Completed SolidWorks prototype, dynamic/kinematic modeling, Unity and ANSYS simulations.
- Achieved basic autonomous control with IMU-gyro-stabilized thruster control and basic image processing.
- The ROV is operational in water and can be further enhanced for competitions and higher autonomy.

---

## 7. Conclusion

The project progressed from literature review and design to a working prototype with thrusters, watertight enclosure, sensors and control systems. The ROV can maintain balance using onboard sensors and demonstrates autonomous control capabilities, simulations, and testing. Future work aims to increase autonomy, add a gripper and apply advanced image processing and AI for robust mission performance.

### 7.1 Achievements

- The "ROV Design" project received funding from TÜBİTAK 2209-b Industry Oriented Undergraduate Research Projects Support Program under the consultancy of Asst. Prof. Dr. Lütfi Mutlu.

---

## 8. References

Selected references:
1. Muhammad Azhar B. Abd Aziz et al., "Development of Wireless System For Data Transfer On Underwater Vehicles Application," UTeRG, Dept. of Mechatronics, University Technical Malaysia Melaka, 2011.  
2. David Smallwood, Ralf Bachmayer, Louis Whitcomb, "A New Remotely Operated Underwater Vehicle for Dynamics and Control Research," Johns Hopkins University, 1999.  
3. Sabiha Wadoo, Pushkin Kachroo, "Autonomous Underwater Vehicles: Modeling, Control Design and Simulation," Taylor and Francis, 2011.  
... (Full reference list and URLs are provided in the Appendix.)

---

## 9. Appendix

- Acronyms (ROV, SLAM, DDPG, AMCL, PID, IMU, MSD, SS)
- Tables:
  - Table 1: Task table
  - Table 2: Time table
  - Table 3: Searched ROV studies
  - Table 4: Mass budget table
  - Table 6: V/R/P values table
- Schemas and Figures:
  - Schema 1: General Algorithm Schema
  - Schema 2: Communication Schema
  - Figures 1–63: Design views, test results, code excerpts, simulation screenshots
- Datasheets:
  - Arduino Mega: https://www.arduino.cc/en/uploads/Tutorial/595datasheet.pdf
  - Raspberry Pi 4 Peripherals: https://datasheets.raspberrypi.org/bcm2711/bcm2711-peripherals.pdf
  - MPU-6050 (MPU-6000 register map): https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf
  - BTS7960 Motor driver: http://www.robotpower.com/downloads/BTS7960_v1.1_2004-12-07.pdf
