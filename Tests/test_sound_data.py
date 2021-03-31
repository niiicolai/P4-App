import unittest
import soundfile as sf
import numpy as np
import copy as cp
from soundData import SoundData


# TEST DATA
# The path to a test wave file
TEST_FILE_NAME = './assets/sound/test.wav'

# Load the wave file using an external library
RAW_DATA, SAMPLE_RATE = sf.read(TEST_FILE_NAME)
# Calculate time data for the raw audio data
RAW_TIME = np.linspace(0, len(RAW_DATA) / SAMPLE_RATE, num=len(RAW_DATA))
# Create a sound data object used for the tests
SOUND_DATA = SoundData(TEST_FILE_NAME)
# Get the default phase shift, used to comparing
DEFAULT_PHASE_SHIFT = SOUND_DATA.get_default_phase_shift()

# Create a version of the raw data with double amplitude
# and is shifted 1 in the amplitude domain
RAW_DATA_DOUBLE_AMP_1_SHIFT = 2 * cp.copy(RAW_DATA) + 1

# Create a version of the raw time that is shifted
# by 2 in the phase shift domain + the default phase shift value
RAW_TIME_SHIFTED_BY_2 = cp.copy(RAW_TIME) + (DEFAULT_PHASE_SHIFT + 2)


class TestSoundData(unittest.TestCase):
    """Used to test the class SoundData in soundData.py"""

    def test_set_amplitude(self):
        """Ensure set_amplitude updates the
           amplitude parameter correctly"""
        initial_value = SOUND_DATA.get_amplitude()
        SOUND_DATA.set_amplitude(initial_value + 1)
        self.assertEqual(SOUND_DATA.get_amplitude(), initial_value + 1, "Should be initial value + 1")

    def test_set_amplitude_shift(self):
        """Ensure set_amplitude_shift updates the
           amplitude_shift parameter correctly"""
        initial_value = SOUND_DATA.get_amplitude_shift()
        SOUND_DATA.set_amplitude_shift(initial_value + .1)
        self.assertEqual(SOUND_DATA.get_amplitude_shift(), initial_value + .1, "Should be initial value + .1")

    def test_set_phase_shift(self):
        """Ensure set_phase_shift updates the
           phase_shift parameter correctly"""
        SOUND_DATA.set_phase_shift(1)
        self.assertNotEqual(SOUND_DATA.get_phase_shift(), DEFAULT_PHASE_SHIFT + 2, "Should not be 2")
        self.assertEqual(SOUND_DATA.get_phase_shift(), DEFAULT_PHASE_SHIFT + 1, "Should be 1")

    def test_get_data(self):
        """Ensure get_data returns a modified version
           of the sound data using the amplitude and
           amplitude_shift parameters"""
        SOUND_DATA.set_amplitude_shift(1)
        SOUND_DATA.set_amplitude(2)
        self.assertEqual((SOUND_DATA.get_data() == RAW_DATA_DOUBLE_AMP_1_SHIFT).all(), True, "Should be True")

    def test_get_sample_rate(self):
        """Ensure get_sample_rate returns the correct
           sample rate parameter"""
        self.assertEqual(SOUND_DATA.get_sample_rate(), SAMPLE_RATE, "Should be equal")

    def test_get_time(self):
        """Ensure get_time returns a modified version
           of time data using the phase shift parameter"""
        SOUND_DATA.set_phase_shift(2)
        self.assertEqual((SOUND_DATA.get_time() == RAW_TIME_SHIFTED_BY_2).all(), True, "Should be True")

    """
        OTHER METHODS:
        The SoundData class contains also the following method.
        But it is concluded that the results of executing them
        easily can be validated either using the visual- or 
        auditory system, or are simply not used in the main 
        application but only exist for debugging purpose. 
                
        - save()
        - play(channel=integer)
        - play_async(channel=integer)
        - plot()
        - plot_against(other=SoundData)
    """


if __name__ == '__main__':
    unittest.main()
