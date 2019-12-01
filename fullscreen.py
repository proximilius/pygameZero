import pygame

FULL = True
###########################################
# This module's name is fullscreen but... #
# there's more I also sugest my pause and #
# exit methode in this file the reson for #
# this i meerly advertisment :D		  #
###########################################

###### Sugested use in parental progam
  # step 1:
    # Import this script in parental program
    # eg. import fullscreen.py
    #
  # step 2: #  needed to pause
    # Define new var at top of program
    # eg. ---> PAUSED = Flase
    #
  #step 3: # needed to pause
    # Whole running routine in update goes under:
    # eg.  -- >  if not PAUSED:
    #
  # step 4:
    # new function in parental program
    # def on_key_down(key):
	    # global PAUSED
	    # if key == keys.F:
		    # fullscreen.toggle_fullscreen(WIDTH, HEIGHT)
    	# if key == keys.ESCAPE:
		    # exit()
	    # if key == keys.P:
		    # if PAUSED:
			    # PAUSED = False
		    # else:
			    # PAUSED = True
	
def toggle_fullscreen(w, h):
	global FULL
	if FULL:
		pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		pygame.mouse.set_visible(False)
		FULL = False
	else:
		pygame.display.set_mode((w, h), pygame.NOFRAME)
		pygame.mouse.set_visible(False)
		FULL = True
		
