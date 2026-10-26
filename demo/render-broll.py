#!/usr/bin/env python3
"""Render presentation cards from actual recorded H-MEM evidence.

Requires Pillow. No credentials, network calls, or production state are read.
The H-MEM panels explicitly identify recorded command output.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html
import json
import textwrap

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "broll"
OUT.mkdir(exist_ok=True)
W, H = 1920, 1080
BG = "#090f1b"
INK = "#f4f7fb"
DIM = "#9daec5"
MINT = "#74ecc2"
BLUE = "#86b8ff"
PANEL = "#121d2f"
LINE = "#2a3b55"
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
MONO = "/System/Library/Fonts/SFNSMono.ttf"

def f(size=32, bold=False, mono=False):
    return ImageFont.truetype(MONO if mono else BOLD if bold else FONT, size)

def base(index, eyebrow, title, subtitle=None):
    im = Image.new("RGB", (W,H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((100,92,150,100),fill=MINT)
    d.text((173,76),eyebrow.upper(),font=f(25,True),fill=MINT)
    d.text((100,150),title,font=f(66,True),fill=INK)
    if subtitle:
        d.text((103,247),subtitle,font=f(29),fill=DIM)
    d.line((100,975,1820,975),fill=LINE,width=2)
    d.text((100,1003),"HUBCREW  /  OPEN AGENT 2026  /  TRACK 03",font=f(21,True),fill=DIM)
    d.text((1515,1003),f"wangwu.ai     {index:02d} / 07",font=f(21),fill=DIM)
    return im,d

def box(d, xy, fill=PANEL, outline=LINE, radius=24):
    d.rounded_rectangle(xy,radius=radius,fill=fill,outline=outline,width=2)

def lines(d, xy, value, size=32, fill=INK, width=None, spacing=13, mono=False, bold=False):
    x,y=xy
    if width:
        wrapped=[]
        for line in value.splitlines():
            wrapped += textwrap.wrap(line,width=width,break_long_words=False,replace_whitespace=False) or [""]
    else:
        wrapped=value.splitlines()
    for line in wrapped:
        d.text((x,y),line,font=f(size,bold,mono),fill=fill)
        y+=size+spacing
    return y

def pill(d,xy,text,color=MINT):
    x,y=xy
    ft=f(21,True)
    width=d.textlength(text,font=ft)+36
    box(d,(x,y,x+width,y+43),fill=BG,outline=color,radius=20)
    d.text((x+18,y+8),text,font=ft,fill=color)

def save(im,name):
    im.save(OUT/name,optimize=True)

# Intro: a quiet visual identity and a precise problem statement.
im,d=base(1,"Reasoning architecture","One person. Many named agents.")
d.text((100,336),"HubCrew",font=f(158,True),fill=INK)
d.text((110,527),"Keep the decisions. Carry the context.",font=f(48),fill=MINT)
lines(d,(113,627),"A structured handoff, grounded memory, and governed data\nfor more reliable decisions and actions.",size=35,fill=DIM,spacing=19)
pill(d,(111,801),"TRACK 03")
pill(d,(294,801),"wangwu.ai",BLUE)
pill(d,(480,801),"RECORDED SPONSOR DEMO")
save(im,"01-intro.png")

# Handoff model is architecture, not an unrecorded end-to-end runtime claim.
im,d=base(2,"The handoff contract","Carry forward what still matters.","Named-agent routing inherits the prior decision context.")
items=[("01","UNFINISHED WORK","What remains open","Finish the deployment only after\nthe required checks are complete."),
       ("02","FAILED PATHS","What has already failed","Keep the rejected attempt and\nits reason in the next session."),
       ("03","LIVE DECISIONS","What still governs action","Deploy only after green CI\nand a rollback check.")]
for i,(n,label,heading,body) in enumerate(items):
    x=100+i*585
    box(d,(x,360,x+550,760))
    d.text((x+35,397),n,font=f(42,True),fill=MINT)
    d.text((x+35,471),label,font=f(24,True),fill=DIM)
    d.text((x+35,525),heading,font=f(32,True),fill=INK)
    lines(d,(x+35,601),body,size=28,spacing=18)
lines(d,(102,826),"Architecture proposal: constitution + skills guide each agent; collaboration is a separate layer.",size=28,fill=DIM)
save(im,"02-handoff.png")

records=json.loads((ROOT/"evidence/hmem-recorded-output.json").read_text())
remember=records[0]["stdout"]
ask=records[1]["stdout"]
assert all(x["exit_code"] == 0 for x in records)
assert "remembered mem-1 via Mining -> Store" in remember
assert "provenance mem-1:" in ask
remember_lines=remember.splitlines()
ask_lines=ask.splitlines()

im,d=base(3,"Meterless H-MEM · recorded terminal output","Remember a deployment decision.","Actual local CLI run · official reference engine · isolated demonstration state")
box(d,(100,339,1820,866))
pill(d,(131,367),"PROCESS 1  /  REMEMBER")
lines(d,(136,447),'$ npx tsx notebook.ts remember\n  "[live_decision] We always deploy HubCrew only after\n   green CI and a rollback check."',size=29,mono=True,spacing=14)
d.line((134,605,1785,605),fill=LINE,width=2)
lines(d,(136,637),remember_lines[0].split(" | state:")[0],size=25,fill=DIM,mono=True)
lines(d,(136,690),remember_lines[1],size=29,fill=MINT,mono=True)
lines(d,(136,749),remember_lines[2].strip(),size=27,mono=True,width=91)
lines(d,(104,903),"The process exits. The next command reloads the memory from disk.",size=28,fill=DIM)
save(im,"03-hmem-remember.png")

im,d=base(4,"Meterless H-MEM · recorded terminal output","Ask, then inspect the provenance.","A new CLI process retrieves the actual stored memory; no generated answer fallback.")
box(d,(100,335,1820,899))
pill(d,(131,362),"PROCESS 2  /  ASK")
lines(d,(136,429),'$ npx tsx notebook.ts ask\n  "current live deployment decision deploy"',size=29,mono=True,spacing=13)
lines(d,(136,537),next(x for x in ask_lines if x.startswith("mode:")),size=25,fill=DIM,mono=True)
lines(d,(136,589),next(x for x in ask_lines if x.startswith("- [mem-1]")),size=29,fill=MINT,mono=True,width=90,spacing=13)
prov=json.loads(next(x for x in ask_lines if x.startswith("provenance mem-1:")).split(": ",1)[1])
lines(d,(136,705),"provenance mem-1:",size=27,mono=True)
lines(d,(136,751),json.dumps({k:prov[k] for k in ["source","origin","label","tags"]},ensure_ascii=False),size=25,fill=DIM,mono=True,width=104,spacing=11)
lines(d,(104,926),"Evidence: demo/evidence/ · retrieval-only · reference hash vectors · temporary state path omitted",size=23,fill=DIM)
save(im,"04-hmem-ask.png")

# Optional neutral interstitial for the actual Zetaris GUI clip.
im,d=base(5,"Zetaris · live local data platform","Query facts before deciding.","The following browser capture shows the SQL result from localhost:3000.")
box(d,(100,366,1820,747))
pill(d,(140,407),"SQL QUERY",MINT)
lines(d,(140,498),"SELECT * FROM TPCDS_DB.reason\nORDER BY r_reason_sk\nLIMIT 5;",size=48,mono=True,spacing=24)
lines(d,(104,820),"Validated local queries: SELECT 1 · NY_TAXI.taxi_zones · TPCDS_DB.reason",size=30,fill=DIM)
lines(d,(104,881),"Local platform verification: 9 / 9 PASS",size=30,fill=MINT)
save(im,"05-zetaris-intro.png")

im,d=base(6,"Architecture · status made explicit","A small core. A separate collaboration layer.","One agent = one entry + its own scheduler. Collaboration sits above the agent core.")
# Top architecture row.
for x,w,title,desc in [(100,460,"HUMAN ENTRY","HubCards / imwire"),(730,460,"COLLABORATION","Named routing + handoff"),(1360,460,"AGENT CORE","Scheduler + reasoning")]:
    box(d,(x,355,x+w,516))
    d.text((x+28,384),title,font=f(24,True),fill=BLUE)
    d.text((x+28,441),desc,font=f(29,True),fill=INK)
for x in (576,1206):
    d.line((x,436,x+124,436),fill=BLUE,width=4)
    d.polygon([(x+124,436),(x+108,426),(x+108,446)],fill=BLUE)
pill(d,(100,544),"ARCHITECTURE / INTENDED INTEGRATION",BLUE)
for x,w,title,desc in [(100,830,"METERLESS H-MEM","remember → ask · memory ID + provenance"),(990,830,"ZETARIS","SQL Editor · TPCDS reason · LIMIT 5")]:
    box(d,(x,636,x+w,799),outline=MINT)
    d.text((x+28,664),title,font=f(28,True),fill=MINT)
    d.text((x+28,722),desc,font=f(29),fill=INK)
pill(d,(100,821),"DEMONSTRATED LOCALLY: TWO SPONSOR BRIDGES")
d.text((102,899),"github.com/wangwu-30/open-agent-2026",font=f(35,True),fill=INK)
save(im,"06-architecture.png")

im,d=base(7,"Open Agent 2026 · Track 03","Meterless + Zetaris shown.","Pre-existing declared. The recorded scope is explicit.")
d.text((102,356),"Memory with provenance.",font=f(65,True),fill=MINT)
d.text((102,446),"Data with visible query results.",font=f(65,True),fill=INK)
box(d,(100,568,1820,794))
d.text((136,600),"PRE-EXISTING",font=f(23,True),fill=DIM)
d.text((136,648),"HubCards · home crew (家用班组) · imwire · teamrecall · benefit",font=ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc",33),fill=INK)
d.text((136,723),"HACKATHON DELTA    public repo + sponsor bridges + demo / slides",font=f(28,True),fill=MINT)
d.text((102,846),"github.com/wangwu-30/open-agent-2026",font=f(36,True),fill=INK)
d.text((102,908),"wangwu.ai   ·   @wangwu-30",font=f(29),fill=DIM)
save(im,"07-outro.png")

overlay=Image.new("RGBA",(W,H),(0,0,0,0))
od=ImageDraw.Draw(overlay)
od.text((40,35),(OUT/"zetaris-live-label.txt").read_text().strip(),font=f(28),fill=MINT)
od.text((40,1015),(OUT/"zetaris-capture-label.txt").read_text().strip(),font=f(22),fill=DIM)
overlay.save(OUT/"zetaris-overlay.png")

pages=sorted(p.name for p in OUT.glob("0*.png"))
(OUT/"index.html").write_text('''<!doctype html>
<html lang="en"><meta charset="utf-8"><title>HubCrew · Recorded B-roll</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>html,body{margin:0;width:100%;height:100%;background:#090f1b;overflow:hidden}body{display:grid;place-items:center}img{width:100vw;height:100vh;object-fit:contain}#help{position:fixed;bottom:8px;right:12px;color:#5f738f;font:11px system-ui;opacity:0;transition:opacity .2s}body:hover #help{opacity:1}</style>
<img id="card" alt="HubCrew recorded demo card"><div id="help">← / → change card · F fullscreen · 1–7 select</div>
<script>
const cards='''+json.dumps(pages)+''';
let i=Math.min(cards.length-1,Math.max(0,Number(new URLSearchParams(location.search).get('page')||1)-1));
const card=document.querySelector('#card');
function show(){card.src=cards[i];history.replaceState(null,'','?page='+(i+1));}
addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key===' '){i=(i+1)%cards.length;show()}if(e.key==='ArrowLeft'){i=(i+cards.length-1)%cards.length;show()}if(/^[1-7]$/.test(e.key)){i=+e.key-1;show()}if(e.key.toLowerCase()==='f')document.documentElement.requestFullscreen()});show();
</script></html>''')
print("Rendered",len(pages),"cards at",OUT)
