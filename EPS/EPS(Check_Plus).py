def calculate_total_energy_over_intervals(data, max_voltage=28, max_current=10, max_power=280):
    """
   Typed up the pseudo code with the desired results and input it into Chatgpt
    
    """
    total_energy = 0
    
    for idx, (voltage, current, duration) in enumerate(data):
        # Validate duration
        if duration < 0:
            raise ValueError(f"Duration in interval {idx+1} must be non-negative.")
        
        # Limit voltage and current to their maximum values
        if voltage > max_voltage:
            print(f"Interval {idx+1}: Voltage ({voltage} V) exceeds max limit ({max_voltage} V). Reducing to {max_voltage} V.")
            voltage = max_voltage
        if current > max_current:
            print(f"Interval {idx+1}: Current ({current} A) exceeds max limit ({max_current} A). Reducing to {max_current} A.")
            current = max_current
        
        # Calculate power and cap at max_power
        power = voltage * current
        if power > max_power:
            print(f"Interval {idx+1}: Power ({power} W) exceeds max limit ({max_power} W). Reducing to {max_power} W.")
            power = max_power
        
        # Calculate energy for the interval
        interval_energy = power * duration
        total_energy += interval_energy
    
    return total_energy

# Input data: (voltage, amperage, duration in seconds)
data = [
    (22, 7, 300),  # Voltage and current exceed limits
    (40, 7, 60),  # Within limits
    (25, 10, 200),  # Current exceeds limit
    (10, 4, 600)   # Within limits
]

# Calculate total energy
total_energy = calculate_total_energy_over_intervals(data)
print(f"Total energy calculated: {total_energy} J")
