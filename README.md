# Dr. Amin Elghanam — Premium Medical Portfolio (Preview)

**A real static, Arabic-first, responsive five-page website**, designed for client review on GitHub Pages, then adaptation into a custom WordPress theme.

## Open / run

Simplest: open `index.html` in a browser. For the most reliable preview, use a local HTTP server:

```bash
cd dr-amin-portfolio
python -m http.server 8000
```

Open **http://localhost:8000**.

The site does **not** use npm, a build step, framework runtime, API keys, or a backend. The core layout and navigation work without any animation CDN.

## Publish on GitHub Pages

1. Create a repository (for example `dr-amin-portfolio`) on GitHub.
2. Upload the **contents of this directory**, keeping `index.html` in the repo root. Do not upload only the ZIP without extracting it.
3. Navigate to **Settings → Pages → Build and deployment**.
4. Choose **Deploy from a branch**, branch **main**, folder **/(root)**; save.
5. The preview will typically be available at `https://YOUR-USERNAME.github.io/dr-amin-portfolio/` after deployment.
6. Send that URL to the client.

> GitHub Pages exposes content publicly in the typical setup. Do not add private files or sensitive patient data. All pages currently contain `<meta name="robots" content="noindex,nofollow">` because the site is a pre-approval preview. Before launching the official site, review and remove that tag, set the real domain, and add canonical URLs.

## Pages

- `index.html` — editorial home, photo-led animated hero, specialties, credentials, media previews, FAQs.
- `about.html` — professional background and supplied credential highlights.
- `specialties.html` — neurosurgery, vascular, spine, nerve and pain services.
- `media.html` — two playable supplied YouTube links; five Facebook video links; one Instagram reference.
- `contact.html` — honest pre-launch contact state and patient preparation guidance.

## Design / engineering

- Direction: Arabic RTL, editorial luxury medical brand, no clinical stock-photo clichés.
- Palette: navy `#183755`, copper `#b9765e`, ivory `#f8f6f1`, blue `#79a8c7`.
- Fonts: IBM Plex Sans Arabic and DM Sans via Google Fonts, with system fallbacks.
- Animations: GSAP 3.12.5 and ScrollTrigger; graceful no-JS/CDN fallback.
- 3D: optional Three.js 0.160.0 wireframe geometry on large screens. Skipped on reduced-motion and smaller screens.
- Polyfill: smoothscroll-polyfill 0.4.4.
- Accessibility: skip link, keyboard navigation, dialog close/ESC, keyboard menu, semantic landmarks, prefers-reduced-motion and image alt text.
- SEO prelaunch: descriptions, favicon, simple Person schema; noindex enabled pending approval.
- Performance: optimized local WebP images, lazy-loaded content images, on-demand YouTube iframe, capped WebGL pixel ratio.

### Edit text and images

Edit each `.html` file directly. Change colors / layout in `assets/css/styles.css`, interactions in `assets/js/site.js`, and photos in `assets/images/`. The transparent cutout is `assets/images/dr-amin-cutout.webp`, extracted from the supplied portrait with gray background.

### Add more videos

- For an ordinary Facebook/Instagram post, add a regular external link (like existing ones in `media.html`). Do not pretend it is embeddable if the platform disallows it.
- For YouTube, add a `data-video="VIDEO_ID"` button and extend `allowedVideoIds` in `assets/js/site.js` with the **same** approved ID. Alternatively, link directly to the watch URL.
- Ask the doctor/team to confirm subject, treatment claims, title, transcription, and permission before publishing captions or patient images.

## Important pre-launch actions

1. **Verify professional titles and credentials** with the doctor. The supplied flyer says 'consultant' while some third-party listings say 'specialist'. The prototype follows the supplied flyer, not an independent license verification.
2. **Confirm current clinic locations, operating times, and official phone/WhatsApp.** The supplied flyer advertises specific August visit dates, not ongoing clinic hours. We intentionally have not used the flyer event hotline as the doctor's private number.
3. Integrate real contact / booking only after receiving verified contact details. **No functional appointment backend exists in this static preview.**
4. Review the exact video titles and medical content; labels in the demo are neutral placeholders.
5. Get clinical/legal sign-off and a privacy policy before going live. Never publish identifiable patient cases, recordings, or medical information without the necessary rights and consent.
6. Provide the official site domain and social profile URLs; add canonical links, Open Graph preview, analytics **with appropriate consent**, structured clinic details, and a legally appropriate privacy notice.

## WordPress migration blueprint

The static site is deliberately prepared for a **custom coded WordPress theme**, not a page-builder-only clone.

| Static prototype | WordPress custom theme |
|---|---|
| Shared header & footer markup | `header.php`, `footer.php`, `functions.php` |
| `index.html` | `front-page.php` |
| `about.html` | `page-about.php` |
| `specialties.html` | `page-specialties.php` + optional service CPT |
| `media.html` | `page-media.php` + media CPT / custom fields |
| `contact.html` | `page-contact.php` + verified booking integration |
| Local CSS and JS | WP-enqueued stylesheet/scripts with versioned dependencies |
| Hero/portrait/video text | Editable via block fields, theme options or ACF-equivalent |

Migration requires WordPress installation, hosting, admin access, staging domain, approved content and confirmed booking integrations. **This ZIP is a working static prototype, not an installable WordPress theme ZIP.**
