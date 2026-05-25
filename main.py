python3 << 'PYEOF'
import base64

with open('/mnt/user-data/uploads/IMG_2754.JPG', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode()

# Write HTML in two parts to keep the placeholder clean
html_part1 = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>مبروك الخطوبة — عبّاس و رَوان</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400;1,700&family=Aref+Ruqaa:wght@400;700&family=Reem+Kufi:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}

  :root{
    --ink:#2b2218;
    --gold:#bf9b5a;
    --gold-bright:#e6c780;
    --gold-deep:#9a7838;
    --rose:#d99a8a;
    --rose-soft:#f0d3c8;
    --sage:#7c8f6f;
    --sage-deep:#5c6e50;
    --cream:#faf3e6;
    --paper:#fdf9ef;
    --champagne:#f3e7cf;
  }

  html,body{
    width:100%;height:100%;overflow:hidden;
    background:#0c0a07;
    font-family:'Reem Kufi',sans-serif;
    cursor:default;user-select:none;
    -webkit-user-select:none;
  }

  /* ───────── ATMOSPHERE LAYERS ───────── */
  #bg{
    position:fixed;inset:0;z-index:0;
    background:
      radial-gradient(ellipse 80% 60% at 50% 18%, rgba(191,155,90,0.22) 0%, transparent 60%),
      radial-gradient(ellipse 120% 90% at 50% 100%, rgba(124,143,111,0.14) 0%, transparent 55%),
      radial-gradient(circle at 50% 40%, #221a10 0%, #110d08 55%, #070504 100%);
  }
  /* slow rotating warm glow */
  #aura{
    position:fixed;left:50%;top:42%;
    width:140vmax;height:140vmax;
    transform:translate(-50%,-50%);
    background:conic-gradient(from 0deg,
      transparent 0deg, rgba(230,199,128,0.05) 40deg,
      transparent 90deg, rgba(217,154,138,0.04) 160deg,
      transparent 220deg, rgba(230,199,128,0.05) 290deg, transparent 360deg);
    animation:auraSpin 50s linear infinite;
    z-index:0;pointer-events:none;
  }
  @keyframes auraSpin{to{transform:translate(-50%,-50%) rotate(360deg)}}

  /* film grain */
  #grain{
    position:fixed;inset:-50%;z-index:1;pointer-events:none;
    opacity:0.04;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
    animation:grainShift 0.6s steps(3) infinite;
  }
  @keyframes grainShift{
    0%{transform:translate(0,0)}33%{transform:translate(-3%,2%)}66%{transform:translate(2%,-3%)}100%{transform:translate(0,0)}
  }

  #petals{position:fixed;inset:0;z-index:2;pointer-events:none}
  #confetti{position:fixed;inset:0;z-index:35;pointer-events:none}

  /* ───────── ENVELOPE SCENE ───────── */
  #scene{
    position:fixed;inset:0;z-index:10;
    display:flex;align-items:center;justify-content:center;
    flex-direction:column;
    transition:opacity 0.6s ease, transform 0.8s cubic-bezier(0.6,0,0.3,1);
  }
  #scene.gone{opacity:0;transform:scale(1.12);pointer-events:none}

  /* monogram above envelope */
  .pre-monogram{
    font-family:'Aref Ruqaa',serif;
    color:var(--gold-bright);
    font-size:15px;letter-spacing:3px;
    margin-bottom:26px;
    opacity:0;animation:fadeDown 1.2s ease 0.3s forwards;
    text-shadow:0 0 20px rgba(230,199,128,0.4);
  }
  @keyframes fadeDown{from{opacity:0;transform:translateY(-14px)}to{opacity:0.9;transform:translateY(0)}}

  #env-stage{
    position:relative;
    width:min(360px,84vw);
    perspective:1400px;
    cursor:pointer;
    animation:floatEnv 5s ease-in-out infinite;
  }
  @keyframes floatEnv{
    0%,100%{transform:translateY(0)}
    50%{transform:translateY(-12px)}
  }
  #env-stage:active{transition:transform .2s;transform:scale(.96)}

  /* glow ring behind envelope */
  .env-glow{
    position:absolute;inset:-14%;
    background:radial-gradient(circle, rgba(230,199,128,0.35) 0%, transparent 65%);
    filter:blur(20px);
    animation:glowPulse 4s ease-in-out infinite;
    z-index:-1;
  }
  @keyframes glowPulse{
    0%,100%{opacity:.5;transform:scale(1)}
    50%{opacity:.95;transform:scale(1.08)}
  }

  .envelope{
    position:relative;width:100%;padding-top:66%;
    transform-style:preserve-3d;
  }

  /* the pocket (back + sides) */
  .env-pocket{
    position:absolute;inset:0;
    background:
      linear-gradient(150deg,#f6e9cd 0%,#e3cd9e 45%,#cdaf74 100%);
    border-radius:6px 6px 14px 14px;
    box-shadow:
      0 30px 70px -12px rgba(0,0,0,0.7),
      0 8px 22px rgba(0,0,0,0.4),
      inset 0 2px 0 rgba(255,255,255,0.35);
  }
  /* paper texture lines on pocket */
  .env-pocket::after{
    content:'';position:absolute;inset:0;border-radius:6px 6px 14px 14px;
    background:repeating-linear-gradient(115deg,transparent 0 7px,rgba(154,120,56,0.05) 7px 8px);
  }

  /* side triangles */
  .env-side{position:absolute;bottom:0;height:50%;width:50%}
  .env-side.l{left:0;background:linear-gradient(135deg,#d9bd84,#c2a266);clip-path:polygon(0 100%,100% 0,0 0)}
  .env-side.r{right:0;background:linear-gradient(225deg,#d9bd84,#c2a266);clip-path:polygon(100% 100%,0 0,100% 0)}
  .env-front-tri{
    position:absolute;bottom:0;left:0;right:0;height:54%;
    background:linear-gradient(180deg,#e9d3a2 0%,#d4b577 100%);
    clip-path:polygon(0 0,50% 92%,100% 0);
    z-index:6;
    box-shadow:0 -2px 8px rgba(0,0,0,0.12) inset;
  }
  .env-front-tri::after{
    content:'';position:absolute;inset:0;
    clip-path:polygon(0 0,50% 92%,100% 0);
    background:linear-gradient(180deg,rgba(255,255,255,0.25),transparent 40%);
  }

  /* the flap that opens */
  .env-flap{
    position:absolute;top:0;left:0;right:0;height:56%;
    transform-origin:top center;
    transform-style:preserve-3d;
    transition:transform 1.1s cubic-bezier(0.7,-0.15,0.25,1);
    z-index:8;
  }
  .env-flap.open{transform:rotateX(-178deg);z-index:1}
  .flap-face{
    position:absolute;inset:0;
    clip-path:polygon(0 0,50% 100%,100% 0);
    backface-visibility:hidden;
  }
  .flap-out{
    background:linear-gradient(170deg,#f1ddb0 0%,#dbbf85 55%,#c8a86c 100%);
    box-shadow:0 4px 10px rgba(0,0,0,0.15);
  }
  .flap-out::after{
    content:'';position:absolute;inset:0;
    clip-path:polygon(0 0,50% 100%,100% 0);
    background:linear-gradient(170deg,rgba(255,255,255,0.4),transparent 45%);
  }
  .flap-in{
    background:linear-gradient(170deg,#c9a86a,#b08f50);
    transform:rotateX(180deg);
  }
  /* gold edge trim on flap */
  .flap-trim{
    position:absolute;top:0;left:0;right:0;height:56%;
    z-index:9;pointer-events:none;
    transform-origin:top center;
    transition:transform 1.1s cubic-bezier(0.7,-0.15,0.25,1);
  }
  .flap-trim.open{transform:rotateX(-178deg);opacity:0}
  .flap-trim svg{width:100%;height:100%;display:block}

  /* wax seal */
  .seal{
    position:absolute;left:50%;top:46%;
    width:64px;height:64px;
    transform:translate(-50%,-50%);
    z-index:12;
    transition:opacity .5s ease, transform .5s ease;
  }
  .seal.gone{opacity:0;transform:translate(-50%,-50%) scale(0) rotate(40deg)}
  .seal-disc{
    width:100%;height:100%;border-radius:50%;
    background:
      radial-gradient(circle at 38% 32%, #c14b52 0%, #9a2f37 55%, #6e1e26 100%);
    box-shadow:
      0 4px 14px rgba(0,0,0,0.55),
      inset 0 2px 6px rgba(255,255,255,0.25),
      inset 0 -4px 8px rgba(0,0,0,0.4);
    display:flex;align-items:center;justify-content:center;
    position:relative;
  }
  .seal-disc::before{
    content:'';position:absolute;inset:5px;border-radius:50%;
    border:1.5px dashed rgba(255,255,255,0.35);
  }
  .seal-letter{
    font-family:'Aref Ruqaa',serif;
    font-size:30px;color:#f5d9bb;
    text-shadow:0 1px 2px rgba(0,0,0,0.5);
  }

  /* tap hint */
  .tap-hint{
    margin-top:46px;
    display:flex;flex-direction:column;align-items:center;gap:8px;
    opacity:0;animation:fadeUp 1.2s ease 1s forwards;
  }
  .tap-hint .txt{
    font-family:'Reem Kufi',sans-serif;
    color:var(--gold-bright);
    font-size:14px;letter-spacing:2px;
    animation:breathe 2.4s ease-in-out infinite;
  }
  .tap-hint .finger{font-size:22px;animation:tapBob 1.6s ease-in-out infinite}
  @keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
  @keyframes breathe{0%,100%{opacity:.55}50%{opacity:1}}
  @keyframes tapBob{0%,100%{transform:translateY(0)}50%{transform:translateY(7px)}}

  /* the letter peeking out as flap opens */
  .env-letter-peek{
    position:absolute;left:6%;right:6%;top:8%;
    height:78%;
    background:linear-gradient(170deg,#fffdf7,#f3e7cf);
    border-radius:4px;
    z-index:5;
    transform:translateY(0);
    transition:transform 1s cubic-bezier(0.5,0,0.2,1) .35s;
    box-shadow:0 -4px 12px rgba(0,0,0,0.12);
    display:flex;align-items:center;justify-content:center;
  }
  .env-letter-peek.rise{transform:translateY(-58%)}
  .peek-deco{
    font-family:'Aref Ruqaa',serif;color:var(--gold-deep);
    font-size:26px;opacity:.5;
  }

  /* ───────── THE CARD / LETTER ───────── */
  #card-wrap{
    position:fixed;inset:0;z-index:30;
    display:flex;align-items:center;justify-content:center;
    padding:18px;
    pointer-events:none;opacity:0;
    transition:opacity .8s ease;
  }
  #card-wrap.show{opacity:1;pointer-events:auto}

  .card{
    position:relative;
    width:min(440px,94vw);
    max-height:94vh;overflow-y:auto;overflow-x:hidden;
    background:
      linear-gradient(170deg,#fdfaf2 0%,#f7eed8 100%);
    border-radius:22px;
    padding:0;
    box-shadow:
      0 40px 100px -20px rgba(0,0,0,0.75),
      0 0 0 1px rgba(191,155,90,0.5),
      0 0 0 9px rgba(253,249,239,0.06),
      0 0 0 10px rgba(191,155,90,0.18);
    transform:translateY(80px) scale(0.85) rotateX(12deg);
    opacity:0;
    transition:transform 1s cubic-bezier(0.34,1.4,0.5,1), opacity .7s ease;
    scrollbar-width:none;
  }
  .card::-webkit-scrollbar{display:none}
  #card-wrap.show .card{transform:translateY(0) scale(1) rotateX(0);opacity:1}

  /* ornate corner frames */
  .corner{position:absolute;width:54px;height:54px;z-index:4;opacity:.85}
  .corner svg{width:100%;height:100%}
  .corner.tl{top:10px;left:10px}
  .corner.tr{top:10px;right:10px;transform:scaleX(-1)}
  .corner.bl{bottom:10px;left:10px;transform:scaleY(-1)}
  .corner.br{bottom:10px;right:10px;transform:scale(-1,-1)}

  .card-inner{padding:40px 30px 38px}

  /* — header crest — */
  .crest{
    display:flex;flex-direction:column;align-items:center;
    margin-bottom:6px;
  }
  .crest-line{
    display:flex;align-items:center;gap:12px;
    width:100%;justify-content:center;
  }
  .crest-line .rule{
    height:1px;flex:1;max-width:70px;
    background:linear-gradient(90deg,transparent,var(--gold));
  }
  .crest-line .rule.flip{background:linear-gradient(270deg,transparent,var(--gold))}
  .crest-diamond{
    width:9px;height:9px;
    background:var(--gold);transform:rotate(45deg);
    box-shadow:0 0 8px rgba(191,155,90,0.6);
  }

  .basmala{
    font-family:'Amiri',serif;
    font-size:13px;color:var(--sage-deep);
    margin:14px 0 4px;letter-spacing:.5px;
  }

  .verse{
    font-family:'Amiri',serif;
    font-size:16px;color:var(--sage-deep);
    line-height:1.9;font-weight:700;
    margin:6px 0 4px;
    text-shadow:0 1px 0 rgba(255,255,255,0.6);
  }
  .verse-src{
    font-family:'Reem Kufi',sans-serif;
    font-size:10px;color:var(--gold-deep);
    letter-spacing:1px;opacity:.7;margin-bottom:18px;
  }

  /* — names — */
  .names-block{margin:10px 0 6px;position:relative}
  .names{
    font-family:'Aref Ruqaa',serif;
    font-size:clamp(40px,12vw,60px);
    color:var(--sage-deep);
    line-height:1.15;
    display:flex;align-items:center;justify-content:center;
    gap:4px;flex-wrap:nowrap;
    text-shadow:0 2px 4px rgba(124,143,111,0.2);
  }
  .names .nm{position:relative}
  .names .conj{
    font-family:'Amiri',serif;
    font-size:.5em;color:var(--gold-deep);
    margin:0 2px;
    align-self:center;
  }
  /* heart between names */
  .names .heartlet{
    font-size:.4em;color:var(--rose);
    margin:0 4px;animation:heartThrob 1.6s ease-in-out infinite;
  }
  @keyframes heartThrob{0%,100%{transform:scale(1)}50%{transform:scale(1.25)}}

  /* — date ribbon — */
  .date-ribbon{
    display:inline-flex;align-items:center;gap:10px;
    margin:14px 0 2px;
    padding:7px 22px;
    background:linear-gradient(135deg,var(--sage),var(--sage-deep));
    border-radius:30px;
    box-shadow:0 6px 16px -4px rgba(92,110,80,0.5),inset 0 1px 0 rgba(255,255,255,0.2);
  }
  .date-ribbon .d{
    font-family:'Reem Kufi',sans-serif;
    color:#f7eed8;font-size:14px;letter-spacing:1px;font-weight:600;
  }
  .date-ribbon .star{color:var(--gold-bright);font-size:11px}

  /* — photo — */
  .photo-frame{
    position:relative;
    margin:22px auto 8px;
    width:100%;
    border-radius:14px;
    padding:7px;
    background:linear-gradient(145deg,var(--gold-bright),var(--gold-deep));
    box-shadow:0 14px 32px -10px rgba(0,0,0,0.45);
  }
  .photo-frame img{
    display:block;width:100%;
    border-radius:9px;
    aspect-ratio:3/3.6;
    object-fit:cover;object-position:center 22%;
  }
  .photo-frame .shine{
    position:absolute;inset:7px;border-radius:9px;
    background:linear-gradient(135deg,rgba(255,255,255,0.45) 0%,transparent 35%);
    pointer-events:none;
  }

  /* — greeting — */
  .mubarak{
    font-family:'Aref Ruqaa',serif;
    font-size:clamp(30px,9vw,42px);
    color:var(--rose);
    margin:24px 0 6px;
    text-shadow:0 2px 6px rgba(217,154,138,0.35);
  }
  .greet-lead{
    font-family:'Amiri',serif;
    font-size:18px;color:var(--ink);
    line-height:1.8;margin-bottom:6px;font-weight:700;
  }
  .greet-body{
    font-family:'Reem Kufi',sans-serif;
    font-size:14.5px;color:#5a4c38;
    line-height:2.05;margin:10px 0 4px;
    font-weight:400;
  }

  /* — dua box — */
  .dua{
    position:relative;
    margin:20px 4px;
    padding:22px 22px 20px;
    background:
      linear-gradient(160deg,rgba(243,231,207,0.9),rgba(250,243,230,0.95));
    border-radius:14px;
    border:1px solid rgba(191,155,90,0.45);
    box-shadow:inset 0 1px 0 rgba(255,255,255,0.7);
  }
  .dua::before,.dua::after{
    content:'❁';
    position:absolute;font-size:15px;color:var(--gold);
    opacity:.8;
  }
  .dua::before{top:-9px;right:18px;background:var(--paper);padding:0 4px}
  .dua::after{bottom:-9px;left:18px;background:var(--paper);padding:0 4px}
  .dua-text{
    font-family:'Amiri',serif;
    font-size:18px;color:var(--sage-deep);
    line-height:2;font-weight:700;
  }

  /* — divider with ornament — */
  .ornament-div{
    display:flex;align-items:center;justify-content:center;
    gap:10px;margin:20px 0 14px;color:var(--gold);
  }
  .ornament-div .rule{height:1px;width:48px;background:linear-gradient(90deg,transparent,var(--gold))}
  .ornament-div .rule.flip{background:linear-gradient(270deg,transparent,var(--gold))}
  .ornament-div .mid{font-size:16px;letter-spacing:4px}

  /* — signature — */
  .sig-from{
    font-family:'Reem Kufi',sans-serif;
    font-size:13px;color:#9a8460;letter-spacing:.5px;
  }
  .sig-name{
    font-family:'Aref Ruqaa',serif;
    font-size:22px;color:var(--gold-deep);
    margin-top:4px;
    text-shadow:0 1px 2px rgba(154,120,56,0.2);
  }

  .blossoms{
    margin-top:18px;font-size:22px;letter-spacing:8px;
  }
  .blossoms span{display:inline-block;animation:bob 2.4s ease-in-out infinite}
  .blossoms span:nth-child(2){animation-delay:.3s}
  .blossoms span:nth-child(3){animation-delay:.6s}
  .blossoms span:nth-child(4){animation-delay:.9s}
  .blossoms span:nth-child(5){animation-delay:1.2s}
  @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}

  /* reveal stagger */
  .rv{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s cubic-bezier(0.2,0.8,0.3,1)}
  .rv.in{opacity:1;transform:translateY(0)}

  /* replay button */
  #replay{
    position:fixed;top:16px;left:16px;z-index:50;
    display:none;align-items:center;gap:6px;
    padding:8px 16px;
    background:rgba(43,34,24,0.55);
    backdrop-filter:blur(10px);
    border:1px solid rgba(191,155,90,0.5);
    border-radius:30px;
    color:var(--gold-bright);
    font-family:'Reem Kufi',sans-serif;
    font-size:13px;cursor:pointer;
    transition:background .25s,transform .15s;
  }
  #replay:hover{background:rgba(43,34,24,0.8)}
  #replay:active{transform:scale(.93)}

  /* music toggle */
  #music{
    position:fixed;top:16px;right:16px;z-index:50;
    width:40px;height:40px;border-radius:50%;
    background:rgba(43,34,24,0.55);
    backdrop-filter:blur(10px);
    border:1px solid rgba(191,155,90,0.5);
    color:var(--gold-bright);
    font-size:16px;cursor:pointer;
    display:flex;align-items:center;justify-content:center;
    transition:background .25s,transform .15s;
  }
  #music:active{transform:scale(.9)}

  /* opening flash */
  #flash{
    position:fixed;inset:0;z-index:40;pointer-events:none;
    background:radial-gradient(circle at 50% 50%,rgba(255,245,220,0.9),transparent 60%);
    opacity:0;
  }
  #flash.fire{animation:flashAnim 1s ease-out forwards}
  @keyframes flashAnim{0%{opacity:0}15%{opacity:1}100%{opacity:0}}
</style>
</head>
<body>

<div id="bg"></div>
<div id="aura"></div>
<div id="grain"></div>
<canvas id="petals"></canvas>

<!-- ENVELOPE SCENE -->
<div id="scene">
  <div class="pre-monogram">۞ رسالة من القلب ۞</div>

  <div id="env-stage">
    <div class="env-glow"></div>
    <div class="envelope">
      <div class="env-pocket"></div>

      <!-- letter rising out -->
      <div class="env-letter-peek" id="peek">
        <div class="peek-deco">❦</div>
      </div>

      <div class="env-side l"></div>
      <div class="env-side r"></div>
      <div class="env-front-tri"></div>

      <!-- flap -->
      <div class="env-flap" id="flap">
        <div class="flap-face flap-out"></div>
        <div class="flap-face flap-in"></div>
      </div>
      <!-- decorative trim drawn over flap -->
      <div class="flap-trim" id="trim">
        <svg viewBox="0 0 360 200" preserveAspectRatio="none">
          <defs>
            <clipPath id="fc"><polygon points="0,0 180,184 360,0"/></clipPath>
          </defs>
          <g clip-path="url(#fc)" fill="none" stroke="#9a7838" stroke-width="1.4" opacity="0.55">
            <polyline points="14,8 180,168 346,8"/>
            <polyline points="30,8 180,150 330,8"/>
            <circle cx="180" cy="40" r="6"/>
            <path d="M180 46 q-14 14 0 28 q14 -14 0 -28"/>
            <path d="M150 20 q12 8 0 20 M210 20 q-12 8 0 20"/>
          </g>
        </svg>
      </div>

      <!-- wax seal -->
      <div class="seal" id="seal">
        <div class="seal-disc"><span class="seal-letter">ع</span></div>
      </div>
    </div>
  </div>

  <div class="tap-hint" id="hint">
    <span class="finger">☝︎</span>
    <span class="txt">إضغطي لفتح الرسالة</span>
  </div>
</div>

<div id="flash"></div>
<canvas id="confetti"></canvas>

<!-- THE CARD -->
<div id="card-wrap">
  <div class="card" id="card">
    <div class="corner tl"><svg viewBox="0 0 60 60" fill="none" stroke="#bf9b5a" stroke-width="1.3"><path d="M6 54 V18 Q6 6 18 6 H54"/><path d="M14 54 V24 Q14 14 24 14 H54"/><circle cx="18" cy="18" r="3.5" fill="#bf9b5a" stroke="none"/><path d="M6 30 Q14 30 14 38" /></svg></div>
    <div class="corner tr"><svg viewBox="0 0 60 60" fill="none" stroke="#bf9b5a" stroke-width="1.3"><path d="M6 54 V18 Q6 6 18 6 H54"/><path d="M14 54 V24 Q14 14 24 14 H54"/><circle cx="18" cy="18" r="3.5" fill="#bf9b5a" stroke="none"/><path d="M6 30 Q14 30 14 38" /></svg></div>
    <div class="corner bl"><svg viewBox="0 0 60 60" fill="none" stroke="#bf9b5a" stroke-width="1.3"><path d="M6 54 V18 Q6 6 18 6 H54"/><path d="M14 54 V24 Q14 14 24 14 H54"/><circle cx="18" cy="18" r="3.5" fill="#bf9b5a" stroke="none"/><path d="M6 30 Q14 30 14 38" /></svg></div>
    <div class="corner br"><svg viewBox="0 0 60 60" fill="none" stroke="#bf9b5a" stroke-width="1.3"><path d="M6 54 V18 Q6 6 18 6 H54"/><path d="M14 54 V24 Q14 14 24 14 H54"/><circle cx="18" cy="18" r="3.5" fill="#bf9b5a" stroke="none"/><path d="M6 30 Q14 30 14 38" /></svg></div>

    <div class="card-inner">

      <div class="crest rv">
        <div class="crest-line">
          <span class="rule"></span>
          <span class="crest-diamond"></span>
          <span class="rule flip"></span>
        </div>
        <div class="basmala">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
      </div>

      <div class="verse rv">هُنَّ لِبَاسٌ لَكُمْ وَأَنْتُمْ لِبَاسٌ لَهُنَّ</div>
      <div class="verse-src">۞ سورة البقرة ۞</div>

      <div class="names-block rv">
        <div class="names">
          <span class="nm">رَوان</span>
          <span class="heartlet">❤</span>
          <span class="nm">عبّاس</span>
        </div>
      </div>

      <div class="rv">
        <div class="date-ribbon">
          <span class="star">✦</span>
          <span class="d">٢٦ مايو ٢٠٢٦</span>
          <span class="star">✦</span>
        </div>
      </div>

      <div class="photo-frame rv">
        <img id="poster" alt="عبّاس و رَوان">
        <div class="shine"></div>
      </div>

      <div class="mubarak rv">مَبْرُوك الخُطُوبَة</div>

      <div class="greet-lead rv">يا رَوان الغالية… يا أحلى عَروسة 🌷</div>

      <div class="greet-body rv">
        من كل قلبنا منهنّيكي بهالخطوة الحلوة،<br>
        وان شاء الله ما تشوفي إلا كل خير وفرح.<br>
        بداية حلوة لقصة عمر مليانة محبة ✨
      </div>

      <div class="dua rv">
        <div class="dua-text">
          بَارَكَ اللَّهُ لَكُمَا وَبَارَكَ عَلَيْكُمَا<br>
          وَجَمَعَ بَيْنَكُمَا فِي خَيْرٍ
        </div>
      </div>

      <div class="greet-body rv">
        ربّنا يكمّل لكم على خير وبركة،<br>
        ويرزقكم حياة مليانة مودّة ورحمة 💛<br>
        ويخليكم لبعض ويسعد قلبكم دايماً 🤍
      </div>

      <div class="ornament-div rv">
        <span class="rule"></span>
        <span class="mid">❦</span>
        <span class="rule flip"></span>
      </div>

      <div class="rv">
        <div class="sig-from">بكل المحبة،</div>
        <div class="sig-name">عيلتكِ الّي بتحبّك 🌺</div>
      </div>

      <div class="blossoms rv">
        <span>🌸</span><span>💛</span><span>🤍</span><span>💛</span><span>🌸</span>
      </div>

    </div>
  </div>
</div>

<button id="replay">↻ إعادة</button>
<button id="music">♪</button>

<script>
const POSTER_SRC = 'data:image/jpeg;base64,'''

html_part2 = r'''';
document.getElementById('poster').src = POSTER_SRC;

/* ══════════ AMBIENT PETALS ══════════ */
const pC = document.getElementById('petals');
const pX = pC.getContext('2d');
let PW,PH;
function pResize(){PW=pC.width=innerWidth;PH=pC.height=innerHeight}
pResize();addEventListener('resize',pResize);

const PETAL_COLORS=['#f0d3c8','#e6c780','#f5e3c4','#d99a8a','#fbe9d0','#cdb98a'];
let petals=[];
function makePetal(){
  return{
    x:Math.random()*PW, y:-30-Math.random()*PH*0.3,
    w:7+Math.random()*11, h:9+Math.random()*13,
    vy:0.5+Math.random()*1.1,
    vx:(Math.random()-0.5)*0.7,
    rot:Math.random()*Math.PI*2,
    vr:(Math.random()-0.5)*0.035,
    sway:Math.random()*Math.PI*2,
    swaySpd:0.012+Math.random()*0.022,
    swayAmp:0.4+Math.random()*1.1,
    color:PETAL_COLORS[(Math.random()*PETAL_COLORS.length)|0],
    opacity:0.45+Math.random()*0.45,
    flip:Math.random()*Math.PI*2,
    flipSpd:0.02+Math.random()*0.03
  };
}
for(let i=0;i<26;i++){let p=makePetal();p.y=Math.random()*PH;petals.push(p)}

function drawPetal(p){
  pX.save();
  pX.translate(p.x,p.y);
  pX.rotate(p.rot);
  pX.scale(1,Math.abs(Math.sin(p.flip))*0.85+0.35);
  pX.globalAlpha=p.opacity;
  /* soft petal shape */
  pX.beginPath();
  pX.moveTo(0,-p.h/2);
  pX.bezierCurveTo(p.w/2,-p.h/2, p.w/2,p.h/3, 0,p.h/2);
  pX.bezierCurveTo(-p.w/2,p.h/3, -p.w/2,-p.h/2, 0,-p.h/2);
  let g=pX.createLinearGradient(0,-p.h/2,0,p.h/2);
  g.addColorStop(0,p.color);
  g.addColorStop(1,'rgba(255,255,255,0.3)');
  pX.fillStyle=g;
  pX.shadowColor='rgba(191,155,90,0.3)';
  pX.shadowBlur=4;
  pX.fill();
  pX.restore();
}

/* ══════════ CONFETTI BURST ══════════ */
const cC=document.getElementById('confetti');
const cX=cC.getContext('2d');
function cResize(){cC.width=innerWidth;cC.height=innerHeight}
cResize();addEventListener('resize',cResize);
let confetti=[];
const HEARTS=['❤','💛','🤍','🌸','🌹','✨','🌷','💐','🌺'];
function fireConfetti(n){
  for(let i=0;i<n;i++){
    setTimeout(()=>{
      const fromSide=Math.random()>0.5;
      confetti.push({
        x:fromSide?(Math.random()>0.5?0:cC.width):Math.random()*cC.width,
        y:fromSide?cC.height*0.5+Math.random()*200:cC.height+20,
        vx:(Math.random()-0.5)*9,
        vy:-(7+Math.random()*9),
        g:0.18+Math.random()*0.12,
        size:14+Math.random()*20,
        rot:Math.random()*6,
        vr:(Math.random()-0.5)*0.3,
        char:HEARTS[(Math.random()*HEARTS.length)|0],
        life:1, decay:0.006+Math.random()*0.006
      });
    }, i*14);
  }
}

let opened=false;
function loop(){
  requestAnimationFrame(loop);
  /* petals */
  pX.clearRect(0,0,PW,PH);
  const spawnCap=opened?40:26;
  if(petals.length<spawnCap && Math.random()<(opened?0.4:0.12)) petals.push(makePetal());
  petals.forEach(p=>{
    p.sway+=p.swaySpd;
    p.flip+=p.flipSpd;
    p.x+=p.vx+Math.sin(p.sway)*p.swayAmp;
    p.y+=p.vy;
    p.rot+=p.vr;
    drawPetal(p);
  });
  petals=petals.filter(p=>p.y<PH+40);

  /* confetti */
  cX.clearRect(0,0,cC.width,cC.height);
  confetti.forEach(c=>{
    c.vy+=c.g; c.x+=c.vx; c.y+=c.vy; c.rot+=c.vr; c.life-=c.decay;
    cX.save();
    cX.globalAlpha=Math.max(0,c.life);
    cX.translate(c.x,c.y);
    cX.rotate(c.rot);
    cX.font=c.size+'px serif';
    cX.textAlign='center';cX.textBaseline='middle';
    cX.fillText(c.char,0,0);
    cX.restore();
  });
  confetti=confetti.filter(c=>c.life>0 && c.y<cC.height+60);
}
loop();

/* ══════════ INTERACTION ══════════ */
const scene=document.getElementById('scene');
const flap=document.getElementById('flap');
const trim=document.getElementById('trim');
const seal=document.getElementById('seal');
const peek=document.getElementById('peek');
const hint=document.getElementById('hint');
const cardWrap=document.getElementById('card-wrap');
const replay=document.getElementById('replay');
const flash=document.getElementById('flash');
const envStage=document.getElementById('env-stage');

function openEnvelope(){
  if(opened) return;
  opened=true;
  hint.style.transition='opacity .4s';
  hint.style.opacity='0';

  /* seal pops off */
  seal.classList.add('gone');

  /* flap opens */
  setTimeout(()=>{
    flap.classList.add('open');
    trim.classList.add('open');
  },180);

  /* letter rises */
  setTimeout(()=>{ peek.classList.add('rise'); },650);

  /* flash + scene leaves */
  setTimeout(()=>{
    flash.classList.add('fire');
    scene.classList.add('gone');
  },1150);

  /* card appears + confetti */
  setTimeout(()=>{
    cardWrap.classList.add('show');
    fireConfetti(70);
    replay.style.display='flex';
    /* stagger reveal */
    const items=document.querySelectorAll('.rv');
    items.forEach((el,i)=>{
      setTimeout(()=>el.classList.add('in'), 250+i*140);
    });
  },1500);

  /* second confetti wave */
  setTimeout(()=>fireConfetti(40),2600);
}

envStage.addEventListener('click',openEnvelope);
seal.addEventListener('click',openEnvelope);
scene.addEventListener('click',e=>{ if(e.target===scene) openEnvelope(); });

/* replay */
replay.addEventListener('click',()=>{
  opened=false;
  cardWrap.classList.remove('show');
  document.querySelectorAll('.rv').forEach(el=>el.classList.remove('in'));
  replay.style.display='none';
  flap.classList.remove('open');
  trim.classList.remove('open');
  seal.classList.remove('gone');
  peek.classList.remove('rise');
  flash.classList.remove('fire');
  scene.classList.remove('gone');
  hint.style.opacity='';
  hint.style.transition='';
});

/* ══════════ MUSIC (gentle chime) ══════════ */
const musicBtn=document.getElementById('music');
let audioCtx=null, musicOn=false, musicTimer=null;
const MELODY=[523.25,587.33,659.25,783.99,659.25,587.33,523.25,440.00];
let noteIdx=0;
function playNote(){
  if(!audioCtx) return;
  const o=audioCtx.createOscillator();
  const g=audioCtx.createGain();
  o.type='sine';
  o.frequency.value=MELODY[noteIdx%MELODY.length];
  noteIdx++;
  g.gain.setValueAtTime(0,audioCtx.currentTime);
  g.gain.linearRampToValueAtTime(0.13,audioCtx.currentTime+0.08);
  g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+1.4);
  o.connect(g);g.connect(audioCtx.destination);
  o.start();o.stop(audioCtx.currentTime+1.5);
}
function toggleMusic(){
  if(!audioCtx) audioCtx=new (window.AudioContext||window.webkitAudioContext)();
  musicOn=!musicOn;
  if(musicOn){
    musicBtn.textContent='♫';
    playNote();
    musicTimer=setInterval(playNote,900);
  }else{
    musicBtn.textContent='♪';
    clearInterval(musicTimer);
  }
}
musicBtn.addEventListener('click',toggleMusic);
</script>
</body>
</html>'''

full = html_part1 + img_b64 + html_part2

with open('/mnt/user-data/outputs/engagement.html','w',encoding='utf-8') as f:
    f.write(full)

print(f"Done — {len(full):,} bytes")
PYEOF