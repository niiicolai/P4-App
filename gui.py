# Dependencies
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from soundModifier import SoundModifier

"""
    The 4 steps below provide the general usage of this class

    1. import class
    from gui import Application

    2. Create some test data
    ORIGINAL_NAMES = ["test.wav"]
    MANIPULATED_NAMES = ["reverb_test.wav"]

    3. Create an Application object a list of file paths to 
       original and manipulated names
    app = Application(ORIGINAL_NAMES, MANIPULATED_NAMES, None)

    4. Run the main loop to show the GUI
    app.mainloop()
"""


# BUTTON COLORS
DEFAULT_BTN_BGG = "white"
ACTIVE_BTN_BGG = "red"

# TEXT COLORS
DEFAULT_TXT_COLOR = "black"
DEFAULT_BGG_COLOR = "white"

# FONTS
HEADER_FONT = ("Arial", 15, 'bold')
TITLE_FONT = ("Arial", 9, 'bold')

# FRAME PROPERTIES
SIZE = "540x520"
TITLE = "P4 Project"


class Application(tk.Frame):
    """A class used to represent the main GUI features"""

    def __init__(self, original_names, manipulated_names, master):
        """The class constructor. Creates a
           sound modifier using the name paths"""
        if master is None: master = tk.Tk()
        super().__init__(master)

        self.sound_modifier = SoundModifier(original_names, manipulated_names)
        self.master = master
        self.master.geometry(SIZE)
        self.master.resizable(False, False)
        self.master.title(TITLE)
        self.create_welcome_widgets()
        self.grid(row=0, column=0)

    # TKINTER METHODS

    def clear_page(self):
        """Loop through the frame's widgets
           and destroy them"""
        for w in self.master.winfo_children():
            w.destroy()

    # WIDGETS METHODS

    def create_welcome_widgets(self):
        """Adds the necessary widgets
           to build the welcome page"""
        # create the label
        top_label = tk.Label(self.master, text="Welcome!", fg=DEFAULT_TXT_COLOR,
                             bg=DEFAULT_BGG_COLOR, width="45", height="3",
                             font=HEADER_FONT)
        # position the label
        top_label.place(x=0, y=0)

        # create the label
        guidelines_label = tk.Label(self.master,
                                    text="Please read the guidelines below",
                                    fg=DEFAULT_TXT_COLOR, bg=DEFAULT_BGG_COLOR,
                                    width="78", height="3", font=TITLE_FONT)
        # position the label
        guidelines_label.place(x=0, y=50)

        # create the label
        guidelines = "Your task is to synchronize two sound using phase shifting.\n\n" \
                     "The sound control page has two sliders:\n" \
                     "1. Changes amplitude\n 2. Shift the phase\n\n" \
                     "The sound control page also have two buttons:\n" \
                     "1. The 'play' button can be used to listen to the sounds\n" \
                     "2. The 'next' button is used to confirm " \
                     "that you perceive the \ntwo sounds to have equal phase " \
                     "and you are ready to be\n presented to two new sounds.\n\n" \
                     "This process will continue until all sounds are evaluated.\n\n" \
                     "Be careful when you press play the first time, it is recommended\n" \
                     "to set the local volume of your computer to a low value, and slowly\n" \
                     "increase it to a suitable volume level.\n\n" \
                     "Thank you for your interest!"
        guidelines_label2 = tk.Label(self.master,
                                     text=guidelines,
                                     fg=DEFAULT_TXT_COLOR,
                                     width="78", height="20", font=TITLE_FONT)
        # position the label
        guidelines_label2.place(x=0, y=120)

        # Create button
        start_button = tk.Button(self.master, text="OK, I understand!", fg=DEFAULT_TXT_COLOR,
                                 bg=DEFAULT_BGG_COLOR, width=37, height=2, command=self.show_sound_control)
        # Place button
        start_button.place(x=135, y=439)

    def create_goodbye_widgets(self):
        """Adds the necessary widgets
           to build the goodbye page"""
        # create the label
        top_label = tk.Label(self.master, text="Thanks for participating!", fg=DEFAULT_TXT_COLOR,
                             bg=DEFAULT_BGG_COLOR, width="45", height="3",
                             font=HEADER_FONT)
        # position the label
        top_label.place(x=0, y=0)

        # create the label
        guidelines = "You can safely close the page now\n" \
                     "by pressing the 'x' up in the right corner."
        guidelines_label2 = tk.Label(self.master,
                                     text=guidelines,
                                     fg=DEFAULT_TXT_COLOR,
                                     width="78", height="20", font=TITLE_FONT)
        # position the label
        guidelines_label2.place(x=0, y=120)

    def create_sound_control_widgets(self):
        """Adds the necessary widgets
           to build the sound control page"""
        # create the top label
        top_label = tk.Label(self.master, text="Synchronize the sounds", fg=DEFAULT_TXT_COLOR,
                             bg=DEFAULT_BGG_COLOR, width="45", height="3",
                             font=HEADER_FONT)
        # position the top label
        top_label.place(x=0, y=0)

        # create the top label
        self.counter_label = tk.Label(self.master,
                                      text=f"Sound {self.sound_modifier.get_current_sound_index() + 1} out " +
                                           f"of {self.sound_modifier.get_number_of_sounds()}",
                                      fg=DEFAULT_TXT_COLOR, bg=DEFAULT_BGG_COLOR,
                                      width="78", height="3", font=TITLE_FONT)
        # position the top label
        self.counter_label.place(x=0, y=50)

        # Create controls
        self.create_amplitude_control()
        self.create_phase_shift_control()

        # Create play button
        self.play_button = tk.Button(self.master, text="Play", fg=DEFAULT_TXT_COLOR,
                                     bg=DEFAULT_BGG_COLOR, width=37, height=2, command=self.toggle_play)
        # Place button
        self.play_button.place(x=240, y=399)

        # Create confirm button
        button = tk.Button(self.master, text="Next Audio Files", fg=DEFAULT_TXT_COLOR,
                           bg=DEFAULT_BGG_COLOR, width=37, height=2, command=self.next_audio_files)
        # Place button
        button.place(x=240, y=445)

        # Plot graph
        self.create_graph()

    # SOUND CONTROL SLIDERS

    def create_amplitude_control(self):
        """Adds the necessary widgets to
           build a slider to control amplitude"""
        title_position = (20, 110)
        title_size = (15, 3)

        # create the top label
        top_label = tk.Label(self.master, text="Amplitude Level\n(db)", fg=DEFAULT_TXT_COLOR,
                             width=title_size[0], height=title_size[1],
                             font=TITLE_FONT)

        # position the top label
        top_label.place(x=title_position[0], y=title_position[1])

        # slider offsets
        slider_top_offset = 50
        slider_left_offset = 16

        # calculate slider start position and size
        slider_length = 330
        slider_position = (title_position[0] + slider_left_offset,
                           title_position[1] + slider_top_offset)

        # Label values
        self.amplitude_labels = [1.6, 1.3, .9, .6, .3, 0, -.3, -.6, -.9, -1.3, -1.6]

        # Build slider
        self.amplitude_slider = tk.Scale(self.master, from_=self.amplitude_labels[0],
                                         to=self.amplitude_labels[len(self.amplitude_labels) - 1],
                                         tickinterval=self.amplitude_labels[len(self.amplitude_labels) - 1],
                                         resolution=.01, length=slider_length)
        self.amplitude_slider["command"] = (lambda amplitude=self.amplitude_slider.get():
                                            self.set_amplitude(amplitude))
        self.amplitude_slider.set(1)
        self.amplitude_slider.place(x=slider_position[0], y=slider_position[1])

    def create_phase_shift_control(self):
        """Adds the necessary widgets to
           build a slider to control phase shift"""
        title_position = (120, 110)
        title_size = (15, 3)

        # create the top label
        top_label = tk.Label(self.master, text="Phase Shift\n(s)", fg=DEFAULT_TXT_COLOR,
                             width=title_size[0], height=title_size[1],
                             font=TITLE_FONT)
        # position the top label
        top_label.place(x=title_position[0], y=title_position[1])

        # slider offsets
        slider_top_offset = 50
        slider_left_offset = 16

        # calculate slider start position and size
        slider_length = 330
        slider_position = (title_position[0] + slider_left_offset,
                           title_position[1] + slider_top_offset)

        # Label values
        self.phase_shift_labels = [1.6, 1.3, .9, .6, .3, 0, -.3, -.6, -.9, -1.3, -1.6]

        # Build slider
        self.phase_shift_slider = tk.Scale(self.master, from_=self.phase_shift_labels[0],
                                           to=self.phase_shift_labels[len(self.phase_shift_labels) - 1],
                                           tickinterval=self.phase_shift_labels[len(self.phase_shift_labels) - 1],
                                           resolution=.01, length=slider_length)
        self.phase_shift_slider["command"] = (lambda phase_shift=self.phase_shift_slider.get():
                                              self.set_phase_shift(phase_shift))
        self.phase_shift_slider.set(0)
        self.phase_shift_slider.place(x=slider_position[0], y=slider_position[1])

    # GRAPHING

    def create_graph(self):
        """Adds the necessary widgets to show a graph
           of the current original and manipulated sounds"""
        f = Figure(figsize=(5, 5), dpi=40)
        self.ax = f.add_subplot(111)
        self.ax.set_ylabel('Amplitude [db]')
        self.ax.set_xlabel('Time [seconds]')
        self.ax.set_title('ADSR')

        x1 = self.sound_modifier.current_original_sound().get_time()
        y1 = self.sound_modifier.current_original_sound().get_data()
        self.ax.plot(x1, y1)

        x2 = self.sound_modifier.current_manipulated_sound().get_time()
        y2 = self.sound_modifier.current_manipulated_sound().get_data()
        self.ax.plot(x2, y2)

        self.canvas = FigureCanvasTkAgg(f, self.master)
        self.canvas.get_tk_widget().place(x=240, y=130, width=270, height=250)

    def plot_current_files(self):
        """Updates the current state of the graph to match
           the current original and manipulated sounds"""
        # call the clear method on your axes
        self.ax.clear()

        # plot the new data
        self.ax.set_ylabel('Amplitude [db]')
        self.ax.set_xlabel('Time [seconds]')
        self.ax.set_title('ADSR')
        x1 = self.sound_modifier.current_original_sound().get_time()
        y1 = self.sound_modifier.current_original_sound().get_data()
        self.ax.plot(x1, y1)

        x2 = self.sound_modifier.current_manipulated_sound().get_time()
        y2 = self.sound_modifier.current_manipulated_sound().get_data()
        self.ax.plot(x2, y2)

        # call the draw method on your canvas
        self.canvas.draw()

    # SHOW SUB PAGE METHODS

    def show_sound_control(self):
        """Remove all widgets and build the
           sound control page"""
        self.clear_page()
        self.create_sound_control_widgets()

    def show_goodbye_widgets(self):
        """Remove all widgets and build the
           goodbye page"""
        self.clear_page()
        self.create_goodbye_widgets()

    # SOUND MODIFIER METHODS

    def set_amplitude(self, amplitude):
        """Change the amplitude of the manipulated
           sound file and updates the current
           state of the graph"""
        self.sound_modifier.set_amplitude(amplitude)
        self.plot_current_files()

    def set_phase_shift(self, phase_shift):
        """Change the phase shift of the manipulated
           sound file and updates the current
           state of the graph"""
        self.sound_modifier.set_phase_shift(phase_shift)
        self.plot_current_files()

    def toggle_play(self):
        """Plays the current original
           and manipulated sound"""
        self.sound_modifier.toggle_play()
        if self.sound_modifier.get_should_play():
            self.play_button.config(text="Play", bg=DEFAULT_BTN_BGG, fg=DEFAULT_TXT_COLOR)
        else:
            self.play_button.config(text="Stop", bg=ACTIVE_BTN_BGG, fg=DEFAULT_BGG_COLOR)

    def next_audio_files(self):
        """Setup the next sound files until it
           has reached one cycle, where it will
           save the results and display the
           goodbye page"""
        self.sound_modifier.next_audio_files()
        if self.sound_modifier.get_finished_sequence() > 0:
            self.show_goodbye_widgets()
        else:
            self.plot_current_files()
            self.counter_label.config(text=f"Sound {self.sound_modifier.get_current_sound_index() + 1} out "
                                           f"of {self.sound_modifier.get_number_of_sounds()}")
