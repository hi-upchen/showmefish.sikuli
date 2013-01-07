showmefish.sikuli
=================

WOW (World of Warcarft) fish bot.
It should works on both Windows and Mac. But I only test it on the Mac.

### System requirements

1. Install a WOW instance.
2. Install the [Sikuli](http://www.sikuli.org/)

### How to start fish

1. Open your WOW application. And the go to your fish spot.
2. Pick a good place. Find a good place is very important for the fish bot. A good fishing spot should
    * The size of the buoies should be the same.
    * The color of the buoies should be as ligh as possible.
3. Capture the buoy screen shot. Put it into this folder with name "buoy.png". This bot will use this image to find the buoy.
4. Put your fish skill to button "1".
5. Execute the sikuli script. Either directly use Sikuli-IDE or use [command line](http://doc.sikuli.org/faq/010-command-line.html).

        Mac: /Applications/Sikuli-IDE.app/sikuli-ide.sh -r showmefish.sikuli

### Custom setups

There are some args you can configure in the script **showmefish.py**

* **APP_NAME** = 'World of Warcraft-64' # The application name
* **bouyImg** = "buoy.png" # Use this image to find the bouy
* **findBouySimilarity** = 0.5 # threshold to find the bouy
* **findSplashSimilarity** = 0.7 # threshold to find the splash

