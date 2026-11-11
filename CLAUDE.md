# Tossana ទស្សនៈ · project notes for Claude

Tossana ("seeing", Pali dassana) is a small Khmer image captioning model by Ing Muyleang, in research.
This repo is its website, deployed to https://muyleanging.github.io/tossana-web/ by GitHub Actions.
Research code and notebooks: ~/research/AI/image-captioning (EXPERIMENTS.md is the result log).

## Project family (keep names and style consistent)
- Akkhara អក្ខរៈ: keyboard (types) · Chakkhu ចក្ខុ: OCR (reads) · Sota សោតៈ: ASR (listens) · Tossana ទស្សនៈ: captions (sees) · VoxPocket: TTS (speaks)

## Website rules
- index.html is GENERATED: edit tools/body.html (content + Tossana CSS) or tools/build.py (head text, scripts), then run
  `python tools/build.py`. The head CSS, brand icons and menu/lightbox/theme scripts are copied from ../sota-web/index.html,
  so a style change on Sota/Chakkhu is picked up by rerunning the build.
- Mark unmeasured numbers as "soon", "planned" or "≈". Never invent results. The only measured numbers so far are the
  English Flickr8k test run (label them as English, not Khmer).
- Hero captions are example sentences, labelled as a preview, not model output.

## Status (2026-11-11)
- English baseline (Flickr8k, ViT-S + 4-layer decoder, 43M): test CIDEr 65.9, BLEU-4 25.5 (1,000 photos, beam 5); best val epoch 3
- Next: pick translator (NLLB-200 vs MADLAD-400), translate Flickr8k to Khmer, human-check 1,000 test photos × 2 captions, train Khmer model
- Planned: concept head + hallucination guard (main research idea), large VLM teacher

## Published names
- GitHub: MuyleangIng/tossana-web (this site)
- HF model: muyleanging/Tossana-Caption-Khmer (card only, no weights yet)
- HF dataset: muyleanging/Tossana-Caption-Khmer (PRIVATE, card only; Flickr8k is research-only)
