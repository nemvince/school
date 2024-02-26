const arithmetic = {
    input_a: document.getElementById('arithmetic-input-a'),
    input_b: document.getElementById('arithmetic-input-b'),
    button: document.getElementById('arithmetic-button'),
    addition: document.getElementById('addition'),
    subtraction: document.getElementById('subtraction'),
    multiplication: document.getElementById('multiplication'),
    division: document.getElementById('division'),
    floor_division: document.getElementById('floor-division'),
    remainder: document.getElementById('remainder'),
    exponentiation: document.getElementById('exponentiation'),
}

const doArithmetic = () => {
    const a = Number(arithmetic.input_a.value);
    const b = Number(arithmetic.input_b.value);

    arithmetic.addition.innerHTML = a + b;
    arithmetic.subtraction.innerHTML = a - b;
    arithmetic.multiplication.innerHTML = a * b;
    arithmetic.division.innerHTML = a / b;
    arithmetic.floor_division.innerHTML = Math.floor(a / b);
    arithmetic.remainder.innerHTML = a % b;
    arithmetic.exponentiation.innerHTML = a ** b;
};

arithmetic.button.addEventListener('click', doArithmetic);
