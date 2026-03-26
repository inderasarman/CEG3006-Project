# Junction Safety System

## 1. System Integration

### Overview

Smart Blind Junction V2P Safety System

This project proposes a Vehicle-to-Pedestrian (V2P) safety system designed to improve road safety at blind, non-signalised junctions. The system leverages roadside sensing and low-latency communication to detect potential collision risks and provide real-time warnings to both drivers and pedestrians.

The solution focuses on environments where traditional traffic control systems are deterministic on user actions, primarily zebra crossings.

### Project Objective

The objective of this project is to design a novel V2P application that enhances the safety and comfort of pedestrians using vehicular communication technologies. The system aims to demonstrate engineering feasibility, originality, and alignment with vehicular network concepts.

### Our Objective

The system aims to:

- Reduce collision risk between vehicles and pedestrians
- Improve situational awareness for both drivers and pedestrians
- Provide early and real-time warnings before dangerous situations occur
- Target blind, non-signalised junctions to avoid redundancy with existing systems

### Problem Statement

Non-signalised junctions pose a significant safety risk due to limited visibility and lack of control infrastructure.

At such locations:

- Drivers may not detect pedestrians due to obstructions
- Pedestrians may misjudge the speed or distance of approaching vehicles
- No traffic lights or warning systems are present

Existing solutions rely heavily on human judgement and do not provide predictive or real-time safety alerts.

### System Architecture

#### Components

##### Vehicle Unit

- Head-Up Display (HUD)
- Speed sensor
- Communication module
- Onboard processing system (OBU)

##### Pedestrian System

- Ground LED strip for visual alerts
- Audio alert system

##### Road Side Unit (RSU)

The system supports two deployment configurations depending on the speed limit of the road:

**Single RSU (standard junctions)** — Used at locations with lower speed limits. One RSU is mounted at the pedestrian crossing and handles all detection and communication.

**Dual RSU (high-speed roads)** — Used where the speed limit exceeds 50 km/h (e.g., expressway-to-residential transitions). An additional external RSU is placed approximately 50 metres before the junction to provide earlier vehicle detection and increased reaction time.

Both configurations use the same RSU hardware:

- LiDAR sensor — detects both pedestrians and approaching vehicles
- Camera — provides visual confirmation of detected objects
- Communication module — receives vehicle speed and location data from the OBU; sends collision risk warnings
- Edge processing unit — computes braking distance based on received vehicle data *(double confirm)*

#### System Flow

##### Step 1: Vehicle Data Transmission

The vehicle's OBU continuously broadcasts its current speed and GPS location to the RSU via low-latency wireless communication. The RSU uses this data alongside its own sensor readings to calculate braking distance.

##### Step 2: Early Vehicle Detection (High-Speed Roads Only)

On higher-speed roads such as expressways, an external RSU is placed approximately 300–400 metres before the junction to detect approaching vehicles early.

At higher speeds (e.g., 80–100 km/h), the total stopping distance can exceed 100 metres. The extended detection range provides additional buffer time for early warning, ensuring that the driver receives alerts well before entering the critical braking zone.

- Cross-references with the vehicle's transmitted speed and location
- Provides additional reaction time before the vehicle reaches the crossing

##### Step 3: Junction Monitoring

The RSU at the pedestrian crossing uses LiDAR and camera to detect:

- Pedestrians near or entering the crossing area
- Vehicles approaching the junction

##### Step 4: Data Processing

The RSU processes all available data:

- Vehicle speed and location (received from OBU)
- Braking distance calculation (from both car and RSU)
- Pedestrian position (from LiDAR and camera)

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

### Key Features

- Adaptive RSU deployment — single RSU for standard junctions, dual RSU for high-speed roads (>50 km/h)
- Vehicle OBU transmits speed and location to RSU for accurate braking distance calculation
- RSU uses LiDAR and camera to detect both pedestrians and vehicles
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

### System Architecture Diagram

Explain the overall architecture of your system. Include diagrams, figures, or drawings that show how components interact.

### Functions and Messages

#### Message Flow

See [Tables/TABLES.md](Tables/TABLES.md#message-flow)

### Hardware Components and Parameters

See [Tables/TABLES.md](Tables/TABLES.md#hardware-list) for the hardware list and [system parameters](Tables/TABLES.md#system-parameters).

### Use Case
Provide a 100-200 word use case that depicts your system in a real-world scenario, demonstrating how it would be used and what benefits it brings.

---
