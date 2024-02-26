const products = {
  alma: { price: 150, displayName: "Alma" },
  korte: { price: 200, displayName: "Körte" },
  szilva: { price: 250, displayName: "Szilva" },
  barack: { price: 300, displayName: "Barack" },
  dinnye: { price: 350, displayName: "Dinnye" },
  szolo: { price: 400, displayName: "Szőlő" },
  cseresznye: { price: 450, displayName: "Cseresznye" },
  meggy: { price: 500, displayName: "Meggy" },
  malna: { price: 550, displayName: "Málna" },
};

const elements = {
  cart: document.getElementById("cart"),
  products: document.getElementById("products"),
};

let cart = {};

function addToCart(productName) {
  if (cart[productName]) {
    cart[productName]++;
  } else {
    cart[productName] = 1;
  }
  renderCart();
}

function removeFromCart(productName) {
  if (cart[productName]) {
    cart[productName]--;
  }
  if (cart[productName] === 0) {
    delete cart[productName];
  }
  renderCart();
}

function renderCart() {
  elements.cart.innerHTML = "";
  Object.keys(cart).forEach((productName) => {
    const product = products[productName];
    const productElement = document.createElement("div");
    productElement.innerHTML = `
      <div>
        <button onclick="removeFromCart('${productName}')">-</button>
        ${product.displayName} (${cart[productName]} db)
        <button onclick="addToCart('${productName}')">+</button>
      </div>
    `;
    elements.cart.appendChild(productElement);
  });
}

function renderProducts() {
  elements.products.innerHTML = "";
  Object.keys(products).forEach((productName) => {
    const product = products[productName];
    const productElement = document.createElement("div");
    productElement.innerHTML = `
      <div>
        <button onclick="addToCart('${productName}')">+</button>
        ${product.displayName} (${product.price} Ft)
      </div>
    `;
    elements.products.appendChild(productElement);
  });
}

renderProducts();