import random
from pydub import AudioSegment
from pydub.playback import play
from typing import Dict
from pypinyin import pinyin,lazy_pinyin,Style
import re
import json


#pitch即选择声线
Tone = 'Girl_A'
#拼音表
keys = ['a','ai','an','ang','ao','b','c','ch','d','e','ei','en','eng','er','f','g','h','i','ia',
		'ian','iang','iong','iao','ie','in','ing','iou','iu','j','k','l','m','n','o','ong','ou','p','q',
		'r','s','sh','t','u','ua','uai','uan','uang','ueng','uei','uen','uo','v','van','ve','vn','x','z','zh', '，','。','？','！']

#中文标点符号表
marklist = ['，','。','？','！']
#输入中文
chinese = input("请输入文字:")
#去掉中文里面的标点符号
chinese_non = re.sub(r'[？ 、；！，。“”?.~…,$\r\n《》——]|(<.*>)', '', chinese.strip())
#中文里分离出声母与韵母
initials = lazy_pinyin(chinese_non, style=Style.INITIALS)
finals = lazy_pinyin(chinese_non, style=Style.FINALS)
stringy = list(zip(initials, finals))
print(stringy)	

#路径字典
sounds = {}
for ltr in keys:
	if ltr != '':
		sounds[ltr] = ".//sounds//"+Tone+"//"+ltr+".wav"

#加载声音特征
if Tone == 'Girl_A':
	rnd_factor = 1.7
if Tone == 'Boy_A':
	rnd_factor = 1.7

#拼音列表循环
setfiles = []
for initial,final in stringy:
	if initial=='' or initial!='':
		setfiles.append(initial)
	if final=='' or final!='':
		setfiles.append(final)

#1/2概率随机替换声母或者韵母为空''
for g in range(len(setfiles)-1):
	if (g)%2!=0:#偶数忽略
		continue
	else:
		x = random.random()
		if x>.7:
			setfiles[g]=''
		if x<=.7 and setfiles[g]!='':
			setfiles[g+1]=''
		if x<=.7 and setfiles[g]=='':
			continue	

#去掉空格
infiles = []
for h in range(len(setfiles)):
	if setfiles[h]!='':
		infiles.append(setfiles[h])	

#重新插回标点符号
chinese = list(chinese)
for index,ltr in enumerate(chinese):
	for i,j in enumerate(marklist):
		if j==ltr:
			infiles.insert(index,marklist[i])
print(infiles)

#找到对应路径,随机音高
combined_sounds = None
for index,sound in enumerate(infiles):
	tempsound = AudioSegment.from_wav(sounds[sound])
	if stringy[len(stringy)-1] == '？':
		if index >= len(infiles)*.8:
			octaves = random.uniform(0.5,1) * rnd_factor+ 1
		   #+ (index-index*.8) * .1 + 2.1  
		else: 
			octaves = random.uniform(0.5,1) * rnd_factor+0.8
			#+ 2.0
	else:
		octaves = random.uniform(0.5,1) * rnd_factor+0.5
	   #+ 2.3 
	new_sample_rate = int(tempsound.frame_rate * (1.2 ** octaves))
	new_sound = tempsound._spawn(tempsound.raw_data, overrides={'frame_rate': new_sample_rate})
	new_sound = new_sound.set_frame_rate(44100) # 统一采样率
	combined_sounds = new_sound if combined_sounds is None else combined_sounds + new_sound
combined_sounds.export("./sound.wav", format="wav")
