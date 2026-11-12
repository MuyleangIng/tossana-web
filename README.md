# Tossana ទស្សនៈ · Khmer image captioning

Website: **https://muyleanging.github.io/tossana-web/**

Tossana ("seeing") is a small Khmer image captioning model in research by Ing Muyleang: it will describe photos in
Khmer, offline on your phone. The site shows the planned architecture, the first (English) test results, the data plan
and the roadmap.

From the maker of [Akkhara](https://muyleanging.github.io/akkhara-web/), [Chakkhu](https://muyleanging.github.io/chakkhu-web/)
and [Sota](https://muyleanging.github.io/sota-web/): Chakkhu reads the text in a picture, Tossana describes the rest.

## Edit the site
`index.html` is built from `tools/body.html` (Tossana's content) plus the shared style and scripts of `~/research/AI/sota-web/index.html`:

```
python tools/build.py
```
