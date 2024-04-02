# subfps.py

A simple python script to change framerate of subtitle files

## Usage
```bash
python3 subfps.py file_location [subtitle_file_fps] [target_video_fps]
```
### Examples
```bash
python3 subfps.py "~/documents/subtitles/My Subtitle.srt" 23.976 30
```
```bash
python3 subfps.py "C:\Users\Username\Documents\Subtitles\My Subtitle.srt" 30 25
```
If only one argument is given, program will arbitrarily default to converting from 25 fps to 23.976 fps
```bash
python3 subfps.py "D:\Documents\Subtitles\My Subtitle.srt"
```
Tip: You can drag and drop the file to get its location in most terminals.

## Version History
* v1.0
    * Initial Release

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE.md file for details
