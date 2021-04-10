import matplotlib
import glob, os
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import random
#import streamlit as st

def poster1(string = 'Your Event', stringTime = '2Days', 
backup_string= 'your backup string', fileString = 1 ,img =  None,  
gray = False, color = 'white', channel = 'green', size =(8, 11), margin=0.00001, dpi = 100):
    plt.ion()
    if len(string) > 12:
        string = string.replace(' ', '\n')
    #string = string.capitalize()

    #define scale
    xsize = float(size[0])
    ysize= float(size[1])
    aspect = float(1) #ysize / xsize

    #load the img
    if img is None:
        img_list = os.listdir(os.path.join(os.getcwd(), 'image'))
        image = imread (os.path.join(os.getcwd(), 'image', random.choice(img_list)))
    else:
        image = imread(img)

    #creat a plot
    plt.figure('poster', figsize = size, dpi = dpi)
    ax= plt.subplot()
    ax.cla()
    plt.setp(ax.get_xticklabels(), visible = False)
    plt.setp(ax.get_xticklines(), visible = False)
    plt.setp(ax.get_yticklabels(), visible = False)
    plt.setp(ax.get_yticklines(), visible = False)
    plt.subplots_adjust(left= margin/xsize , right = 1.0 - margin/xsize, 
    top=1.0 - margin/ysize, bottom = margin/ysize )

        
    #crop image to the right ratio
    imageaspect = float(image.shape[0]) / float(image.shape[1])
    if imageaspect > aspect:
        #image is taller than poster
        trim = (image.shape[0] - aspect * image.shape[1]/aspect)/2
        image = image[:, trim: -trim]

    #draw backgrouunf image set to gray with vmax 500 cmap= 'gray', interpolation = 'nearest', vmax= 500
    if gray:
        #convert image to greyscale
        if len(image.shape) ==3:
            rgb = dict(red=0, green=1, blue=2)
            image = image[:, :, rgb[channel.lower()]]
        ax.imshow(image, extent= [0, xsize, 0, ysize], cmap= 'gray', interpolation = 'nearest')
    else:
        ax.imshow(image, extent= [0, xsize, 0, ysize], )

    #draw the text
    ax.text(4.25, 0.75, backup_string.lower(), fontsize= 20,
    ha='center', weight = 'normal', color= color)
    ax.text(4.25, 2.25, string, fontsize = 40, ha ='center', 
    weight='bold', color= color)
    ax.text(4.25, 9, stringTime, fontsize = 60, color= color,
    ha='center', weight='bold', va='top')
    ax.text(4.25, 7, 'to go', fontsize = 30, color= color,
    ha='center', weight='bold', va='top')
    #this event is in 1 day 20 hr 30 min, 2 days to go event name

    #save img in a directory
    try:
        os.mkdir('posters')
        os.mkdir('posters/poster1')
    except:
        pass
    #fileString= string.lower().replace(' ', '')
    #fileString = fileString.replace(' ', '')
    filename_png = 'posters/' + 'poster1/' + str(fileString) +'.png'
    #filename_jpeg = 'posters/' + fileString + '.jpeg'
    #filename_pdf = 'posters/' + fileString + '.pdf'

    plt.savefig(filename_png, edgecolor ='none', transparent = True)

    #st.write(plt.draw())
    #plt.draw()


def poster2(string = 'Your Event', stringTime = '2Days', 
backup_string= 'Be Ready!', fileString = 1 ,img =  None, 
gray = False, color = 'white', channel = 'green',size =(8, 11), margin=0.00001, dpi = 100, ):
    plt.ion()

    #string = string.capitalize()
    if len(string) > 12:
        string = string.replace(' ', '\n')

    #define scale
    xsize = float(size[0])
    ysize= float(size[1])
    aspect = float(1) #ysize / xsize

    #load the img
    if img is None:
        img_list = os.listdir(os.path.join(os.getcwd(), 'image'))
        image = imread (os.path.join(os.getcwd(), 'image', random.choice(img_list)))
    else:
        image = imread(img)

    #creat a plot
    plt.figure('poster', figsize = size, dpi = dpi)
    ax= plt.subplot()
    ax.cla()
    plt.setp(ax.get_xticklabels(), visible = False)
    plt.setp(ax.get_xticklines(), visible = False)
    plt.setp(ax.get_yticklabels(), visible = False)
    plt.setp(ax.get_yticklines(), visible = False)
    plt.subplots_adjust(left= margin/xsize, right = 1.0 - margin/xsize, 
    top=1.0 - margin/ysize, bottom = margin/ysize)


       

    #crop image to the right ratio
    imageaspect = float(image.shape[0]) / float(image.shape[1])
    if imageaspect > aspect:
        #image is taller than poster
        trim = (image.shape[0] - aspect * image.shape[1]/aspect)/2
        image = image[:, trim: -trim]

    #draw background image set to gray with vmax 500 cmap= 'gray',  interpolation = 'nearest',
    if gray:
         #convert image to greyscale
        if len(image.shape) ==3:
            rgb = dict(red=0, green=1, blue=2)
            image = image[:, :, rgb[channel.lower()]]
        ax.imshow(image, extent= [0, xsize, 0, ysize], cmap= 'gray', interpolation = 'nearest', vmax = 500)
    else:
       ax.imshow(image, extent= [0, xsize, 0, ysize])

    #draw the text
    ax.text(4.25, 0.75, backup_string.capitalize(), fontsize= 20,
    ha='center', weight = 'normal', color= color)
    ax.text(4.25, 3.25, stringTime, fontsize = 60, ha ='center', 
    weight='bold', color= color)
    ax.text(4.25, 9, string, fontsize = 40, color= color,
    ha='center', weight='bold', va= 'top')
    ax.text(4.25, 6, 'happening in', fontsize = 25, color= color,
    ha='center', weight='bold', va= 'top')
    #this event is in 1 day 20 hr 30 min, 2 days to go event name

    #save img in a directory
    try:
        os.mkdir('posters')
        os.mkdir('posters/poster2')
    except:
        pass
    #fileString= string.lower().replace(' ', '')
    #fileString = fileString.replace(' ', '')
    filename_png = 'posters/' + 'poster2/' + str(fileString) + '.png'
    #filename_jpeg = 'posters/' + fileString + '.jpeg'
    #filename_pdf = 'posters/' + fileString + '.pdf'
    plt.savefig(filename_png, transparent = True)
   
    #st.write(plt.draw())
    #plt.draw()

'''
if __name__ == '__main__':
    poster1()
    poster2()
    print('...Done')
'''