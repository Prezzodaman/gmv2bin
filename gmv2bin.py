import sys
import os

print("gmv2bin - Python version")
print("Original by Mercury, 2010; Python version by Prezzo, 2024")
print()
if len(sys.argv) >= 3:
	input_filename = sys.argv[1]
	output_filename = sys.argv[2]
	if os.path.exists(input_filename):
		valid_file = True
		with open(input_filename, "rb") as file:
			try:
				if file.read(10).decode("ascii") != "Gens Movie":
					valid_file = False
			except:
				valid_file = False
			if valid_file:
				file.seek(0x40)
				input_file = file.read()
		if valid_file:
			button_now = 0  # current button state
			button_last = 0  # previous button state
			button_time = 0  # frames that the current button's been held
			demo_length = 0  # demo length in frames

			button_a = 0b01000000
			button_b = 0b00010000
			button_c = 0b00100000
			button_a_gmv = 0b00010000
			button_b_gmv = 0b00100000
			button_c_gmv = 0b01000000

			output_file = bytearray()
			output_file.append(0)  # start with 0 (no button state)
			step = 3
			for pos in range(0, len(input_file) - step, step):
				button_last = button_now
				button_now = 0xff - input_file[pos]  # get current button state

				button_abc = 0  # a, b and c are out of order for some reason
				if button_now & button_a_gmv:  # a pressed?
					button_now &= ~button_a_gmv  # remove it from button state
					button_abc |= button_a   # put it where it should be!
				if button_now & button_b_gmv:  # b pressed?
					button_now &= ~button_b_gmv
					button_abc |= button_b
				if button_now & button_c_gmv:  # c pressed?
					button_now &= ~button_c_gmv
					button_abc |= button_c
				button_now |= button_abc

				# the demo code is basically RLE compression - if the current button states are identical to the previous frame, increase the amount of frames, otherwise write them both to the file and reset the counter
				if button_now != button_last:  # different button pressed?
					output_file.append(button_time)
					output_file.append(button_now)
					button_time = 0
				else:  # same button pressed?
					button_time += 1
					if button_time == 0xff:  # highest possible byte, so wrap round
						output_file.append(button_time)
						output_file.append(button_now)
						button_time = 0
				
				demo_length += 1

			while len(output_file) % 16 != 0:  # pad output file
				output_file.append(0)

			with open(output_filename, "wb") as file:
				file.write(output_file)
			print("File converted!")
			print(f"Demo length in bytes: {len(output_file)}")
			print(f"Demo length in frames: {demo_length}")
			print(f"Demo length in seconds: {(demo_length / 60):.2f}")
		else:
			print("Input file isn't a Gens Movie!")
	else:
		print("Input file doesn't exist!")
else:
	print("Output file must be specified!")