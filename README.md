# Rhota

Rhota is a rhythm game made with python featuring three songs and a note editor. Currently still in development, with working demo.

## Usage

- **Itch**

    This project can be accessed on [itch.io](https://uselesslyuseful.itch.io/rhota). There is currently no mobile support. 

- **Cloning**

   This game uses the pygame module. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

   ```bash
   pip install pygame
   ```

## Features

- **Home Screen**
   
   Allows for song selection, using up and down arrows. The enter key is used to select a song for play. Displays song names.

- **Songs**
  
  Each song has their own chart, which can be played by selecting from the home screen. These charts use the keys "s", "d", "j", and "k" to hit notes coming from four separate lanes. 
  
  **List of Songs**

  **NONE OF THESE SONGS ARE COMPLETE. Only Bad Apple!! is currently completely synced with music.**

  - *Never Meet Again - Hua Chenyu*
  - *Self-Inflicted Achromatic - JubyPhonic*
  - *Bad Apple!! - Masayoshi Minoshima*

- **Score Page**
  
  Calculates score earned during each game, and the percentage of the total available score achieved. Automatically shows up after each song, and returns to the home page through the enter key.

  Note: There will be a message showing "Cadences earned." Cadences are currently not used for anything.

- **Note Editor**

    A functioning note editor can be accessed via pressing the left key on the Home Screen. The usage of this editor is as below:

    **Usage**

    - Keys
        - P: Places a tap note on the judgement line.
        - H: Places a hold note on the judgement line. Default time is one quarter note (calculated using current BPM).
    - Mouse
        - Hold left click + Drag mouse: Moves notes. No snapping has been incorporated.
        - Right click on note: Shows exact details of note which can be edited. (format: first character is one of sdjk (indicating lane), next character(s) is integer indicating frame, and last character is n or s, indicating normal or double value. For hold notes, there will be a hyphen in the middle, separating two integers. The first is the start time and the second is the end time.) Left click anywhere to escape detailed editing, or press enter key.
    - On-screen
        - BPM Marker (Bottom Right): Left click to edit, enter to escape. Change this to whatever the BPM of your song is.
        - Frames per note (Bottom Left): Automatically calculated using BPM value. Left click to swap between displaying frames per eight, quarter, or sixteenth.
        - Export Button (Top Right): Currently only for use in development. In an IDE, it prints a list of your notes in the format accepted by the program. 
        - Play Button (Top Right): Allows you to play your current chart. Chart will save after playthrough.

## Known Bugs

- **Note Hitting**
  
  Sometimes key presses will not register, for unclear reasons. This does not occur often, but tends to be on a tap note after a hold note in the same lane. 

- **Out of Sync Caused by Lag**

  While code has been implemented to attempt to prevent this. pygame mixer is unreliable and the addition of the web browser means it may often be a second out of sync. Restarting the game tends to fix this. 

## Support

Gmail: sleep.cats.books@gmail.com
