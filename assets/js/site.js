/* Progressive enhancement, never hide critical content behind animation. */
(()=>{'use strict';
 const $=(sel,ctx=document)=>ctx.querySelector(sel);
 const header=$('#site-header');const menu=$('.menu-toggle');const nav=$('#primary-nav');
 if(menu&&nav){
  const close=()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');document.body.classList.remove('menu-open');};
  menu.addEventListener('click',()=>{const next=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(next));nav.classList.toggle('open',next);});
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));
  window.addEventListener('keydown',ev=>{if(ev.key==='Escape')close()});
  window.addEventListener('resize',()=>{if(innerWidth>980)close()},{passive:true});
 }
 const top=$('.to-top');const sync=()=>{header?.classList.toggle('scrolled',window.scrollY>25);top?.classList.toggle('visible',window.scrollY>600)};
 window.addEventListener('scroll',sync,{passive:true});sync();
 const year=$('#copyright-year');if(year)year.textContent=String(new Date().getFullYear());
 try{window.__drAminSmoothScrollPolyfill?.polyfill?.();window.smoothscroll?.polyfill?.()}catch(_){}
 const reduce=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
 if(!reduce && window.gsap && window.ScrollTrigger){
  const g=window.gsap;g.registerPlugin(window.ScrollTrigger);
  g.utils.toArray('[data-reveal]').forEach(el=>{
   g.fromTo(el,{opacity:0,y:26},{opacity:1,y:0,duration:.95,ease:'power2.out',clearProps:'transform,opacity',scrollTrigger:{trigger:el,start:'top 93%',once:true}});
  });
  const halo=$('.hero-halo--1');if(halo)g.to(halo,{rotate:360,duration:80,repeat:-1,ease:'none'});
  const halo2=$('.hero-halo--2');if(halo2)g.to(halo2,{rotate:-360,duration:95,repeat:-1,ease:'none'});
 }
 // Mobile/tablet rendering remains usable without GSAP/CDN.
})();
