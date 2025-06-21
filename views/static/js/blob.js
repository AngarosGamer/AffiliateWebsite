// Make login/signup blob follow cursor.

const blob = document.getElementById("blob"); // Get the blob item

window.onpointermove = event => { // For each pointer move event (user moves cursor)
    const { clientX, clientY } = event; // Get position on screen


    blob.animate({ // Move towards new cursor location, with 3s smoothing
        left: `${clientX}px`,
        top: `${clientY}px`
    }, { duration: 15000, fill: "forwards" });
}