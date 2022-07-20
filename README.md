# pls-steal-price-is-right
A script to cheat in the pls steal minigame, price is right 

Uses spellchecking to guess the closet limited name to the one you inputted: (ex: dom prae -> Dominus Praefectus). The script works about 70% of the time but since pls steal's item updater only updates every couple of days, the prices could be way off in terms of a projected. The script will return to you, the rap, the selling price, and the average of the rap and selling price. I recommend that you use the average to determine your pick. 

This script will only work while you're playing if you're a fast typer (100 wpm+) so that you have enough time to type in half the item's name. Also as rounds progress, the script will become obsolete since the rounds are going by way too fast.

**How it works**

Uses my own point-based spellchecking algorithm that I wrote a few months ago to guess the closest match to a word in a specified dictionary (`items.txt`)
It will then match that to rolimons RAP data as well as sale data from Roblox's API and return them to you in nicely formatted text.

**Usage**

The files required are:
- `main.py`
- `spellcheck.py`
- `colors.py` (Only if you want colors, if not remove ln 2 from `main.py`)\

`items.txt` is generated everytime you run the program so that new limteds are added in.
You will need to put your Roblox cookie into an environmental variables called TOKEN (It is needed to make requests to Roblox's itemdata endpoint).

**Examples**

![image](https://user-images.githubusercontent.com/100868154/180101143-ad51d6e3-6ab4-4b1a-8122-c65e095d690e.png)
