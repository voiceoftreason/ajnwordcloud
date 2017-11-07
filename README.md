# ajnwordcloud - wordclouds in Python

## About
ajnwordcloud is a simple word cloud generator written in Python (with some Cython).  You can generate a cloud from a dictionary of word counts and functions are included for counting words from a string or a text file, or loading word counts from a CSV.  Also included are a set of basic colour schemes, fonts and masks.

The following can be configured when creating a cloud:

* font, size and shape
* text and background colour
* proportion of rotated words

## Installation

You can install from the Python package index:

`pip install ajnwordcloud`

You will need a compiler installed, on Linux you should already have what you need, Mac you will need Xcode, Windows you will need Visual Studio with C++ installed or you can install the C++ Build Tools

## Usage

#### Load some resources:

```python
from ajnwordcloud import red, orange, blue, white
from ajnwordcloud import font_xkcd, font_mouse_memoirs, font_chunkfive
from ajnwordcloud import mask_ellipse, mask_roundrect, mask_cloud
```

#### Load data:

```python
from ajnwordcloud import load_txt

aliens = load_txt('aliens.txt')
```

#### Create cloud with default options:

```python
from ajnwordcloud import wordcloud

im = wordcloud(aliens)
```

![default cloud](https://github.com/voiceoftreason/ajnwordcloud/blob/master/examples/output_1_0.png)

#### Change the size and shape of the cloud:

```python
im = wordcloud(aliens, 
				cloudsize=(640, 480), 
				mask=mask_ellipse)
```

![size and shape](https://github.com/voiceoftreason/ajnwordcloud/blob/master/examples/output_2_0.png)

#### Apply a colour scheme:

```python
im = wordcloud(aliens, 
				cloudsize=(640, 480), 
				colours=red, 
				mask=mask_ellipse)
```

![colour](https://github.com/voiceoftreason/ajnwordcloud/blob/master/examples/output_3_0.png)

#### Change the default font:

```python
im = wordcloud(aliens, 
				fontname=font_chunkfive, 
				colours=blue+orange
				cloudsize=(640, 480), 
				mask=mask_cloud)
```

![colour scheme](https://github.com/voiceoftreason/ajnwordcloud/blob/master/examples/output_4_0.png)

#### Change proportion of rotated words:

```python
im = wordcloud(aliens, 
				fontname=font_mouse_memoirs, 
				cloudsize=(640, 480), 
				scale=18, 
				colours=white, 
				background='black', 
				mask=mask_roundrect, 
				rotated=0)
```

![rotation](https://github.com/voiceoftreason/ajnwordcloud/blob/master/examples/output_5_0.png)
