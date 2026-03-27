# Tables

## Message Flow

| Source | Destination | Message | Purpose |
| ------ | ----------- | ------- | ------- |
| Vehicle OBU | RSU | Speed, GPS, Vehicle Weight | Inform RSU of vehicle state |
| RSU | Vehicle | Risk Warning | Alert driver |
| RSU | Pedestrian System | Alert Signal | Warn pedestrian |

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

| Your System                | Module Concept     |
| -------------------------- | ------------------ |
| Car ↔ RSU communication    | V2I, V2P (DSRC)    |
| RSU ↔ Pedestrian           | V2P                |
| Real-time warning          | Safety application |
| Low latency (<100 ms)      | DSRC requirement   |
| Car sending speed/location | WAVE messages      |

## System Parameters

| Parameter | Value |
| --------- | ----- |
| Speed Limit | 60 km/h |
| Maximum Detection Range | 1000 m (1 RSU) / 1150 m (2 RSU) |
| Maximum Detection Range with LiDAR | 150 m (1 RSU) / 300 m (2 RSU) |
| Required Communication Latency | < 300 ms |
| Braking Time | Configurable by threshold |

> Maximum Detection Range takes into account maximum line-of-sight range of DSRC communication from RSU to vehicles.
>
> Maximum Detection Range with LiDAR takes LiDAR's range into account.
>
> 2nd RSU is placed 150m away from 1st RSU at the pedestrian crossing.
