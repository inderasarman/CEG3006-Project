from dataclasses import dataclass
from enum import Enum


# =========================
# CONFIGURABLE PARAMETERS
# =========================

# Speed limit of the road in km/h
SPEED_LIMIT = 60

# Estimated system + driver reaction time (seconds)
# Includes perception, decision, and actuation delay before braking starts
# Larger value → more conservative (longer stopping distance)
REACTION_TIME_S = 1.0

# Reference deceleration capability (m/s^2)
# Represents baseline braking strength for a reference vehicle under normal conditions
# Typical comfortable braking: ~3–5 m/s^2, aggressive braking: ~6–8 m/s^2
# Larger value → shorter braking distance (less conservative)
REFERENCE_DECELERATION_MPS2 = 6.0

# Reference vehicle mass (kg)
# Sets the baseline for mass comparison:
# Increase → less conservative (most vehicles appear lighter → shorter stopping distance)
# Decrease → more conservative (most vehicles appear heavier → longer stopping distance)
REFERENCE_MASS_KG = 1500.0

# Exponent controlling how vehicle mass affects braking distance
# p = 0   → ignore mass effect (all vehicles treated the same)
# p = 1   → braking distance scales linearly with mass
# 0 < p < 1 → moderate influence of mass (recommended)
# Larger value → heavier vehicles penalised more
MASS_EXPONENT = 0.6

# Fixed safety buffer before the crossing (metres)
# Ensures the vehicle does not stop exactly at the crossing line
# Accounts for positioning uncertainty and safety margin
CROSSING_BUFFER_M = 5.0

# Constant threshold margin in metres
# For configuring of when to send cautioning message
SAFE_MARGIN_M = 5.0

# Risk scaling factor (dimensionless)
# Used in risk score calculation: Risk = 1 - D_cross / (k * D_required)
# Larger value → system becomes more conservative (higher perceived risk)
# Smaller value → system becomes less sensitive to risk
RISK_MULTIPLIER = 1.0


# =========================
# MODEL DEFINITIONS
# =========================

class CrossingDecision(str, Enum):
    NORMAL = "normal"
    CAUTION = "caution"
    MUST_STOP = "must_stop"


@dataclass
class CrossingModelConfig:
    reaction_time_s: float
    reference_deceleration_mps2: float
    reference_mass_kg: float
    mass_exponent: float
    crossing_buffer_m: float
    safe_margin_m: float
    risk_multiplier: float

    def __post_init__(self):
        self.verify_configs()

    def verify_configs(self):
        # Implementation to validate configs
        

def create_default_config() -> CrossingModelConfig:
    return CrossingModelConfig(
        reaction_time_s=REACTION_TIME_S,
        reference_deceleration_mps2=REFERENCE_DECELERATION_MPS2,
        reference_mass_kg=REFERENCE_MASS_KG,
        mass_exponent=MASS_EXPONENT,
        crossing_buffer_m=CROSSING_BUFFER_M,
        safe_margin_m=SAFE_MARGIN_M,
        stop_threshold=STOP_THRESHOLD,
        risk_multiplier=RISK_MULTIPLIER,
    )


# =========================
# CORE FUNCTIONS
# =========================

def required_stopping_distance(speed_mps, vehicle_mass_kg, config):
    # required stopping distance influence by configurations
    reaction_distance = speed_mps * config.reaction_time_s

    mass_factor = (vehicle_mass_kg / config.reference_mass_kg) ** config.mass_exponent

    braking_distance = (speed_mps ** 2 / (2.0 * config.reference_deceleration_mps2)) * mass_factor

    return reaction_distance + braking_distance + config.crossing_buffer_m


def stopping_margin(distance_to_crossing_m, speed_mps, vehicle_mass_kg, config):
    # margin for stopping, taking into account threshold paramters
    return distance_to_crossing_m - required_stopping_distance(speed_mps, vehicle_mass_kg, config)


def crossing_decision(distance_to_crossing_m, speed_mps, vehicle_mass_kg, config):
    if speed_mps > SPEED_LIMIT:
        return CrossingDecision.MUST_STOP

    margin = stopping_margin(distance_to_crossing_m, speed_mps, vehicle_mass_kg, config)

    # see if safety margin is fulfilled
    if margin >= config.safe_margin_m:
        return CrossingDecision.NORMAL
    # safety margin unfulfilled, send warning
    elif margin >= 0.0:
        return CrossingDecision.CAUTION
    # not meeting threshold requirements (actual braking distance accounting threshold params > actual distance to crossing)
    # send emergency alert to vehicle
    else:
        return CrossingDecision.MUST_STOP


def evaluate_crossing(distance_to_crossing_m, speed_mps, vehicle_mass_kg, config):
    d_req = required_stopping_distance(speed_mps, vehicle_mass_kg, config)
    r = distance_to_crossing_m / d_req if d_req > 0 else float("inf")
    risk = risk_score(distance_to_crossing_m, speed_mps, vehicle_mass_kg, config)
    decision = crossing_decision(distance_to_crossing_m, speed_mps, vehicle_mass_kg, config)

    return get_alert_level(r, risk)


# =========================
# EXAMPLE USAGE
# =========================

# # Default config
# config = create_default_config()
#
# # Custom config
# config = CrossingModelConfig(
#     REACTION_TIME_S,
#     REFERENCE_DECELERATION_MPS2,
#     REFERENCE_MASS_KG,
#     MASS_EXPONENT,
#     CROSSING_BUFFER_M,
#     SAFE_MARGIN_M,
#     RISK_MULTIPLIER,
# )
#
# result = evaluate_crossing(
#     distance_to_crossing_m=30.0,
#     speed_mps=12.0,
#     vehicle_mass_kg=1800.0,
#     config=config,
# )
#
# for k, v in result.items():
#     print(f"{k}: {v}")
