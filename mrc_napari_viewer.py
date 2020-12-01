import argparse

import easygui
import mrcfile
import napari

'''
MRC file viewer purely based on napari (https://napari.org/) and mrcfile.

Allows viewing/slicing/surface rendering of large MRCS stacks as well as volume files and single MRC images. 

Script written by Dawid Zyla, LJI.
'''


parser = argparse.ArgumentParser(
    description='Preview MRC data in a friendly way')
parser.add_argument('--i', type=str, help='MRC/MRCS/MAP path')
args = parser.parse_args()

extensionsToCheck = ('.mrc', '.mrcs', '.map', '.MRC', '.MRCS', '.MAP')

if args.i != None:
    if str(args.i).endswith(extensionsToCheck):
        file = args.i
    else:
        print('Only MRC/MRCS/MAP files supported!')
        print(args.i)
        quit()
else:
    file = ''

while not file.endswith(extensionsToCheck):

    print('Select MRC, MRCS or MAP file')
    file = easygui.fileopenbox(filetypes=['\*.mrc', '\*.mrcs', '\*.map'])

    if file == None:
        file = str('')

# Map data rather than open everything at once.
file = mrcfile.mmap(file, permissive=True).data


with napari.gui_qt():
    viewer = napari.view_image(file)
