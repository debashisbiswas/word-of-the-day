# Word of the Day Generator
Generates a 今日の言葉 ("Word of the Day") message for the #japanese channel in the [Knights of Academia: International](https://discord.gg/Fuvabsm) Discord server. Japanese learners in the community are assigned a day of the week to share a "Word of the Day" post, in which they share information about a Japanese word of their choice. The purpose of this program is to automate the process of collecting and formatting information for this weekly post.

## Setup
You must be using a version of Python 3. Install the necessary requirements with

    pip install -r requirements.txt

## Usage
    python main.py
When the program is run, you will be prompted to type in your word. The word must be in kana or kanji. If your word is a verb, it must be in dictionary form.

## Output
When your word is found, the program will contain the following information, using a common post format for the #japanese channel. 
- your word
- reading in kana (in spoiler tag)
- pitch accent (in spoiler tag)
- definitions (in spoiler tag)
- a randomly selected example sentence
- english translation of the example sentence (in spoiler tag)

## Sources
[JMDict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) is used for words and definitions, as well as the example sentences and their translations.

The [ja_pitch_accent](https://github.com/kishimoto-tsuneyo/ja_pitch_accent) repository by [kishimoto-tsuneyo](https://github.com/kishimoto-tsuneyo) on GitHub is used for pitch accent and readings.
