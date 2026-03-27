# Junction Safety System (Group 6)

## 1. System Integration

### Overview

Smart Blind Junction V2P Safety System

This project proposes a Vehicle-to-Pedestrian (V2P) safety system designed to improve road safety at blind, non-signalised junctions. The system leverages roadside sensing and low-latency communication to detect potential collision risks and provide real-time warnings to both drivers and pedestrians.

The solution focuses on environments where traditional traffic control systems are deterministic on user actions, primarily zebra crossings.


## 2. Literature Review

Vehicle-to-Pedestrian (V2P) communication has emerged as a key research direction for improving the safety of Vulnerable Road Users (VRUs), including pedestrians and cyclists, in mixed traffic environments. [Sewalkar and Seitz (2019)][1] provide an extensive survey of existing V2P systems and show that they serve both safety and convenience purposes while targeting different VRU groups with diverse mobility patterns and interaction needs. They argue that effective V2P design must consider VRU heterogeneity, the specific pre-crash scenarios being addressed, and the underlying communication technology, and they propose a design framework that organizes these elements as core system parameters. Their work also highlights persistent challenges in integrating VRUs into broader V2X ecosystems, such as ensuring timely communication under non-line-of-sight conditions and avoiding information overload for users.

Building on this foundation, [Wu et al. (2014)][2] demonstrate a practical DSRC-based V2P system in which vehicles “talk to phones” by exchanging safety messages between equipped vehicles and pedestrians carrying smartphones. Their architecture implements a DSRC stack on the smartphone’s Wi-Fi chipset and leverages GPS and inertial sensors so that both the vehicle and the pedestrian can broadcast position, speed, and heading, enabling real-time collision risk assessment and bidirectional warnings. Field tests reported in their work show that such systems can effectively warn drivers and pedestrians in typical crossing scenarios, but they also expose limitations related to channel congestion, smartphone distraction, and reliance on pedestrians owning, carrying, and correctly operating compatible devices.

Complementary to this, [Lee and Kim (2015)][3] focus on the energy constraints of mobile devices that act as V2P nodes, noting that continuous safety beaconing quickly depletes smartphone batteries and may limit adoption of purely device-centric V2P approaches. They propose an energy-efficient communication method based on Wi-Fi Direct to reduce power consumption while still supporting timely safety message exchange between vehicles and pedestrians. These findings collectively motivate infrastructure-supported architectures such as the Smart Blind Junction V2P Safety System, which offloads sensing and computation to Road Side Units using LiDAR, depth cameras, and edge processing, thereby avoiding dependence on pedestrian devices, mitigating energy and usability issues, and targeting high-risk, blind, non-signalised junctions that are under-served by traditional traffic control systems.

[1]: https://doi.org/10.3390/s19020358 (P. Sewalkar and J. Seitz, “Vehicle-to-Pedestrian Communication for Vulnerable Road Users: Survey, Design 
Considerations, and Challenges,” Sensors, vol. 19, no. 2, p. 358, Jan. 2019)

[2]: https://doi.org/10.1109/VTCFall.2014.6965898 (X. Wu et al., "Cars Talk to Phones: A DSRC Based Vehicle-Pedestrian Safety System,"2014 IEEE 80th Vehicular Technology Conference \(VTC2014-Fall\), Vancouver, BC, Canada, 2014, pp. 1-7)

[3]: https://doi.org/10.1007/s11277-015-3160-1 (S. Lee and D. Kim, “An Energy Efficient Vehicle to Pedestrian Communication Method for Safety Applications,” Wireless Personal Communications, vol. 86, no. 4, pp. 1845–1856, Dec. 2015)

## 2. Project Objective

The objective of this project is to design a novel V2P application that enhances the safety and comfort of pedestrians using vehicular communication technologies. The system aims to demonstrate engineering feasibility, originality, and alignment with vehicular network concepts.

### Our Objective

The system aims to:

- Reduce collision risk between vehicles and pedestrians at non-signalised crossings
- Improve situational awareness for both drivers and pedestrians
- Provide early, real-time warnings to prevent worst-case scenarios (pedestrian-vehicle collisions)
- Target blind, non-signalised junctions to avoid redundancy with existing systems

### Problem Statement

Non-signalised junctions pose a significant safety risk due to limited visibility and lack of control infrastructure.

At such locations:

- Drivers may not detect pedestrians due to obstructions
- Pedestrians may misjudge the speed or distance of approaching vehicles
- No traffic lights or warning systems are present

Existing solutions rely heavily on human judgement and do not provide predictive or real-time safety alerts.

## 3. System Architecture

#### Components

##### [Vehicle Unit](Subsystems/Car/README.md)

- [Head-Up Display (HUD)](Files/CarARImagine.png)
- Accelerometer sensor
- Communication module
- Onboard processing system (OBU)

##### [Pedestrian System](Subsystems/Pedestrian/README.md)

- Ground LED strip for visual alerts
- Audio alert system

##### [Road Side Unit (RSU)](Subsystems/RSU/README.md)

The system supports two deployment configurations depending on the speed limit of the road:

**Single RSU (standard junctions)** — Used at locations with lower speed limits. One RSU is mounted at the pedestrian crossing and handles all detection and communication.

**Dual RSU (high-speed roads)** — Used where the speed limit exceeds 50 km/h (e.g., expressway-to-residential transitions). An additional external RSU is placed approximately 150 metres before the junction to provide earlier vehicle detection and increased reaction time.

Both configurations use the same RSU hardware:

- LiDAR sensor — detects approaching vehicles
- Depth camera — detects pedestrians at/near pedestrian crossings
- Communication module — receives vehicle speed and location data from the OBU; sends collision risk warnings; sends pedestrian crossing warnings
- Edge processing unit — computes braking distance based on received vehicle data and configurable threshold parameters

#### System Flow

##### Step 1: Vehicle Data Transmission

The vehicle's OBU continuously broadcasts its current speed and GPS location to the RSU via low-latency wireless communication. The RSU uses this data alongside its own sensor readings to calculate braking distance.

##### Step 2: Early Vehicle Detection (High-Speed Roads Only)

On higher-speed roads such as expressways, an external RSU is placed approximately 300–400 metres before the junction to detect approaching vehicles early.

At higher speeds (e.g., 80–100 km/h), the total stopping distance can exceed 100 metres. The extended detection range provides additional buffer time for early warning, ensuring that the driver receives alerts well before entering the critical braking zone.

- Cross-references with the vehicle's transmitted speed and location
- Provides additional reaction time before the vehicle reaches the crossing

##### Step 3: Junction Monitoring

The RSU at the pedestrian crossing uses LiDAR and depth camera to detect:

- Pedestrians near or entering the crossing area
- Vehicles approaching the junction

##### Step 4: Data Processing

The RSU processes all available data:

- Vehicle speed and location (received from OBU)
- Braking distance calculation (from both car and RSU)
- Pedestrian position (from LiDAR and depth camera)

##### Step 4: Collision Risk Prediction

The system evaluates whether a collision may occur based on:

- Relative distance
- Vehicle speed
- Stopping capability

The system determines if the vehicle can safely stop before reaching the pedestrian.

##### Step 5: Communication

The RSU sends warning signals between the vehicle and pedestrian using low-latency wireless communication.

- Ensures real-time alert delivery
- Supports bidirectional communication

##### Step 6: Driver Alert

The driver receives warnings via the vehicle heads up display (HUD):

- Braking distance visualization
- Warning indicator for unsafe speed

The display is designed to be minimal and non-intrusive.

##### Step 7: Pedestrian Alert

The pedestrian receives alerts through:

- LED strip lighting on the ground
- Audio warning signals

Alert intensity increases based on risk level.

##### Step 8: Preventive Action

Both parties respond to the warning:

- Driver slows down
- Pedestrian delays crossing

This prevents potential collisions before entering the junction.
## 4. Features and Improvements

### Key Features

- Adaptive RSU deployment — single RSU for standard junctions, dual RSU for high-speed roads (>50 km/h)
- Vehicle OBU transmits speed and location to RSU for accurate braking distance calculation
- RSU uses LiDAR and depth camera to detect both pedestrians and vehicles
- Predictive collision risk analysis based on vehicle data and sensor input
- Bidirectional communication between vehicle and pedestrian
- Multi-modal feedback (visual and audio)
- Non-redundant design focused on blind, non-signalised junctions

### System Outcome

The system improves safety by:

- Detecting and predicting collision risks early
- Providing real-time warnings to both drivers and pedestrians
- Operating effectively in areas without traffic lights

### Future Improvements

- Integration of AI-based pedestrian behaviour prediction
- Adaptive warning thresholds based on weather and lighting conditions
- Integration with smart infrastructure systems
- Support for alternative communication technologies

---

## 5. System Architecture Diagram

### Functions and Messages

#### Message Flow

See [Message Flow](Tables/TABLES.md#message-flow)

The table above outlines the messages exchanged between the vehicle, RSU, and pedestrian system. The RSU pseudo code demonstrates how these messages are processed in practice — [RSU v1](Subsystems/RSU/v1/pseudo_code_example.py) covers the initial implementation of the message handling and safety logic, while [RSU v2](Subsystems/RSU/v2/pseudo_code_rsu_main.py) refines this with improved structure, alongside a dedicated [threshold definition file](Subsystems/RSU/v2/pseudo_code_rsu_threshold.py) that governs how incoming vehicle data is evaluated against safety limits.

### Hardware Components and Parameters

The hardware components span across the vehicle, the RSU at the junction, and the pedestrian crossing. Each component plays a specific role in enabling real-time detection, communication, and alerting within the system.

See [Hardware List](Tables/TABLES.md#hardware-list) and [System Parameters](Tables/TABLES.md#system-parameters).

### Use Case

At the [Lornie Highway exit towards Kheam Hock Road](Files/Lornie%20highway%20Exit%20to%20Kheam%20hock%20road.png), a zebra crossing is situated along a sharp curve, limiting driver visibility. As a vehicle exits the highway at speed, a Road Side Unit (RSU) positioned 300 metres upstream continuously monitors vehicle data via DSRC (IEEE 802.11p), enabling low-latency V2I communication. The system determines that the vehicle's speed exceeds the safe stopping distance for the crossing ahead.

A warning is immediately transmitted to the vehicle's On-Board Unit (OBU), prompting a real-time braking distance alert on the [head-up display (HUD)](Files/AR_HUD_Driving.gif). This allows the driver to decelerate gradually before reaching the hazard zone. Simultaneously, the RSU detects a jogger approaching the crossing using LiDAR and activates ground LED indicators and an audio alert, signalling the pedestrian to wait.

By combining predictive risk analysis with bidirectional communication, the system enhances situational awareness, reduces reliance on line-of-sight, and proactively prevents potential collisions in complex road environments.

---

#### AI Prompts and responses

### Prompt 1: 

From the given pseudo code below, describe any ambiguities pertaining to the overall flow. Disregard any improper technical implementation and syntax. [include pseudo code written]

### Response 1:

Ambiguities in the Code
Dictionary Comparison in set_safety_level

The condition self.vehicle_data > self.threshold_limits is unclear because both operands are dictionaries. Python does not define a natural ordering for dicts, and the intended meaning is likely a per‑field comparison (e.g., speed > threshold_speed or braking distance > threshold_braking or distance to crossing > threshold_distance). Without explicit logic, the behaviour is undefined.

Priority of Safety States

In set_safety_level, if vnu.connections is true, the method immediately sets AMBER, regardless of the vehicle data values. This means that even if the vehicle data exceed the thresholds (which would warrant a RED alert), the system never reaches RED because the elif branch is skipped. The intended priority is ambiguous; possibly the designer meant to check thresholds first and then fall back to AMBER only if no threshold is exceeded but a connection exists.

Asynchronous Nature of Vehicle Information Retrieval

get_vehicle_info sends a request and immediately checks vnu.ready. There is no mechanism to wait for a response or to handle multiple vehicles. In a real system, this would require a callback, a polling loop, or an event‑driven approach. The pseudo‑code assumes an instantaneous, blocking response.

Undefined Constants and Values

The severities OFF, AMBER, RED, and alarm levels LOW, HIGH are used but never defined. They are likely global constants, but their absence in the snippet creates ambiguity about their exact values or states.

Initial set_safety(OFF) Call

The main block calls set_safety(OFF) before the loop. Inside the loop, when pedestrian_flag is false, no safety‑level update occurs. Therefore the system remains OFF until a pedestrian is detected. This may be intended, but the code does not explicitly revert to OFF after a pedestrian leaves the scene. Once a pedestrian is detected, the state is set by set_safety_level and stays that way even after the pedestrian disappears (unless the loop later sets it again when a new pedestrian appears). This could lead to stale alerts.

Vehicle Data Structure

The vehicle_data dictionary stores only one vehicle’s information, but a roadside unit typically interacts with multiple vehicles. The code does not specify how multiple vehicles are handled; it overwrites vehicle_data each time get_vehicle_info is called, likely using data from the last‑responding vehicle. Which vehicle’s data should be considered for safety decisions is not addressed.

vnu.connections vs. vnu.ready

The code uses vnu.connections in set_safety_level and vnu.ready in get_vehicle_info. The relationship between these two attributes is not explained – e.g., whether ready implies at least one connection, or whether they are independent. This could affect the logic when a connection exists but no data is ready.

Threshold Units and Values

The thresholds are set as integers (40, 10, 50) but their units are not specified. This makes it unclear how they should be compared with actual vehicle data. Also, the distance to crossing threshold (dist_to_cross) is set to 50, but the initial vehicle_data entry for that field is 0; it is not obvious what scale is used.

Depth camera Object Detection

cam.get_depth camera_objects() presumably populates cam.depth camera_vision_objects. However, the method does not store the result locally; it relies on an attribute that may be updated asynchronously. The pseudo‑code does not indicate any delay or guarantee that the object list is current at the moment of checking.

These ambiguities would need to be resolved in a concrete implementation to ensure the system behaves as intended.

---

#### Individual Reflection

### Alfred
I was able to contribute to the team's efforts by adding the original versions of the system flowcharts and pseudo code. 
The overall flow was done after much discussion with the team to come to a consensus on what we expect of the system.
There were some disagreements that happened over certain decisions but it was ultimately resolved by considering the engineering factors and cross-referencing with the objectives.
After deliberation, myself with the help of a teammate made the amendments to the flowcharts and pseudo code to better align with the key points of discussion.
By the end of the project, I feel that the team was cohesive and arrived at a potentially viable solution that could see further testing and implementation.

### Max

### Cheston
For the project I was involved in the brainstorming of enhancements and implementation of this new ideas into the overall system flow. The project gave me a much clearer sense of how many trade‑offs sit behind a roadside safety system. I went in thinking mostly about getting the detection logic to work, but along the way found out more about the need for various additional information such as power, installation complexity, and accessibility for different types of pedestrians. Choosing things like mid‑range sensing, LED plus audio alerts, and a weather‑resistant enclosure showed me that engineering is often about picking what is appropriate rather than what is technically maximal. I also became more aware of the needs of different types of users and how design choices can have a direct impact on their comfort and safety. The project has made me aware of how the solutions are able to fits its real‑world context and the people who will interact with it.

### Muhammad

My contribution focused on developing a contextually grounded real world use case that demonstrates the practical applicability of the proposed system. I selected the Lornie Highway exit towards Kheam Hock Road as it presents a sharp curve that limits driver visibility and creates a genuine collision risk between vehicles and pedestrians accessing the nearby park. This allowed the scenario to be anchored in a realistic and safety critical environment rather than a purely hypothetical setting.

To enhance clarity and communication, I used Gemini to generate an AI simulated driving scenario showing vehicle deceleration at the junction, together with an augmented reality head up display visualisation. These assets helped translate abstract system functionalities such as RSU based detection, low latency communication, and real time driver feedback into intuitive visual representations. As a result, the interaction between dual RSUs and predictive braking alerts can be clearly illustrated, demonstrating how the system operates cohesively to reduce risk in real world conditions.

### Indera

Throughout the project, I was responsible for designing and implementing the overall repository structure and baseline documentation template, which served as the foundation for all subsequent work. This required careful consideration of how to organise subsystem content in a way that was both technically coherent and easy to navigate, especially as the system evolved. I developed and iteratively refined the Car subsystem overview to ensure it accurately represented the system architecture and communication flow, particularly in incorporating DSRC based on IEEE 802.11p to reflect the low latency requirements of V2X safety applications. One challenge was balancing technical accuracy with clarity, as early drafts were either too simplified or overly detailed. I also contributed to the development of the module mapping table together with my team, which helped strengthen the conceptual link between our design and key vehicular networking concepts such as V2I, V2P, and DSRC. Through this process, I improved in structuring technical documentation with both engineering depth and readability in mind.
