#!/usr/bin/env python3
"""Social cards, designed to stay legible at LinkedIn's 128x72 thumbnail.
Run: DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib python3 brand/make-og.py"""
import cairosvg, io, glob, re, os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
W,H=1200,630; DARK=(19,19,18); AMBER=(245,158,11); WHITE=(245,244,240); MUTED=(150,145,135)
TF='/System/Library/Fonts/Supplemental/Arial Bold.ttf'; SF='/System/Library/Fonts/Helvetica.ttc'
def fm(p):
    s=open(p).read().split('---')[1]
    g=lambda k:(re.search(rf'^{k}:\s*"?(.+?)"?\s*$',s,re.M) or [None,''])[1]
    return g('title'),g('cover'),g('shortLabel'),g('category')
def bolt(d,cx,cy,s,fill):
    pts=[(.55,0),(.28,.45),(.48,.45),(.43,.77),(.72,.32),(.53,.32),(.55,0)]
    d.polygon([(cx+(x-.5)*s,cy+(y-.4)*s) for x,y in pts],fill=fill)
os.makedirs('public/og',exist_ok=True)
for md in sorted(glob.glob('src/content/journal/*.md')):
    pid=os.path.basename(md)[:-3]; title,cover,label,cat=fm(md)
    label=(label or cat or 'JOURNAL').upper()
    card=Image.new('RGB',(W,H),DARK)
    if cover and os.path.exists('public'+cover):
        # render big and zoom in: the motif must read at 128px wide
        art=Image.open(io.BytesIO(cairosvg.svg2png(url='public'+cover,output_width=2000,output_height=1500))).convert('RGB')
        r=max(W/art.width,H/art.height)*1.45          # zoom past fill so the graphic is large
        art=art.resize((int(art.width*r),int(art.height*r)),Image.LANCZOS)
        l=(art.width-W)//2; t=int((art.height-H)*0.46)
        art=art.crop((l,t,l+W,t+H))
        art=ImageEnhance.Contrast(art).enhance(1.18)  # survive heavy downscaling
        card.paste(art,(0,0))
    # bottom scrim only: keeps the graphic visible, guarantees the word reads
    sc=Image.new('L',(W,H),0); sd=ImageDraw.Draw(sc)
    for y in range(H):
        f=max(0.0,(y-H*0.42)/(H*0.58)); sd.line([(0,y),(W,y)],fill=int(232*(f**1.15)))
    card=Image.composite(Image.new('RGB',(W,H),DARK),card,sc)
    d=ImageDraw.Draw(card)
    size=150
    while size>70:
        f=ImageFont.truetype(TF,size)
        if d.textlength(label,font=f)<=W-150: break
        size-=6
    f=ImageFont.truetype(TF,size)
    d.text((72,H-size-132),label,font=f,fill=WHITE)
    bolt(d,88,H-70,54,AMBER)
    bf=ImageFont.truetype(TF,27); mf=ImageFont.truetype(SF,23)
    d.text((120,H-86),"The Physical",font=bf,fill=WHITE)
    d.text((120+d.textlength("The Physical ",font=bf),H-86),"Layer",font=bf,fill=AMBER)
    d.text((120,H-54),"thephysicallayer.fyi",font=mf,fill=MUTED)
    card.save(f'public/og/{pid}.png',optimize=True)
    # prove it reads small: save a 128px proof next to it
    card.resize((128,72),Image.LANCZOS).save(f'/tmp/proof_{pid}.png')
    print(f'{pid}: "{label}" @{size}px  {os.path.getsize(f"public/og/{pid}.png")//1024}KB')
