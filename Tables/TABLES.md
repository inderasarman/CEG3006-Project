# Tables

## Message Flow

| Source | Destination | Message | Purpose |
| ------ | ----------- | ------- | ------- |
| Vehicle OBU | RSU | Speed, GPS | Inform RSU of vehicle state |
| RSU | Vehicle | Risk Warning | Alert driver |
| RSU | Pedestrian System | Alert Signal | Warn pedestrian |

## Hardware List

| Component | Function | Location |
| --------- | -------- | -------- |
| RSU (LiDAR + Camera) | Detect vehicles and pedestrians | Junction |
| Vehicle OBU | Transmit speed and location | Vehicle |
| HUD | Display warnings to driver | Vehicle |
| LED Strip | Visual warning for pedestrian | Crossing |
| Audio Alert | Sound warning for pedestrian | Crossing |

## System Parameters

| Parameter | Value |
| --------- | ----- |
| Speed Limit | 50 km/h |
| Detection Range | 50–70 m |
| High-speed Detection | 300–400 m |
| Communication Latency | <100 ms |
| Braking Time | 3.5–4.6 s |
