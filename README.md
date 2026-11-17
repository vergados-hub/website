# Christos Vergados — Industrial Modernism × Editorial Luxury (V3)

A complete, responsive, **dependency-free static website** built from the original quiet-luxury concept, with content updated from the two LinkedIn career strategy documents.

## Included

- `index.html` — homepage: original restrained design with smaller headings and updated positioning
- `work.html` — work index
- `about.html` — professional narrative
- `projects/adamow.html` — energy infrastructure case study
- `projects/entrepreneurship-talks.html` — nonprofit / entrepreneurship case study
- `projects/digital-twin.html` — academic digital twin case study
- `projects/air-cargo.html` — EUROAVIA project case study
- `assets/styles.css` — full responsive design
- `assets/favicon.svg`, `robots.txt`, `sitemap.xml`
- `build.py` — regenerates pages (Python standard library only). After changing the text in this file, run `python build.py`.

## Preview locally

From the project directory: `python -m http.server 8000`, then open `http://localhost:8000`.

You can also open `index.html` directly, though a local HTTP server is preferable for testing.

## Publish without Framer

The site can be uploaded to a static host (Vercel, Netlify, Cloudflare Pages, GitHub Pages) without a build step. Set the **publish/output directory to the project root**. Keep cvergados.com registered at Namecheap; after testing your new deployment, configure the domain in your chosen host and add the DNS records the host specifies in Namecheap. Do not disconnect the existing Framer site until the new version is ready.

## Changes needed before public launch

1. **Portrait.** The initial hero preserves an abstract `cv` monogram from the liked concept, intentionally avoiding an unrelated stock photograph. For a real portrait, add `assets/portrait.jpg` and uncomment the documented `<img>` element in `build.py`; rerun `python build.py`.
2. **Email.** The previous prototype used an email address that was not independently confirmed. V3 links to LinkedIn instead. Once your real professional email is confirmed, add it to the Contact section and header.
3. **Claims.** The website uses 560 MW **net** as the Adamów project scale (not personal contribution). Confirm that the METLEN package and role summaries are appropriate to disclose before publishing.
4. **Entrepreneurship Talks data.** The 65+ podcast episodes, 3M+ impressions and €60k grant are **organisational** achievements, not personal production/ownership. Verify that figures remain current and that approved grant status is described accurately.
5. **Copyright and confidentiality.** Visuals are abstract drawings created for this prototype. Do not upload non-public site photos, contract details, drawings or supplier information without permission.
6. **Links and legal.** Verify LinkedIn URL, organization URL, any desired privacy/legal disclosures, and spelling before launch.
7. **Optional photo and project images.** When approved photos/renders are available, choose a small set with a consistent editorial crop. The site does not need stock imagery to feel complete.

## Visual system

- Warm ivory `#f5f3ee`
- Forest graphite `#172d2c`
- Sage `#7f9684`
- Cream, soft-grey and muted steel accents
- Sharp but restrained modernist grid
- Sans-serif with elegant editorial italics
- Reduced headline scale compared with the original prototype

This is a custom-coded site and is **not** a native Framer project. It has **not** been deployed or connected to Namecheap.
