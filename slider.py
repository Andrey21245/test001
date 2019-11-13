
# Класс Слайдер, рисующий значок, который бежит по строке. 

# Использование:
#
# from slider  import Slider
#
# slider = Slider() # without parameters with values by default
# slider.show()
#
# slider = Slider(80, '$$$') 		# with custom parameters
# slider.show(3, 0.03)


from sys  import stdout
from time import sleep

class Slider:
	def __init__ (self, row_lenght= 50, symbol='X'):
		self.row_lenght = row_lenght
		self.symbol= symbol

	def show(self, show_tymes = 5, delay_in_sec = 0.01):
		for show_count in range (1, show_tymes): # repeat row showing N tymes

			#show steps
			for position in range(1,self.row_lenght+1):
				# define prefix and suffix lenghts
				prefix_lenght = position
				suffix_lenght = self.row_lenght-position

				# create prefix and suffix 
				prefix=''
				suffix=''					
				prefix_position = 0
				suffix_position = 0
				while prefix_position < prefix_lenght: # build prefix
					prefix += '-'
					prefix_position += 1
					#while-end
				while suffix_position < suffix_lenght: # build suffix
					suffix += '-'
					suffix_position += 1
					#while-end

				# combine output row for the current position
				output="\r" + prefix + self.symbol + suffix	

				# show output
				stdout.write(output)  #show output
				stdout.flush()			  #clean screen
				# alternatively 
				# print(output)

				sleep(delay_in_sec)
				#for-step-end

		print('') # move the cursor to the next line