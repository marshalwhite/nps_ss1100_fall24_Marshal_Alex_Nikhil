# Thermal Control Subsystem (TCS)
# This script handles temperature control for spacecraft systems.

def adjust_temperature(current_temperature, target_temperature):
    """
    Adjust the temperature towards the target by a maximum of 25% of the difference.
    """
    MAX_CHANGE_FACTOR = 0.25  # 25% of the difference
    temperature_difference = target_temperature - current_temperature
    adjustment = temperature_difference * MAX_CHANGE_FACTOR
    new_temperature = current_temperature + adjustment

    print(f"Adjusting temperature by {adjustment:.2f}°C towards target.")
    return round(new_temperature, 2)

# Test the function with example values
print("Task 1: Temperature Adjustment")
current_temp = 20.0  # Current temperature in °C
target_temp = 30.0  # Target temperature in °C
new_temp = adjust_temperature(current_temp, target_temp)
print(f"New temperature: {new_temp}°C\n")

# Simulation for dynamic temperature control
def dynamic_temperature_control(initial_temp, target_temp, cycles=10):
    """
    Simulate temperature control over a series of cycles.
    Adjust temperature incrementally towards the target in each cycle.
    """
    current_temp = initial_temp
    print(f"Starting temperature: {current_temp}°C")
    for cycle in range(1, cycles + 1):
        current_temp = adjust_temperature(current_temp, target_temp)
        print(f"Cycle {cycle}: Current temperature: {current_temp}°C")
        if abs(current_temp - target_temp) < 0.1:
            print("Target temperature reached.")
            break
    print(f"Final temperature after {cycle} cycles: {current_temp}°C")
    return current_temp

# Example simulation
print("Task 2: Dynamic Temperature Control Simulation")
initial_temperature = 10.0  # Starting temperature in °C
target_temperature = 25.0  # Target temperature in °C
dynamic_temperature_control(initial_temperature, target_temperature, cycles=15)

### Script created with ChatGPT on 02DEC2024
## Prompt: Create a script in Python that meets the following parameters and executes the following instructions : "input Space craft paramters"
# Features
# Adjust Temperature:
# Adjusts the current temperature by up to 25% of the difference with the target.
# Prints the magnitude of the adjustment for clarity.
# Returns the new temperature.
# Dynamic Temperature Control:
# Simulates a realistic scenario where temperature is adjusted incrementally across a set number of cycles.
# Stops early if the target temperature is reached within a threshold (0.1°C).
# Logs temperature after each adjustment.