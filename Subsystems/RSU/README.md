# RSU Overview

## Purpose of Road Side Unit

The Road Side Unit (RSU) acts as the central intelligence of the system. Its primary role is to monitor the junction environment, process incoming vehicle data, compute collision risk, and distribute warnings to both the vehicle and pedestrian units. It serves as the coordination hub that links all subsystems in real time.

## Key Responsibilities

- Detect pedestrians and approaching vehicles using onboard sensors
- Receive vehicle speed and location data from the On-Board Unit (OBU)
- Calculate braking distance based on vehicle data and sensor readings
- Assess collision risk and determine the appropriate warning level
- Transmit risk warnings to the vehicle unit
- Transmit alert signals to the pedestrian unit

## Inputs

The RSU receives the following inputs:

From the vehicle unit:
- Vehicle speed
- Vehicle GPS location

From onboard sensors:
- LiDAR scan data — detects presence and position of pedestrians and vehicles
- Camera feed — provides visual confirmation of detected objects

## Outputs

The RSU produces the following outputs:

- **Collision risk warning** (safe, warning, critical) — sent to the vehicle unit
- **Recommended braking distance** — sent to the vehicle unit
- **Pedestrian detection status** — sent to the vehicle unit
- **Alert signal** — sent to the pedestrian unit to trigger LED and audio warnings

## Components

The RSU consists of the following components:

- **LiDAR Sensor** — primary sensor for detecting pedestrians and vehicles within the junction area (detection range: 50–70 m; up to 300–400 m for high-speed external RSU)
- **Camera** — provides visual confirmation of LiDAR detections and supports object classification
- **DSRC Communication Module** — handles low-latency wireless communication with the vehicle OBU and pedestrian unit via IEEE 802.11p
- **Edge Processing Unit** — runs the collision risk algorithm and braking distance calculations locally at the junction

## Communication

The RSU supports bidirectional communication:

### Inbound

- Receives vehicle speed and GPS location from the vehicle OBU via **DSRC (IEEE 802.11p)**

### Outbound

- Sends collision risk warnings and braking distance to the vehicle unit via **DSRC (IEEE 802.11p)**
- Sends alert trigger signals to the pedestrian unit via low-latency wireless communication

## Deployment Configurations

The system supports two RSU deployment configurations based on road speed limit:

### Single RSU (Standard Junctions)
Used at junctions with a speed limit at or below 50 km/h. One RSU is mounted at the pedestrian crossing and handles all detection, processing, and communication.

### Dual RSU (High-Speed Roads)
Used where the speed limit exceeds 50 km/h (e.g., expressway-to-residential transitions). An additional external RSU is placed approximately 300–400 metres before the junction. This external RSU detects vehicles early and cross-references their transmitted speed and location to provide increased reaction time before the vehicle enters the critical braking zone.

Both configurations use the same RSU hardware.

## Operational Behaviour

The RSU continuously scans the junction area using LiDAR and camera. When a vehicle's OBU begins transmitting speed and location data, the RSU fuses this with its sensor readings to compute a braking distance and evaluate whether the vehicle can safely stop before reaching the crossing.

If a pedestrian is detected near or entering the crossing while a vehicle is approaching, the RSU calculates the collision risk level and transmits warnings simultaneously to both the vehicle unit via DSRC and the pedestrian unit via low-latency wireless communication. The risk level is updated in real time as conditions change.

## Design Considerations

The RSU is designed as the single point of truth for collision risk in the system. By centralising detection and processing at the roadside, the solution avoids placing computational burden on the vehicle or pedestrian units. This approach ensures:

- Consistent and accurate risk assessments across all road users
- Low-latency alert delivery within the system's <100 ms communication target
- Scalability — the same RSU hardware supports both single and dual deployment configurations
- Independence from vehicle or pedestrian-owned hardware for detection
