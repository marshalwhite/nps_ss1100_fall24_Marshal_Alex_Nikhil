# @author: alexanderbeyrooty
import os
from rotate_me import apply_corrections, read_orientation_from_file, write_orientation_to_file

# Function to read the current state from a file
def read_current_state(file_path="current_state.txt"):
    """
    Read the current orientation from the state file.
    If the file doesn't exist, initialize it to (0, 0, 0).
    :param file_path: Path to the file storing current orientation
    :return: Tuple of (X, Y, Z) orientation
    """
    if not os.path.exists(file_path):
        write_orientation_to_file(file_path, (0, 0, 0))  # Default initial orientation
    return read_orientation_from_file(file_path)


# Function to calculate the rotation corrections
def calculate_rotation(current_orientation, target_orientation):
    """
    Calculate the rotation required in each axis to achieve the target orientation.
    :param current_orientation: Tuple of current (X, Y, Z) orientation
    :param target_orientation: Tuple of target (X, Y, Z) orientation
    :return: Tuple of rotation required in (X, Y, Z)
    """
    return tuple(target - current for current, target in zip(current_orientation, target_orientation))


# Function to check if orientation is within the specified tolerance
def within_tolerance(current_orientation, target_orientation, tolerance=0.1):
    """
    Check if the current orientation is within tolerance of the target orientation.
    :param current_orientation: Tuple of current (X, Y, Z) orientation
    :param target_orientation: Tuple of target (X, Y, Z) orientation
    :param tolerance: Allowed deviation in degrees
    :return: True if within tolerance, False otherwise
    """
    return all(
        abs(current - target) <= tolerance
        for current, target in zip(current_orientation, target_orientation)
    )


# Main function to align the satellite
def align_satellite(target_orientation, file_path="current_state.txt", tolerance=0.1):
    """
    Align the satellite to the target orientation.
    :param target_orientation: Tuple of target (X, Y, Z) orientation
    :param file_path: Path to the file storing current orientation
    :param tolerance: Allowed deviation in degrees
    """
    # Read the current orientation
    current_orientation = read_current_state(file_path)
    iteration = 0

    print(f"Starting alignment. Target orientation: {target_orientation}")
    while not within_tolerance(current_orientation, target_orientation, tolerance):
        iteration += 1
        print(f"\nIteration {iteration}:")
        print(f"Current orientation: {current_orientation}")

        # Calculate rotation corrections
        corrections = calculate_rotation(current_orientation, target_orientation)
        print(f"Applying corrections: {corrections}")

        # Apply corrections using the rotate_me's apply_corrections function
        current_orientation = apply_corrections(current_orientation, corrections)

        # Write the updated orientation back to the file
        write_orientation_to_file(file_path, current_orientation)
        print(f"Updated orientation: {current_orientation}")

    print("\nAlignment complete!")
    print(f"Final orientation: {current_orientation} (within {tolerance} degrees tolerance)")
    print(f"Total iterations: {iteration}")


# Example usage
if __name__ == "__main__":
    # Define the target orientations
    target_orientations = [
        (100, 200, 300),  # Target orientation 1
        (0, 0, 0),        # Target orientation 2
        (3, 30, 300)      # Target orientation 3
    ]

    # Align the satellite for each target orientation
    for idx, target in enumerate(target_orientations, start=1):
        print(f"\n=== Aligning to Target Orientation {idx}: {target} ===")
        align_satellite(target)
