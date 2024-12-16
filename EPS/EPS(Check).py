def solar_power_and_energy(voltage, current, time_elapsed, max_voltage=28, max_current=10, max_power=280):
    """
    Typed up the pseudo code with the desired results and input it into Chatgpt
    Modified the code by adding the Check plus pseudo code in Chatgpt
    
    """
    # Limit voltage and current to their maximum values
    if voltage > max_voltage:
        print(f"Voltage ({voltage} V) exceeds maximum limit ({max_voltage} V). Reducing to {max_voltage} V.")
        voltage = max_voltage
    if current > max_current:
        print(f"Current ({current} A) exceeds maximum limit ({max_current} A). Reducing to {max_current} A.")
        current = max_current
    
    # Calculate power and ensure it does not exceed max_power
    power = voltage * current
    if power > max_power:
        print(f"Power ({power} W) exceeds maximum limit ({max_power} W). Reducing to {max_power} W.")
        power = max_power
    
    # Ensure time elapsed is non-negative
    if time_elapsed < 0:
        raise ValueError("Time elapsed must be non-negative.")
    
    # Calculate total energy
    energy = power * time_elapsed
    
    # Return results as a dictionary
    return {
        'power': power,
        'energy': energy
    }

# Inputs
voltage = 30  # Volts
current = 8  # Amperes
time_elapsed = 180  # Seconds (1 hour)

# Calculate power and energy
results = solar_power_and_energy(voltage, current, time_elapsed)
print(f"Instantaneous power: {results['power']} W")
print(f"Total energy available for battery charging: {results['energy']} J")
