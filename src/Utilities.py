def deslocar():
	for i in range(0): #-y
	
		move(South) 
		
	for i in range(0): #-x
	  
		move(West)
		 
	for i in range(0): #y
	
		move(North) 
		
	for i in range(3): #x
	 
		move(East) 
	
def xy0():
	change_hat(Hats.Wizard_Hat)
	
	
	for i in range(get_pos_y()):
		move(South)
	for i in range(get_pos_x()):
		move(West)
zz()	
def pait():
	a=[0, 0, 0, 0, 0, 0, 
	   0, 0, 0, 0, 0, 0,
	   0, 0, 0, 0, 0, 0,
	   0, 0, 0, 0, 0, 0,
	   0, 0, 0, 0, 0, 0,
	   0, 0, 0, 0, 0, 0]
	T=1
	campo=[T, 0, T, T, 0, T, 
		   0, T, 0, 0, T, 0,
		   0, 0, T, T, 0, 0,
		   0, 0, T, T, 0, 0,
		   0, T, 0, 0, T, 0,
		   0, 0, 0, 0, 0, 0]
		   
	yposition= 5 - get_pos_y()
	for i in range(yposition):
			move(North)
	for i in range(get_pos_x()):
			move(West)
	a=0
	for j in campo:
		
		if j == 1:
			till()
		
		move(East)
		a+=1
		if a == 6:
			move(South)
			a=0
