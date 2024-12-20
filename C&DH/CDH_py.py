# @author: alexanderbeyrooty

def parse_command(command):
    """
    Parse a command string based on the formatted schema.
    :param command: String command in the format "SUB:CMDxx:parameter"
    :return: Tuple (subsystem_name, command_description, parameter_value) or error message
    """
    subsystems = {
        "RCS": "Reaction Control Subsystem",
        "TCS": "Thermal Control Subsystem",
        "ACS": "Attitude Control Subsystem",
        "EPS": "Electrical Power Subsystem",
        "CDH": "Command & Data Handling",
        "TTC": "Telemetry, Tracking, & Command",
        "PL1": "Payload System 1",
        "PL2": "Payload System 2"
    }

    commands = {
        "CMD01": "THRUST X",
        "CMD02": "THRUST Y",
        "CMD03": "THRUST Z",
        "CMD04": "SAFE MODE"
    }

    try:
        # Split the command into its components
        parts = command.split(":")
        if len(parts) != 3:
            raise ValueError("Invalid command format. Must be 'SUB:CMDxx:parameter'.")

        subsystem_code, command_code, parameter = parts
        subsystem_name = subsystems.get(subsystem_code, "Unknown Subsystem")
        command_description = commands.get(command_code, "Unknown Command")
        parameter_value = float(parameter)

        return subsystem_name, command_description, parameter_value

    except ValueError as e:
        return f"Error parsing command: {e}"


# Example usage
command = "RCS:CMD01:10"
result = parse_command(command)
print(result)


def parse_and_validate_command(command, command_ranges):
    """
    Parse a command and validate the parameter against acceptable ranges.
    :param command: String command in the format "SUB:CMDxx:parameter"
    :param command_ranges: Dictionary with command ranges for validation
    :return: Tuple (subsystem_name, command_description, parameter_value) or error message
    """
    subsystems = {
        "RCS": "Reaction Control Subsystem",
        "TCS": "Thermal Control Subsystem",
        "ACS": "Attitude Control Subsystem",
        "EPS": "Electrical Power Subsystem",
        "CDH": "Command & Data Handling",
        "TTC": "Telemetry, Tracking, & Command",
        "PL1": "Payload System 1",
        "PL2": "Payload System 2"
    }

    commands = {
        "CMD01": "THRUST X",
        "CMD02": "THRUST Y",
        "CMD03": "THRUST Z",
        "CMD04": "SAFE MODE"
    }

    try:
        # Split the command into its components
        parts = command.split(":")
        if len(parts) != 3:
            raise ValueError("Invalid command format. Must be 'SUB:CMDxx:parameter'.")

        subsystem_code, command_code, parameter = parts
        subsystem_name = subsystems.get(subsystem_code, "Unknown Subsystem")
        command_description = commands.get(command_code, "Unknown Command")

        # Convert parameter to float and validate
        parameter_value = float(parameter)
        if command_code in command_ranges:
            min_value, max_value = command_ranges[command_code]
            if not (min_value <= parameter_value <= max_value):
                raise ValueError(
                    f"Parameter {parameter_value} out of range for {command_code} "
                    f"({min_value} - {max_value})."
                )

        return subsystem_name, command_description, parameter_value

    except ValueError as e:
        return f"Error parsing or validating command: {e}"


# Command ranges for validation
command_ranges = {
    "CMD01": (0, 100),  # Example range for THRUST X
    "CMD02": (0, 100),
    "CMD03": (0, 100),
    "CMD04": (-10, 10)  # Example range for SAFE MODE
}

# Example usage
command = "RCS:CMD01:120"  # Invalid parameter
result = parse_and_validate_command(command, command_ranges)
print(result)

commands_to_test = [
    "EPS:CMD01:0",      # Valid command
    "ACS:CMD04:-1",     # Valid but near boundary
    "RCS:INVALID:0",    # Invalid command code
    "RCS:CMD01:150"     # Parameter out of range
]

for cmd in commands_to_test:
    print(parse_and_validate_command(cmd, command_ranges))
