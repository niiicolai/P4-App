# P4-App

# gui.py
The 4 steps below provide the general usage of this class

1. import class
```python
from gui import Application
```

2. Create some test data
```python
ORIGINAL_NAMES = ["test.wav"]
MANIPULATED_NAMES = ["reverb_test.wav"]
```

3. Create an Application object a list of file paths to original and manipulated names
```python
app = Application(ORIGINAL_NAMES, MANIPULATED_NAMES, None)
```

4. Run the main loop to show the GUI
```python
app.mainloop()
```

# csvWriter.py
The 4 steps below provide the general usage of this class

1. import class
```python
from csvWriter import CSVWriter
```

2. Create some test data
```python
data = [{
  {"original":{"amplitude":1, "phase_shift":0}},
  {"manipulated":{"amplitude":1, "phase_shift":0}}
}]
```

3. Create a CSVWriter object using the data
```python
writer = CSVWriter(data)
```

4. Write the data to a CSV file specified at the path above
```python
writer.save()
```

# soundData.py
The 7 steps below provide the general usage of this class

1. import class
```python
from soundData import SoundData
```

2. Create a sound data object using the original data
```python
original_sound = SoundData('original_sound.wav')
```

3. Load a manipulated version of the original data
```python
manipulated_sound = SoundData('manipulated_sound.wav')
```

4. Manipulate the sound
```python
manipulated_sound.set_phase_shift(1)  # +1
manipulated_sound.set_amplitude_shift(.1) # +.1
manipulated_sound.set_amplitude(5) # +5
```

5. Plot the sounds against each other
```python
original_sound.plot_against(manipulated_sound)
```

6. Play the original sound
```python
original_sound.play()
```

7. Play the manipulated sound
```python
manipulated_sound.play()
```

# soundModifier.py
The 10 steps below provide the general usage of this class

1. import class
```python
from soundModifier import SoundModifier
```

2. Create some test data
```python
ORIGINAL_NAMES = ["test.wav"]
MANIPULATED_NAMES = ["reverb_test.wav"]
```

3. Create a SoundModifier object a list of file paths to original and manipulated names
```python
sound_modifier = SoundModifier(ORIGINAL_NAMES, MANIPULATED_NAMES)
```

4. Graph current state of original sound file
```python
x = self.sound_modifier.current_original_sound().get_time()
y = self.sound_modifier.current_original_sound().get_data()
plt.figure(1)
plt.plot(x, y)
plt.show()
```

5. Graph current state of manipulated sound file
```python
x = self.sound_modifier.current_manipulated_sound().get_time()
y = self.sound_modifier.current_manipulated_sound().get_data()
plt.figure(1)
plt.plot(x, y)
plt.show()
```

6. Change amplitude of manipulated sound
```python
sound_modifier.set_amplitude(amplitude=2)
```

7. Phase shift manipulated sound
```python
sound_modifier.set_phase_shift(phase_shift=.5)
```

8. Toggle play
```python
sound_modifier.toggle_play()
```

9. Move to next audio files
```python
sound_modifier.next_audio_files()
```

10. Check if all audio files has been played
```python
if sound_modifier.get_finished_sequence() > 0:
  print("ALL SOUND FILES HAS BEEN HEARD")
```
