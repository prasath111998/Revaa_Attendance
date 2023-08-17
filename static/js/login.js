document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const employeeIdInput = document.getElementById("InputUsername");
    const passwordInput = document.getElementById("InputPasssord");
    form.addEventListener("submit", function(event) {
        let isValid = true;
        // Clear previous error messages
        const employeeIdError = document.getElementById("employeeIderror");
        const passwordError = document.getElementById("employeepassworderror");
        employeeIdError.textContent = "";
        passwordError.textContent = "";
        // Validate Employee ID
        if (employeeIdInput.value.trim() === "") {
            isValid = false;
            employeeIdError.textContent = "Employee ID is required.";
        }
        // Validate Password
        if (passwordInput.value.trim() === "") {
            isValid = false;
            passwordError.textContent = "Password is required.";
        }
        if (!isValid) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});

