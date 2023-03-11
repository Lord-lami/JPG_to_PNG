from sys import argv
from pathlib import Path
from PIL import Image


def getPaths(jpg_path='.', png_path=''):
	"""Checks if jpg_path is given and exists
	Raises and returns a FileNotFoundError if it doesn't exist
	References the current folder if it isn't given
	Checks if png_path is given and exists
	Creates a new_png_folder if it isn't given
	Creates the passed in direcotry if it doesn't exist
	Returns a Path object with both paths
	"""
	if jpg_path == '.':
		jpg_folder = Path(jpg_path)
	else:
		jpg_folder = Path(jpg_path).with_suffix('')
		if not jpg_folder.exists():
			raise FileNotFoundError
			return FileNotFoundError()

	
	if png_path:
		png_folder = Path(png_path).with_suffix('')
		if not png_folder.exists():
			png_folder.mkdir()
	else:
		png_folder = Path('./new_png_folder')
		tries = 1
		while  png_folder.exists():
			png_folder = Path(f'./new_png_folder{tries}')
			tries += 1
		png_folder.mkdir()

	return jpg_folder, png_folder


if __name__ == '__main__':
	# Grab the two directory arguments
	try:
		jpg_folder, png_folder = getPaths(argv[1], argv[2])
	except IndexError:
		if len(argv) == 1:
			jpg_folder, png_folder = getPaths()
		elif len(argv) == 2:
			jpg_folder, png_folder = getPaths(argv[1])

	# Loop through jpg_folder directory and convert images to PNG
	# Extract only .jpg images from jpg folder
	jpg_image_path_list = [jpg_image_path for jpg_image_path in jpg_folder.iterdir() if jpg_image_path.suffix == '.jpg']

	# png_folder_path = png_folder.as_posix()

	for jpg_image_path in jpg_image_path_list:
		jpg_image_path_str = jpg_image_path.as_posix()
		img = Image.open(jpg_image_path_str)
		# Save them to png_folder directory
		file_name = jpg_image_path.stem
		img.save(png_folder.joinpath(file_name + '.png').as_posix(), 'png')

	print('JPG to PNG Conversion Complete')


