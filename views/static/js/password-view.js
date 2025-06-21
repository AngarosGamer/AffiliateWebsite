/*

This code handles the "show password" button embedded in the login / register forms.

 */

// Always
passwordInput = document.getElementById("password");
viewPasswordButton = document.getElementById("form-view-password");

// When on Signup page
confirmPasswordInput = document.getElementById("confirm-password");
viewConfirmPasswordButton = document.getElementById("form-view-confirm-password");

// When the embedded button is clicked
viewPasswordButton.addEventListener("click", () => {
    if (passwordInput.type === "password") { // Already hiding password ?
        passwordInput.type = "text"; // Show password
        // Switch from closed eye to open eye
        viewPasswordButton.firstElementChild.classList.remove("fa-eye-slash")
        viewPasswordButton.firstElementChild.classList.add("fa-eye")
    } else {
        // Currently showing password?
        passwordInput.type = "password"; // Hide password
        // Switch from open eye to closed eye
        viewPasswordButton.firstElementChild.classList.remove("fa-eye")
        viewPasswordButton.firstElementChild.classList.add("fa-eye-slash")
    }
});

// When the embedded button is clicked (confirmation password)
if (confirmPasswordInput) {
    viewConfirmPasswordButton.addEventListener("click", () => {
        if (confirmPasswordInput.type === "password") { // Already hiding confirmation password ?
            confirmPasswordInput.type = "text"; // Show confirmation password
            // Switch from closed eye to open eye
            viewConfirmPasswordButton.firstElementChild.classList.remove("fa-eye-slash")
            viewConfirmPasswordButton.firstElementChild.classList.add("fa-eye")
        } else {
            // Currently showing confirmation password?
            confirmPasswordInput.type = "password"; // Hide confirmation password
            // Switch from open eye to closed eye
            viewConfirmPasswordButton.firstElementChild.classList.remove("fa-eye")
            viewConfirmPasswordButton.firstElementChild.classList.add("fa-eye-slash")
        }
    });
}