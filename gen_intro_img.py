import sys, shutil
from gradio_client import Client
from PIL import Image

TOK="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"
STYLE=" , monochrome grayscale ink illustration, storybook picture-book style, soft grain, atmospheric, fairytale, no text, no words"

JOBS = {
 "intro_stair":  "a grand ethereal staircase of light connecting a bright surface world above and a dark underground cavern far below, glowing steps descending into the deep",
 "intro_together":"silhouettes of a human child and a small gentle horned fairy creature holding hands together, raising one tiny glowing lantern flame in a dark cavern, warm and peaceful",
 "intro_door":   "an enormous ancient stone door carved with a pair of tightly shut closed eyes, sealing a cave entrance, cold and ominous, heavy chains",
 "intro_wait":   "many lonely small round storybook creatures sitting scattered in a vast dark underground cavern, each cradling a faint tiny flame, waiting quietly for someone to return",
 "intro_awaken": "a small child lying on cold stone ground at the bottom of a deep cavern, a single thin ray of pale light falling from a tiny hole far far above, soft glowing flowers blooming around the child",
 "intro_path":   "a winding trail of softly glowing flowers leading deeper into an ancient underground cavern, old worn carvings of people and creatures on the stone walls, mysterious",
}

client = Client("evalstate/flux1_schnell", token=TOK)
for i,(name,prompt) in enumerate(JOBS.items()):
    try:
        res = client.predict(prompt=prompt+STYLE, seed=1234+i, randomize_seed=True,
                             width=768, height=576, num_inference_steps=4, api_name="/infer")
        src = res[0] if isinstance(res,(list,tuple)) else res
        im = Image.open(src).convert("L").resize((640,480), Image.LANCZOS)
        out = f"img/{name}.png"
        im.save(out)
        print("OK", out, im.size)
    except Exception as e:
        print("FAIL", name, repr(e)[:160])
