import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_rgb_image(red_csv, green_csv, blue_csv):
    """
    Typed up my pseudo code with detailed instructions of what I want my code to do
    and input it into Chatgpt. This is the result.
    
    """
    # Load the raw R, G, and B band data from CSV files
    # Had to fix this part of the code as it gave me a blank image
    red_band = pd.read_csv(red_csv).to_numpy()
    green_band = pd.read_csv(green_csv).to_numpy()
    blue_band = pd.read_csv(blue_csv).to_numpy()

    # Ensure that all bands have the same dimensions
    if not (red_band.shape == green_band.shape == blue_band.shape):
        raise ValueError("All bands must have the same dimensions.")

    # Combine the bands into a single RGB image
    rgb_image = np.stack((red_band, green_band, blue_band), axis=-1)

    # Normalize values for visualization if necessary
    rgb_image_normalized = rgb_image / np.max(rgb_image)

    # Visualize the results
    plt.figure(figsize=(10, 10))
    plt.imshow(rgb_image_normalized)
    plt.title("RGB Image")
    plt.axis("off")
    plt.show()

    return rgb_image

# File locations:
red_csv = r"C:\Users\Nikhil Taniparti\Desktop\Nikhil Narayan Taniparti\Naval Postgraduate School (NPS)\Fall AY25\SS1100 Intro to Programming for Space Applications\Final Project\red.csv"
green_csv = r"C:\Users\Nikhil Taniparti\Desktop\Nikhil Narayan Taniparti\Naval Postgraduate School (NPS)\Fall AY25\SS1100 Intro to Programming for Space Applications\Final Project\green.csv"
blue_csv = r"C:\Users\Nikhil Taniparti\Desktop\Nikhil Narayan Taniparti\Naval Postgraduate School (NPS)\Fall AY25\SS1100 Intro to Programming for Space Applications\Final Project\blue.csv"

rgb_image = create_rgb_image(red_csv, green_csv, blue_csv)
