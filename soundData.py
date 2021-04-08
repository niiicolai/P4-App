# Dependencies
import threading
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import sounddevice
import time
import copy as cp

"""
    The 7 steps below provide the general usage of this class
   
    1. import class
    from soundData import SoundData
   
    2. Create a sound data object using the original data
    original_sound = SoundData('original_sound.wav')
   
    3. Load a manipulated version of the original data
    manipulated_sound = SoundData('manipulated_sound.wav')
   
    4. Manipulate the sound
    manipulated_sound.set_phase_shift(1)  # +1
    manipulated_sound.set_amplitude_shift(.1) # +.1
    manipulated_sound.set_amplitude(5) # +5
    
    5. Plot the sounds against each other
    original_sound.plot_against(manipulated_sound)
    
    6. Play the original sound using the left speaker
    original_sound.play(channel=1)
    
    7. Play the manipulated sound using the right speaker
    manipulated_sound.play(channel=2)
"""


class SoundData:
    """A class used to easy manipulate an audio file,
       plot its graph, and listen to its output"""

    def __init__(self, filename):
        """The class constructor. Reads an audio file with
           the name provided as an argument and save its
           data as a 1-D. array of amplitude and a related
           sample rate"""
        self.__data, self.__sample_rate = sf.read(filename)
        self.__amplitude = 1
        self.__amplitude_shift = 0
        self.__phase_shift = 0
        self.__is_playing = False
        self.__possible_duration = 1.6

    def get_shifted_data_array(self):
        """Returns the audio audio shifted either left or right
           using zeros matching the phase shift in a given direction"""

        # Calculate number of shifts
        shifts = np.zeros(int(self.__sample_rate * abs(self.__phase_shift)))

        # Get possible shifts
        possible_shifts = np.zeros(int(self.__sample_rate * self.__possible_duration))

        # Copy original data
        copied_data = cp.copy(self.__data)

        # Calculate missing shifts
        missing_zeros = int(self.__sample_rate * self.__possible_duration)-len(shifts)
        opposite_side_zeros = abs(int(self.__possible_duration+missing_zeros))
        missing_shifts = np.zeros(opposite_side_zeros)

        # Insert shifts before
        copied_data = np.append(shifts, copied_data)
        # Insert possible shifts after
        # + the missing shifts on the left side
        # to ensure the list always has the same length
        copied_data = np.append(copied_data, missing_shifts)

        return copied_data

    def set_amplitude(self, amplitude):
        """Changes the amplitude of the final data output"""
        self.__amplitude = amplitude

    def set_amplitude_shift(self, amplitude_shift):
        """Shifts the amplitude of the final data output,
           valid range: (0.0-0.9)"""
        self.__amplitude_shift = amplitude_shift

    def set_phase_shift(self, phase_shift):
        """Shifts the phase of the final data output,
           currently only working in the positive direction
           when playing the sound, however it works when plotting
           the graph in both directions"""
        self.__phase_shift = phase_shift

    def get_data(self):
        """Returns the data multiplied with the amplitude parameter
           and shifted by adding the amplitude-shift parameter"""
        return self.get_shifted_data_array() * self.__amplitude #+ self.__amplitude_shift

    def get_amplitude_shift(self):
        """Returns the amplitude shift parameter"""
        return self.__amplitude_shift

    def get_amplitude(self):
        """Returns the amplitude parameter"""
        return self.__amplitude

    def get_phase_shift(self):
        """Returns the phase shift parameter"""
        return self.__phase_shift

    def get_sample_rate(self):
        """Returns the audio files sample rate"""
        return self.__sample_rate

    def get_time(self):
        """Returns an array of evenly spaced time points used
           to represent the audio files time sequence on the x-axis"""
        data = self.get_data()
        return np.linspace(0, len(data) / self.__sample_rate, num=len(data))

    def save(self, name):
        """Save the current state of the data to a file"""
        sounddevice.write(name, self.get_data(), self.__sample_rate)

    def play(self, channel):
        """Plays the current state of the audio data"""
        sounddevice.play(self.get_data(), self.__sample_rate, mapping=[channel])
        return sounddevice.wait()

    def play_async(self, channel):
        """Play the audio file in a separate thread"""
        thread = threading.Thread(target=self.play, args=(channel, ))
        thread.start()

    def plot(self, title="Plot of a single audio wave"):
        """Plot the current state of data with time on the
           x-axis and amplitude on the y-axis"""
        plt.figure(1)
        plt.title(title)
        plt.plot(self.get_time(), self.get_data())
        plt.show()

    def plot_against(self, other, title="Plot of two audio waves"):
        """Plot the current state of data with time on the
           x-axis and amplitude on the y-axis, against the
           same parameters on another sound data object"""
        plt.figure(1)
        plt.title(title)
        plt.plot(self.get_time(), self.get_data())
        plt.plot(other.get_time(), other.get_data())
        plt.show()
