import pyautogui
import mss
from PIL import Image, ImageOps
import numpy as np

##################################################################################################
# site to access dino
# chrome://dino/
##################################################################################################

#Initialize variables
origin_x = 400 #Top left of section
origin_y = 750 #Top left of section
size_x = 400 #width
size_y = 250 #height
treshhold = 36.5

jump_cnt = 1

#define functions
def press_space():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def restart_game():
    pyautogui.click((960,230))
    press_space()

def jump():
    print('JUMP')
    press_space()

    image_name = './jump' + str(jump_cnt) + '.png'
    frame = Image.open('./screen.png') #open image
    image_section = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y +size_y)) #crop image
    image_section.save(image_name)


def update_screen():
    with mss.mss() as sct:
        sct.shot(output='screen.png')

def get_color_avg():
    frame = Image.open('./screen.png') #open image
    image_section = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y +size_y)) #crop image

    grey_image_section = ImageOps.grayscale(image_section) #remove color

    #turn image into an array of pixels and get average of the numbers
    image_pixel_array = np.array(grey_image_section.getdata())
    image_color_avg = np.mean(image_pixel_array)

    print(image_color_avg)
    return image_color_avg

def should_jump(x):
    if x > treshhold:
        return True
    return False

#Runtime
restart_game()

while True:
    update_screen()
    image_color_avg = get_color_avg()
    if should_jump(image_color_avg) is True:
        jump()
        jump_cnt += 1