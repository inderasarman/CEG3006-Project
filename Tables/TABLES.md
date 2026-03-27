# Tables

## Message Flow

| Source | Destination | Message | Protocol | Trigger |
| ------ | ----------- | ------- | -------- | ------- |
| Vehicle OBU | RSU | Speed, GPS location, Vehicle Weight | DSRC (IEEE 802.11p) | Continuous while driving |
| RSU (External) | RSU (Junction) | Vehicle detected early | Serial | Vehicle enters detection range |
| RSU | Vehicle OBU | Risk warning, braking distance | DSRC (IEEE 802.11p) | Collision risk detected |
| RSU | Pedestrian System | Alert signal | Serial | Pedestrian detected + risk present |

## Hardware List

| Component | Function | Location |
| --------- | -------- | -------- |
| RSU ([LiDAR](https://www.seyond.com/products/falcon-k1/) + [Depth Camera](https://amicus.com.sg/products/intel-r-realsense-tm-depth-camera-d455f/)) | Detect vehicles and pedestrians | Junction |
| Vehicle OBU | Transmit speed, weight and location | Vehicle |
| HUD | Display warnings to driver | Vehicle |
| LED Strip | Visual warning for pedestrian | Crossing |
| Audio Alert | Audible warning for pedestrian | Crossing |

> Example LiDAR's max range is 500m. System assumes max LiDAR range as 150m for reliability.

## Module Mapping

| System Function            | Module Concept     | Description                                        |
| -------------------------- | ------------------ | -------------------------------------------------- |
| Car ↔ RSU communication    | V2I (DSRC)         | Vehicle communicates with roadside infrastructure  |
| RSU ↔ Pedestrian           | V2P                | Infrastructure delivers warnings to pedestrians    |
| Real-time warning          | Safety application | Collision risk alert triggered by RSU logic        |
| Low latency (<100 ms)      | DSRC requirement   | Communication delay constraint for safety messages |

## System Parameters

| Parameter | Value |
| --------- | ----- |
| Speed Limit | 50 km/h (Normal roads) / 90 km/h (Expressways) |
| Maximum Detection Range | 1000 m (1 RSU) / 1150 m (2 RSU) |
| Maximum Detection Range with LiDAR | 150 m (1 RSU) / 300 m (2 RSU) |
| Required Communication Latency | < 300 ms |
| Braking Time | Configurable by threshold |

> Maximum Detection Range takes into account maximum line-of-sight range of DSRC communication from RSU to vehicles.
>
> Maximum Detection Range with LiDAR takes LiDAR's range into account.
>
> 2nd RSU is placed 150m away from 1st RSU at the pedestrian crossing.
>
> 300 ms latency was deemed sufficient in comparison to estimated human reaction time of 200 ms to give drivers enough time to react.
