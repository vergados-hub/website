"""Build standalone static HTML pages for cvergados.com.
No dependencies outside Python's standard library.
"""
from pathlib import Path
from html import escape

ROOT=Path(__file__).resolve().parent

POWER='''<svg viewBox="0 0 620 320" fill="none" role="img" aria-label="Abstract line drawing of industrial energy infrastructure"><g stroke="#719890" stroke-width=".8" opacity=".27"><path d="M0 275H620M0 235H620M0 195H620M0 155H620M0 115H620"/><path d="M30 0V320M90 0V320M150 0V320M210 0V320M270 0V320M330 0V320M390 0V320M450 0V320M510 0V320M570 0V320"/></g><g stroke="#c5dac8" stroke-width="1.5" opacity=".9"><path d="M79 269V152H136V269M170 269V82H223V269M255 269V120H308V269M355 269V48H402V269M443 269V166H525V269M48 269H565"/><path d="M170 84L151 56M223 84L243 56M355 49L333 24M402 49L426 24"/><path d="M79 178H136M170 123H223M170 158H223M170 201H223M255 157H308M355 96H402M355 147H402M443 203H525"/><path d="M136 239H170M223 215H255M308 247H355M402 224H443"/></g><g stroke="#98bdb0" stroke-dasharray="3 7"><path d="M115 152V85H355M400 146H513V120"/></g><path d="M65 272H560" stroke="#e4efdb" stroke-width="2"/><circle cx="563" cy="272" r="3" fill="#e4efdb"/></svg>'''
NETWORK='''<svg viewBox="0 0 620 320" fill="none" role="img" aria-label="Abstract network of people and connections"><g stroke="#e7efe5" stroke-width="1.5" opacity=".65"><path d="M110 247L219 137L360 185L475 90M219 137L173 52M219 137L361 55M360 185L500 266M360 185L291 277M475 90L500 266"/><circle cx="110" cy="247" r="34"/><circle cx="219" cy="137" r="53"/><circle cx="360" cy="185" r="47"/><circle cx="475" cy="90" r="60"/><circle cx="173" cy="52" r="17"/><circle cx="361" cy="55" r="18"/><circle cx="500" cy="266" r="19"/><circle cx="291" cy="277" r="15"/></g><g fill="#f0f5ea"><circle cx="110" cy="247" r="7"/><circle cx="219" cy="137" r="9"/><circle cx="360" cy="185" r="9"/><circle cx="475" cy="90" r="11"/><circle cx="173" cy="52" r="4"/><circle cx="361" cy="55" r="4"/><circle cx="500" cy="266" r="4"/><circle cx="291" cy="277" r="4"/></g></svg>'''
TWIN='''<svg viewBox="0 0 620 320" fill="none" role="img" aria-label="Abstract isometric digital twin diagram"><g stroke="#607e70" stroke-width="1.6" opacity=".85"><path d="M145 265V112L310 25L477 112V263L310 306L145 265Z"/><path d="M145 112L310 190L477 112M310 190V306"/><path d="M227 67L394 146M227 153V285M394 146V281" opacity=".65"/><path d="M145 265L310 190L477 263M145 112L310 25L477 263" stroke-dasharray="4 8" opacity=".45"/><path d="M217 238L289 201L395 224L321 260L217 238Z"/><path d="M268 225L272 169L305 150L320 164L301 194L323 209"/><circle cx="272" cy="169" r="8"/><circle cx="305" cy="150" r="6"/></g><g fill="#517061"><circle cx="310" cy="190" r="5"/><circle cx="145" cy="112" r="4"/><circle cx="477" cy="112" r="4"/></g></svg>'''
AIR='''<svg viewBox="0 0 620 320" fill="none" role="img" aria-label="Technical-outline illustration of an air-cargo UAV"><g stroke="#a8c5b7" opacity=".8"><path d="M65 262H564M65 288H564" stroke-dasharray="4 9"/><path d="M92 172L284 137L332 61L362 64L360 136L525 171L529 185L360 187L338 251L302 249L288 187L92 185Z" stroke-width="2"/><path d="M284 137L288 187M360 136L360 187M302 249L338 251"/><path d="M98 172L98 185M93 178L525 178" stroke-dasharray="3 8"/></g><circle cx="326" cy="176" r="6" fill="#cce0d2"/></svg>'''


def ref(href, depth=0):
    return ('../'*depth)+href


def head(title, description, path, depth=0):
    full_title=f'{title} | Christos Vergados' if title!='Home' else 'Christos Vergados — Engineering & Entrepreneurship'
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description,quote=True)}">
<meta name="theme-color" content="#f5f3ee">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Christos Vergados">
<meta property="og:title" content="{escape(full_title,quote=True)}">
<meta property="og:description" content="{escape(description,quote=True)}">
<link rel="canonical" href="https://cvergados.com/{path}">
<link rel="icon" href="{ref('assets/favicon.svg',depth)}" type="image/svg+xml">
<link rel="stylesheet" href="{ref('assets/styles.css',depth)}">
</head><body><a class="skip" href="#main">Skip to content</a>'''


def nav(active='',depth=0):
    def link(label,href,slug):
        cur=' aria-current="page"' if active==slug else ''
        return f'<a href="{ref(href,depth)}"{cur}>{label}</a>'
    return f'''<div class="header-wrap"><header class="container site-header">
 <a href="{ref('index.html',depth)}" class="brand" aria-label="Christos Vergados home">cv<i>.</i></a>
 <nav class="nav" aria-label="Primary navigation">
 {link('Selected work','work.html','work')}
 {link('About','about.html','about')}
 <a href="{ref('index.html#experience',depth)}">Experience</a>
 <a href="{ref('index.html#contact',depth)}">Contact</a>
 </nav>
 <a class="header-action" href="{ref('index.html#contact',depth)}"><span>Let's connect</span><span class="arrow" aria-hidden="true">↗</span></a>
 </header></div>'''


def footer(depth=0):
    return f'''<footer class="container footer"><span>© 2026 Christos Vergados</span><span>Engineering · Entrepreneurship · International collaboration</span><div class="footer-links"><a href="https://www.linkedin.com/in/christos-vergados-/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="{ref('work.html',depth)}">Work</a><a href="{ref('index.html',depth)}">Back to home ↑</a></div></footer></body></html>'''


def work_card(tag,kicker,title,description,href,art,theme):
    label_class=' ink' if theme=='stone' else ''
    return f'''<a class="work-card" href="{href}"><div class="work-visual {theme}"><span class="visual-label{label_class}">{tag}</span>{art}</div><div class="work-info"><div class="work-info-top"><span class="work-kicker">{kicker}</span><span class="work-arrow" aria-hidden="true">↗</span></div><h3>{title}</h3><p>{description}</p></div></a>'''

home = head('Home','Mechanical Project Engineer at METLEN and Co-founder of Entrepreneurship Talks. Selected work in international energy infrastructure, entrepreneurship and engineering.','')
home+=nav()
home+='''<main id="main">
<section class="container hero" aria-labelledby="hero-title"><div class="hero-copy">
<div class="eyebrow kicker-line">Christos Vergados <span aria-hidden="true">/</span> Athens, Greece</div>
<h1 class="hero-title" id="hero-title">Engineering <em>ideas</em><br>into impact.</h1>
<p class="hero-description">I’m a Mechanical Project Engineer at METLEN and Co-founder &amp; Managing Director of Entrepreneurship Talks. My work brings together technical execution, international projects, and the people behind them.</p>
<div class="hero-subline"><span>EPC energy infrastructure</span><span class="small-dot"></span><span>Entrepreneurship</span><span class="small-dot"></span><span>Europe</span></div>
<div class="hero-cta"><a class="btn-primary" href="#work">Explore selected work <span aria-hidden="true">↗</span></a><a class="underlink" href="about.html">More about me</a></div>
</div><div class="hero-visual" aria-label="Abstract architectural monogram inspired by industrial modernism"><div class="arch"><div class="arch-ring"></div><div class="arch-ring two"></div><span class="arch-monogram" aria-hidden="true">cv</span><!-- Optional: add a licensed portrait as assets/portrait.jpg and uncomment the line below. --><!-- <img class="arch-img" src="assets/portrait.jpg" alt="Portrait of Christos Vergados"> --></div><span class="hero-side-note">Engineering · Organisations · People</span><div class="hero-chip"><span class="light" aria-hidden="true"></span><div><strong>Based in Athens</strong><small>Working across borders</small></div></div></div>
</section>
<div class="facts-band"><div class="container facts-inner"><span>Mechanical engineering</span><i></i><span>International infrastructure</span><i></i><span>Entrepreneurship</span><i></i><span>Cross-border collaboration</span></div></div>
<section class="container section" id="work"><div class="section-lead"><span class="section-label">01 / Selected work</span><h2 class="section-heading">Work in <em>practice.</em></h2></div>
<div class="featured-grid">'''
home+=work_card('Energy infrastructure','METLEN / POLAND','Adamów CCGT — project engineering','Engineering, procurement and construction interfaces on a 560 MW net combined-cycle power project.','projects/adamow.html',POWER,'dark')
home+=work_card('Entrepreneurship & people','ENTREPRENEURSHIP TALKS','Building an organisation','Co-founding a nonprofit connecting young people with entrepreneurship, international partnerships and European opportunities.','projects/entrepreneurship-talks.html',NETWORK,'sage')
home+='''</div><div class="work-extra">
<div class="mini-feature"><span class="mini-number">03</span><div><h3>Digital twin &amp; robotic manufacturing</h3><p>A hybrid manufacturing-cell digital twin developed as my engineering thesis at the University of Patras.</p><a href="projects/digital-twin.html">Explore the project ↗</a></div></div>
<div class="mini-feature"><span class="mini-number">04</span><div><h3>Air Cargo Challenge</h3><p>Structural design and collaborative engineering within the EUROAVIA M.ACH team, 13th of 30 at the 2024 competition.</p><a href="projects/air-cargo.html">Explore the project ↗</a></div></div>
</div><p class="section-footnote">The visuals are abstract editorial illustrations, not proprietary engineering drawings or documentation.</p>
</section>
<section class="dark-section" aria-labelledby="about-preview"><div class="container dark-inner"><span class="section-label">02 / Perspective</span><div><h2 class="big-copy" id="about-preview">An engineering foundation, with an interest in the <em>wider system</em> — the people, decisions and organisations that turn plans into reality.</h2><div class="dark-blurbs"><p>My work at METLEN connects technical engineering with procurement and construction, including time spent with project teams on site in Poland.</p><p>Alongside engineering, Entrepreneurship Talks has been a different kind of learning environment: building a team, developing partnerships and shaping international programmes.</p></div><a class="dark-link" href="about.html">About my background <span aria-hidden="true">↗</span></a></div></div></section>
<section class="container section" id="experience"><div class="section-lead"><span class="section-label">03 / Background</span><h2 class="section-heading">A trajectory shaped by <em>practice.</em></h2></div><div class="timeline">
<div class="timeline-row"><span class="timeline-year">2026 — Present</span><h3>METLEN</h3><p>Mechanical Project Engineering · EPC power projects<br>Engineering, technical procurement and construction interfaces</p></div>
<div class="timeline-row"><span class="timeline-year">2022 — Present</span><h3>Entrepreneurship Talks</h3><p>Co-founder &amp; Managing Director<br>Community, international partnerships and European programmes</p></div>
<div class="timeline-row"><span class="timeline-year">2025</span><h3>University of Patras</h3><p>Diploma, Mechanical &amp; Aeronautical Engineering<br>Thesis in digital twin and robotic manufacturing</p></div>
<div class="timeline-row"><span class="timeline-year">Earlier work</span><h3>Manufacturing &amp; aerospace</h3><p>Athenian Brewery manufacturing experience · EUROAVIA air-cargo UAV design</p></div>
</div></section>
<section class="contact-section" id="contact"><div class="container"><span class="section-label">04 / Contact</span><h2 class="contact-title">A good project starts with a <em>conversation.</em></h2><div class="contact-actions"><a class="btn-primary" href="https://www.linkedin.com/in/christos-vergados-/" target="_blank" rel="noopener noreferrer">Connect on LinkedIn <span aria-hidden="true">↗</span></a><a class="underlink" href="work.html">Explore the work</a></div><p class="small-disclaimer">Professional enquiries &amp; collaborations. A direct email address can be added once confirmed.</p></div></section>
</main>'''
home+=footer()
(ROOT/'index.html').write_text(home,encoding='utf-8')

work = head('Selected Work','Selected work of Christos Vergados across energy infrastructure, EPC project engineering, entrepreneurship, digital twins and aerospace.','work.html')+nav('work')
work+='''<main id="main"><section class="container inner-hero"><span class="section-label">01 / Portfolio</span><div><h1 class="inner-main-title">Selected <em>work.</em></h1><p class="inner-summary">Engineering projects and initiatives that have shaped how I approach technical challenges, international collaboration and organisational development.</p></div></section><section class="container section" style="padding-top:0"><div class="work-list">'''
for n,title,desc,meta,slug in [
    ('01','Adamów CCGT — project engineering','Engineering, procurement and construction interfaces on an international combined-cycle power project.','METLEN / POLAND / 2026–PRESENT','adamow'),
    ('02','Entrepreneurship Talks','Building a nonprofit platform for youth entrepreneurship, partnerships, events and European opportunities.','CO-FOUNDER & MANAGING DIRECTOR','entrepreneurship-talks'),
    ('03','Digital twin & robotics','Mechanical engineering thesis on a hybrid manufacturing-cell digital twin, connecting physical processes and their digital representation.','UNIVERSITY OF PATRAS / 2025','digital-twin'),
    ('04','Air Cargo Challenge','Structural design and collaborative development of an air-cargo UAV as part of the M.ACH team.','EUROAVIA / AACHEN / 2024','air-cargo')]:
    work+=f'<a class="work-list-row" href="projects/{slug}.html"><span class="num">{n}</span><h2>{title}</h2><div><span class="meta">{meta}</span><p class="desc">{desc}</p></div><span class="linkarr" aria-hidden="true">↗</span></a>'
work+='''</div><div style="padding-top:65px"><p class="pull-quote">“I’m interested in the space where good technical thinking meets the realities of getting things done.”</p></div></section></main>'''+footer()
(ROOT/'work.html').write_text(work,encoding='utf-8')

about=head('About','About Christos Vergados: mechanical project engineer at METLEN, Co-founder of Entrepreneurship Talks, and mechanical and aeronautical engineering graduate of the University of Patras.','about.html')+nav('about')
about+='''<main id="main"><section class="container inner-hero"><span class="section-label">02 / About</span><div><h1 class="inner-main-title">Engineering, people<br>&amp; <em>perspective.</em></h1><p class="inner-summary">I’m a mechanical engineer with an interest in how complex projects come together — not only through design and technical decisions, but through organisations, people and execution.</p></div></section><section class="container about-grid"><div class="prose"><p>I studied Mechanical &amp; Aeronautical Engineering at the University of Patras, with a technical foundation in manufacturing, automation and mechanical systems. My diploma thesis explored a digital twin for a hybrid robotic manufacturing cell.</p><p>Today, I work as a Mechanical Project Engineer at METLEN, supporting the delivery of international EPC energy infrastructure. My responsibilities sit between engineering, procurement and construction: reviewing technical deliverables, helping define subcontractor packages, coordinating interfaces and learning from the realities of site execution.</p><p>Outside my engineering role, I co-founded Entrepreneurship Talks, a nonprofit initiative centred on entrepreneurship education, media, community and international opportunity. Building the organisation has involved partnerships, programmes, people and responsibilities very different from — but complementary to — engineering.</p><p>I’m interested in project delivery, industrial systems, entrepreneurship and the commercial side of building things. I value technical depth, clear thinking, and working with people who turn ideas into something tangible.</p><a class="underlink" href="work.html">View selected work ↗</a></div><aside class="about-aside"><div class="eyebrow">At a glance</div><dl><div><dt>Based in</dt><dd>Athens, Greece</dd></div><div><dt>Current work</dt><dd>Mechanical Project Engineering · METLEN</dd></div><div><dt>Other role</dt><dd>Co-founder &amp; Managing Director · Entrepreneurship Talks</dd></div><div><dt>Education</dt><dd>University of Patras · Mechanical &amp; Aeronautical Engineering</dd></div><div><dt>Interests</dt><dd>Industrial systems · Infrastructure · Project delivery · Entrepreneurship</dd></div></dl><p>For the most detailed and current professional history, visit my LinkedIn profile. This website is a selected account of work and perspective, not a full résumé.</p></aside></section></main>'''+footer()
(ROOT/'about.html').write_text(about,encoding='utf-8')

CASES={
 'adamow':dict(title='Adamów CCGT',italic='Project engineering',subtitle='Mechanical project engineering within the execution of a large-scale combined-cycle power project in Turek, Poland.',tag='Energy infrastructure',meta=['METLEN','Turek, Poland','560 MW net · project capacity','2026–Present'],art=POWER,theme='dark',
    intro='The Adamów Combined Cycle Gas Turbine project is a 560 MW net power plant in Poland, delivered within an EPC framework by the METLEN–Siemens Energy consortium. The plant’s scale is project context; my role is a contribution within the wider engineering and construction team.',
    involvement='My work is at the interfaces between engineering, technical procurement, subcontracting and construction. I support the translation of technical requirements into packages, documentation and coordination that teams can execute.',
    bullets=['Review multidisciplinary engineering information, including P&IDs, layouts, mechanical specifications and piping documentation.','Prepare and coordinate RFQs and scopes of work for mechanical and construction work packages.','Support supplier and subcontractor clarifications, interface coordination and technical follow-up.','Participate in periodic site assignments involving constructability and engineering-to-field coordination.'],
    bottom='Technical details and project materials are intentionally limited to publicly disclosable information. No confidential drawings, supplier evaluations or internal project records are reproduced.'),
 'entrepreneurship-talks':dict(title='Entrepreneurship Talks',italic='Building connections',subtitle='Co-founding and helping develop a nonprofit platform connecting young people with entrepreneurship, international communities and practical opportunities.',tag='Entrepreneurship & people',meta=['Co-founder & Managing Director','Greece / International','Nonprofit initiative'],art=NETWORK,theme='sage',
    intro='Entrepreneurship Talks is a youth-led nonprofit working across entrepreneurship education, media, community events and international projects. What began as an initiative around conversations and ecosystem access has developed into a platform for partnerships and European programmes.',
    involvement='My involvement includes organisational direction, partnerships, EU programme development and the operational work required to grow an initiative beyond its original format.',
    bullets=['Co-founded and helped develop the organisation, including activities connecting young people with founders and innovation ecosystems.','Worked on international partnerships, EU programme development and organisational coordination.','Supported the development of podcast, educational, networking and community initiatives.','Contributed to securing an Erasmus+ KA153-YOU mobility grant as coordinating organisation.'],
    bottom='The figures shown are Entrepreneurship Talks organisational achievements, not individual results. Grant approval is not presented as completed project implementation.'),
 'digital-twin':dict(title='Digital twin',italic='Robotic manufacturing',subtitle='A diploma thesis exploring digital representation and process-control optimisation in a hybrid robotic manufacturing cell.',tag='Technical foundation',meta=['University of Patras','Diploma thesis · 2025','Robotics / Manufacturing'],art=TWIN,theme='stone',
    intro='My diploma thesis focused on the design and development of a digital twin of a hybrid manufacturing cell, connecting robotic production processes with a digital environment for simulation and process-control exploration.',
    involvement='The project combined mechanical engineering, manufacturing systems, automation and digital modelling. It was developed within the Mechanical & Aeronautical Engineering programme at the University of Patras.',
    bullets=['Explored digital-twin architecture for an industrial cell featuring a six-axis robotic system.','Connected engineering modelling, process logic and digital representation of manufacturing operations.','Developed a stronger foundation in systems thinking, automation and the interface between software and machinery.'],
    bottom='This page is a high-level academic project summary. Thesis figures and original renders can be incorporated with permission and proper attribution.'),
 'air-cargo':dict(title='Air Cargo Challenge',italic='Engineering for flight',subtitle='Collaborative UAV design and manufacturing as part of the EUROAVIA M.ACH team competing in Aachen in 2024.',tag='Aerospace & teamwork',meta=['EUROAVIA','Aachen, Germany','2024 competition'],art=AIR,theme='midnight',
    intro='The Air Cargo Challenge brings student engineering teams together to design and operate aircraft around a constrained cargo-carrying mission. I contributed to the structural sub-team of the M.ACH project.',
    involvement='The experience introduced me to the practical connection between engineering design, constraints, fabrication and team coordination in a competition environment.',
    bullets=['Contributed to structural design and development activities for an air-cargo UAV.','Supported design/manufacturing work within a multidisciplinary student team.','Participated in a team that finished 13th among 30 competitors at the 2024 Air Cargo Challenge in Aachen.'],
    bottom='The result is attributed to the full M.ACH team, not to an individual contribution.')
}
for slug,data in CASES.items():
    title=data['title']
    doc=head(title,data['subtitle'],f'projects/{slug}.html',1)+nav(depth=1)
    meta=''.join(f'<span>{escape(item)}</span>' for item in data['meta'])
    art_label=' ink' if data['theme']=='stone' else ''
    lis=''.join(f'<li>{escape(x)}</li>' for x in data['bullets'])
    doc+=f'''<main id="main"><section class="container project-hero"><div><div class="breadcrumb"><a href="../work.html">Selected work</a><span aria-hidden="true">/</span><span>{escape(data['tag'])}</span></div><h1>{escape(data['title'])}<br><em>{escape(data['italic'])}.</em></h1><p>{escape(data['subtitle'])}</p><div class="project-meta">{meta}</div></div><div class="project-visual work-visual {data['theme']}"><span class="visual-label{art_label}">Selected work</span>{data['art']}</div></section><section class="container case-content"><span class="section-label">Project notes</span><div class="case-copy"><h2>Context</h2><p>{escape(data['intro'])}</p><h2>My involvement</h2><p>{escape(data['involvement'])}</p><ul>{lis}</ul>'''
    if slug=='entrepreneurship-talks':
        doc+='''<div class="metric-strip"><div class="metric-item"><strong>65+</strong><span>Podcast episodes produced by the organisation</span></div><div class="metric-item"><strong>3M+</strong><span>Digital impressions across its media activity</span></div><div class="metric-item"><strong>€60k</strong><span>Erasmus+ KA153-YOU grant secured as coordinator</span></div></div><p><a class="underlink" href="https://www.entrepreneurshiptalks.org/" target="_blank" rel="noopener noreferrer">Visit Entrepreneurship Talks ↗</a></p>'''
    if slug=='adamow':
        doc+='''<p><a class="underlink" href="https://www.metlen.com/news/press-releases/mytilineos-signs-2nd-ccgt-project-in-poland/" target="_blank" rel="noopener noreferrer">Public project announcement ↗</a></p>'''
    doc+=f'''<p class="case-small">{escape(data['bottom'])}</p></div></section><div class="container related"><div class="eyebrow">Explore further</div><a href="../work.html">All selected work ↗</a></div></main>'''+footer(1)
    (ROOT/'projects').mkdir(exist_ok=True)
    (ROOT/'projects'/f'{slug}.html').write_text(doc,encoding='utf-8')

paths=['','work.html','about.html']+[f'projects/{slug}.html' for slug in CASES]
xml='''<?xml version="1.0" encoding="utf-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''+''.join(f'<url><loc>https://cvergados.com/{p}</loc></url>\n' for p in paths)+'</urlset>\n'
(ROOT/'sitemap.xml').write_text(xml,encoding='utf-8')
print('Wrote',len(paths),'HTML pages:',*[str(ROOT/p if p else ROOT/'index.html') for p in paths],sep='\n')
