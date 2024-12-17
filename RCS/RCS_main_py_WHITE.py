# Reaction Control Subsystem (RCS)
# This script handles malfunction detection and velocity change calculations for spacecraft thrusters.

def check_thruster_limits(thrust, flow_rate, exhaust_velocity):
    """
    Check input values for thrust, flow rate, and exhaust velocity against set limits.
    Print out-of-limit parameters.
    """
    MAX_THRUST = 100  # Newtons
    MAX_FLOW_RATE = 0.05  # kg/s
    MAX_EXHAUST_VELOCITY = 2000  # m/s

    if thrust > MAX_THRUST:
        print(f"Thruster malfunction: Thrust exceeds limit by {thrust - MAX_THRUST} N")
    if flow_rate > MAX_FLOW_RATE:
        print(f"Thruster malfunction: Flow rate exceeds limit by {flow_rate - MAX_FLOW_RATE} kg/s")
    if exhaust_velocity > MAX_EXHAUST_VELOCITY:
        print(f"Thruster malfunction: Exhaust velocity exceeds limit by {exhaust_velocity - MAX_EXHAUST_VELOCITY} m/s")


def calculate_velocity_change(flow_rate, exhaust_velocity, elapsed_time, spacecraft_mass):
    """
    Calculate change in velocity (Δv) for a maneuver event.
    """
    thrust = flow_rate * exhaust_velocity
    delta_v = (thrust * elapsed_time) / spacecraft_mass
    return delta_v


def calculate_velocity_change_3d(flow_rates, exhaust_velocities, elapsed_times, spacecraft_mass):
    """
    Calculate change in velocity (Δv) for maneuvers across three axes.
    """
    delta_v = [0, 0, 0]  # Change in velocity for x, y, z axes
    for i in range(3):
        thrust = flow_rates[i] * exhaust_velocities[i]
        delta_v[i] = (thrust * elapsed_times[i]) / spacecraft_mass
    return tuple(delta_v)


# Spacecraft Parameters
spacecraft_mass = 500  # kg

# Task 1: Malfunction Detection
print("Task 1: Malfunction Detection")
check_thruster_limits(120, 0.06, 2100)  # Example test case
check_thruster_limits(80, 0.03, 1500)  # Example test case

# Task 2: Velocity Change Calculation
print("\nTask 2: Velocity Change Calculation")
events = [
    (0.02, 1000, 5),  # ṁ, ve, Δt
    (0.06, 1000, 3),
    (0.05, 2000, 10),
]
for flow_rate, exhaust_velocity, elapsed_time in events:
    delta_v = calculate_velocity_change(flow_rate, exhaust_velocity, elapsed_time, spacecraft_mass)
    print(f"Δv for event (ṁ={flow_rate}, ve={exhaust_velocity}, Δt={elapsed_time}) is {delta_v:.2f} m/s")

# Check Plus: 3D Velocity Change
print("\nCheck Plus: 3D Velocity Change")
flow_rates = [0.04, 0.03, 0.01]  # kg/s for x, y, z
exhaust_velocities = [2000, 2000, 2000]  # m/s for x, y, z
elapsed_times = [15, 4, 3]  # seconds for x, y, z
delta_v_3d = calculate_velocity_change_3d(flow_rates, exhaust_velocities, elapsed_times, spacecraft_mass)
print(f"Δv for 3D event is {delta_v_3d}")
# Script created with ChatGPT on 02DEC2024.
# Prompt used: Create a script in Python that meets the following parameters and executes the following instructions : "input Space craft paramters" 
# Features
# Malfunction Detection:
# Checks if thruster values exceed their maximum limits.
# Outputs which parameter is malfunctioning and by how much.
# Velocity Change Calculation:
# Computes Δv for single thruster events.
# 3D Velocity Change Calculation:
# Computes Δv for all three thrusters operating simultaneously.
# Example Outputs
# Malfunction Detection:
# Identifies any thrusters exceeding the predefined limits.
# Velocity Change Calculation:
# Calculates Δv for predefined inputs.
# Check Plus:
# Computes Δv for maneuvers in 3D space.