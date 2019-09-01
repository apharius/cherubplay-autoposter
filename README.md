# Apharius' Cherp Auto-poster

A basic script for automatically posting all your Cherp prompts.

## What is it?
It's a simple Python script that creates a web browser and automates the keypresses needed to post all your saved 
Cherp prompts to the front page. Keep in mind that I mainly wrote this script for myself.

## Installation
### Prerequisites;
* Python (I use Python 3.7.1, but other versions might work too. Haven't tried)
* pip 
* [Chromedriver](http://chromedriver.chromium.org/) (You can use similar tools for other browsers if you're willing to do some
manual reconfiguring)

### Installation procedure:
(This guide is written for Linux, since that's what I use. For other operating systems, translate commands and such into your OS' equivalent)
1. Make sure all prerequisites are installed.
2. Clone or download this repository.
3. Open a terminal, step to the location you saved this repository to, and issue the command `pip install -r requirements.txt`
This will install the necessary packages for the script to run.
4. Open the script in your preferred texteditor and make sure that the path to Chromedriver matches the location of your Chromedriver 
installation, changing it if necessary.

## Running the script
In a terminal, step into this repository's location and issue the command `python cherp-autoposter.py` to run the script. Enter your Cherp username
and password when prompted. A Chrome window will open and the script will post all your saved prompts to the front page.

## Q & A
**Q: Does the script share my username and password with anyone?**

**A:** No. All it does is put the username and password into the proper fields when signing you in.

**Q: Will you extend functionality to include directory requests?**

**A:** I already have. However, I am not releasing it to the public. The chaos that would cause is not something I want to be responsible for.

**Q: Do you accept suggestions from others?**

**A:** Yes! This is a quick solution that's most likely far from optimal, so please contribute with improvements.
