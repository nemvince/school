function updateFavicon() {
  const link = document.createElement('link')

  link.rel = "icon"

  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    link.href = "assets/img/favicon/favicon-dark-mode.svg"
  } else {
    link.href = "assets/img/favicon/favicon-light-mode.svg"
  }
  document.head.appendChild(link);
}

updateFavicon()

function updateTheme() {
  document.querySelector("html").setAttribute("data-bs-theme",
  window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")
}

updateTheme()

const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
darkModeQuery.addEventListener('change', updateFavicon);
darkModeQuery.addEventListener('change', updateTheme)