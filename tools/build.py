"""Build tossana-web/index.html from the Sota site's shared style + Tossana's own content.

    python tools/build.py          (run from the tossana-web folder)

Shared with sota-web (copied, so a style change there is picked up by rerunning this):
  the <head> CSS (Chakkhu style), the brand icons, the menu / lightbox / back-to-top / theme scripts.
Tossana's own parts: tools/body.html (content + extra CSS) and the script at the end of this file.
"""
import re
from pathlib import Path

here = Path(__file__).resolve().parent.parent
sota = (here.parent.parent / "sota-web" / "index.html").read_text(encoding="utf-8")   # ~/research/AI/sota-web
body = (here / "tools" / "body.html").read_text(encoding="utf-8")

# 1. head + shared CSS: everything up to Sota's own additions block
head = sota[: sota.index("<style>\n/* ---- Sota additions")]
head = head.replace("<title>Sota · Khmer speech recognition</title>", "<title>Tossana · Khmer image captioning</title>")
head = re.sub(r'<meta name="description" content="[^"]*">',
              '<meta name="description" content="Tossana (ទស្សនៈ, seeing) is a small Khmer image captioning model in research by Ing Muyleang: architecture, first results, data and roadmap.">', head)
head = head.replace('content="Sota · Khmer speech recognition"', 'content="Tossana · Khmer image captioning"')
head = re.sub(r'<meta property="og:description" content="[^"]*">',
              '<meta property="og:description" content="A small model that describes photos in Khmer, offline on your phone. In research.">', head)
assert "Sota" not in head.split("<style>")[0], "leftover Sota text in <head>"

# 2. brand icons exactly as on the Sota site
for sym in ["b-github", "b-huggingface"]:
    src = re.search(rf'<symbol id="{sym}".*?</symbol>', sota, re.S).group(0)
    body = re.sub(rf'<symbol id="{sym}".*?</symbol>', lambda m: src, body, flags=re.S)

# 3. shared scripts: copy citation, phone menu, lightbox, back to top, active link, theme
start = sota.index("<script>\n// ---- copy citation")
end = sota.index("// ---- hero preview")
shared = sota[start:end].replace("'sota-theme'", "'tossana-theme'")

own = r"""
// ---- hero preview: a picture is scanned, the Khmer caption appears ---------------------------
(function(){
  const CAPS=[["ព្រះអាទិត្យរះពីលើភ្នំ ក្បែរបឹង","the sun rises over a mountain by a lake"],
              ["ទូកមួយកំពុងអណ្តែតលើទន្លេ","a boat is floating on the river"],
              ["ផ្ទះមួយនៅក្បែរដើមឈើធំ","a house next to a big tree"]];
  const pics=[...document.querySelectorAll('#scene svg')], out=document.getElementById('capOut'), gl=document.getElementById('capGloss');
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const seg=('Segmenter' in Intl)? new Intl.Segmenter('km',{granularity:'grapheme'}) : null;
  const parts=s=>seg? [...seg.segment(s)].map(x=>x.segment) : [...s];
  (async()=>{
    const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
    for(let k=0;;k=(k+1)%CAPS.length){
      pics.forEach((p,i)=>p.classList.toggle('off',i!==k)); out.textContent=''; gl.textContent='';
      if(still){out.textContent=CAPS[k][0]; gl.textContent=CAPS[k][1]; return;}
      await sleep(1400);
      const p=parts(CAPS[k][0]);
      for(let i=1;i<=p.length;i++){out.textContent=p.slice(0,i).join(''); await sleep(70);}
      gl.textContent='“'+CAPS[k][1]+'”';
      await sleep(2600);
    }
  })();
})();

// ---- validation CIDEr per training round (measured, Flickr8k English test run) ---------------
(function(){
  const V=[52.1,64.4,70.5,70.2,69.3,68.6,66.6,66.3,65.0,64.3], best=2, top=80;
  const c=document.getElementById('curve'), x=document.getElementById('curveX');
  if(!c) return;
  c.innerHTML=V.map((v,i)=>`<div class="${i===best?'best':''}" style="height:${100*v/top}%" title="round ${i+1}: CIDEr ${v}"><span>${v.toFixed(1)}</span></div>`).join('');
  x.innerHTML=V.map((_,i)=>`<span>${i+1}</span>`).join('');
})();
</script>
</body>
</html>
"""
html = head + body + "\n" + shared + own
(here / "index.html").write_text(html, encoding="utf-8")
print(f"index.html {len(html)/1e3:.0f} kB")
