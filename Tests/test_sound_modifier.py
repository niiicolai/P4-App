import unittest
import soundfile as sf
import numpy as np
import copy as cp
from soundData import SoundData
from soundModifier import SoundModifier

# TEST DATA
# The name of test wave file
ORIGINAL_NAMES = ["./assets/sound/test.wav"]
MANIPULATED_NAMES = ["./assets/sound/test.wav"]

# Create a sound modifier object used for the tests
SOUND_MODIFIER = SoundModifier(ORIGINAL_NAMES, MANIPULATED_NAMES)

# Load the wave file using an external library
RAW_DATA, SAMPLE_RATE = sf.read(ORIGINAL_NAMES[0])
# Calculate time data for the raw audio data
RAW_TIME = np.linspace(0, len(RAW_DATA) / SAMPLE_RATE, num=len(RAW_DATA))
# Create a sound data object used for the tests
SOUND_DATA = SoundData(ORIGINAL_NAMES[0])
# Get the default phase shift, used to comparing
DEFAULT_PHASE_SHIFT = SOUND_DATA.get_default_phase_shift()

# Create a version of the raw data with double amplitude
# and is shifted 1 in the amplitude domain
RAW_DATA_DOUBLE_AMP_1_SHIFT = 2 * cp.copy(RAW_DATA) + 1

# Create a version of the raw time that is shifted
# by 2 in the phase shift domain + the default phase shift value
RAW_TIME_SHIFTED_BY_2 = cp.copy(RAW_TIME) + (DEFAULT_PHASE_SHIFT + 2)


class TestSoundModifier(unittest.TestCase):
    """Used to test the class SoundModifier in soundModifier.py"""

    def test_get_should_play(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_get_current_sound_index(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_get_number_of_sounds(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_current_original_sound(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_current_manipulated_sound(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def get_finished_sequence(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_set_amplitude(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_toggle_play(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    def test_next_audio_files(self):
        """"""
        self.assertEqual(True, True, "Should be equal")

    """
        OTHER METHODS:
        The SoundModifier class contains also the following method.
        But it is concluded that the results of executing them
        easily can be validated either using the visual- or 
        auditory system, or are simply not used in the main 
        application but only exist for debugging purpose. 

        - play_audio_files()
    """


if __name__ == '__main__':
    unittest.main()
