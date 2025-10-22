// Menu mobile simple
(function(){
  const button = document.querySelector('.btn-mobile-toggle');
  // noop if not present — files restent simples
})();

// Small reveal effect
document.addEventListener('DOMContentLoaded', function(){
  const els = document.querySelectorAll('.card, .service-card, .proj-card');
  const onScroll = () =>{
    const top = window.innerHeight * 0.85;
    els.forEach(el=>{
      if(el.getBoundingClientRect().top < top) el.style.opacity = 1;
      else el.style.opacity = 0.12;
    })
  };
  onScroll(); window.addEventListener('scroll', onScroll);
});
