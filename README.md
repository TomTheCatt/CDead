# CDead
CDead can check dead words, and the amount of said dead words, within an essay or paragraph(s) inputted within a text file. CDead automatically highlights the places where dead words are found and displays a counter of all found dead words.

## Instructions
A) Install Python 3 via their [Download site.](https://www.python.org/downloads/)

B) Download the code

C) Unzip or paste the CDead file outside of the `.zip` file.

E) Run `main.py`. Modules should be automatically installed by CDead.

## Usage
Type or copy-and-paste in text into `type_in_here.txt`. Save the file and run `main.py` in the *terminal*, NOT IDLE shell. CDead will attempt to install modules necessary to its functions. Once this is done, it will display the text in `type_in_here.txt` in the terminal. Highlighted red are dead words that CDead has found.

You may change the text in `type_in_here.txt` and re-process the file by entering in "y". Entering in anything else will close CDead.

To add on more dead words, or change the dead words list, go to `dead_words.txt`, and type in your dead word with "-" seperating each word/phrase. Words/phrases cannot exceed over 3 words.

## Documentation
12/22/2021 - Added detection for dead words. Displays will show if dead words are present or not.
12/21/2020 - Fixed multiple issues involving detection of dead words

## Known Bugs
Copy-and-pasting in words from certain fonts may have special characters not readable by the file, and therefore causes an error. To fix, simply replace the following characters from their modified to current version by doing ctrl+H, copy-and-pasting in the incorrect character, put in the correct character in the "replace" box, and replace all said characters.
### List of Possibly Incorrect Characters
```
"
'
.
,
. . .
```
