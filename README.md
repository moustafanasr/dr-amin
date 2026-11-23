# Dr. Amin Elghanam — Portfolio Website V4

A redesigned bilingual (Arabic RTL / English LTR) medical personal portfolio. Built with hand-authored HTML, CSS and JavaScript for **GitHub Pages preview** and a potential later WordPress conversion.

## Pages

| Arabic | English |
|---|---|
| `/index.html` | `/en/index.html` |
| `/about.html` | `/en/about.html` |
| `/specialties.html` | `/en/specialties.html` |
| `/media.html` | `/en/media.html` |
| `/contact.html` | `/en/contact.html` |

The content reflects the supplied **Almana Marketing Profile** and the reference videos. Four specialty categories, academic qualifications and clinical fellowships are reproduced as informational copy, not claims about patient outcomes.

## Preview locally

Open `index.html` for Arabic and `en/index.html` for English. For a development server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/`.

## Deploy to GitHub Pages

1. Extract the ZIP archive.
2. Copy all contents of this folder into the root of the Git repository: `https://github.com/moustafanasr/dr-amin.git`. **Do not upload a single enclosing folder**; `index.html` must be in the repository root.
3. In the project terminal:

```bash
git add .
git commit -m "Redesign Dr Amin website V4 — responsive bilingual pages"
git push origin main
```

4. In GitHub Settings → Pages, select **Deploy from a branch**, `main`, `/(root)`.
5. Arabic preview: `https://moustafanasr.github.io/dr-amin/`
6. English preview: `https://moustafanasr.github.io/dr-amin/en/`

## Tech notes

- Pure HTML/CSS/JS, no build framework or PHP needed for GitHub Pages.
- GSAP and ScrollTrigger loaded from a CDN **as optional enhancements**; site remains usable without those libraries. Smooth-scroll polyfill is also optional.
- Responsive mobile menu; language switch stays on the corresponding page.
- Abstract layered circular 3D-like elements are CSS decorations; they do not block clicks or text.
- All local images are bundled and use relative paths; the website works under `/dr-amin/`.
- Run `python build.py` to regenerate all 10 HTML pages using the included `medical_content.py` copy source.
- CSS: `assets/css/styles.css`; JS: `assets/js/site.js`.
- `robots=noindex,nofollow` is **intentional for a temporary client preview**. Change this when the site is approved and deployed to the public domain.

## Important content awaiting confirmation

- Clinic addresses, locations and visiting hours.
- Official booking/WhatsApp phone number.
- Final verification of medical titles/qualifications and public email.
- Approved video titles and descriptions.

The current contact page offers the email from the submitted professional profile and clearly marks clinics and booking information as unconfirmed. There is no fake booking form or appointment system.

## QA notes

- Static local references and page-fragment anchors validated across all ten HTML pages (256 internal refs checked, zero missing targets).
- Browser rendering checks completed on 320, 390, 768 and 1440 px widths: **40 successful renders**, zero horizontal overflow, zero broken local images after eager loading, zero page script errors in test, mobile menu open/close passed.
- Check external video destinations and final WordPress implementation separately; these have not been fully tested in production.

## WordPress conversion notes

Convert these into WordPress templates for Home, About, Specialties, Media and Contact; move static doctor content into editable fields (e.g. ACF or native blocks). Keep medical copy, language metadata and approved booking contact details centrally managed. Do not upload this ZIP as a WordPress theme, because it is a static website preview.
