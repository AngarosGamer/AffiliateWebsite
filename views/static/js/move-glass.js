// Used in 404 page.
// Displaces magnifying glass in a "search" pattern with random movement.

const glass = document.getElementById('magnifying-glass');

let x_invert = false; // On average, make x position change signs each cycle for greater spreads
let y_invert = false; // On average, make x position change signs each cycle for greater spreads

setInterval(() => {

    const x = Math.random() * 20 * (x_invert? -1 : 1); // Random horizontal position, within 50px of origin
    const y = Math.random() * 20 * (y_invert? -1 : 1); // Random vertical position, within 50px of origin


    // The following lines were added after noticing glass often moves diagonally repetitively.
    // Instead, we want a semi-random spread that often goes around from one place to another.
    if (Math.random() >= 0.5) x_invert = !x_invert; // At random intervals, flip the inversion to induce more variety
    if (Math.random() >= 0.5) y_invert = !y_invert; // At random intervals, flip the inversion to induce more variety


    glass.style.transform = `translate(${x}px, ${y}px)`; // Move the glass around with translate.
}, 1500);
