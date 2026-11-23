#!/usr/bin/env python3
"""Dr. Amin Elghanam: static bilingual site builder, editorial refinement V4.
Grounded copy from the client's submitted professional profile. No unsupported booking claims.
Run: python build.py
"""
from pathlib import Path
from html import escape
import medical_content as src

ROOT=Path(__file__).resolve().parent
SERV=src.SERVICES
ED=src.EDUCATION
FEL=src.FELLOWSHIPS
COPY=src.COPY
NAV=['index.html','about.html','specialties.html','media.html','contact.html']
D={
'ar':{
 'navigation':'تصفح الموقع','home_label':'الرئيسية','about_label':'عن الدكتور','specialties_label':'التخصصات','media_label':'الفيديوهات','contact_label':'التواصل','view':'اكتشف المزيد','consultation':'الاستفسارات والمواعيد','language':'English','menu':'فتح القائمة','close_menu':'إغلاق القائمة',
 'hero_lead':'رعاية تبدأ بالثقة','hero_title':'دقة في العلم.<br><em>إنسانية في الرعاية.</em>','hero_body':'الدكتور أمين الغنام، استشاري جراحات المخ والأعصاب والعمود الفقري. خبرة أكاديمية وتدريب سريري في مصر وفرنسا، مع اهتمام بشرح خيارات العلاج بوضوح.','hero_cta':'تعرّف على التخصصات','hero_cta2':'عن الدكتور','hero_caption':'DR. AMIN ELGHANAM / NEUROSURGERY','hero_side':'NEUROSURGERY<br>SPINE SURGERY<br>INTERVENTIONAL CARE',
 'strip1':'جراحات المخ والأعصاب','strip2':'العمود الفقري والتدخل المحدود','strip3':'زمالات وتدريب في فرنسا',
 'intro_label':'مجالات الخبرة','intro_title':'خبرة متخصصة،<br><em>لكل حالة تفاصيلها.</em>','intro_body':'أربع مجموعات رئيسية من التخصصات توضح الحالات والإجراءات المذكورة في الملف المهني للدكتور.','area_bottom':'الاطلاع على التخصص',
 'bio_label':'تعرّف على الطبيب','bio_title':'مسار علمي يجمع<br><em>مصر وفرنسا.</em>','bio_body':'تشمل السيرة المهنية دكتوراه جراحة المخ والأعصاب، ودبلومات وزمالات إكلينيكية في مجالات جراحات المخ والأوعية الدموية والعمود الفقري والتقنيات محدودة التدخل.','bio_link':'اقرأ السيرة المهنية',
 'years_label':'مراحل من التدريب المتخصص','qualifications':'المؤهلات والزمالات','approach_label':'فلسفة الرعاية','approach_title':'قبل أي إجراء،<br><em>يأتي الفهم.</em>','approach_body':'المحتوى يساعد المريض على فهم طبيعة التخصصات والتحضير للاستشارة، ولا يحل محل التقييم السريري أو يقدم توصية علاجية فردية.','approach1':'الاستماع للتاريخ المرضي','approach2':'فهم الفحوصات وخيارات العلاج','approach3':'توضيح الخطوات المناسبة لكل حالة',
 'video_label':'مكتبة الفيديو','video_title':'المعرفة الطبية،<br><em>بلغة أقرب.</em>','video_body':'محتوى مصوّر ولقاءات شاركها الدكتور. تظهر الروابط الأصلية دون تغيير أو إضافة عناوين طبية غير مؤكدة.','view_media':'استعرض كل الفيديوهات',
 'cta_label':'تواصل معنا','cta_title':'ابدأ بسؤال.<br><em>وخُذ الخطوة التالية بوضوح.</em>','cta_body':'بيانات العيادات والمواعيد قيد التأكيد. يمكن الاطلاع على وسائل التواصل المتاحة حاليًا في صفحة التواصل.','cta_button':'التواصل والاستفسار',
 'interior_about_label':'السيرة المهنية','interior_about_title':'خبرة تتشكّل<br><em>بالعلم والممارسة.</em>','interior_about_body':'تعرف على المؤهلات الأكاديمية والزمالات الإكلينيكية والتدريب المتخصص للدكتور أمين الغنام.','about_story_label':'من هو د. أمين الغنام؟','about_story_title':'الدكتور أمين الغنام','about_story_body':'استشاري جراحات المخ والأعصاب والعمود الفقري. يشمل المسار الأكاديمي دكتوراه في جراحة المخ والأعصاب وتدريبًا تخصصيًا في مستشفيات جامعية بفرنسا، مع خبرة في جراحات المخ والأوعية الدموية والعمود الفقري.','about_story_detail':'وتشمل المجالات المذكورة في الملف المهني الجراحات الميكروسكوبية، جراحات العمود الفقري محدودة التدخل، القسطرة المخية، وإجراءات علاج بعض أنواع آلام الأعصاب.','education':'التعليم والشهادات','clinical':'الزمالات والتدريب السريري','study_note':'المؤهلات والسنوات من الملف المهني المقدم، وتحتاج اعتماد الصياغة النهائية قبل النشر العام.',
 'interior_spec_label':'التخصصات','interior_spec_title':'تخصصات دقيقة.<br><em>شرح واضح.</em>','interior_spec_body':'استكشف مجالات الخبرة والأمثلة على الحالات والإجراءات كما وردت في الملف المهني.','jump':'انتقل إلى التخصص','conditions':'الحالات والإجراءات','focus':'النهج والتقنيات','spec_notice':'تحديد ملاءمة العلاج يعتمد على تشخيص الحالة ومراجعة الطبيب، ولا تُعد المعلومات توصية علاجية فردية.',
 'interior_media_label':'فيديوهات ولقاءات','interior_media_title':'معرفة تُشاهَد.<br><em>وتُفهَم.</em>','interior_media_body':'مقاطع الفيديو المرسلة من الدكتور، مع روابط منصاتها الأصلية. يمكن إضافة وصف كل فيديو بعد اعتماد المحتوى.','watch':'شاهد على يوتيوب','facebook':'افتح على فيسبوك','video_sub':'قائمة الفيديوهات','social_sub':'مقاطع قصيرة','media_note':'قد تتطلب روابط فيسبوك تسجيل الدخول، وهي تفتح على المنصة الأصلية.',
 'interior_contact_label':'تواصل','interior_contact_title':'الخطوة التالية<br><em>تبدأ من هنا.</em>','interior_contact_body':'معلومات التواصل المهنية المتاحة حاليًا، مع مساحة جاهزة لإضافة العيادات ومواعيدها بمجرد اعتمادها.','email_label':'البريد الإلكتروني','email_body':'البريد المدون في الملف المهني للدكتور. يُراجع قبل الإطلاق العام.','send_email':'إرسال بريد إلكتروني','location_label':'العيادات والمواقع','location_body':'بانتظار تأكيد العناوين ومواعيد العيادات الجديدة من الفريق الطبي.','booking_label':'الحجز والاستفسارات','booking_body':'سيُضاف رقم الحجز أو واتساب عند اعتماد وسيلة التواصل الرسمية.','pending':'بانتظار الاعتماد','emergency':'تنبيه: الموقع تعريفي ولا يوفر تشخيصًا عن بعد أو خدمة طوارئ. في الحالات الطارئة تواصل مع خدمات الطوارئ المحلية.','footer_desc':'الملف المهني والتخصصات والمحتوى المرئي للدكتور أمين الغنام. المعلومات توعوية ولا تغني عن الاستشارة الطبية.','footer_end':'جميع الحقوق محفوظة','privacy':'لا تُدخل بيانات صحية شخصية في البريد الإلكتروني العام.',
 'medical_note':'معلومات عامة وليست تشخيصًا طبيًا','powered':'تصميم وتجربة رقمية للدكتور أمين الغنام','videos':'فيديو من يوتيوب','social':'مقطع على فيسبوك','read_more':'اكتشف التفاصيل','return_up':'للأعلى'
},
'en':{
 'navigation':'Explore the site','home_label':'Home','about_label':'About','specialties_label':'Specialties','media_label':'Videos','contact_label':'Contact','view':'Discover more','consultation':'Contact & inquiries','language':'العربية','menu':'Open menu','close_menu':'Close menu',
 'hero_lead':'Care begins with trust','hero_title':'Precision in science.<br><em>Humanity in care.</em>','hero_body':'Dr. Amin Elghanam is a Consultant Neurosurgeon and Spine Surgeon with academic qualifications and clinical training in Egypt and France, and a focus on clearly explaining care options.','hero_cta':'Explore specialties','hero_cta2':'Meet Dr. Amin','hero_caption':'DR. AMIN ELGHANAM / NEUROSURGERY','hero_side':'NEUROSURGERY<br>SPINE SURGERY<br>INTERVENTIONAL CARE',
 'strip1':'Brain & neurosurgery','strip2':'Spine & minimally invasive care','strip3':'Clinical fellowships in France',
 'intro_label':'Areas of expertise','intro_title':'Focused expertise.<br><em>Individual care.</em>','intro_body':'Four areas of practice, based on the procedures and conditions listed in Dr. Amin’s professional profile.','area_bottom':'Explore this specialty',
 'bio_label':'Meet your specialist','bio_title':'An academic journey<br><em>from Egypt to France.</em>','bio_body':'His professional profile includes a doctoral qualification in neurosurgery, specialized diplomas, and clinical fellowships in neurosurgery, cerebrovascular care, and minimally invasive spine procedures.','bio_link':'Discover the full profile',
 'years_label':'Milestones of advanced training','qualifications':'Qualifications & fellowships','approach_label':'Approach to care','approach_title':'Understanding comes<br><em>before intervention.</em>','approach_body':'This website provides general information about areas of practice and helps visitors prepare for consultations. It does not replace an individual clinical assessment.','approach1':'Understand the patient history','approach2':'Review investigations and options','approach3':'Explain the next steps clearly',
 'video_label':'Video library','video_title':'Medical knowledge,<br><em>made approachable.</em>','video_body':'Videos and interviews shared as source references for the website. Original links are preserved; specific medical titles await approval.','view_media':'Explore all videos',
 'cta_label':'Get in touch','cta_title':'A question is<br><em>a good place to begin.</em>','cta_body':'Current clinic locations and appointment schedules are being confirmed. Visit the contact page for available professional contact details.','cta_button':'Contact and inquiries',
 'interior_about_label':'Professional profile','interior_about_title':'A career shaped<br><em>by science and practice.</em>','interior_about_body':'Explore Dr. Amin Elghanam’s qualifications, clinical fellowships and specialist hospital training.','about_story_label':'Meet Dr. Amin Elghanam','about_story_title':'Dr. Amin Elghanam','about_story_body':'A Consultant Neurosurgeon and Spine Surgeon whose professional record includes a doctorate in neurosurgery and specialist training at university hospitals in France.','about_story_detail':'His listed areas of practice include microsurgery, minimally invasive spine surgery, cerebrovascular surgery and interventional approaches to selected types of nerve pain.','education':'Education and qualifications','clinical':'Clinical fellowships','study_note':'Dates and qualifications are taken from the submitted professional profile. Final terminology should be approved before public launch.',
 'interior_spec_label':'Specialties','interior_spec_title':'Specialized care.<br><em>Clearly explained.</em>','interior_spec_body':'Explore Dr. Amin’s recorded areas of expertise and examples of procedures and conditions, organized for easy reading.','jump':'Jump to specialty','conditions':'Conditions and procedures','focus':'Techniques and approach','spec_notice':'Treatment suitability depends on an individual clinical evaluation. This content is general information, not personal medical advice.',
 'interior_media_label':'Videos & insights','interior_media_title':'Knowledge to see.<br><em>And understand.</em>','interior_media_body':'The supplied videos link back to their original channels. Approved video descriptions may be added later.','watch':'Watch on YouTube','facebook':'Open on Facebook','video_sub':'Video collection','social_sub':'Short-form clips','media_note':'Facebook clips may require login and open on their original platform.',
 'interior_contact_label':'Contact','interior_contact_title':'The next step<br><em>starts here.</em>','interior_contact_body':'Available professional contact details, with clearly reserved space for confirmed clinic addresses, schedules and booking information.','email_label':'Email address','email_body':'This address is listed in the submitted professional profile and should be verified before public launch.','send_email':'Send an email','location_label':'Clinics & locations','location_body':'Updated clinic addresses and visiting schedules are awaiting confirmation from the medical team.','booking_label':'Appointments & inquiries','booking_body':'The official booking phone number or WhatsApp contact will be activated once confirmed.','pending':'Awaiting confirmation','emergency':'Notice: This informational website does not provide remote diagnosis or emergency services. For emergencies, contact local emergency services.','footer_desc':'The professional profile, specialties and video resources of Dr. Amin Elghanam. This site is educational and not a substitute for medical consultation.','footer_end':'All rights reserved','privacy':'Avoid sending private medical details to a general email address.',
 'medical_note':'Information only — not medical advice','powered':'Digital experience for Dr. Amin Elghanam','videos':'YouTube video','social':'Facebook clip','read_more':'Explore details','return_up':'Back to top'
}}
YOUTUBE=[('tbu3TAHza4w','01'),('DAtmoYU0274','02')]
FACEBOOK=['https://www.facebook.com/share/r/U3TqcRnqjkzUNo5D/','https://www.facebook.com/share/r/D5bntnGavaQSFnzt/','https://www.facebook.com/share/r/DzFtrmLGvPaHprPj/','https://www.facebook.com/share/r/bWp6guie797ae8vT/','https://www.facebook.com/share/r/q6EQXG8sgc4Rzopn/']

def esc(t):return escape(str(t),quote=True)
def root(l):return '' if l=='ar' else '../'
def link(l,p):return p
def langlink(l,p):return ('en/' if l=='ar' else '../')+p
def image(l,n):return root(l)+'assets/images/'+n
ICON_ARROW='<svg viewBox="0 0 24 24" width="19" height="19" aria-hidden="true"><path d="M4 12h16m-7-7 7 7-7 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_MENU='<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'
ICON_PLAY='<svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true"><path d="m9 5 10 7-10 7z" fill="currentColor"/></svg>'

def section_tag(text):return f'<span class="eyebrow"><span class="eyebrow-rule"></span>{text}</span>'
def btn(txt,href,typ='primary'):
 return f'<a class="btn btn--{typ}" href="{esc(href)}"><span>{txt}</span>{ICON_ARROW}</a>'

def header(l,p):
 d=D[l]
 navs=''.join(f'<a href="{f}"'+(' class="active" aria-current="page"' if p==f else '')+f'>{d[k+"_label"]}</a>' for f,k in zip(NAV,['home','about','specialties','media','contact']))
 return f'''<a href="#main" class="skip-link">Skip to content</a><div class="notice-bar"><div class="container"><span>AMIN ELGHANAM · NEUROSURGERY & SPINE</span><span class="notice-second">FRANCE / EGYPT</span></div></div>
 <header class="site-header" id="site-header"><div class="container header-inner"><a class="identity" href="index.html" aria-label="Dr Amin Elghanam"><span class="identity-mark"><img src="{root(l)}assets/amin-monogram.svg" width="52" height="52" alt="" aria-hidden="true"></span><span class="identity-name">DR. AMIN ELGHANAM<small>{'استشاري جراحات المخ والأعصاب والعمود الفقري' if l=='ar' else 'CONSULTANT NEUROSURGEON & SPINE SURGEON'}</small></span></a>
 <nav class="nav-links" id="primary-nav" aria-label="{d['navigation']}">{navs}<a href="contact.html" class="nav-cta">{d['consultation']} {ICON_ARROW}</a></nav>
 <div class="header-tools"><a class="lang-switch" href="{langlink(l,p)}" hreflang="{'en' if l=='ar' else 'ar'}">{d['language']}</a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="{d['menu']}">{ICON_MENU}</button></div></div></header>'''

def footer(l):
 d=D[l]
 navs=''.join(f'<a href="{f}">{d[k+"_label"]}</a>' for f,k in zip(NAV,['home','about','specialties','media','contact']))
 return f'''<footer class="footer"><div class="container"><div class="footer-top"><div class="footer-intro"><div class="footer-wordmark"><img src="{root(l)}assets/amin-monogram.svg" alt="" aria-hidden="true" width="48" height="48"><span class="footer-name">DR. AMIN <b>ELGHANAM.</b></span></div><p>{d['footer_desc']}</p></div><div class="footer-links"><span>EXPLORE</span>{navs}</div><div class="footer-links"><span>EXPERTISE</span>{''.join(f'<a href="specialties.html#{s["id"]}">{esc(s[l])}</a>' for s in SERV)}</div></div><div class="footer-bottom"><span>© DR. AMIN ELGHANAM. {d['footer_end']}.</span><span>{d['medical_note']}</span></div></div></footer><a class="to-top" href="#main" aria-label="{d['return_up']}">↑</a>'''

def document(l,p,title,desc,content):
 d=D[l];pref=root(l)
 other='en' if l=='ar' else 'ar'
 # Do not include devtools/extension-generated elements in source.
 return f'''<!DOCTYPE html><html lang="{l}" dir="{'rtl' if l=='ar' else 'ltr'}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#10283A"><title>{esc(title)} | Dr. Amin Elghanam</title><meta name="description" content="{esc(desc)}"><meta name="robots" content="noindex,nofollow"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)} | Dr. Amin Elghanam"><meta property="og:description" content="{esc(desc)}"><link rel="alternate" hreflang="{other}" href="{langlink(l,p)}"><link rel="icon" href="{pref}assets/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap" rel="stylesheet"><link rel="stylesheet" href="{pref}assets/css/styles.css"></head><body>{header(l,p)}<main id="main">{content}</main>{footer(l)}<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script><script defer src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script><script defer src="https://cdn.jsdelivr.net/npm/smoothscroll-polyfill@0.4.4/dist/smoothscroll.min.js"></script><script defer src="{pref}assets/js/site.js"></script></body></html>'''

def closing(l):
 d=D[l]
 return f'''<section class="end-cta"><div class="container end-cta-inner"><div>{section_tag(d['cta_label'])}<h2>{d['cta_title']}</h2><p>{d['cta_body']}</p></div>{btn(d['cta_button'],'contact.html','light')}</div></section>'''

def home(l):
 d=D[l]
 cards=''.join(f'''<a class="specialty-card specialty-card--{i+1}" href="specialties.html#{s['id']}" data-reveal><div class="card-top"><span class="card-type">NEUROSURGERY · SPINE</span><span class="card-arrow">{ICON_ARROW}</span></div><div class="specialty-icon">{'✦' if i==0 else '◌' if i==1 else '⊕' if i==2 else '⌁'}</div><div><h3>{esc(s[l])}</h3><p>{esc(s['intro_'+l])}</p><span class="card-read">{d['area_bottom']} {ICON_ARROW}</span></div></a>''' for i,s in enumerate(SERV))
 edu=''.join(f'<div class="small-credential"><strong class="credential-symbol" aria-hidden="true">✦</strong><span>{esc(title_ar if l=="ar" else title_en)}</span></div>' for year,title_ar,title_en,_,__ in [ED[0], ED[2], ED[3]])
 first_id=YOUTUBE[0][0]
 return f'''<section class="home-hero"><div class="container home-hero-grid"><div class="hero-copy"><div class="hero-kicker">{section_tag(d['hero_lead'])}</div><h1>{d['hero_title']}</h1><p>{d['hero_body']}</p><div class="hero-buttons">{btn(d['hero_cta'],'specialties.html')}{btn(d['hero_cta2'],'about.html','ghost')}</div><div class="hero-foot"><span class="pulse-dot"></span>{d['medical_note']}</div></div><div class="hero-photo"><div class="hero-photo-backdrop"></div><div class="hero-halo hero-halo--1"></div><div class="hero-halo hero-halo--2"></div><img src="{image(l,'dr-amin-cutout.webp')}" width="956" height="1280" fetchpriority="high" alt="Dr. Amin Elghanam" class="doctor-cutout"><div class="photo-label"><span>DR.</span><strong>AMIN<br>ELGHANAM</strong><small>CONSULTANT NEUROSURGEON</small></div><div class="medal"><span>FR</span><small>CLINICAL<br>TRAINING</small></div></div><div class="hero-aside">{d['hero_side']}</div></div><div class="hero-bottomline"><div class="container"><span>PERSONAL PORTFOLIO / MEDICAL PROFILE</span><span>SCROLL TO DISCOVER <span aria-hidden="true">↓</span></span></div></div></section>
<section class="cred-strip"><div class="container cred-strip-inner"><div><span class="strip-symbol" aria-hidden="true">✦</span>{d['strip1']}</div><div><span class="strip-symbol" aria-hidden="true">✦</span>{d['strip2']}</div><div><span class="strip-symbol" aria-hidden="true">✦</span>{d['strip3']}</div></div></section>
<section class="section expertise-home"><div class="container"><div class="section-heading"><div>{section_tag(d['intro_label'])}<h2>{d['intro_title']}</h2></div><p>{d['intro_body']}</p></div><div class="specialty-grid">{cards}</div></div></section>
<section class="section profile-feature"><div class="container profile-feature-grid"><div class="profile-visual" data-reveal><img src="{image(l,'dr-amin-speaking.webp')}" width="1280" height="914" loading="lazy" alt="Dr. Amin Elghanam during a medical talk"><div class="profile-photo-tag">NEUROSURGERY<br>AND SPINE SURGERY</div></div><div class="profile-content" data-reveal>{section_tag(d['bio_label'])}<h2>{d['bio_title']}</h2><p>{d['bio_body']}</p><div class="credential-stack">{edu}</div>{btn(d['bio_link'],'about.html','outline')}</div></div></section>
<section class="care-section"><div class="container care-grid"><div>{section_tag(d['approach_label'])}<h2>{d['approach_title']}</h2><p>{d['approach_body']}</p></div><div class="care-steps"><div><span aria-hidden="true">✧</span><strong>{d['approach1']}</strong></div><div><span aria-hidden="true">✧</span><strong>{d['approach2']}</strong></div><div><span aria-hidden="true">✧</span><strong>{d['approach3']}</strong></div></div></div><div class="care-orbit" aria-hidden="true"></div></section>
<section class="section media-teaser"><div class="container"><div class="section-heading"><div>{section_tag(d['video_label'])}<h2>{d['video_title']}</h2></div><p>{d['video_body']}</p></div><div class="media-teaser-grid"><a class="media-feature-image" target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v={first_id}" style="--cover:url('{image(l,'dr-amin-brand.webp')}')"><img src="{image(l,'dr-amin-brand.webp')}" width="1280" height="474" loading="lazy" alt="Dr. Amin Elghanam video reference"><span class="play-control">{ICON_PLAY}</span><span class="media-counter">WATCH VIDEO</span></a><div class="media-teaser-copy"><span class="meta-small">YOUTUBE · VIDEO</span><h3>{d['videos']}</h3><p>{d['video_body']}</p>{btn(d['view_media'],'media.html','outline')}</div></div></div></section>{closing(l)}'''

def page_hero(l,kind,portrait=False):
 d=D[l];t=d['interior_'+kind+'_title'];subtitle=d['interior_'+kind+'_body'];k=d['interior_'+kind+'_label']
 photo=(f'<div class="page-hero-photo"><img src="{image(l,"dr-amin-whitecoat.webp" if kind!="about" else "dr-amin-speaking.webp")}" alt="Dr. Amin Elghanam" loading="eager"></div>' if portrait else f'<div class="page-hero-decoration" aria-hidden="true"><img src="{root(l)}assets/amin-monogram.svg" width="190" height="190" alt=""></div>')
 return f'''<section class="page-hero page-hero--{kind}"><div class="container page-hero-grid"><div><div class="breadcrumb"><a href="index.html">{d['home_label']}</a><span>/</span><strong>{k}</strong></div>{section_tag(k)}<h1>{t}</h1><p>{subtitle}</p></div>{photo}</div></section>'''

def about(l):
 d=D[l]
 ed=''.join(f'''<article class="history-item" data-reveal><div class="history-year">{esc(e[0])}</div><div><h3>{esc(e[1] if l=='ar' else e[2])}</h3><p>{esc(e[3] if l=='ar' else e[4])}</p></div></article>''' for e in sorted(ED,key=lambda e:int(e[0][:4]),reverse=True))
 fel=''.join(f'''<article class="fellowship" data-reveal><div class="fellowship-year">{esc(e[0])}</div><h3>{esc(e[1] if l=='ar' else e[2])}</h3><p>{esc(e[3] if l=='ar' else e[4])}</p></article>''' for e in sorted(FEL,key=lambda e:int(e[0][:4]),reverse=True))
 return f'''{page_hero(l,'about',True)}<section class="section about-story"><div class="container about-story-grid"><div class="about-photo" data-reveal><img src="{image(l,'dr-amin-speaking.webp')}" alt="Dr. Amin Elghanam" width="1280" height="914" loading="lazy"><span>DR. AMIN ELGHANAM / NEUROSURGERY</span></div><div class="about-story-copy" data-reveal>{section_tag(d['about_story_label'])}<h2>{d['about_story_title']}</h2><p>{d['about_story_body']}</p><p>{d['about_story_detail']}</p><div class="profile-seals"><span>MD / PhD</span><span>MICROSURGERY</span><span>SPINE</span></div></div></div></section>
<section class="section education-section"><div class="container education-grid"><div class="sticky-heading">{section_tag('ACADEMIC BACKGROUND')}<h2>{d['education']}</h2><p>{d['years_label']}</p></div><div class="history">{ed}</div></div></section>
<section class="section fellowships-section"><div class="container">{section_tag('CLINICAL TRAINING')}<h2 class="section-large-heading">{d['clinical']}</h2><div class="fellowship-grid">{fel}</div><p class="source-footnote">{d['study_note']}</p></div></section>{closing(l)}'''

def specialties(l):
 d=D[l]
 quick=''.join(f'<a href="#{s["id"]}" class="index-pill"><span aria-hidden="true" class="index-symbol">✦</span>{esc(s[l])}{ICON_ARROW}</a>' for s in SERV)
 panels=''
 for i,s in enumerate(SERV):
  items=''.join(f'<li>{esc(item)}</li>' for item in s['items_'+l])
  panels+=f'''<section class="specialty-detail" id="{s['id']}"><div class="detail-top"><span class="detail-index">{d['specialties_label']}</span><span class="detail-decoration">{'✦' if i==0 else '◌' if i==1 else '⊕' if i==2 else '⌁'}</span></div><h2>{esc(s[l])}</h2><p class="detail-desc">{esc(s['intro_'+l])}</p><div class="detail-content"><div><h3>{d['conditions']}</h3><ul>{items}</ul></div><div class="focus-box"><span>{d['focus']}</span><p>{esc(s['focus_'+l])}</p></div></div></section>'''
 return f'''{page_hero(l,'spec')}<section class="specialty-page"><div class="container specialty-page-grid"><aside class="specialty-sidebar"><div class="sidebar-sticky"><span class="eyebrow">{d['jump']}</span><nav aria-label="{d['jump']}">{quick}</nav></div></aside><div class="specialty-panels">{panels}<div class="specialty-advisory">{d['spec_notice']}</div></div></div></section>{closing(l)}'''

def media(l):
 d=D[l]
 cards=''
 for id,num in YOUTUBE:
  cards+=f'''<a href="https://www.youtube.com/watch?v={id}" target="_blank" rel="noopener noreferrer" class="media-card" data-reveal><div class="media-card-image"><img src="{image(l,'dr-amin-brand.webp' if num=='01' else 'dr-amin-speaking.webp')}" alt="Dr. Amin Elghanam" loading="lazy"><span class="play-control">{ICON_PLAY}</span><span class="media-number">YOUTUBE VIDEO</span></div><div class="media-card-text"><span>{d['videos']}</span><strong>{d['watch']} {ICON_ARROW}</strong></div></a>'''
 soc=''.join(f'''<a class="social-video" href="{esc(url)}" target="_blank" rel="noopener noreferrer"><span>FACEBOOK REELS</span><strong>{d['social']}</strong>{ICON_ARROW}</a>''' for i,url in enumerate(FACEBOOK,1))
 return f'''{page_hero(l,'media')}<section class="section media-page"><div class="container">{section_tag('YOUTUBE')}<h2 class="section-large-heading">{d['video_sub']}</h2><div class="media-card-grid">{cards}</div><div class="social-heading">{section_tag('FACEBOOK REELS')}<h2 class="section-large-heading">{d['social_sub']}</h2><p>{d['media_note']}</p></div><div class="social-video-grid">{soc}</div></div></section>{closing(l)}'''

def contact(l):
 d=D[l]
 return f'''{page_hero(l,'contact')}<section class="section contact-page"><div class="container contact-grid"><div class="contact-main" data-reveal>{section_tag(d['email_label'])}<h2>{d['email_label']}</h2><p>{d['email_body']}</p><a class="contact-email-link" href="mailto:amin.elghanam@gmail.com">amin.elghanam@gmail.com {ICON_ARROW}</a>{btn(d['send_email'],'mailto:amin.elghanam@gmail.com','light')}<p class="contact-privacy">{d['privacy']}</p></div><div class="contact-side"><div class="contact-info" data-reveal><h3>{d['location_label']}</h3><p>{d['location_body']}</p><span class="pending">◌ {d['pending']}</span></div><div class="contact-info" data-reveal><h3>{d['booking_label']}</h3><p>{d['booking_body']}</p><span class="pending">◌ {d['pending']}</span></div></div></div><div class="container"><div class="emergency-note"><span>!</span><p>{d['emergency']}</p></div></div></section>'''

def build():
 for l in ('ar','en'):
  out=ROOT if l=='ar' else ROOT/'en'
  out.mkdir(exist_ok=True)
  for f,gen,title,desc in [
   ('index.html',home,D[l]['home_label'],D[l]['hero_body']),
   ('about.html',about,D[l]['about_label'],D[l]['interior_about_body']),
   ('specialties.html',specialties,D[l]['specialties_label'],D[l]['interior_spec_body']),
   ('media.html',media,D[l]['media_label'],D[l]['interior_media_body']),
   ('contact.html',contact,D[l]['contact_label'],D[l]['interior_contact_body'])]:
   (out/f).write_text(document(l,f,title,desc,gen(l)),encoding='utf-8')
 print('Rendered 10 responsive HTML pages')
if __name__=='__main__':build()
