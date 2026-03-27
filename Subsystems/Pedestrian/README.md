# Pedestrian Overview

## Purpose of Pedestrian Unit

The pedestrian unit acts as the pedestrian-facing component of the system. Its primary role is to receive collision risk alerts from the Road Side Unit (RSU) and deliver timely, intuitive warnings to pedestrians at or near the crossing. This enables safer decision-making when approaching or entering a blind, non-signalised junction.

## Key Responsibilities

- Receive collision risk warnings from the RSU
- Alert pedestrians through visual and audio feedback
- Escalate warning intensity based on risk level
- Deter pedestrians from entering the crossing when a collision risk is detected

## Inputs

The pedestrian unit receives the following inputs from the RSU:

- Collision risk level (e.g., safe, warning, critical)
- Alert trigger signal indicating an approaching vehicle

## Outputs

The pedestrian unit produces the following outputs:

- **Ground LED strip** — visual warning embedded at the crossing, intensity increases with risk level
- **Audio alert** — audible warning signal to attract pedestrian attention, escalates with risk level

## Components

The pedestrian unit consists of the following components:

- **Ground LED Strip** — provides a highly visible, ground-level visual cue to warn pedestrians at the crossing
- **Audio Alert System** — emits warning sounds to reach pedestrians who may not be looking at the ground

## Communication

The pedestrian unit receives one-way communication from the RSU:

- RSU transmits alert signals to the pedestrian unit via serial communication
- No outbound communication is required from the pedestrian unit

## Operational Behaviour

When the RSU detects a vehicle approaching the junction and determines a collision risk, it transmits an alert signal to the pedestrian unit. The unit activates its LED strip and audio system in response, with warning intensity scaled to the risk level.

At low risk, the LED strip may flash gently as a precaution. At critical risk, the LED and audio alerts intensify to clearly discourage the pedestrian from crossing. Once the risk clears, the alerts are deactivated.

## Design Considerations

The pedestrian unit is designed to be passive and infrastructure-mounted, requiring no input or device from the pedestrian themselves. This ensures:

- No dependency on smartphones or wearable devices
- Accessibility for all pedestrians regardless of age or technical familiarity
- Immediate, instinctive response through multi-modal alerts (visual and audio)
- Minimal maintenance footprint as a fixed installation at the crossing
