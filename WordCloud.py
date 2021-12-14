#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

from konlpy.tag import Okt
from konlpy.tag import Hannanum
from collections import Counter
get_ipython().system('pip install stylecloud')


# In[27]:


##lyric data open
with open('ballad.txt', 'r',encoding='UTF8') as f2:
    result = f2.read()
    
okt = Okt()
noun = okt.nouns(result)

nouns = [n for n in noun if len(n)>1]
count = Counter(nouns)
tags = count.most_common(100)

mask = Image.new("RGBA", image.size, (255,255,255)) #(2555,2575)는 사진 크기, (255,255,255)는 색을의미
image = Image.open('BB.png').convert("RGBA")
x,y = image.size
mask.paste(image,(0,0,x,y),image)
mask = np.array(mask)

from wordcloud import WordCloud
wordcould = WordCloud(font_path='C:\Windows\Fonts\gulim.ttc', background_color='white', mask=mask).generate_from_frequencies(dict(tags))

fig = plt.figure()
plt.axis('off')
plt.imshow(wordcould)

tags


# In[30]:


##lyric data open
with open('hiphop.txt', 'r',encoding='UTF8') as f2:
    result = f2.read()
    
okt = Okt()
noun = okt.nouns(result)

nouns = [n for n in noun if len(n)>1]
count = Counter(nouns)
tags = count.most_common(100)

mask = Image.new("RGBA",(2555,2575), (255,255,255)) #(2555,2575)는 사진 크기, (255,255,255)는 색을의미
image = Image.open('HH.png').convert("RGBA")
x,y = image.size
mask.paste(image,(0,0,x,y),image)
mask = np.array(mask)

from wordcloud import WordCloud
wordcould = WordCloud(font_path='C:\Windows\Fonts\gulim.ttc', background_color='white', width=2000, height=1600, mask=mask).generate_from_frequencies(dict(tags))

fig = plt.figure()
plt.axis('off')
plt.imshow(wordcould)

tags

