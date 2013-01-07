# Copyright 2013, Up Chen
# Released under the MIT License.
#
# Author: Up Chen
# Github: https://github.com/wallat/showmefish.sikuli

import logging

# finding vars
APP_NAME = 'World of Warcraft-64'
bouyImg = "buoy.png" # use this image to find the bouy
findBouySimilarity = 0.5 # threshold to find the bouy
findSplashSimilarity = 0.7 # threshold to find the splash

# setup envs
Settings.MoveMouseDelay = 0

# init logging
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s %(message)s')

def log(msg):
	logging.debug(msg)

# define constants
CAST_BOUY = 'cast_bouy'
FIND_BOUY = 'find_bouy'
WAIT_SPLASH = 'wait_splash'
PICK_FISH = 'pick_fish'

# setup the searching area
App.focus(APP_NAME)
searchingArea = selectRegion('Drag the fishing area')

# select the WOW application
App.focus(APP_NAME)

# init
status = CAST_BOUY
startTime = time.time()
foundBouy = None
bouyImg = Pattern(bouyImg)

while True:
	elapsedTime = time.time() - startTime

	if elapsedTime>20:
		status = CAST_BOUY

	# rethrow if it cannot find the buoy for a long time
	if status==FIND_BOUY and elapsedTime>8:
		status = CAST_BOUY

	if status==CAST_BOUY:
		type('1')
		mouseMove(searchingArea.getTopLeft())
		startTime = time.time()
		status = FIND_BOUY
		sleep(1)

	if status==FIND_BOUY:
		foundBouy = searchingArea.exists(bouyImg.similar(findBouySimilarity))

		if foundBouy:
			status = WAIT_SPLASH
			mouseMove(foundBouy)

	if status==WAIT_SPLASH:
		expand = foundBouy.nearby(10)

		if not expand.exists(bouyImg.similar(findSplashSimilarity), 1):
			log('SPLASH!!')
			status = PICK_FISH

	if status==PICK_FISH:
		rightClick(foundBouy, KeyModifier.SHIFT)
		status = CAST_BOUY
		sleep(3)
