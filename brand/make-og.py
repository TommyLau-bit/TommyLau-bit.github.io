#!/usr/bin/env python3
"""Regenerate public/og/<slug>.png from each piece's cover diagram.
Run from the project root:  DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py"""
import cairosvg, io, glob, re, os
from PIL import Image, ImageDraw, ImageFont
W,H=1200,630; DARK=(19,19,18); AMBER=(245,158,11); WHITE=(240,239,234); MUTED=(150,145,135)
TF='/System/Library/Fonts/Supplemental/Arial Bold.ttf'; SF='/System/Library/Fonts/Helvetica.ttc'
def fm(p):
    s=open(p).read().split('---')[1]
    g=lambda k:(re.search(rf'^{k}:\s*"?(.+?)"?\s*$',s,re.M) or [None,''])[1]
    return g('title'),g('cover'),g('category')
def wrap(d,t,f,mw):
    out=[];cur=''
    for w in t.split():
        x=(cur+' '+w).strip()
        if d.textlength(x,font=f)<=mw: cur=x
        else: out.append(cur);cur=w
    if cur: out.append(cur)
    return out
def bolt(d,cx,cy,s,fill):
    pts=[(.55,0),(.28,.45),(.48,.45),(.43,.77),(.72,.32),(.53,.32),(.55,0)]
    d.polygon([(cx+(x-.5)*s,cy+(y-.4)*s) for x,y in pts],fill=fill)
os.makedirs('public/og',exist_ok=True)
for md in sorted(glob.glob('src/content/journal/*.md')):
    pid=os.path.basename(md)[:-3]; title,cover,cat=fm(md)
    card=Image.new('RGB',(W,H),DARK)
    if cover and os.path.exists('public'+cover):
        art=Image.open(io.BytesIO(cairosvg.svg2png(url='public'+cover,output_width=1600,output_height=1200))).convert('RGB')
        r=max(W/art.width,H/art.height); art=art.resize((max(W,int(art.width*r)),max(H,int(art.height*r))),Image.LANCZOS)
        l=(art.width-W)//2; t=(art.height-H)//2; card.paste(art.crop((l,t,l+W,t+H)),(0,0))
    sc=Image.new('L',(W,H),0); sd=ImageDraw.Draw(sc)
    for x in range(W): sd.line([(x,0),(x,H)],fill=int(238*(max(0.0,1.0-(x/(W*.80)))**1.25)))
    card=Image.composite(Image.new('RGB',(W,H),DARK),card,sc); d=ImageDraw.Draw(card)
    for size in (60,56,52,48,44,40):
        f=ImageFont.truetype(TF,size); lines=wrap(d,title,f,660)
        if len(lines)<=4: break
    y=H//2-(len(lines)*(size+10))//2-24
    for ln in lines: d.text((72,y),ln,font=f,fill=WHITE); y+=size+10
    d.text((72,y+14),(cat or 'Journal').upper(),font=ImageFont.truetype(TF,20),fill=AMBER)
    bolt(d,88,H-64,52,AMBER); bf=ImageFont.truetype(TF,26); mf=ImageFont.truetype(SF,22)
    d.text((118,H-80),"The Physical",font=bf,fill=WHITE)
    d.text((118+d.textlength("The Physical ",font=bf),H-80),"Layer",font=bf,fill=AMBER)
    d.text((118,H-50),"thephysicallayer.fyi",font=mf,fill=MUTED)
    card.save(f'public/og/{pid}.png',optimize=True); print('wrote',pid)
