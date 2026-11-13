#!/usr/bin/env python3
"""Builds the Tockbee site: every page shares one head, dock and footer.
Run from the repo root:  python3 tools/build.py   (edit this file, never the generated *.html)
Facts come from the owner's sources only: dotxline.com/tockbee.html, Wages App/PLAN.md,
Wages App/tockbee/docs/app-store.md and Wages App/design/brand-guidelines.md."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://tockbee.dotxline.com/'
APPLE = '<svg class="apple" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.5 2-3.6-1.1-1.6-2.8-1.8-3.4-1.8-1.4-.1-2.8.9-3.5.9s-1.8-.9-3-.8c-1.5 0-3 .9-3.8 2.3-1.6 2.8-.4 7 1.2 9.3.8 1.1 1.7 2.4 2.9 2.3 1.2 0 1.6-.7 3-.7s1.8.7 3 .7c1.3 0 2.1-1.1 2.8-2.3.9-1.3 1.3-2.6 1.3-2.6s-2.5-1-2.5-3.7zM14.1 5.6c.6-.8 1.1-1.9 1-3-.9 0-2.1.6-2.7 1.4-.6.7-1.1 1.8-1 2.9 1 .1 2.1-.5 2.7-1.3z"/></svg>'
NAV = [('index.html', 'Overview'), ('how-it-works.html', 'How it works'), ('pay.html', 'Pay'), ('your-record.html', 'Your record'), ('support.html', 'Support')]
# the mark, as one inline symbol: ring (coral), hand (cocoa, cream on dark), tip (sunshine)
MARK = '<svg class="tb-mark" viewBox="10 10 80 80" aria-hidden="true"><path class="m-ring" pathLength="1" d="M50 19 A31 31 0 1 1 49.99 19"/><g class="m-hand"><path d="M50 50 H81"/><circle class="m-tip" cx="81" cy="50" r="11"/></g></svg>'
I = lambda d: f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
ICON = {
 'pin': I('<path d="M12 21s7-6.2 7-11a7 7 0 0 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
 'undo': I('<path d="M9 14 4 9l5-5"/><path d="M4 9h10a6 6 0 0 1 0 12h-3"/>'),
 'phone': I('<rect x="7" y="2.5" width="10" height="19" rx="3"/><path d="M10.5 18.5h3"/>'),
 'cal': I('<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17"/>'),
 'wifi': I('<path d="M2.5 9a14 14 0 0 1 19 0M5.5 12.5a9.5 9.5 0 0 1 13 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/>'),
 'tap': I('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.5"/>'),
 'rates': I('<path d="M4 7h10M18 7h2M4 17h2M10 17h10"/><circle cx="16" cy="7" r="2"/><circle cx="8" cy="17" r="2"/>'),
 'card': I('<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M3 10h18M16 15h2"/>'),
 'sun': I('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'),
 'uc': I('<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M8 3v4M16 3v4M3.5 10h17M9 15l2 2 4-4"/>'),
 'check': I('<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 14l2 2 3-3"/>'),
 'doc': I('<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 13h6M9 17h6"/>'),
 'csv': I('<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M3.5 10h17M10 5v15"/>'),
 'lock': I('<rect x="5" y="11" width="14" height="10" rx="3"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>'),
}

HEAD = '''<!doctype html>
<html lang="en" data-type="software" data-radius="round" data-buttons="solid" data-motion>
<head>
<meta charset="utf-8">
<script>try{{var t=localStorage.getItem("tb-theme");if(t==="light"||t==="dark")document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{site}media/tockbee-preview.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<meta name="theme-color" content="#FFF8EE" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#140C09" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{site}{canon}">
<meta name="site-kind" content="software">
<meta name="page-type" content="software">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500..600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/system.css">
<link rel="stylesheet" href="assets/ui/cards.css">
<link rel="stylesheet" href="assets/motion/motion.css">
<link rel="stylesheet" href="assets/layout/layout.css">
<style>
:root {{
  --p-bg: #FFF8EE; --p-surface: #FFFFFF; --p-ink: #2A1712; --p-muted: #6B5248;
  --p-accent: #FF7A2F; --p-accent-ink: #2A1712; --p-action: #2A1712; --p-action-ink: #FFF6E8;
  --p-inv-bg: #2A1712; --p-inv-surface: #3A2219; --p-inv-ink: #FFF6E8; --p-inv-muted: #E1CCB8;
  --p-inv-accent: #FF7A2F; --p-inv-accent-ink: #2A1712; --p-inv-action: #FF7A2F; --p-inv-action-ink: #2A1712;
  --font-display: "Fredoka", ui-rounded, system-ui, sans-serif;
  --font-text: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, system-ui, sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  --display-weight: 600; --display-tracking: -0.01em; --display-tracking-xl: -0.02em;
  --ly-scale: 0.92;
}}
</style>
<link rel="stylesheet" href="assets/tb.css">
<script>document.documentElement.classList.add('m-enter','tb-js');setTimeout(()=>document.documentElement.classList.add('m-enter-done'),700)</script>
</head>'''

def dock(cur):
    links = ''.join(f'<a href="{h}"{" aria-current=page" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return f'''<header class="dock" data-root="">
  <div class="dock__bar">
    <a class="skip-link" href="#top">Skip to content</a>
    <a class="dock__home" href="https://dotxline.com/" aria-label="Back to dotXline"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg><span>dotXline</span></a>
    <a class="dock__logo" href="index.html"><img src="img/tockbee-icon-512.png" alt="">tockbee</a>
    <nav class="dock__links" id="dock-links" aria-label="Main">{links}</nav>
    <button class="icon-btn theme-btn" type="button" aria-label="Switch light and dark"><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></svg></button>
    <button class="icon-btn dock__menu" type="button" aria-expanded="false" aria-controls="dock-links" aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 8h16M4 16h16"/></svg></button>
    <a class="btn btn--primary" href="#get" data-appstore>{APPLE}<span class="lbl-long">Get&nbsp;</span>Tockbee</a>
  </div>
</header>'''

FOOTER = f'''<footer class="footer closing footer--dark ground-inverse" id="get" aria-labelledby="close-h">
  <div class="wrap">
    <div class="closing__cta close--word">
      <div class="section-head--split">
        <div><h2 id="close-h">Every hour you work, on the record</h2><p class="t-lead">Tockbee for iPhone. No account, no ads, no tracking.</p></div>
        <a class="btn btn--primary" href="#get" data-appstore>{APPLE}Get Tockbee</a>
      </div>
      <p class="close__word" aria-hidden="true">tockbee</p>
    </div>
    <div class="closing__links">
      <div class="grid">
        <div class="span-4 stack-4">
          <a class="dock__logo" href="index.html" style="color:inherit"><img src="img/tockbee-icon-512.png" alt="">tockbee</a>
          <p class="footer__lede">A shift and pay tracker for UK hourly and shift workers, made by dotXline LTD in Cardiff.</p>
        </div>
        <div class="span-2 start-7 footer__col"><h3>Tockbee</h3><ul><li><a href="index.html">Overview</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="pay.html">Pay</a></li><li><a href="your-record.html">Your record</a></li></ul></div>
        <div class="span-2 footer__col"><h3>Help</h3><ul><li><a href="support.html">Support</a></li><li><a href="privacy.html">Privacy policy</a></li><li><a href="mailto:hello@dotxline.com">hello@dotxline.com</a></li></ul></div>
        <div class="span-2 footer__col"><h3>dotXline</h3><ul><li><a href="https://dotxline.com/">Back to dotXline</a></li><li><a href="https://xpense.dotxline.com/">Xpense</a></li><li><a href="https://freshbit.dotxline.com/">FreshBit</a></li></ul></div>
      </div>
      <div class="footer__legal"><span>&copy; 2026 dotXline LTD</span><span>Tax figures are estimates. Your payslip is the official figure.</span></div>
    </div>
  </div>
</footer>
<script type="module" src="assets/system.js"></script>
<script type="module" src="assets/motion/motion.js"></script>
<script type="module" src="assets/layout/layout.js"></script>
<script src="assets/tb.js" defer></script>'''

def write(path, title, desc, body):
    html = HEAD.format(title=title, desc=desc, site=SITE, canon='' if path == 'index.html' else path) + f'''
<body data-page="{path[:-5]}">
{dock(path)}
<main id="top">
{body}</main>
{FOOTER}
</body>
</html>
'''
    (ROOT / path).write_text(html)
    print('built', path)

def page_head(label, h1, lead, side=''):
    side = side or f'<div class="span-4 start-9 tb-head-mark" aria-hidden="true">{MARK}</div>'
    return f'''  <section class="page-head" aria-labelledby="ph-h">
    <div class="wrap grid">
      <div class="span-7 stack-4">
        <p class="t-label tb-k">{MARK}{label}</p>
        <h1 id="ph-h" data-tb-tick>{h1}</h1>
        <p class="t-lead measure" data-tb-tick>{lead}</p>
      </div>
      {side}
    </div>
  </section>
'''

def cards(items):
    return '<ul>' + ''.join(f'<li data-tb-tick><span class="fi">{ICON[i]}</span><b>{b}</b><span>{t}</span></li>' for i, b, t in items) + '</ul>'

def shot(src, alt, cls=''):
    return f'<div class="tph {cls}"><img src="media/{src}.jpg" alt="{alt}" width="552" height="1200" loading="lazy" decoding="async"></div>'


SCREENS = f'''  <section class="section ground-surface" id="screens" aria-labelledby="screens-h">
    <div class="wrap">
      <div class="section-head"><h2 id="screens-h" data-tb-tick>Tockbee, screen by screen</h2><p class="t-lead measure" data-tb-tick>Real screens from the app. Today, Shifts, Pay, Payslip check and Export.</p></div>
      <div class="tb-screens">
        <figure data-tb-tick>{shot('today', 'Today: a running shift at Riverside Care Home and the Clock out button')}<h3>Today</h3><p>The running shift, the timer and the Clock button.</p></figure>
        <figure data-tb-tick>{shot('shifts', 'Shifts: every shift with its times, breaks and how it was recorded')}<h3>Shifts</h3><p>Times, breaks and how each shift was recorded.</p></figure>
        <figure data-tb-tick>{shot('pay', 'Pay: base pay, tax, National Insurance and estimated take-home')}<h3>Pay</h3><p>Gross, overtime and estimated take-home.</p></figure>
        <figure data-tb-tick>{shot('payslip', 'Payslip check: possibly underpaid by £12.71 compared with your log')}<h3>Payslip check</h3><p>What your payslip says against what you logged.</p></figure>
      </div>
    </div>
  </section>
'''

GROUPS = f'''  <section class="section" id="features" aria-labelledby="features-h">
    <div class="wrap">
      <div class="section-head"><h2 id="features-h" data-tb-tick>Everything Tockbee does</h2><p class="t-lead measure" data-tb-tick>Made for UK hourly, shift and gig workers. Plain words: rota, payslip, take-home.</p></div>
      <div class="tb-groups">
        <div class="tb-group" data-tb-tick><p class="tb-k">Clock</p><h3>It knows when you’re at work</h3>{cards([('pin', 'Automatic clock-in', 'By location at a work site, or by joining your work Wi-Fi.'), ('undo', 'Undo, every time', 'Each automatic clock-in sends a notification you can reverse.'), ('phone', 'Live Activity and widgets', 'For the Lock Screen, the Dynamic Island and the Home Screen.'), ('cal', 'Rota reminders', 'So a shift never starts unrecorded.')])}</div>
        <div class="tb-group" data-tb-tick><p class="tb-k">Pay</p><h3>What it should pay</h3>{cards([('rates', 'Rates and rules', 'Overtime, weekends, nights and unpaid breaks.'), ('card', 'Estimated take-home', 'After PAYE (including Scottish rates), National Insurance, student loan and pension.'), ('sun', 'Holiday accrual', 'At 12.07%, plus tips and business miles at HMRC rates.'), ('uc', 'Universal Credit periods', 'If your pay is assessed that way.')])}</div>
        <div class="tb-group" data-tb-tick><p class="tb-k">Record</p><h3>Your record, your call</h3>{cards([('check', 'Payslip check', 'Shows any hours or pay that went missing.'), ('doc', 'Timesheet pack', 'A PDF with every shift, how it was recorded and a record check, with a letter template and Acas guidance.'), ('csv', 'CSV export', 'For spreadsheets.'), ('lock', 'Face ID lock', 'Keeps it private on a shared phone.')])}</div>
      </div>
    </div>
  </section>
'''

FAQ_ITEMS = [('Do I need an account?', 'No. Open Tockbee and start. There is nothing to sign up for.'),
       ('Why does Tockbee ask for location “Always”?', 'Only to notice when you arrive at or leave a work site you created, so it can clock you in and out. There is no continuous tracking and your location never leaves your phone. You can use work Wi-Fi or the Clock button instead.'),
       ('Are the tax figures exact?', 'No. Take-home is an estimate after tax, National Insurance, student loan and pension. Your payslip is the official figure.'),
       ('Where is my data?', 'In the app’s own storage on your phone. Backups go only to a folder you pick, such as your own iCloud Drive.')]
def faq_section(n=4):
    items = ''.join(f'<div class="faq__item" data-tb-tick><h3>{q}</h3><p>{a}</p></div>' for q, a in FAQ_ITEMS[:n])
    return f'''  <section class="section ground-surface" id="questions" aria-labelledby="questions-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="questions-h" data-tb-tick>Questions about Tockbee</h2>
        <p class="t-lead measure" data-tb-tick>More answers on the <a class="link" href="support.html">support page</a>, or write to hello@dotxline.com.</p>
        <div class="tb-stats" data-tb-tick><div><b>£12.71</b><span>National Living Wage the app checks against</span></div><div><b>12.07%</b><span>holiday accrual</span></div></div>
      </div>
      <div class="span-7 start-6 faq">{items}</div>
    </div>
  </section>
'''

MORE = lambda here: ''

# ---------- home ----------
HERO = f'''  <section class="hero tb-hero" data-enter aria-labelledby="hero-h">
    <div class="wrap grid">
      <div class="span-6 tb-hero__text">
        <img class="hero__icon" src="img/tockbee-icon-512.png" alt="" width="72" height="72">
        <p class="t-label tb-k hero__fact">iPhone · UK hourly and shift workers · Data not collected</p>
        <h1 id="hero-h">Shift and pay tracker for UK workers</h1>
        <p class="t-lead measure">Tockbee keeps your own record of every hour you work, so you can check your payslip and sort out missing pay.</p>
        <div class="btn-row"><a class="btn btn--primary" href="#get" data-appstore>{APPLE}Get Tockbee</a><a class="btn btn--secondary" href="#story">What the logo means</a></div>
      </div>
      <div class="span-5 start-8 tb-hero__ph">
        <div class="tb-orbit" aria-hidden="true">{MARK}</div>
        <div class="tph"><video id="tb-hero" autoplay muted loop playsinline preload="metadata" poster="media/tockbee-preview.jpg" aria-label="Tockbee preview: the Today screen with a running shift and the Clock out button"><source src="media/tockbee-preview.mp4" type="video/mp4"></video></div>
      </div>
    </div>
  </section>
'''
FILM = '''  <section class="film" id="story" data-scroll-moment aria-label="What the Tockbee logo means">
    <div class="wrap film-pin">
      <div class="film-inner grid">
        <svg class="span-5" viewBox="10 10 80 80" aria-hidden="true">
          <path class="ghost-path" d="M50 19 A31 31 0 1 1 49.99 19"/><path class="ghost-path" d="M50 50 L71.92 28.08"/>
          <path class="draw ring" data-step="0" data-to=".9" pathLength="1" d="M50 19 A31 31 0 1 1 49.99 19"/>
          <g data-kind="rotate" data-step="1" data-from=".15" data-a0="90" data-a1="-45" data-cx="50" data-cy="50" transform="rotate(-45 50 50)"><path class="draw hand" data-step="1" data-to=".2" pathLength="1" d="M50 50 H81"/></g>
          <circle class="tip" data-kind="pop" data-step="2" data-to=".6" data-cx="71.92" data-cy="28.08" cx="71.92" cy="28.08" r="11"/>
        </svg>
        <div class="film-caps span-7 start-6">
          <div class="film-cap on"><p class="t-label tb-k">The ring</p><h2>Arrive. You’re clocked in.</h2><p>Tockbee clocks you in when you reach work, by location or by your work Wi-Fi. Every automatic clock-in comes with a notification and Undo.</p></div>
          <div class="film-cap"><p class="t-label tb-k">The hand</p><h2>Every minute counts.</h2><p>Overtime, weekend and night rates and unpaid breaks, worked out as you go. Then an estimated take-home after tax, National Insurance, student loan and pension.</p></div>
          <div class="film-cap"><p class="t-label tb-k">The tip</p><h2>Check it against your payslip.</h2><p>The yellow tip is the moment you clock in. Type in your payslip and Tockbee shows any hours or pay that went missing.</p></div>
        </div>
      </div>
      <p class="film-count" aria-hidden="true"><b data-film-n>1</b> / 3</p>
      <div class="film-rail" aria-hidden="true"><i class="on"></i><i></i><i></i></div>
      <div class="film-progress" aria-hidden="true"><i></i></div>
    </div>
  </section>
'''
TOUR = f'''  <section class="section" id="tour" aria-labelledby="tour-h">
    <div class="wrap">
      <div class="section-head"><h2 id="tour-h" data-tb-tick>Tockbee, page by page</h2><p class="t-lead measure" data-tb-tick>Made for UK hourly, shift and gig workers. Plain words: rota, payslip, take-home.</p></div>
      <div class="tb-tour">
        <a class="tb-tour__card" href="how-it-works.html" data-tb-tick>{shot('today', 'Today: a running shift at Riverside Care Home and the Clock out button')}<div><p class="tb-k">Clock</p><h3>How it works</h3><p>Clocks you in by location, work Wi-Fi or a tap.</p></div><span class="tb-go" aria-hidden="true">→</span></a>
        <a class="tb-tour__card" href="pay.html" data-tb-tick>{shot('pay', 'Pay: base pay, tax, National Insurance and estimated take-home')}<div><p class="tb-k">Pay</p><h3>What it should pay</h3><p>Rates, breaks and an estimated take-home.</p></div><span class="tb-go" aria-hidden="true">→</span></a>
        <a class="tb-tour__card" href="your-record.html" data-tb-tick>{shot('export', 'Export: a PDF timesheet or CSV spreadsheet for any dates')}<div><p class="tb-k">Record</p><h3>Your record</h3><p>A timesheet to share. Data not collected.</p></div><span class="tb-go" aria-hidden="true">→</span></a>
      </div>
    </div>
  </section>
'''
write('index.html', 'Tockbee: a shift and pay tracker for UK workers',
      'Tockbee clocks you in when you arrive, works out your pay and take-home, and gives you a timesheet to show your manager. No account, no ads, no tracking.',
      HERO + '\n' + FILM + '\n' + SCREENS + '\n' + GROUPS + '\n' + TOUR + '\n' + faq_section(4))

# ---------- how it works ----------
DEMO = '''<div class="tph app-demo" data-ui><div class="tph__screen tb-today" data-tb-today role="group" aria-label="Working demo of the Today screen. Tap Clock in.">
  <span class="wm">tockbee</span>
  <span class="pill"><i></i>On shift at Riverside Care Home</span>
  <span class="timer" data-timer aria-live="off">0:00:00</span>
  <span class="how" data-how>Not on shift</span>
  <button type="button" class="tb-clock" data-clock>Clock in</button>
  <div class="tb-week"><small>This week so far</small><b data-earned>£458.20</b><span>at £12.71 an hour</span></div>
  <p class="tb-toast" data-toast role="status" aria-live="polite"></p>
</div></div>'''
HOW = page_head('How it works', 'Tockbee clocks you in when you arrive',
    'By location at a work site, or by joining your work Wi-Fi. Every automatic clock-in sends a notification you can undo. The Clock button always works too.') + f'''
  <section class="section" id="clock" aria-labelledby="clock-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="clock-h" data-tb-tick>Three ways to clock in</h2>
        <div class="tb-group tb-group--flat">{cards([('pin', 'Location', 'Around work sites you create. No continuous tracking; your location never leaves your phone.'), ('wifi', 'Work Wi-Fi', 'For people who would rather not share location.'), ('tap', 'The Clock button', 'For the days you would rather tap. Try it on the right.')])}</div>
      </div>
      <div class="span-7 start-6 tb-center">{DEMO}</div>
    </div>
  </section>

  <section class="section ground-surface" id="today" aria-labelledby="today-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="today-h" data-tb-tick>Your shift, wherever you look</h2>
        <p class="t-lead measure" data-tb-tick>The running shift sits on your Lock Screen and in the Dynamic Island. Rota reminders mean a shift never starts unrecorded.</p>
        <div class="tb-group tb-group--flat">{cards([('undo', 'Undo, every time', 'Each automatic clock-in sends a notification you can reverse.'), ('phone', 'Live Activity and widgets', 'For the Lock Screen, the Dynamic Island and the Home Screen.'), ('cal', 'Rota reminders', 'So a shift never starts unrecorded.')])}</div>
      </div>
      <div class="span-7 start-6 tb-pair">{shot('sites', 'Sites: your work sites on a map')}{shot('shifts', 'Shifts: every shift with its times, breaks and how it was recorded', 'tph--lift')}</div>
    </div>
  </section>
'''
write('how-it-works.html', 'How it works: Tockbee', 'Tockbee clocks you in by location, work Wi-Fi or a tap, with a notification and Undo every time.', HOW + SCREENS + faq_section(4))

# ---------- pay ----------
RECEIPT = '''<div class="tb-receipt" data-ui role="img" aria-label="An itemised shift: base pay, overtime, then estimated take-home after tax, National Insurance and pension">
  <p class="tb-receipt__h">This week · Riverside Care Home</p>
  <div data-tb-row><span>Rate</span><b>£12.71 an hour</b></div>
  <div data-tb-row><span>Unpaid break</span><b>Not paid</b></div>
  <div data-tb-row><span>Overtime after 5 h</span><b>£15.89</b></div>
  <div data-tb-row class="sum"><span>Week total</span><b>£111.64</b></div>
  <p class="tb-receipt__note" data-tb-row>Estimated take-home after tax, National Insurance, student loan and pension is worked out for your pay period. Your payslip is the official figure.</p>
</div>'''
PAY = page_head('Pay', 'What your shifts should pay',
    'Overtime, weekend and night rates and unpaid breaks, worked out minute by minute. Then an estimated take-home for your pay period.') + f'''
  <section class="section" id="rates" aria-labelledby="rates-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="rates-h" data-tb-tick>Rates and rules, priced to the minute</h2>
        <div class="tb-group tb-group--flat">{cards([('rates', 'Rates and rules', 'Overtime, weekends, nights and unpaid breaks. Midnight, weekends and clock changes are exact.'), ('card', 'Estimated take-home', 'After PAYE (including Scottish rates), National Insurance, student loan and pension.'), ('sun', 'Holiday accrual', 'At 12.07%, plus tips and business miles at HMRC rates.'), ('uc', 'Universal Credit periods', 'If your pay is assessed that way.')])}</div>
      </div>
      <div class="span-7 start-6 tb-center">{RECEIPT}</div>
    </div>
  </section>

  <section class="section ground-surface" id="payslip" aria-labelledby="payslip-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="payslip-h" data-tb-tick>Payslip check: possibly underpaid? You’ll know</h2>
        <p class="t-lead measure" data-tb-tick>Copy in what your payslip says. Tockbee compares it with the shifts you logged for the same dates and shows the difference. Calm facts, never alarms.</p>
      </div>
      <div class="span-7 start-6 tb-pair">{shot('pay', 'Pay: this week and this pay period, before tax and after')}{shot('payslip', 'Payslip check: possibly underpaid by £12.71 compared with your log', 'tph--lift')}</div>
    </div>
  </section>
'''
write('pay.html', 'Pay: Tockbee', 'Overtime, weekend and night rates, unpaid breaks, an estimated take-home and a payslip check.', PAY + GROUPS + faq_section(3))

# ---------- your record ----------
RECORD = page_head('Your record', 'Your timesheet, ready to share',
    'A PDF or CSV with every shift and how it was recorded. Choose what goes in, then share it with your manager, keep it, or print it.') + f'''
  <section class="section" id="itemised" aria-labelledby="itemised-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="itemised-h" data-tb-tick>Your shift, itemised</h2>
        <p class="t-lead measure" data-tb-tick>Every shift, how it was recorded and what it should pay, laid out like a receipt you can check against your payslip.</p>
        <div class="tb-group tb-group--flat">{cards([('doc', 'Timesheet pack', 'A PDF with every shift, how it was recorded and a record check, with a letter template and Acas guidance.'), ('csv', 'CSV export', 'For spreadsheets.')])}</div>
      </div>
      <div class="span-7 start-6 tb-center"><div class="tph"><video autoplay muted loop playsinline preload="none" poster="media/tockbee-itemised.jpg" aria-label="Tockbee film: your shift, itemised"><source src="media/tockbee-itemised.mp4" type="video/mp4"></video></div></div>
    </div>
  </section>

  <section class="section ground-surface" id="private" aria-labelledby="private-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <p class="tb-label">{MARK}Data not collected</p>
        <h2 id="private-h" data-tb-tick>Everything stays on your phone</h2>
        <p class="t-lead measure" data-tb-tick>No account, no ads, no tracking. Tockbee doesn’t have a server to send your hours to.</p>
      </div>
      <div class="span-7 start-6 tb-points">
        <div data-tb-tick><b>No account</b><span>Open it and start. Nothing to sign up for.</span></div>
        <div data-tb-tick><b>No server</b><span>Your shifts and pay never leave your phone.</span></div>
        <div data-tb-tick><b>Your backups</b><span>Backups go only to a folder you pick, such as your own iCloud Drive.</span></div>
        <div data-tb-tick><b>Face ID lock</b><span>Keeps it private on a shared phone.</span></div>
      </div>
    </div>
  </section>
'''
write('your-record.html', 'Your record: Tockbee', 'A PDF timesheet or CSV for any dates. No account, no server: your shifts and pay stay on your phone.', RECORD + SCREENS + faq_section(4))

# ---------- support ----------
FAQ = [('Do I need an account?', 'No. Open Tockbee and start. There is nothing to sign up for.'),
       ('Why does Tockbee ask for location “Always”?', 'Only to notice when you arrive at or leave a work site you created, so it can clock you in and out. There is no continuous tracking and your location never leaves your phone. You can use work Wi-Fi or the Clock button instead.'),
       ('Are the tax figures exact?', 'No. Take-home is an estimate after tax, National Insurance, student loan and pension. Your payslip is the official figure.'),
       ('Where is my data?', 'In the app’s own storage on your phone. Backups go only to a folder you pick, such as your own iCloud Drive.'),
       ('Is there an Android version?', 'Tockbee is built for iPhone and Android from one codebase. Android is coming soon.')]
SUPPORT = page_head('Support', 'Tockbee support and questions',
    'Questions or ideas? Write to us. Include your iPhone model, iOS version and what happened.',
    '<div class="span-4 start-9 tb-contact" data-tb-tick><small>Email us</small><a class="link" href="mailto:hello@dotxline.com?subject=Tockbee%20support">hello@dotxline.com</a><p>dotXline LTD, Cardiff, United Kingdom</p></div>') + f'''
  <section class="section" id="faq" aria-labelledby="faq-h">
    <div class="wrap grid">
      <div class="span-5 stack-4">
        <h2 id="faq-h" data-tb-tick>Tockbee details</h2>
        <ul class="rows rows--spec"><li><span class="rows__name">Device</span><span class="rows__value">iPhone, iOS 26 and later</span></li><li><span class="rows__name">Made for</span><span class="rows__value">UK hourly and shift workers</span></li><li><span class="rows__name">Category</span><span class="rows__value">Finance</span></li><li><span class="rows__name">Privacy</span><span class="rows__value">Data not collected</span></li><li><span class="rows__name">Android</span><span class="rows__value">Coming soon</span></li></ul>
      </div>
      <div class="span-7 start-6 faq">{''.join(f'<div class="faq__item" data-tb-tick><h3>{q}</h3><p>{a}</p></div>' for q, a in FAQ)}</div>
    </div>
  </section>
'''
write('support.html', 'Support: Tockbee', 'Help for Tockbee: contact, location, tax estimates, your data and Android.', SUPPORT)

# ---------- privacy policy: from the App Store privacy label and review notes (docs/app-store.md) ----------
PRIV = '''<h1>Privacy Policy</h1><p class="meta">Tockbee is made by dotXline LTD. Last updated: 13 November 2026.</p>
<h2>Data not collected</h2><p>Tockbee has no account, no server, no analytics and no third-party tools that collect data. Your shifts, pay, work sites and settings stay in the app’s own storage on your phone.</p>
<h2>Location</h2><p>If you choose clock-in by location, Tockbee uses your phone’s region monitoring around the work sites you create, to clock you in and out. There is no continuous tracking, and your location is never sent off your phone. You can use your work Wi-Fi or the Clock button instead.</p>
<h2>Backups and exports</h2><p>Backups go only to a folder you pick, such as your own iCloud Drive. Timesheets you export (PDF or CSV) go wherever you choose to share or save them.</p>
<h2>This website</h2><p>This website does not use cookies, analytics or advertising trackers. If you email us, we keep your message to reply.</p>
<h2>Contact</h2><p>dotXline LTD, Cardiff, United Kingdom<br><a href="mailto:hello@dotxline.com">hello@dotxline.com</a></p>'''
write('privacy.html', 'Privacy policy: Tockbee', 'Tockbee collects no data: no account, no server, no analytics. Your shifts and pay stay on your phone.',
      f'  <section class="doc-main"><div class="wrap"><article class="doc">{PRIV}</article></div></section>\n')
