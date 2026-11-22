# Dr. Amin Elghanam — Bilingual Portfolio Preview v2.1

A handcrafted, accessible, responsive medical portfolio built as a **static preview** for GitHub Pages and subsequent custom WordPress implementation.

## Pages

| Arabic (RTL, default) | English (LTR) |
|---|---|
| `index.html` | `en/index.html` |
| `about.html` | `en/about.html` |
| `specialties.html` | `en/specialties.html` |
| `media.html` | `en/media.html` |
| `contact.html` | `en/contact.html` |

`assets/` contains local CSS, JavaScript and licensed-to-client images provided for the project.  Site layout is fully functional without GSAP, Three.js or Google Fonts (those are progressively enhanced from CDNs).

## Build and preview

- Open `index.html` to review Arabic, or `en/index.html` to review English.
- For a development server: `python -m http.server 8000` then visit `http://localhost:8000/`.
- If you edit copy in `build.py`, run `python build.py` to regenerate all ten HTML pages. Requires Python 3 only (stdlib). Direct HTML edits are possible but will be overwritten by regeneration.
- Editable category source for both languages is exported to `content/source-categories.json` (generated from `build.py`).

## Publish on GitHub Pages

The repository must have `index.html` in the root, not inside a nested folder. From the extracted website root:

```bash
git init
git add .
git commit -m "Update Dr Amin bilingual portfolio v2"
git branch -M main
git remote add origin https://github.com/moustafanasr/dr-amin.git
git push -u origin main
```

If an `origin` remote already exists, use `git remote set-url origin https://github.com/moustafanasr/dr-amin.git` instead of `git remote add`. If the remote has commits you do not have locally, fetch/reconcile history before pushing; do **not** force push an existing project.

Go to **GitHub → Settings → Pages → Deploy from a branch → main / (root)**.

Expected preview URL once deployed:

- Arabic: `https://moustafanasr.github.io/dr-amin/`
- English: `https://moustafanasr.github.io/dr-amin/en/`

## Interactions implemented

- Mobile navigation with keyboard Escape behavior.
- Matching Arabic/English routes (no automated translations or stale language mix).
- Accessible HTML details/summary FAQ.
- On-site YouTube modal for two provided videos, external Facebook links for five supplied reels.
- Email link and copy-to-clipboard on Contact (browser may prompt if clipboard permission is missing).
- GSAP/ScrollTrigger entrance animations with reduced-motion detection and safe fallback.
- Decorative 3D Three.js geometry, loaded only on sufficiently large screens, with safe fallback.
- Local image assets, native lazy loading on below-the-fold imagery.

## Medical content & review

- Professional credentials, clinical fellowships and four practice categories are mapped from **Almana Marketing Profile, pages 1–4** and the supplied Amin Elghanam flyer.
- No fabricated hospital location, clinic hours, booking availability, cure claims, patient outcomes or testimonial counts.
- **Professional email in the submitted profile:** `amin.elghanam@gmail.com`. It appears for inquiries and needs client sign-off before official launch. The Saudi mobile number on the profile is deliberately *not* used as an appointment hotline because current availability is unconfirmed.
- YouTube videos have generic labels until the doctor approves exact titles and descriptions.
- The site currently has `noindex,nofollow` metadata **by design**, to keep this GitHub preview out of search results. Before production, remove this after content approval and configure canonical URLs, hreflang absolute links, sitemap, SEO and current contact details.
- Do not deploy as clinical booking software or claim to collect appointment requests: the preview does not have a backend or form submission.

## Conversion to WordPress

Recommended mapping: front-page.php (Home), page-about.php, page-specialties.php, page-media.php, page-contact.php. Build language equivalents through WPML or Polylang; use WP fields or CPTs for specialties, media and clinic details. Replace static anchor paths with WordPress URLs; enqueue assets and scripts with versioning, use local WordPress Media Library assets. Review personal-data practices, consent, any cookie/analytics requirements and medical advertising rules before launch.

## Pre-launch confirmation checklist

- Doctor's final degree titles and translations; approval of academic timeline.
- Clinic locations, addresses, appointment hours, map pins, booking contact number and WhatsApp.
- Verify professional email should be public.
- Approved video titles, captions, thumbnails, and privacy/public distribution consent.
- Site domain, SEO indexation, analytics/consent requirements, policies, hosting and official WordPress setup.
