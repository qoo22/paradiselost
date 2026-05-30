import sys, requests, io
from PIL import Image
TOKEN="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"
URL="https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
def gen(prompt, out, size=512):
    r=requests.post(URL, headers={"Authorization":"Bearer "+TOKEN,"Accept":"image/png"},
                    json={"inputs":prompt}, timeout=120)
    if r.status_code!=200:
        print("FAIL", out, r.status_code, r.text[:200]); return False
    im=Image.open(io.BytesIO(r.content)).convert("L")          # グレースケール(モノクロ・ゲーム調)
    im=im.resize((size,size), Image.LANCZOS)
    im.save(out)
    print("OK", out, im.size)
    return True
if __name__=="__main__":
    name=sys.argv[1]; prompt=sys.argv[2]; out=sys.argv[3]
    gen(prompt, out)
