import json
from pprint import pprint
import os, sys
from shutil import move
import numpy as np
import scipy.misc
import pickle
import cv2

json_path ='./wikiart/wikiart/meta/'
image_path = './wikiart/wikiart/images/'
image_save_path = './5c640/'
meta_save_path = './5c64_meta/'

target3_style =['Romanticism','Realism','Impressionism']
target3_genre=['portrait','landscape','genre painting']
target5_style = ['Impressionism', 'Realism', 'Romanticism', 'Expressionism', 'Post-Impressionism']
target5_genre = ['portrait', 'landscape', 'genre painting', 'cityscape', 'sketch and study'] 
target10_style = ['Impressionism', 'Realism', 'Romanticism', 'Expressionism', 'Post-Impressionism', 'Surrealism' ,'Art Nouveau (Modern)', 'Baroque', 'Symbolism', 'Abstract Expressionism']
target10_genre = ['portrait', 'landscape', 'genre painting', 'abstract', 'religious painting', 'cityscape', 'sketch and study', 'figurative', 'illustration', 'still life'] 

dic = {}
dic_genre = {}
dic_style = {}
Flag = 2 # 0 : small, 1 : middle, 2 : large
opt = True # True : make dataset, False : count the number of artworks by each style and genre
size = 64

er ={}
num = 1
def my_mkdir(path) :
    if not os.path.exists(path) :
        os.mkdir(path)

def check(genre, style, Flag) :
    if Flag is 0 :
      if not genre in target3_genre :
          return False
      if not style in target3_style:
          return False
    elif Flag is 1 :
      if not genre in target5_genre :
          return False
      if not style in target5_style:
          return False
    else :
      if not genre in target10_genre :
          return False
      if not style in target10_style:
          return False
    return True

def count (filename) :
    with open(filename) as data_file:
        data = json.load(data_file)
        l = len(data)
        e = 0
        i = 0
        for element in data :
            try :
                contentId = str(element['contentId'])
	        genre = element['genre']
                style = element['style']
                if ',' in style :
                    print (contentId)
                if not check(genre, style,Flag) :
                    continue
                key = genre+'|'+style
                if key in dic :
                    dic[key] = dic[key] + 1
                else :
                    dic[key] = 1
                i = i +1
            except :
                e = e +1
                pass
    print (filename.split("/")[-1].split(".")[0]+" has Images : " + str(l)+'save : '+str(i)+ " and error : " + str(e))
    return l-e

def resize (path,contentId) :
    print path
    image = cv2.imread(path)#scipy.misc.imread(path)
    (b,g,r) = cv2.split(image)
    image = cv2.merge([r,g,b])
    image = scipy.misc.imresize(image,(size,size))
    scipy.misc.imsave(image_save_path+contentId+'.jpg',image)
                
def open_json (filename) :
    with open(filename) as data_file:
        data = json.load(data_file)
        l = len(data)
        e = 0
        i = 0
        for element in data :
            try :
                contentId = str(element['contentId'])
	        genre = element['genre']
                style = element['style']
                if not check(genre, style,Flag) :
                    continue
                path = image_path + contentId+'.jpg'
                resize(path,contentId)
                dic_style[contentId] = style
                dic_genre[contentId] = genre
                i = i +1
            except :
 #               os.system('wget -O %s -t 10 %s' % (name, element['image'].replace('!','\!')))
                e = e +1
                pass

    print (filename.split("/")[-1].split(".")[0]+" has Images : " + str(l)+'save : '+str(i)+ " and error : " + str(e))
    return l-e


def read_artist(limit) :
    num = 0
    image_list = os.listdir(json_path)
    for e in image_list :
       if(limit ==0) :
           break
       if opt :
           num = num + open_json(json_path+e)
       else :
           num = num + count(json_path +e )
       limit = limit -1
    print("TOTAL NUMBER : " + str(num))

def save_labels () :
    with open(meta_save_path+'genre.pkl','w') as fgenre, open(meta_save_path+'style.pkl','w') as fstyle :
        pickle.dump(dic_genre, fgenre)
        pickle.dump(dic_style, fstyle)

def save_dic() : # count by each style and genre
    with open('count.txt','w') as c :
        for k,v in dic.iteritems() :
            print k,v
            c.write(k.encode('utf8'))
            c.write('|'+str(v)+'\n')

#initialize
my_mkdir(image_save_path)
my_mkdir(meta_save_path)

read_artist(-1)
if opt :
    save_labels()
else :
    save_dic()
