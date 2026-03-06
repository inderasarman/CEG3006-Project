# Junction Safety System

## 1. System Integration

### Brief Description
The proposed Junction Safety System is designed to improve pedestrian safety at road junctions by warning approaching vehicles when pedestrians are detected near a crossing area.

In this system, proximity sensors are installed at pedestrian traffic lights near the junction. These sensors continuously monitor the waiting area near the pedestrian crossing. When a pedestrian is detected within the sensing range, the system assumes that a pedestrian may intend to cross the road.

Once the proximity sensor detects a pedestrian, the traffic light unit sends a signal to a nearby wireless communication relay unit (RSU). This relay unit broadcasts a warning message to approaching vehicles using short-range wireless communication.

Vehicles equipped with the Junction Safety System receive this signal through their Onboard Unit (OBU). The vehicle then uses its current speed and navigation information to calculate the required braking distance needed to safely stop before the junction or pedestrian crossing.

This braking distance is displayed to the driver through the Head-Up Display (HUD) on the windshield. The display provides the driver with a visual indication of how much distance is required to stop safely if a pedestrian begins crossing.

By detecting pedestrians early and communicating this information to vehicles, the Junction Safety System helps drivers slow down earlier and reduce the risk of collisions at intersections.

### System Architecture
Explain the overall architecture of your system. Include diagrams, figures, or drawings that show how components interact.

### Functions and Messages
Describe the key functions and messages used by your system. You may include flow charts, pseudocode, or tables to illustrate how data flows between parts of the system.

### Hardware Components and Parameters

| # | Component | Function | Range | Latency | Bandwidth |
|---|-----------|----------|-------|---------|-----------|
| 1 | Pedestrian Traffic Light with Proximity Sensor | Detects pedestrians near crossing | 5-10m | <100ms | N/A |
| 2 | Wireless Vehicle Communication Relay (RSU) | Broadcasts safety messages to vehicles | 100-500m | <50ms | 10 Mbps |
| 3 | Vehicle with Junction Safety System (OBU + HUD) | Receives message and displays braking distance | Vehicle receiver | <100ms | 5 Mbps |



### Use Case
Provide a 100-200 word use case that depicts your system in a real-world scenario, demonstrating how it would be used and what benefits it brings.

## 2. Decision Log

The decision log records technical decisions, their rationale, and evolution of the system. The log should have at least 10 entries, with references to repository documentation where appropriate.

| Date | Trigger / Problem | Options / Alternatives | Evaluation Criteria | Decision and Rationale | AI Usage (if any) | Team Members |
|------|-------------------|------------------------|---------------------|------------------------|-------------------|--------------|
| YYYY-MM-DD | Describe what caused this entry | List realistic alternative approaches | Explain how options were compared (metrics: latency, cost, power, etc.) | State the decision taken and rationale | Note how AI contributed and what required human correction | Team member(s) responsible |

(Repeat rows until you have at least 10 entries.)

---

*Feel free to include this log either in the README or as a separate file as needed.*
