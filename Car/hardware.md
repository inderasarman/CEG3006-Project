# Car Overview

## Purpose of Vehicle Unit

The vehicle unit acts as the driver-facing component of the system. Its primary role is to receive real-time collision risk information from the Road Side Unit (RSU), process this information together with the vehicle’s current state, and present clear, non-intrusive warnings to the driver. This enables safer decision-making when approaching blind, non-signalised junctions.

---

## Key Responsibilities

- Receive collision risk warnings from the RSU  
- Transmit vehicle data such as speed and location to the RSU  
- Validate the relevance of incoming warnings based on current vehicle state  
- Display warnings to the driver through the Head-Up Display (HUD)  
- Assist the driver in making safe decisions without taking direct control  

---

## Inputs

The vehicle unit receives the following inputs from the RSU:

- Collision risk level (e.g., safe, warning, critical)  
- Recommended braking distance  
- Pedestrian detection status  
- Distance to junction (optional)  

Additionally, the vehicle uses internal inputs:

- Current vehicle speed  
- Vehicle position (GPS data)  

---

## Outputs

The vehicle unit produces the following outputs:

- Visual warnings displayed on the HUD  
- Braking distance visualization  
- Speed warning indicator if the vehicle is travelling too fast  
- Continuous transmission of vehicle speed and location to the RSU  

---

## Components

The vehicle unit consists of the following components:

- **On-Board Unit (OBU)** — Handles communication and processing of incoming and outgoing data  
- **DSRC Module** — Enables low-latency communication with the RSU  
- **Speed Sensor** — Provides real-time vehicle speed data  
- **Head-Up Display (HUD)** — Displays warnings and braking information to the driver  
- **CAN Interface** — Connects internal vehicle systems and distributes relevant data  

---

## Communication

The vehicle unit supports two types of communication:

### External Communication
- Vehicle communicates with the RSU using **DSRC (IEEE 802.11p)**  
- Enables low-latency transmission of safety-critical messages  

### Internal Communication
- Data is shared within the vehicle using the **CAN bus**  
- Ensures reliable communication between the OBU, sensors, and display systems  

---

## Operational Behaviour

When the vehicle approaches a blind junction, the On-Board Unit continuously transmits its speed and location to the RSU. The RSU processes this information along with its sensor data to determine collision risk.

Upon receiving a warning message, the vehicle evaluates the risk level against its current speed and position. If the warning is relevant, the system displays braking distance and visual alerts on the HUD. The driver is then able to respond by slowing down or stopping before reaching the junction.

---

## Design Considerations

The vehicle system is designed as a driver-assistance system rather than an autonomous control system. It does not directly control braking or steering. Instead, it enhances situational awareness by providing timely and relevant information to the driver.

This approach ensures that:
- The driver remains in full control of the vehicle  
- The system is non-intrusive and does not disrupt normal driving behaviour  
- The solution remains practical and feasible within real-world constraints  
