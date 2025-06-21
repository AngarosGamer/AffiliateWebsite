/*

This code does **FRONTEND-ONLY** verification for the user passwords, ensuring it meets our validation criteria.

 */

// Define all View items in an object we'll reference
const view = {
    emailInput : document.getElementById("email"),
    passwordInput : document.getElementById("password"),
    confirmationPasswordInput : document.getElementById("confirm-password"),
    connectButton : document.getElementById("signup-button-action"),
    checklist : {
        pwdLen : document.getElementById("password-check-len"),
        min: document.getElementById("password-check-min"),
        maj: document.getElementById("password-check-maj"),
        num: document.getElementById("password-check-num"),
        special: document.getElementById("password-check-special"),
        mustmatch: document.getElementById("password-check-match"),
    }
}


// Replace the xmark icon by a check icon if the condition is now true, and vice versa.
const updateChecklistElement = (viewElement, condition) => {
    console.log(viewElement);
    const icon = viewElement.querySelector("i");
    if (condition){
        // Success
        //icon.classList.remove("fa-xmark");
        //icon.classList.add("fa-check");
        //viewElement.style.color = '#7A7EFF'; // Success Color
        viewElement.classList.add("hidden")
    }
    else {
        // Error
        icon.classList.remove("fa-check");
        icon.classList.add("fa-xmark");
        viewElement.style.color = '#FF7979'; // Error Color
        viewElement.classList.remove("hidden"); // Show invalid elements
    }
    return condition;
}

const validatePassword = () => {
    const inputContent = view.passwordInput.value;
    const emailContent = view.emailInput.value;
    const results = {
        pwdLen: inputContent.length >= 8,
        maj: /[A-Z]/.test(inputContent),
        min: /[a-z]/.test(inputContent),
        num: /[0-9]/.test(inputContent),
        special: /['^£$%&*()}{@#~?><,.|=_+!-]/.test(inputContent),
    };
    const allValid = Object.values(results).every(Boolean);
    return { results, allValid };
};

// Verify that the 2 input boxes for password have matching passwords
const passwordsMatch = () => {
    const password = view.passwordInput.value;
    const confirmation = view.confirmationPasswordInput.value;
    return password === confirmation;
};

// Display only failing checklist items
const displayChecklist = () => {
    const { results } = validatePassword();
    Object.entries(results).forEach(([key, valid]) => {
        console.log(key)
        updateChecklistElement(view.checklist[key], valid);
    });
    updateChecklistElement(view.checklist.mustmatch, passwordsMatch());
};

// Check all validation rules
const isFormValid = () => {
    const { allValid } = validatePassword();
    return allValid && passwordsMatch();
};

// Prevent form submission if validation fails
view.connectButton.addEventListener("click", (event) => {
    if (!isFormValid()) {
        event.preventDefault(); // Prevent form submission
        displayChecklist(); // Show the checklist with updated states
    }
});

// Avoid form submission on Enter key
document.addEventListener('keypress', (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        view.connectButton.click();
    }
});