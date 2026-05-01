function addToCart(btn) {
  btn.textContent = '✓ Added!';
  btn.classList.add('added');
  btn.disabled = true;
  setTimeout(() => {
    btn.textContent = 'Add to Cart';
    btn.classList.remove('added');
    btn.disabled = false;
  }, 2000);
}