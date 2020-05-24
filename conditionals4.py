
direction = input("Do you want to go (N)orth, (S)ourth, (E)ast, or (W)est?")

if direction == "n":
	  print("You head north, into the forest.")
elif direction == "s":
	  print("The coast blocks your path south.")
elif direction == "w":
	  print("The western fields are comforting to walk through.")
elif direction == "e":
	  print("You were eaten by a grue.")
else:
	  print("I don't recognize your choice.")

