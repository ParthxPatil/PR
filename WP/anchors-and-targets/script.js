// Smooth scroll with highlight effect on ToC links
document.querySelectorAll('.toc-sidebar a').forEach(link => {
  link.addEventListener('click', function (e) {
    document.querySelectorAll('.toc-sidebar a').forEach(l => l.style.background = '');
    this.style.background = '#3b1f6e';
  });
});

// Highlight active section in ToC on scroll
const sections = document.querySelectorAll('section[id]');
const tocLinks = document.querySelectorAll('.toc-sidebar a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    if (window.scrollY >= section.offsetTop - 80) {
      current = section.getAttribute('id');
    }
  });
  tocLinks.forEach(link => {
    link.style.background = '';
    if (link.getAttribute('href') === '#' + current) {
      link.style.background = '#3b1f6e';
    }
  });
});