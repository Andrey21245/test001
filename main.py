#print("START")
# i = 15
# n = 15
# while(i != 0):
# 	while(n != 8):
# 		print("_")
# 		n = n-1
# 	print("@")
# 	while(n != 0):
# 		print("_")
# 		n = n-1

from slider  import Slider

slider = Slider()
slider.show()

slider = Slider(80, '$$$')
slider.show(3, 0.03)

