/* progressive enhancement: site works without CDN scripts */
(() => {
  'use strict';
  const $ = (s, root=document) => root.querySelector(s);
  const $$ = (s, root=document) => [...root.querySelectorAll(s)];
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const year = $('#current-year'); if (year) year.textContent = String(new Date().getFullYear());
  const header = $('#site-header');
  const nav = $('#site-nav');
  const toggle = $('#nav-toggle');
  const topButton = $('#to-top');
  const progress = $('#header-progress');

  function onScroll() {
    const y = window.scrollY;
    header?.classList.toggle('is-scrolled', y > 18);
    topButton?.classList.toggle('visible', y > 500);
    if (progress) {
      const max = Math.max(1, document.documentElement.scrollHeight - innerHeight);
      progress.style.width = `${Math.min(100, y / max * 100)}%`;
    }
  }
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  function closeMenu() {
    nav?.classList.remove('is-open');
    toggle?.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('no-scroll');
  }
  toggle?.addEventListener('click', () => {
    const open = !nav.classList.contains('is-open');
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('no-scroll', open && innerWidth <= 900);
  });
  $$('#site-nav a').forEach(link => link.addEventListener('click', closeMenu));
  addEventListener('resize', () => { if (innerWidth > 900) closeMenu(); }, { passive: true });
  topButton?.addEventListener('click', () => scrollTo({ top: 0, behavior: reducedMotion ? 'auto' : 'smooth' }));
  if ('smoothscroll' in window) window.smoothscroll.polyfill();

  $$('.faq-item button').forEach(button => {
    const panel = document.getElementById(button.getAttribute('aria-controls'));
    button.addEventListener('click', () => {
      const shouldOpen = button.getAttribute('aria-expanded') !== 'true';
      $$('.faq-item button').forEach(b => {
        b.setAttribute('aria-expanded', 'false');
        const p = document.getElementById(b.getAttribute('aria-controls'));
        if (p) p.style.maxHeight = '0px';
      });
      button.setAttribute('aria-expanded', String(shouldOpen));
      if (panel) panel.style.maxHeight = shouldOpen ? `${panel.scrollHeight + 16}px` : '0px';
    });
  });

  const modal = $('#video-modal');
  const frame = $('#video-frame');
  let returnFocus = null;
  const allowedVideoIds = new Set(['tbu3TAHza4w', 'DAtmoYU0274']);
  function closeVideo() {
    if (!modal) return;
    modal.setAttribute('aria-hidden', 'true');
    if (frame) frame.removeAttribute('src');
    document.body.classList.remove('no-scroll');
    returnFocus?.focus();
  }
  $$('[data-video]').forEach(b => b.addEventListener('click', () => {
    const id = b.getAttribute('data-video');
    if (!allowedVideoIds.has(id) || !modal || !frame) return;
    returnFocus = b;
    frame.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0`;
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('no-scroll');
    $('#video-close')?.focus();
  }));
  $('#video-close')?.addEventListener('click', closeVideo);
  modal?.addEventListener('click', e => { if (e.target === modal) closeVideo(); });
  addEventListener('keydown', e => {
    if (e.key === 'Escape') { closeVideo();closeMenu(); }
    if (e.key === 'Tab' && modal?.getAttribute('aria-hidden') === 'false') {
      e.preventDefault();$('#video-close')?.focus();
    }
  });

  // ScrollTrigger animations: no hidden content until GSAP is confirmed loaded.
  function animate() {
    if (reducedMotion || !window.gsap || !window.ScrollTrigger) return;
    document.documentElement.classList.add('motion-safe');
    gsap.registerPlugin(ScrollTrigger);
    const hero = $('.hero');
    if (hero) {
      gsap.from('.hero-content > *', { y: 34, opacity: 0, duration: 1.0, stagger: .105, ease: 'power3.out', delay: .12, clearProps: 'all' });
      gsap.from('.hero-doctor', { y: 50, opacity: 0, scale: .95, duration: 1.4, ease: 'power3.out', delay: .20, clearProps: 'opacity' });
      gsap.from('.hero-circle', { scale: .85, opacity: 0, duration: 1.2, ease: 'power3.out', delay: .05 });
      gsap.to('.hero-ring', { rotation: '+=30', duration: 35, ease: 'none', repeat: -1 });
      gsap.to('.hero-orbit', { y: -15, duration: 3, ease: 'sine.inOut', repeat: -1, yoyo: true });
      gsap.to('.hero-doctor', { y: 24, scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: .65 } });
    }
    $$('[data-reveal]').forEach(el => {
      gsap.from(el, { y: 42, opacity: 0, duration: .9, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 90%', once: true } });
    });
    $$('.specialty-card,.credential-card,.journey-step').forEach((el,i) => {
      gsap.from(el, { y: 28, opacity: 0, duration: .68, delay: (i%4)*.065, scrollTrigger: { trigger: el, start: 'top 94%', once: true } });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', animate);
  else animate();

  // Subtle WebGL wireframe sculpture. Progressive; lazy and disabled for touch / reduced motion.
  const canvasHost = $('#hero-three');
  if (canvasHost && !reducedMotion && matchMedia('(min-width: 901px)').matches) {
    import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js').then(THREE => {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(35, 1, .1, 100);
      camera.position.z = 9;
      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: 'low-power' });
      renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5));
      renderer.setClearColor(0x000000,0);
      canvasHost.appendChild(renderer.domElement);
      const group = new THREE.Group(); scene.add(group);
      const mat = new THREE.MeshBasicMaterial({ color: 0xb9765e, wireframe: true, transparent: true, opacity: .24 });
      const ringMat = new THREE.MeshBasicMaterial({ color: 0x6d94ac, wireframe: true, transparent: true, opacity: .22 });
      const torus = new THREE.Mesh(new THREE.TorusKnotGeometry(1.65,.16,150,12,2,3),mat);
      group.add(torus);
      const mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(2.2,1),ringMat);
      group.add(mesh);
      group.position.set(-1.55,.3,0);
      let stop=false, req=0;
      function size() { const r=canvasHost.getBoundingClientRect(); if(r.width&&r.height){renderer.setSize(r.width,r.height);camera.aspect=r.width/r.height;camera.updateProjectionMatrix();} }
      size();
      const resize = new ResizeObserver(size);resize.observe(canvasHost);
      function tick(){if(stop)return;req=requestAnimationFrame(tick);torus.rotation.y+=.0022;torus.rotation.x+=.001;mesh.rotation.y-=.0008;renderer.render(scene,camera);}
      tick();
      document.addEventListener('visibilitychange',()=>{if(document.hidden){stop=true;cancelAnimationFrame(req);}else if(stop){stop=false;tick();}});
      window.addEventListener('pagehide',()=>{stop=true;cancelAnimationFrame(req);resize.disconnect();renderer.dispose();});
    }).catch(() => {});
  }
})();
