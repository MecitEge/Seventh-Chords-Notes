from tkinter import *
from tkinter import messagebox
from random import choice

total = 0
right = 0
new_chord = None

chords_names = ["Am7", "Bm7", "Cm7", "Dm7", "Em7", "Fm7", "Gm7", "A#m7", "C#m7", "D#m7", "F#m7", "G#m7",
                "Amaj7", "Bmaj7", "Cmaj7", "Dmaj7", "Emaj7", "Fmaj7", "Gmaj7", "A#maj7", "C#maj7", "D#maj7", "F#maj7",
                "G#maj7", "A7", "B7", "C7", "D7", "E7", "F7", "G7", "A7", "C7", "D7", "F#", "G7"
                ]
chords_notes = {
    "Am7": "A C E G",
    "Bm7": "B D F A",
    "Cm7": "C D# G A#",
    "Dm7": "D F A C",
    "Em7": "E G B D",
    "Fm7": "F G# C D#",
    "Gm7": "G A# D F",
    "A#m7": "A# C# F G#",
    "C#m7": "C# E G# B",
    "D#m7": "D# F# A# C#",
    "F#m7": "F# A C# E",
    "G#m7": "G# B D# F#",
    "Amaj7": "A C# E G#",
    "Bmaj7": "B D# F# A#",
    "Cmaj7": "C E G B",
    "Dmaj7": "D F# A C#",
    "Emaj7": "E G# B D#",
    "Fmaj7": "F A C E",
    "Gmaj7": "G B D F#",
    "A#maj7": "A# D F A",
    "C#maj7": "C# F G# C",
    "D#maj7": "D# G A# D",
    "F#maj7": "F# A# C# F",
    "G#maj7": "G# C D# G",
    "A7": "A C# E G",
    "B7": "B D# F# A",
    "C7": "C E G A#",
    "D7": "D F# A C",
    "E7": "E G# B D",
    "F7": "F A C D#",
    "G7": "G B D F",
    "A#7": "A# D F G#",
    "C#7": "C# F G# B",
    "D#7": "D# G A# C#",
    "F#7": "F# A# C# E",
    "G#7": "G# C D# F#",

}


# ----------- FUNCTIONS ----------


def begin_game():
    global total, right, new_chord
    new_chord = choice(chords_names)
    chord.config(text=new_chord)
    start_button.config(text="Next Chord")
    submit.config(state=NORMAL)
    score_label.config(text=f"\n\nScore: {right} / {total}")


def submit_guess():
    global total, right, new_chord
    guess = (answer.get()).upper()
    try:
        if guess == chords_notes[new_chord]:
            total += 1
            right += 1
            score_label.config(text=f"Correct\n\nScore: {right} / {total}")
        else:
            total += 1
            score_label.config(text=f"Wrong\n{chords_notes[new_chord]}\nScore: {right} / {total}")
        answer.delete(0, "end")
        submit.config(state=DISABLED)
    except KeyError:
        pass


def how_to():
    messagebox.showinfo("Instructions", "Insert one space between every note.\nAll accidentals are sharps.\n"
                                        "You can use both lower and uppercase letters.\nExample:\nQuestion: "
                                        "Cm7\nAnswer: C D# G A#")


# ----------- UI ---------


window = Tk()
window.title("Memorize Notes of Seventh Chords")
window.config(padx=50, pady=50)

chord = Label(text="Click Start!", font=("", 40, "bold"))
chord.grid(row=0, column=0, columnspan=2, pady=20)

score_label = Label(text=f"\n\nScore: {right} / {total}", font=("Calibri", 20, "normal"), fg="brown")
score_label.grid(row=3, column=0, sticky="w")

answer = Entry(font=("Calibri", 20, "normal"))
answer.grid(row=1, column=0)

submit = Button(text="Submit", width=15, height=2, command=submit_guess, state=DISABLED)
submit.grid(row=1, column=1, padx=3)

start_button = Button(text="Start", width=15, height=2, command=begin_game)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

howtouse = Button(text="How to Use", width=15, height=2, command=how_to)
howtouse.grid(row=3, column=1, sticky="se")

window.mainloop()
