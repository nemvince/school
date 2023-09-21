//  <li class="nav-item">
//   <a class="nav-link">Active</a>
// </li>

const navbar = document.getElementById('navbar');


const h2Elements = document.querySelectorAll('h2');

h2Elements.forEach(function(h2Element) {
  let listElement = document.createElement('li');
  let aElement = document.createElement('a');

  aElement.href = `#${h2Element.id}`;
  aElement.textContent = h2Element.textContent;
  aElement.classList.add('nav-link')

  listElement.classList.add('nav-item')
  listElement.appendChild(aElement);
  

  navbar.appendChild(listElement);
  console.log(h2Element.id);
});