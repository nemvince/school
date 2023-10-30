const quadratic = {
    input_a: document.getElementById('quadratic-input-a'),
    input_b: document.getElementById('quadratic-input-b'),
    input_c: document.getElementById('quadratic-input-c'),
    button: document.getElementById('quadratic-button'),
    solution_div: document.getElementById('quadratic-solution-div'),
    solution_1: document.getElementById('quadratic-solution-1'),
    solution_2: document.getElementById('quadratic-solution-2'),
    solution_problem: document.getElementById('quadratic-solution-problem'),
    bonus_checkbox: document.getElementById('quadratic-bonus-checkbox'),
    bonus_mode: false,
}

const toggleBonus = () => {
    quadratic.bonus_mode = !quadratic.bonus_mode;
    quadratic.bonus_checkbox.checked = quadratic.bonus_mode;
    console.log(quadratic.bonus_mode);
}

quadratic.bonus_checkbox.addEventListener('click', toggleBonus);

const doQuadratic = () => {
    const a = Number(quadratic.input_a.value);
    const b = Number(quadratic.input_b.value);
    const c = Number(quadratic.input_c.value);
    

    if (!quadratic.bonus_mode) {
        const discriminant = b ** 2 - 4 * a * c;
        if (discriminant < 0) {
            quadratic.solution_div.classList.add('hidden');
            quadratic.solution_problem.classList.remove('hidden');
        } else {
            const x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            const x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            quadratic.solution_1.innerHTML = `${x1}`;
            quadratic.solution_2.innerHTML = `${x2}`;
            quadratic.solution_div.classList.remove('hidden');
            quadratic.solution_problem.classList.add('hidden');
        }
    } else {
        quadratic.solution_problem.classList.add('hidden');
        const x1 = (-b + Math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
        const x2 = (-b - Math.sqrt(b ** 2 - 4 * a * c)) / (2 * a);
        quadratic.solution_div.classList.remove('hidden');
        quadratic.solution_1.innerHTML = `${x1}`;
        quadratic.solution_2.innerHTML = `${x2}`;
    }

};

quadratic.button.addEventListener('click', doQuadratic);
