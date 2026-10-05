#!/usr/bin/env python3
"""Builds BLOOP's public pages (privacy policy and support for the stores):
English at the root, Polish under /pl/. GitHub Pages serves this folder at
BASE_URL.
    python3 site/build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
BASE_URL = 'https://szymdzie.github.io/bloop/'
EMAIL = 'chochoapps@gmail.com'
STORE = 'https://apps.apple.com/app/id6817773708'

TEMPLATE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="pl" href="{url_pl}">
<meta name="theme-color" content="#0b1e4a">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{base}assets/icon-256.png">
<link rel="icon" type="image/png" sizes="32x32" href="{root}assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{root}assets/favicon-64.png">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jersey+10&display=swap">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{home}"><img src="{root}assets/icon-256.png" alt="" width="40" height="40"><span>BLOOP</span></a>
  <nav aria-label="{nav_label}">
    <a href="{home}support/"{cur_support}>{nav_support}</a>
    <a href="{home}privacy/"{cur_privacy}>{nav_privacy}</a>
    <a href="{other}" hreflang="{other_lang}">{other_name}</a>
  </nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <span>© 2026 Szymon Dziedzic</span>
  <a href="mailto:{email}">{email}</a>
  <a href="{home}privacy/">{nav_privacy}</a>
  <a href="{home}support/">{nav_support}</a>
</div></footer>
</body>
</html>
"""

LANGS = {
    'en': {'dir': '', 'nav_label': 'Main', 'nav_support': 'Support', 'nav_privacy': 'Privacy', 'other': 'pl', 'other_name': 'Polski'},
    'pl': {'dir': 'pl/', 'nav_label': 'Menu', 'nav_support': 'Pomoc', 'nav_privacy': 'Prywatność', 'other': 'en', 'other_name': 'English'},
}

PAGES = {
    ('en', 'index'): (
        'BLOOP: Water Ring Toss',
        'The classic water ring toss game: ten toys, 150 levels, bosses and tilt control. No ads, works offline.',
        f"""<section class="hero">
  <img src="assets/icon-256.png" alt="BLOOP app icon">
  <div>
    <h1>BLOOP</h1>
    <p class="lead">The classic water ring toss, in your pocket.</p>
    <a class="badge" href="{STORE}">Get it on the App Store</a>
  </div>
</section>
<div class="card">
  <h2>Push. Bubble. Bloop!</h2>
  <p>Press the buttons, watch the bubbles lift the rings and land them on the pegs, just like the toy you remember.
  Ten toys in one game, 150 adventure levels in 10 worlds, crazy bosses, tilt control that really moves the water,
  and more than 50 looks to collect.</p>
  <p>No ads. No account. Works offline.</p>
</div>
<p class="muted"><a href="support/">Support</a> · <a href="privacy/">Privacy Policy</a></p>"""),
    ('en', 'privacy'): (
        'BLOOP – Privacy Policy',
        'BLOOP collects no personal data. Everything stays on your device.',
        f"""<h1>Privacy Policy</h1>
<p class="muted">BLOOP: Water Ring Toss · last updated 3 October 2026</p>
<p class="lead">BLOOP collects no personal data. Everything you do in the game stays on your device.</p>
<div class="card">
<ul>
  <li><b>No account.</b> There is no sign-in and no registration.</li>
  <li><b>No ads, no analytics, no tracking.</b> The game contains no advertising or analytics tools and never asks to track you.</li>
  <li><b>Saved on your device only.</b> Your progress, stars, pearls, unlocked looks and settings are stored on the device.
  Deleting the game deletes them. Settings → Reset progress erases your progress (Premium stays).</li>
  <li><b>Purchases.</b> Premium and pearl packs are sold through the App Store or Google Play. The store handles the payment;
  we never see your payment details. The game remembers on the device what you bought, and Settings → Restore purchases asks the store again.</li>
  <li><b>Motion sensors.</b> Tilt control reads the device's motion sensors while you play, only to move the water in the game.
  The readings are never stored or sent anywhere. You can turn tilt control off in Settings.</li>
  <li><b>Works offline.</b> The game makes no internet connections of its own.</li>
  <li><b>Crash reports.</b> If you chose to share analytics with app developers in your device settings, Apple or Google may pass us
  anonymous crash reports. They contain no personal data.</li>
  <li><b>Children.</b> We collect no data from anyone, including children.</li>
  <li><b>Changes.</b> If this policy ever changes, the new version will appear on this page with a new date.</li>
</ul>
</div>
<p>Questions? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
    ('en', 'support'): (
        'BLOOP – Support',
        'Help with BLOOP: Water Ring Toss. Purchases, tilt control, progress and contact.',
        f"""<h1>Support</h1>
<p class="lead">Something not working, or an idea for a new toy? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.
We answer every message.</p>
<div class="card">
  <h2>My purchase did not arrive</h2>
  <p>Open Settings → Restore purchases, signed in with the same Apple ID or Google account you used to buy.</p>
  <h2>How do I turn tilt control on or off?</h2>
  <p>Settings → Tilt control. With it on, tilting the phone tilts the water in the toy.</p>
  <h2>Will my progress move to a new phone?</h2>
  <p>Progress is saved on the device (there is no account). A full device backup (iCloud or computer) includes it,
  and Premium can always be brought back with Restore purchases.</p>
  <h2>How do I change the language?</h2>
  <p>Settings → Language. BLOOP speaks English and Polish.</p>
  <h2>Can I start over?</h2>
  <p>Settings → Reset progress erases stars, records and pearls. Premium stays.</p>
</div>
<p class="muted">Please include your device model and the game version (Settings, at the bottom) when you report a problem.</p>"""),
    ('pl', 'index'): (
        'BLOOP: wodne kółka',
        'Kultowa gra w wodne kółka: dziesięć zabawek, 150 poziomów, bossowie i sterowanie przechyłem. Bez reklam, działa offline.',
        f"""<section class="hero">
  <img src="../assets/icon-256.png" alt="Ikona aplikacji BLOOP">
  <div>
    <h1>BLOOP</h1>
    <p class="lead">Kultowa gra w wodne kółka, zawsze pod ręką.</p>
    <a class="badge" href="{STORE}">Pobierz z App Store</a>
  </div>
</section>
<div class="card">
  <h2>Wciśnij. Bąbelki. Bloop!</h2>
  <p>Wciskaj przyciski, patrz, jak bąbelki unoszą kółka i nadziewają je na bolce, zupełnie jak w zabawce z dzieciństwa.
  Dziesięć zabawek w jednej grze, 150 poziomów przygody w 10 światach, szaleni bossowie, przechył, który naprawdę rusza wodą,
  i ponad 50 wyglądów do zebrania.</p>
  <p>Bez reklam. Bez konta. Działa offline.</p>
</div>
<p class="muted"><a href="support/">Pomoc</a> · <a href="privacy/">Polityka prywatności</a></p>"""),
    ('pl', 'privacy'): (
        'BLOOP – Polityka prywatności',
        'BLOOP nie zbiera danych osobowych. Wszystko zostaje na Twoim urządzeniu.',
        f"""<h1>Polityka prywatności</h1>
<p class="muted">BLOOP: wodne kółka · ostatnia zmiana 3 października 2026</p>
<p class="lead">BLOOP nie zbiera danych osobowych. Wszystko, co robisz w grze, zostaje na Twoim urządzeniu.</p>
<div class="card">
<ul>
  <li><b>Bez konta.</b> Nie ma logowania ani rejestracji.</li>
  <li><b>Bez reklam, analityki i śledzenia.</b> Gra nie zawiera narzędzi reklamowych ani analitycznych i nigdy nie prosi o zgodę na śledzenie.</li>
  <li><b>Zapis tylko na urządzeniu.</b> Postępy, gwiazdki, perły, odblokowane wyglądy i ustawienia są zapisane na urządzeniu.
  Usunięcie gry je usuwa. Ustawienia → Wyzeruj postępy kasuje postępy (Premium zostaje).</li>
  <li><b>Zakupy.</b> Premium i paczki pereł sprzedajemy przez App Store lub Google Play. Płatność obsługuje sklep;
  nie widzimy danych płatniczych. Gra zapamiętuje na urządzeniu, co kupiłeś, a Ustawienia → Przywróć zakupy pyta sklep jeszcze raz.</li>
  <li><b>Czujniki ruchu.</b> Sterowanie przechyłem odczytuje czujniki ruchu urządzenia w trakcie gry, wyłącznie po to, żeby poruszać wodą w grze.
  Odczyty nie są nigdzie zapisywane ani wysyłane. Przechył wyłączysz w Ustawieniach.</li>
  <li><b>Działa offline.</b> Gra sama nie łączy się z internetem.</li>
  <li><b>Raporty o awariach.</b> Jeśli w ustawieniach urządzenia zgodzisz się na udostępnianie analiz twórcom aplikacji, Apple lub Google
  mogą przekazać nam anonimowe raporty o awariach. Nie zawierają danych osobowych.</li>
  <li><b>Dzieci.</b> Nie zbieramy danych od nikogo, także od dzieci.</li>
  <li><b>Zmiany.</b> Jeśli kiedyś zmienimy tę politykę, nowa wersja pojawi się na tej stronie z nową datą.</li>
</ul>
</div>
<p>Pytania? Napisz na <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
    ('pl', 'support'): (
        'BLOOP – Pomoc',
        'Pomoc do gry BLOOP: wodne kółka. Zakupy, przechył, postępy i kontakt.',
        f"""<h1>Pomoc</h1>
<p class="lead">Coś nie działa albo masz pomysł na nową zabawkę? Napisz na <a href="mailto:{EMAIL}">{EMAIL}</a>.
Odpowiadamy na każdą wiadomość.</p>
<div class="card">
  <h2>Zakup nie dotarł</h2>
  <p>Otwórz Ustawienia → Przywróć zakupy, będąc zalogowanym na to samo Apple ID lub konto Google, którym płaciłeś.</p>
  <h2>Jak włączyć lub wyłączyć przechył?</h2>
  <p>Ustawienia → Sterowanie przechyłem. Gdy jest włączone, przechylenie telefonu przechyla wodę w zabawce.</p>
  <h2>Czy postępy przejdą na nowy telefon?</h2>
  <p>Postępy są zapisane na urządzeniu (gra nie ma kont). Pełna kopia zapasowa urządzenia (iCloud lub komputer) je obejmuje,
  a Premium zawsze odzyskasz przez Przywróć zakupy.</p>
  <h2>Jak zmienić język?</h2>
  <p>Ustawienia → Język. BLOOP mówi po polsku i po angielsku.</p>
  <h2>Czy mogę zacząć od nowa?</h2>
  <p>Ustawienia → Wyzeruj postępy kasuje gwiazdki, rekordy i perły. Premium zostaje.</p>
</div>
<p class="muted">Zgłaszając problem, podaj model urządzenia i wersję gry (na dole Ustawień).</p>"""),
}


def main():
    for (lang, page), (title, description, body) in PAGES.items():
        cfg = LANGS[lang]
        sub = '' if page == 'index' else page + '/'
        depth = cfg['dir'].count('/') + sub.count('/')
        root = '../' * depth
        home = root + cfg['dir']
        other = LANGS[cfg['other']]
        canonical = BASE_URL + cfg['dir'] + sub
        out = ROOT / cfg['dir'] / sub / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(TEMPLATE.format(
            lang=lang, title=title, description=description, canonical=canonical, base=BASE_URL, root=root or './', home=home or './',
            url_en=BASE_URL + sub, url_pl=BASE_URL + 'pl/' + sub, body=body, email=EMAIL,
            other=root + other['dir'] + sub or './', other_lang=cfg['other'], other_name=cfg['other_name'],
            cur_support=' aria-current="page"' if page == 'support' else '',
            cur_privacy=' aria-current="page"' if page == 'privacy' else '',
            **{k: cfg[k] for k in ('nav_label', 'nav_support', 'nav_privacy')}), encoding='utf-8')
        print(out.relative_to(ROOT))
    (ROOT / '.nojekyll').write_text('')


if __name__ == '__main__':
    main()
