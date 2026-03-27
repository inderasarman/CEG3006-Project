# Tables

## Message Flow

| Source | Destination | Message | Protocol | Trigger |
| ------ | ----------- | ------- | -------- | ------- |
| Vehicle OBU | RSU | Speed, GPS location | DSRC (IEEE 802.11p) | Continuous while driving |
| RSU (External) | RSU (Junction) | Vehicle detected early | Serial | Vehicle enters detection range |
| RSU | Vehicle OBU | Risk warning, braking distance | DSRC (IEEE 802.11p) | Collision risk detected |
| RSU | Pedestrian System | Alert signal | Serial | Pedestrian detected + risk present |

## Hardware List

| Component | Function | Location |
| --------- | -------- | -------- |
| LiDAR Sensor | Detect vehicles and pedestrians | Junction |
| Depth Camera | Visual confirmation of detected objects | Junction |
| Edge Processing Unit | Compute collision risk and braking distance | Junction |
| DSRC Communication Module | Send and receive messages between RSU and vehicle | Junction + Vehicle |
| Vehicle OBU | Process incoming warnings and transmit vehicle data | Vehicle |
| Speed Sensor | Provide real-time vehicle speed | Vehicle |
| HUD | Display braking distance and warnings to driver | Vehicle |
| LED Strip | Visual warning for pedestrian | Crossing |
| Audio Alert | Audible warning for pedestrian | Crossing |

## Module Mapping

| System Function            | Module Concept     | Description                                          |
| -------------------------- | ------------------ | ---------------------------------------------------- |
| Car ↔ RSU communication    | V2I (DSRC)         | Vehicle communicates with roadside infrastructure    |
| RSU ↔ Pedestrian           | V2P                | Infrastructure delivers warnings to pedestrians      |
| Real-time warning          | Safety application | Collision risk alert triggered by RSU logic          |
| Low latency (<100 ms)      | DSRC requirement   | Communication delay constraint for safety messages   |

## System Parameters

| Parameter                   | Value       | Notes                              |
| --------------------------- | ----------- | ---------------------------------- |
| Speed Limit (Standard)      | 50 km/h     | Single RSU deployment              |
| Speed Limit (High-speed)    | >50 km/h    | Dual RSU deployment                |
| Detection Range             | 50–70 m     | Junction RSU                       |
| High-speed Detection Range  | 300–400 m   | External RSU on high-speed roads   |
| Communication Latency       | <100 ms     | DSRC requirement                   |
| Estimated Stopping Time     | 3.5–4.6 s   | Based on vehicle speed at junction |
