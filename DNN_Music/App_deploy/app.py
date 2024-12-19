import gradio as gr
import numpy as np
import keras as k
from sklearn.preprocessing import StandardScaler as skp
import joblib

# Load the previously saved model and scaler
model = k.models.load_model("DNN_v1.h5")
scaler = joblib.load('scaler.pkl')
genres = {
    "0": "Blues",
    "1": "Classical",
    "2": "Country",
    "3": "Disco",
    "4": "HipHop",
    "5": "Jazz",
    "6": "Metal",
    "7": "Pop",
    "8": "Reggae",
    "9": "Rock"
}


print("Model loaded successfully.")

# Instructions for the user
instructions = """
Please enter the feature values in the following format (comma-separated) this is a valid input entry classified as Blues:

0.335406363, 0.091048293, 0.130405024, 0.003521004, 1773.065032, 167541.6309, 1972.744388, 117335.7716, 3714.560359, 1080789.886, 
0.081850962, 0.000557687, -7.85E-05, 0.00835359, -6.82E-05, 0.005535193, 129.1992188, -118.6279144, 2440.286621, 125.0836258, 260.9569092,
-23.44372368, 364.0817261, 41.32148361, 181.6948547, -5.976108074, 152.9631348, 20.11514091, 75.65229797, -16.04541016, 40.22710419,
17.85519791, 84.32028198, -14.6334343, 83.43723297, 10.27052689, 97.00133514, -9.708278656, 66.66989136, 10.18387508, 45.10361099,
-4.681614399, 34.16949844, 8.417439461, 48.26944351, -7.233476639, 42.7709465, -2.853603363, 39.68714523, -3.241280317, 36.4882431,
0.722208977, 38.09915161, -5.050335407, 33.61807251, -0.243026793, 43.77176666

Ensure that the values are separated by commas and in the correct order as described below:

| Variable               | Description                                                                                           | Data Type | Possible Values               |Estimated Range                              |
|------------------------|-------------------------------------------------------------------------------------------------------|-----------|--------------------------------|----------------------------------------------|
| chroma_stft_mean       | Mean of the chroma short-time Fourier transform, related to the tonality.                             | Numeric   | Real values.                  |  [0.0, 1.0]                                   |
| chroma_stft_var        | Variance of the chroma short-time Fourier transform, measures tonal dispersion.                       | Numeric   | Real values.                  |  [0.0, 0.1]                                   |
| rms_mean               | Mean of the root mean square of the spectrum, reflects the average intensity.                         | Numeric   | Real values.                  |  [0.0, 1.0]                                   |
| rms_var                | Variance of the root mean square, indicates variability in intensity.                                  | Numeric   | Real values.                  |  [0.0, 0.1]                                   |
| spectral_centroid_mean | Mean spectral centroid, indicates the "brightness" of the sound.                                      | Numeric   | Real values.                  |  [0.0, 8000.0]                                |
| spectral_centroid_var  | Variance of spectral centroid, measures brightness variation.                                         | Numeric   | Real values.                  |  [0.0, 1000000.0]                             |
| spectral_bandwidth_mean| Mean spectral bandwidth, measures the width of the frequency range.                                    | Numeric   | Real values.                  |  [0.0, 4000.0]                                |
| spectral_bandwidth_var | Variance of spectral bandwidth, indicates fluctuations in the frequency range.                         | Numeric   | Real values.                  |  [0.0, 1000000.0]                             |
| rolloff_mean           | Mean rolloff frequency, where 85% of the spectral energy is concentrated.                             | Numeric   | Real values.                  |  [0.0, 8000.0]                                |
| rolloff_var            | Variance of rolloff frequency, reflects changes in spectral energy distribution.                       | Numeric   | Real values.                  |  [0.0, 1000000.0]                             |
| zero_crossing_rate_mean| Mean zero-crossing rate, indicates the frequency of sign changes in the signal.                        | Numeric   | Real values.                  |  [0.0, 1.0]                                   |
| zero_crossing_rate_var | Variance of zero-crossing rate, measures variability in sign changes.                                 | Numeric   | Real values.                  |  [0.0, 0.1]                                   |
| harmony_mean           | Mean harmony in the signal, reflects the overall tonality.                                            | Numeric   | Real values.                  |  [0.0, 1.0]                                   |
| harmony_var            | Variance of harmony, measures tonal dispersion.                                                      | Numeric   | Real values.                  | [0.0, 0.1]                                   |
| perceptr_mean          | Mean perceptuality, describes perceptual aspects of the sound.                                        | Numeric   | Real values.                  |  [0.0, 1.0]                                   |
| perceptr_var           | Variance of perceptuality, measures variability in perceptual aspects.                                | Numeric   | Real values.                  |  [0.0, 0.1]                                   |
| tempo                  | Estimated tempo of the signal, in beats per minute (bpm).                                              | Numeric   | Real values (typical: 0-300).  |  [0.0, 300.0]                                 |
| mfccX_mean             | Mean of the Mel-frequency cepstral coefficient in frequency X, related to texture of the sound.       | Numeric   | Real values.                  |  [-50.0, 50.0]                                |
| mfccX_var              | Variance of the Mel-frequency cepstral coefficient in frequency X, measures variability in texture.   | Numeric   | Real values.                  | [0.0, 100.0]                                 |

Take note that mfccX_mean and mfccX_var go from X = 1 up to 20.

Make sure to enter the features in the correct order as shown in the table.
"""

# Function to make predictions
def predict(features):
    try:
        # Split input string by commas and convert to float
        features_array = np.array([float(x) for x in features.split(",")]).reshape(1, -1)
        
        # Check if the number of features matches the expected number
        if len(features_array[0]) != 57:
            return f"Error: You must provide exactly 57 features, but you provided {len(features_array[0])}."
        
        # Apply scaling
        features_array_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(features_array_scaled)
        
        # Return the class with the highest probability
        predicted_class = np.argmax(prediction, axis=1)[0]

                # Get the genre name using the predicted class
        predicted_genre = genres[str(predicted_class)]
        
        return f"Prediction: {predicted_class} - {predicted_genre}"
    
    except ValueError as ve:
        return f"Error: Invalid input format. Please ensure all values are numbers. {ve}"
    except Exception as e:
        return f"Error: {e}"

# Create the Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Features (comma-separated)"),
    outputs="text",
    title="Music genre classificator with Keras",
    description=instructions
)

# Launch the interface
if __name__ == "__main__":
    interface.launch(share=True)
