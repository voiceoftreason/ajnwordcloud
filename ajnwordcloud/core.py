import numpy as np
from PIL import Image, ImageDraw, ImageFont
from random import random, choice
from math import log, ceil
from operator import itemgetter
from . import ii_search
from .fonts import font_xkcd

def __generate_ii(im):
    """
    Create integral image array
    
    Arguments:
    im -- "L" mode PIL image
    
    Returns:
    2D numpy array of integral image
    """
    im_arr = np.fromstring(im.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((im.size[1], im.size[0]))
    return im_arr.cumsum(axis=0).cumsum(axis=1).astype(np.uint32)

def __scale_words(data, 
                  scale, 
                  maxwords, 
                  uppercase):
    """
    Calculate font sizes for each word using specified scaling method
        
    Arguments:
    data -- dictionary of word counts/values
    scale -- int value as base size for log scale
    maxwords -- maximum number of words used to create cloud
    uppercase -- convert words to uppercase
    
    Returns:
    List of word/font size tuples sorted in descending order
    """
    # scale values
    vocab = { k.upper() if uppercase else k: int(ceil(log(v) * scale)) for k, v in data.items() }
    # return provided max words from sorted list
    return sorted(vocab.items(), key=itemgetter(1), reverse=True)[0:maxwords]
    
def wordcloud(words, 
              fontname=font_xkcd, 
              cloudsize=(400, 400), 
              maxwords=500, 
              uppercase=False, 
              scale=12, 
              minfontsize=7, 
              colours=['black'], 
              background='white', 
              step=1, 
              fontstep=1, 
              rotated=0.5, 
              mask=None):
    """
    Generate the word cloud image
        
    Arguments:
    words -- dictionary of word counts
    fontname -- name of truetype font to use
    cloudsize -- size of wordcloud image (default: (400, 400)
    maxwords -- maximum number of words to use (default: 500)
    uppercase -- whether to change words to upper case (default: False)
    scale -- scaling factor for font sizes (default: 16)
    minfontsize -- minimum font size (default: 7)
    colours -- list of colour names/hex values to use, see colours.py for built in schemes (default: multi)
    background -- background colour to use (default: None)
    step -- size of step when scanning image for available areas (default: 1)
    fontstep -- size of font reduction when word doesn't fit (default: 1)
    rotated -- proportion of words to rotate when placed (default: 0.5) 
    mask -- black and white image to define shape/area to use for cloud, will be resized to cloudsize (default: None)
    
    Returns:
    im - PIL image of completed cloud
    """
    # scale font sizes and sort words
    words = __scale_words(words, scale, maxwords, uppercase)
    # create main image
    im = Image.new("RGBA", cloudsize, background)
    # open mask image or create blank b/w image
    if mask:
        im1bit = Image.open(mask).convert("L").resize(cloudsize, Image.NEAREST) 
    else:
        im1bit = Image.new("L", cloudsize, 0)
    #initial integral image
    ii = __generate_ii(im1bit)
    # arbitrary large font size for initial check
    fontsize = 5000
    for word, fontsize_orig in words[0:maxwords]:
        # check so font size never increases
        if fontsize_orig < fontsize:
            fontsize = fontsize_orig
        # handle word rotation
        rotate=False
        if random() < rotated:
            rotate = True
        while True:
            # get font at current size and measure
            font = ImageFont.truetype(fontname, fontsize)
            size = ImageDraw.Draw(im).textsize(word, font=font)
            searchsize = (size[1], size[0]) if rotate else size
            # find possible spots
            if step > 1:
                spots = ii_search.ii_search(ii, searchsize[0], searchsize[1], step=step)
            else:
                spots = ii_search.ii_search_nostep(ii, searchsize[0], searchsize[1])
            if len(spots) > 0:
                # spots available so create text patch and place randomly
                im1 = Image.new("RGB", (size[0] + 16, size[1] + 16), background)
                alpha = Image.new("L", im1.size, 0)
                ImageDraw.Draw(im1).text((8, 8), word, font=font, fill=choice(colours))
                ImageDraw.Draw(alpha).text((8, 8), word, font=font, fill='white')
                spot = choice(spots)
                if rotate:
                    im1 = im1.rotate(90, expand=1)
                    alpha = alpha.rotate(90, expand=1)
                im.paste(im1, (spot[1]-8, spot[0]-8), alpha)
                im1bit.paste(alpha, (spot[1]-8, spot[0]-8), alpha)
                # regenerate the integral image and move to next word
                ii = __generate_ii(im1bit)
                break
            else:
                # no spots, decrease font size and try again
                fontsize -= fontstep
            # return when we hit the min font size
            if fontsize <= minfontsize:
                return im
    # return when we run out of words
    return im