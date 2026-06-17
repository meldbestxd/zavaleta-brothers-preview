const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const open = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
}

const modal = document.getElementById('contact-options');
const openModal = (event) => {
  if (event) event.preventDefault();
  if (!modal) return;
  modal.hidden = false;
  document.body.style.overflow = 'hidden';
  const first = modal.querySelector('a, button');
  if (first) first.focus({ preventScroll: true });
};
const closeModal = () => {
  if (!modal) return;
  modal.hidden = true;
  document.body.style.overflow = '';
};
document.querySelectorAll('.contact-choice-trigger').forEach((trigger) => {
  trigger.addEventListener('click', openModal);
});
document.querySelectorAll('[data-close-modal]').forEach((control) => {
  control.addEventListener('click', closeModal);
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') closeModal();
});

const filterButtons = document.querySelectorAll('.filter-button');
const projectCards = document.querySelectorAll('.project-card');
filterButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filterButtons.forEach((btn) => btn.classList.toggle('active', btn === button));
    projectCards.forEach((card) => {
      const show = filter === 'all' || card.dataset.category === filter;
      card.hidden = !show;
    });
  });
});
