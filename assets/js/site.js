/* Progressive enhancement. All links/content work with JS disabled. */
(() => {
  'use strict';
  const one = (s, ctx = document) => ctx.querySelector(s);
  const all = (s, ctx = document) => Array.from(ctx.querySelectorAll(s));
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const header = one('#site-header');
  const nav = one('#main-nav');
  const toggle = one('.nav-toggle');
  const back = one('#back-top');
  const year = one('#year');
  if (year) year.textContent = String(new Date().getFullYear());

  const onScroll = () => {
    header?.classList.toggle('is-scrolled', window.scrollY > 20);
    back?.classList.toggle('is-visible', window.scrollY > 520);
  };
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();
  function closeNav() {
    nav?.classList.remove('is-open');
    toggle?.setAttribute('aria-expanded','false');
    document.body.classList.remove('no-scroll');
  }
  toggle?.addEventListener('click', () => {
    if (!nav) return;
    const isOpen = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded',String(isOpen));
    document.body.classList.toggle('no-scroll',isOpen && innerWidth <= 930);
  });
  all('.nav a').forEach(a=>a.addEventListener('click', closeNav));
  window.addEventListener('resize',()=>{if(innerWidth>930)closeNav();},{passive:true});
  back?.addEventListener('click',()=>window.scrollTo({top:0,behavior:reduced?'auto':'smooth'}));
  // No-op if the polyfill CDN is unavailable.
  if (window.smoothscroll?.polyfill) window.smoothscroll.polyfill();

  const videoDialog = one('#video-dialog');
  const frame = one('#video-frame');
  const ids = new Set(['tbu3TAHza4w','DAtmoYU0274']);
  let lastFocus = null;
  function closeVideo() {
    if (!videoDialog) return;
    videoDialog.hidden = true;
    if(frame)frame.removeAttribute('src');
    document.body.classList.remove('no-scroll');
    lastFocus?.focus();
  }
  all('[data-video]').forEach(el => el.addEventListener('click',()=>{
    const id=el.getAttribute('data-video');
    if(!ids.has(id) || !videoDialog || !frame)return;
    lastFocus=el;
    frame.src='https://www.youtube-nocookie.com/embed/'+encodeURIComponent(id)+'?autoplay=1&rel=0';
    videoDialog.hidden=false;
    document.body.classList.add('no-scroll');
    one('#video-close')?.focus();
  }));
  one('#video-close')?.addEventListener('click',closeVideo);
  videoDialog?.addEventListener('click', e => {if(e.target === videoDialog)closeVideo();});
  document.addEventListener('keydown', e=>{
    if(e.key==='Escape'){closeVideo();closeNav();}
    if(e.key==='Tab' && videoDialog && !videoDialog.hidden){
      e.preventDefault();one('#video-close')?.focus();
    }
  });

  const copy = one('#copy-email');
  copy?.addEventListener('click', async () => {
    const value=copy.dataset.copy || '';
    if (!value) return;
    try {
      if (navigator.clipboard?.writeText) await navigator.clipboard.writeText(value);
      else {
        const el=document.createElement('textarea');el.value=value;el.style.position='fixed';el.style.opacity='0';document.body.appendChild(el);el.select();
        if (!document.execCommand('copy'))throw Error('copy failed');el.remove();
      }
      copy.textContent=copy.dataset.copied||'Copied';
    } catch {
      window.prompt('Copy email:', value);
    }
  });

  function initGsap() {
    if(reduced || !window.gsap || !window.ScrollTrigger) return;
    const {gsap,ScrollTrigger}=window;
    gsap.registerPlugin(ScrollTrigger);
    if(one('.hero')){
      gsap.from('[data-hero]',{autoAlpha:0,y:26,duration:1,stagger:.11,ease:'power3.out',clearProps:'all'});
      gsap.from('.hero-person',{autoAlpha:0,y:32,duration:1.25,ease:'power3.out',delay:.18,clearProps:'all'});
      gsap.to('.hero-contour',{rotation:50,duration:32,ease:'none',repeat:-1});
    }
    all('[data-reveal]').forEach(el=>{
      gsap.from(el,{autoAlpha:0,y:27,duration:.82,ease:'power2.out',scrollTrigger:{trigger:el,start:'top 94%',once:true},clearProps:'all'});
    });
  }
  try{initGsap();}catch(e){console.warn('Animation fallback active.',e);}

  // Tiny progressive 3D sculpture, intentionally not an essential UI component.
  const host=one('#hero-three');
  if(!host || reduced || !window.matchMedia('(min-width: 931px)').matches)return;
  import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js')
    .then(T=>{
      const scene=new T.Scene(),camera=new T.PerspectiveCamera(37,1,.1,100);camera.position.z=8;
      const renderer=new T.WebGLRenderer({alpha:true,antialias:true,powerPreference:'low-power'});
      renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.5));host.appendChild(renderer.domElement);
      const group=new T.Group();scene.add(group);group.position.set(.7,0,0);
      const mat=new T.MeshBasicMaterial({color:0xffffff,wireframe:true,transparent:true,opacity:.56});
      const torus=new T.Mesh(new T.TorusGeometry(2,.014,8,120),mat);torus.rotation.x=.65;group.add(torus);
      const torus2=new T.Mesh(new T.TorusGeometry(1.65,.012,8,120),mat);torus2.rotation.y=.8;group.add(torus2);
      let raf=0,alive=true;
      function resize(){let r=host.getBoundingClientRect();if(r.width && r.height){renderer.setSize(r.width,r.height);camera.aspect=r.width/r.height;camera.updateProjectionMatrix();}}
      resize();const observer=new ResizeObserver(resize);observer.observe(host);
      function tick(){if(!alive||document.hidden)return;raf=requestAnimationFrame(tick);group.rotation.y+=.0015;group.rotation.z+=.00045;renderer.render(scene,camera);}
      tick();
      document.addEventListener('visibilitychange',()=>{cancelAnimationFrame(raf);if(!document.hidden)tick();});
      window.addEventListener('pagehide',()=>{alive=false;cancelAnimationFrame(raf);observer.disconnect();torus.geometry.dispose();torus2.geometry.dispose();mat.dispose();renderer.dispose();},{once:true});
    }).catch(()=>{});
})();
