# To pause a pygameZero script follow these steps

# step 1:
  # Define new var at top of program
  PAUSED = Flase
  #
# step 2:
  # inside the update function the whole running routine goes under:
  if not PAUSED: # so the running routine is paused if PAUSED is True
  #
# step 3:
  # whe need a Pause hotkey so here's a function
  def on_key_down(key):
	  global PAUSED
	  if key == keys.P:
		  if PAUSED:
			  PAUSED = False
		  else:
			  PAUSED = True
        
