## Stage of the game:
🐣

## About arcade:

A good place to start is: http://arcade.academy/suggested_curriculum.html

## How to install the required dependencies:


1. Make sure you have Python 3 installed
2. Make sure you have pip3 installed. If on Windows, google how to do that for your version.
If on Linux , or Linux installed in VMware or similar do:

* `sudo apt update`
* `sudo apt install python3-pip`. Verify with: `pip3 --version`

3. We need to install requirements. 
Do: 
`pip3 install -r requirements.txt`
4. Verify if it works with: `python3 jewels.py` 

## What it can do now:

The game should behave, but it doesn't yet :-)
It will someday, lol.
For the moment you can just close the window and rerun it to match some gems. 
Then you'll see your score increase. 
You can also click the gems and you'll have the column and row printed, and the gem's colour changed.

## What it should do:

What I'd be happy with is when you match 3 or more gems, they explode, get replaced by new random ones and the score increases. I also need to find a way to restart it without closing the window.
In an ideal scenario, the final version would behave like this, without that annoying key:
https://www.youtube.com/watch?v=qn5DJilxm2U
