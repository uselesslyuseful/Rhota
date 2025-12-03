# Uploading Rhota to itch.io

Your game has been successfully compiled for web using pygbag! Follow these steps to upload it to itch.io:

## Build Location
The compiled web files are located in: `build/web/`

## Upload Steps

1. **Log in to itch.io**
   - Go to https://itch.io and log in to your account

2. **Create a New Project**
   - Click on your profile → "Create new project"
   - Or go directly to: https://itch.io/game/new

3. **Project Settings**
   - **Project title**: Rhota 
   - **Project URL**: Choose a unique URL for your game
   - **Kind of project**: Select **"HTML"**

4. **Upload Files**
   - In the "Uploads" section, click "Add files" or drag and drop
   - Upload **ALL files** from the `build/web/` directory:
     - `index.html` (the main HTML file)
     - `rhota.apk` (contains all game assets - images, audio, fonts, Python files)
     - `favicon.png` (the game icon)
   - **Important**: The `rhota.apk` file contains all your game assets packaged together, so you only need these 3 files!

5. **Configure Embed Options**
   - Under "Embed options" or "Viewing options":
     - **Width**: `480` (your game's screen width)
     - **Height**: `800` (your game's screen height)
   - This ensures the game displays at the correct size

6. **Additional Settings**
   - **Visibility**: Choose "Public" or "Draft" as needed
   - Add a description, tags, and screenshots if desired
   - Set pricing (Free or Paid)

7. **Save and Publish**
   - Click "Save" to save your project
   - Click "View page" to see your game live
   - The game will be playable directly in the browser!

## Testing Locally (Optional)

Before uploading, you can test the build locally:

```bash
cd build/web
python3 -m http.server 8000
```

Then open your browser to: `http://localhost:8000`

## Notes

- The game uses WebAssembly and may take a moment to load
- Audio files are included and should work in the browser
- Keyboard controls (S, D, J, K, Arrow keys, Enter, Escape) work in the browser
- Make sure all assets are uploaded for the game to work properly

## Troubleshooting

If the game doesn't load:
- Check that all files from `build/web/` were uploaded
- Verify the embed dimensions match your game size (480x800)
- Check the browser console for any error messages
- Ensure you selected "HTML" as the project type

Good luck with your release! 🎮

