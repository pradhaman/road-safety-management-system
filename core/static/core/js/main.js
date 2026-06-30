// Road Safety Management System — front-end interactivity

document.addEventListener('DOMContentLoaded', function () {

  // ---- Mobile nav toggle ----
  const toggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });
  }

  // ---- Auto-dismiss alerts after 6s ----
  document.querySelectorAll('.alert[data-autohide]').forEach(function (el) {
    setTimeout(function () {
      el.style.transition = 'opacity 0.4s ease';
      el.style.opacity = '0';
      setTimeout(function () { el.remove(); }, 400);
    }, 6000);
  });

  // ---- Photo preview on hazard report form ----
  const photoInput = document.getElementById('id_photo');
  const previewBox = document.getElementById('photoPreview');
  if (photoInput && previewBox) {
    photoInput.addEventListener('change', function (e) {
      const file = e.target.files[0];
      if (!file) { previewBox.innerHTML = ''; return; }
      const reader = new FileReader();
      reader.onload = function (ev) {
        previewBox.innerHTML = '<img src="' + ev.target.result + '" alt="Photo preview" style="max-width:100%;border-radius:4px;margin-top:10px;">';
      };
      reader.readAsDataURL(file);
    });
  }

  // ---- Confirm before deleting a report ----
  document.querySelectorAll('[data-confirm]').forEach(function (el) {
    el.addEventListener('click', function (e) {
      if (!confirm(el.getAttribute('data-confirm'))) {
        e.preventDefault();
      }
    });
  });

  // ---- Live character count for hazard description ----
  const desc = document.getElementById('id_description');
  const counter = document.getElementById('descCounter');
  if (desc && counter) {
    const update = () => { counter.textContent = desc.value.length + ' characters'; };
    desc.addEventListener('input', update);
    update();
  }
});
