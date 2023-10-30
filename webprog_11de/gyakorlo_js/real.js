const real_numbers = {
    input: document.getElementById('real-numbers-input'),
    button: document.getElementById('real-numbers-button'),
    sin: document.getElementById('real-numbers-sin'),
    cos: document.getElementById('real-numbers-cos'),
    tan: document.getElementById('real-numbers-tan'),
    problem: document.getElementById('real-numbers-problem'),
}

const doRealNumbers = () => {
    const x = parseFloat(real_numbers.input.value);

    if (isNaN(x)) {
        real_numbers.sin.innerHTML = '';
        real_numbers.cos.innerHTML = '';
        real_numbers.tan.innerHTML = '';
        real_numbers.problem.classList.remove('hidden');
    } else {
        real_numbers.problem.classList.add('hidden');
        real_numbers.sin.innerHTML = Math.sin(x);
        real_numbers.cos.innerHTML = Math.cos(x);
        real_numbers.tan.innerHTML = Math.tan(x);
    
    }
};

real_numbers.button.addEventListener('click', doRealNumbers);