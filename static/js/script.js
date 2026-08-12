document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const startInput = document.querySelector('input[name="start_date]');
    const endInput = document.querySelector('input[name="end_date"]');


    if (form && startInput && endInput) {
        form.addEventListener("submit", function (event) {
            const start = new Date(startInput.value);
            const end = new Date(endInput.value);

            if (end <= start) {
                event.preventDefault();
                alert("End date must be after the start date.");
            }
        })
    }
})

document.addEventListener("DOMContentLoaded", function () {
    const registerForm = document.querySelector('form[action=""], form');
    const emailInput = document.querySelector('input[name="email"]');
    const passwordInput = document.querySelector('input[name="password"]');

    if (emailInput && passwordInput) {
        const form = emailInput.closest("form");

        form.addEventListener("submit", function (event) {
            const email = emailInput.value;
            const password = passwordInput.value;

            if (!email.includes("@") || !email.includes(".")) {
                event.preventDefault();
                alert("Please enter a valid email address.");
                return;
            }

            if (password.length < 8) {
                event.preventDefault();
                alert("Password must be at least 8 characters long.");
                return;
            }
        });
    }
});