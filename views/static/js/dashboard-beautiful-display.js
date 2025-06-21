/*

 This file handles the visual "beautiful-displays" in the main dashboard.
 Note: The amount of bars displayed depends on the screen width (for some limited compatibility with smaller screens).

*/

// Define a function on which we apply callbacks and listeners
const initializeBeautifulDisplays = () => {
    // Access all cards that contain our elements
    document.querySelectorAll('.card-right').forEach(container_width => {
        // Grab the display under the card
        const display = container_width.querySelector('.beautiful-display');
        let cardRightWidth = container_width.offsetWidth; // Get display current width
        display.innerHTML = ''; // Generate empty container

        const width = 5;
        const gap = 5;

        let max = Math.floor(cardRightWidth / (width + gap));
        let numBars = Math.min(15, max); // 15 bars max

        const isPositive = true;
        const colors = isPositive ? ['#afd430', '#53a626'] : ['#ffb6b6', '#ff8888'];

        for (let i = 0; i < numBars; i++) { // Spawn bars
            const bar = document.createElement('div');

            bar.style.height = `${(Math.random() * 20) + 40}px`; // 40->60px height
            bar.style.transform = `translateY(${(Math.random() * 30) - 15}px)`; // -15->15px transform
            bar.style.backgroundColor = colors[i % 2];
            display.appendChild(bar);
        }
    });
};

document.addEventListener('DOMContentLoaded', initializeBeautifulDisplays); // Only when loaded
window.onresize = initializeBeautifulDisplays; // On resize (for compatibility)
