/* Tockbee site behaviour: the glass dock, the theme switch, the logo film, the tick-in motion and the
   working Clock demo. The kit's system.js, motion.js and layout.js run everything else. */
(function () {
  'use strict';
  // The one place for the App Store link. Replace it with the real link when Apple gives it
  // (apps.apple.com/...); every [data-appstore] link on every page uses it.
  var APP_STORE_URL = 'https://dotxline.com/tockbee.html';
  var d = document, root = d.documentElement;
  var RM = matchMedia('(prefers-reduced-motion: reduce)');
  var clamp = function (v) { return Math.max(0, Math.min(1, v)); };
  if (APP_STORE_URL) d.querySelectorAll('a[data-appstore]').forEach(function (a) { a.href = APP_STORE_URL; a.target = '_blank'; a.rel = 'noopener'; });

  // theme: the new look grows out of the button
  function dark() { var t = root.getAttribute('data-theme'); return t ? t === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches; }
  d.querySelectorAll('.theme-btn').forEach(function (b) {
    b.addEventListener('click', function () {
      var next = dark() ? 'light' : 'dark';
      var apply = function () { root.setAttribute('data-theme', next); try { localStorage.setItem('tb-theme', next); } catch (e) {} };
      if (!d.startViewTransition || RM.matches) return apply();
      var r = b.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      var end = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
      d.startViewTransition(apply).ready.then(function () {
        root.animate({ clipPath: ['circle(0px at ' + x + 'px ' + y + 'px)', 'circle(' + end + 'px at ' + x + 'px ' + y + 'px)'] },
          { duration: 750, easing: 'cubic-bezier(.76,0,.24,1)', pseudoElement: '::view-transition-new(root)' });
      }).catch(function () {});
    });
  });

  // the dock: a glass pill that tucks into the Tockbee icon when you scroll down
  var dock = d.querySelector('.dock'), links = d.getElementById('dock-links'), menu = d.querySelector('.dock__menu');
  if (menu && links) {
    menu.addEventListener('click', function () { var o = links.classList.toggle('open'); menu.setAttribute('aria-expanded', String(o)); });
    links.addEventListener('click', function (e) { if (e.target.closest('a')) { links.classList.remove('open'); menu.setAttribute('aria-expanded', 'false'); } });
  }
  if (dock) (function () {
    var bar = dock.querySelector('.dock__bar');
    var dot = d.createElement('button');
    dot.className = 'dock-dot'; dot.type = 'button'; dot.tabIndex = -1; dot.setAttribute('aria-label', 'Open the menu'); dot.setAttribute('aria-expanded', 'false');
    dot.innerHTML = '<img src="' + (dock.getAttribute('data-root') || '') + 'img/tockbee-icon-512.png" alt="">';
    bar.appendChild(dot);
    function measure() { if (dock.classList.contains('collapsed')) return; var pad = parseFloat(getComputedStyle(dock).paddingLeft) || 0; bar.style.setProperty('--pw', Math.min(1180, dock.clientWidth - pad * 2) + 'px'); dock.classList.add('ready'); }
    function set(c) {
      if (c === dock.classList.contains('collapsed')) return;
      dock.classList.toggle('collapsed', c); dot.setAttribute('aria-expanded', String(!c)); dot.tabIndex = c ? 0 : -1;
      [].forEach.call(bar.children, function (k) { if (k !== dot) { if (c) k.setAttribute('inert', ''); else k.removeAttribute('inert'); } });
    }
    var lastY = scrollY, hold = 0, tick = false;
    addEventListener('scroll', function () {
      if (tick) return; tick = true;
      requestAnimationFrame(function () {
        tick = false; var y = scrollY, dy = y - lastY, open = links && links.classList.contains('open');
        if (y < 70) set(false); else if (dy > 6 && y > 180 && !open && Date.now() > hold) set(true); else if (dy < -6) set(false);
        if (Math.abs(dy) > 6) lastY = y;
      });
    }, { passive: true });
    dot.addEventListener('click', function () { hold = Date.now() + 2500; lastY = scrollY; set(false); });
    dock.addEventListener('focusin', function () { set(false); });
    measure(); addEventListener('resize', measure); if (d.fonts) d.fonts.ready.then(measure);
  })();

  // the logo film: ring, hand, tip. Pieces: [data-step=n] belongs to chapter n; data-kind = draw | rotate | pop
  var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
  function setPiece(el, v) {
    var kind = el.getAttribute('data-kind') || 'draw';
    if (kind === 'draw') { el.style.strokeDashoffset = (1 - v).toFixed(4); el.style.opacity = v > .002 ? 1 : 0; }
    else if (kind === 'rotate') { var a0 = +el.getAttribute('data-a0'), a1 = +el.getAttribute('data-a1'); el.setAttribute('transform', 'rotate(' + (a0 + (a1 - a0) * ease(v)).toFixed(2) + ' ' + el.getAttribute('data-cx') + ' ' + el.getAttribute('data-cy') + ')'); }
    else if (kind === 'pop') { var k = ease(v), cx = el.getAttribute('data-cx'), cy = el.getAttribute('data-cy'); el.style.opacity = k.toFixed(3); el.setAttribute('transform', 'translate(' + cx + ' ' + cy + ') scale(' + (.2 + .8 * k).toFixed(3) + ') translate(' + (-cx) + ' ' + (-cy) + ')'); }
  }
  d.querySelectorAll('.film').forEach(function (film) {
    var caps = film.querySelectorAll('.film-cap'), n = caps.length || 3;
    var pieces = [].slice.call(film.querySelectorAll('[data-step]')), rail = [].slice.call(film.querySelectorAll('.film-rail i')), num = film.querySelector('[data-film-n]');
    if (RM.matches) return;
    film.classList.add('live');
    var go = false;
    function upd() {
      go = false;
      var r = film.getBoundingClientRect(), p = clamp(-r.top / Math.max(1, r.height - innerHeight));
      film.style.setProperty('--p', p.toFixed(4));
      pieces.forEach(function (el) {
        var step = +el.getAttribute('data-step'), from = +(el.getAttribute('data-from') || 0), to = +(el.getAttribute('data-to') || 1);
        setPiece(el, clamp(((p * n - step) - from) / Math.max(.001, to - from)));
      });
      var stage = Math.min(n - 1, Math.floor(p * n + .0001));
      caps.forEach(function (c, i) { c.classList.toggle('on', i === stage); });
      rail.forEach(function (dot, i) { dot.classList.toggle('on', i === stage); });
      if (num) num.textContent = stage + 1;
    }
    addEventListener('scroll', function () { if (!go) { go = true; requestAnimationFrame(upd); } }, { passive: true });
    addEventListener('resize', upd); upd();
  });

  // tick-in: things arrive like a clock ticking; the small mark in a label draws itself
  var money = function (p) { return '£' + (p / 100).toLocaleString('en-GB', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var tickEls = d.querySelectorAll('[data-tb-tick], [data-tb-row]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) {
      var el = e.target, idx = [].indexOf.call(el.parentNode.children, el);
      el.style.transitionDelay = Math.min(idx, 6) * 70 + 'ms'; el.classList.add('in'); io.unobserve(el); } }); }, { threshold: .2 });
    tickEls.forEach(function (el) { io.observe(el); });
    d.querySelectorAll('.tb-k').forEach(function (el) { io.observe(el); });
  } else { tickEls.forEach(function (el) { el.classList.add('in'); }); d.querySelectorAll('.tb-k').forEach(function (el) { el.classList.add('in'); }); }

  // working demo: Today. Tap Clock in and the timer runs; Clock out logs the shift.
  d.querySelectorAll('[data-tb-today]').forEach(function (s) {
    var btn = s.querySelector('[data-clock]'), timer = s.querySelector('[data-timer]'), how = s.querySelector('[data-how]'),
        earned = s.querySelector('[data-earned]'), toast = s.querySelector('[data-toast]'), t0 = 0, tick = 0, base = 45820, rate = 1271, tt;
    var fmt = function (ms) { var sec = Math.floor(ms / 1000), h = Math.floor(sec / 3600), m = Math.floor(sec % 3600 / 60), q = sec % 60; return h + ':' + (m < 10 ? '0' : '') + m + ':' + (q < 10 ? '0' : '') + q; };
    function say(msg) { toast.textContent = msg; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('on'); }, 2400); }
    btn.addEventListener('click', function () {
      if (!t0) {
        t0 = Date.now(); s.classList.add('on'); btn.textContent = 'Clock out'; how.textContent = 'Clocked in by tap';
        say('Clocked in. Every automatic clock-in comes with Undo.');
        tick = setInterval(function () { var ms = (Date.now() - t0) * 600; timer.textContent = fmt(ms); }, 250);
      } else {
        var ms = (Date.now() - t0) * 600; clearInterval(tick);
        var add = Math.round(ms / 3600000 * rate); base += add; earned.textContent = money(base);
        s.classList.remove('on'); btn.textContent = 'Clock in'; how.textContent = 'Last shift ' + fmt(ms); timer.textContent = '0:00:00'; t0 = 0;
        say('Nice one, ' + fmt(ms).replace(/:\d\d$/, '').replace(':', 'h ') + 'm logged.');
      }
    });
  });
})();
