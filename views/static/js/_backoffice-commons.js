document.addEventListener('DOMContentLoaded', () => {
    const alertBox = document.getElementById("customAlertBox");
    const alertMessage = document.getElementById("alertMessage");
    const closePopup = document.querySelector(".close");
    const userListContainer = document.getElementById("users-list"); // Parent container for dynamic content

    let currentForm = null;

    // Handle the close button for the alert popup
    closePopup.addEventListener('click', () => {
        alertBox.style.display = "none";
    });

    // Add a click listener to the parent container
    if (typeof userListContainer != "undefined" && userListContainer != null) {
        userListContainer.addEventListener("click", (event) => {
            const target = event.target;
            if (target.id === "user-form-delete-button") {
                event.preventDefault();
                currentForm = target.closest('form'); // Get the form related to this button

                alertMessage.innerHTML = `
                    <p>Are you sure you want to delete user n°${currentForm.children.item(0).value}?</p>
                    <div class="alert-buttons">
                        <button id="confirm-delete" class="form-button-confirm">Confirm</button>
                        <button id="cancel-delete" class="form-button-cancel">Cancel</button>
                    </div>
                `;
                alertBox.style.display = "block"; // Show the alert popup
            }
        });
    }

    // Handle confirm and cancel actions inside the alert popup
    alertBox.addEventListener('click', (event) => {
        if (event.target.id === "confirm-delete") {
            if (currentForm) currentForm.submit(); // Submit the form
        } else if (event.target.id === "cancel-delete") {
            alertBox.style.display = "none"; // Close the alert popup
        }
    });
});
