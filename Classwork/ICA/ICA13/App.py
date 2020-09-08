#We will need the os, time, and pygame modules imported here
import pygame 
import os
import time
import tkinter as tk
from shutil import copy


Cat_directory = "Cats"
Dog_directory = "Dogs"

if not os.path.exists(Cat_directory):
    os.mkdir(Cat_directory)
    print("Directory", Cat_directory, "Created")
else:
    print("Directory", Cat_directory, "Already Exists")

if not os.path.exists(Dog_directory):
    os.mkdir(Dog_directory)
    print("Directory", Dog_directory, "Created")
else:
    print("Directory", Dog_directory, "Already Exists")
# If the 'Cats' directory does not exist, make a new 'Cats' directory and print "Cats directory created successfully"
# Otherwise, print a message indicating that directory already exists.
# If the 'Dogs' directory does not exist, make a new 'Dogs' directory and print "Dogs directory created successfully"
# Otherwise, print a message indicating that directory already exists.
# os.path.exists and os. mkdir may be helpful.
for file_name in os.listdir(os.getcwd() + '/imgs'):
    line = file_name.split('_')
    if line[0] == 'cat':
        copy(os.getcwd() + '/imgs/' + file_name, os.getcwd() + '/Cats/')
    elif line[0] == 'dog':
        copy(os.getcwd() + '/imgs/' + file_name, os.getcwd() + '/Dogs/')    
# Loop through all images in the Images folder
# Copy all the cat images to the Cats folder
# Copy all the dog images to the Dogs folder


directories = ['/Cats/', '/Dogs/']
pygame.init()
# Write the for loop line needed here to iterate over the file names in the Cats directory
for directory in directories:
    for file_name in os.listdir(os.getcwd() + directory):
        img = pygame.image.load(os.getcwd() + directory + file_name)
        pygame.display.set_caption(file_name) 
        display_surface = pygame.display.set_mode((img.get_rect().size[0], img.get_rect().size[1]))
        display_surface.blit(img, (0, 0))
        pygame.display.update()
        time.sleep(3)

# Try copying this code and have it display the dog images (or modify the above loop to go over both folders)

