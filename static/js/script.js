document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");

    if (emailInput && passwordInput) {
        const form = emailInput.closest("form");
        const submitBtn = document.getElementById("submit-btn");

        const emailFeedback = document.getElementById("email-feedback");
        const emailIcon = document.getElementById("email-icon");
        const emailHint = document.getElementById("email-hint");

        const passwordFeedback = document.getElementById("password-feedback");
        const passwordIcon = document.getElementById("password-icon");
        const passwordHint = document.getElementById("password-hint");

        function setFieldState(feedbackEl, iconEl, hintEl, state, message) {
            feedbackEl.className = "field-feedback " + state;
            iconEl.className = "icon " + (state === "" ? "" : state);
            hintEl.textContent = message;
        }

        function isValidEmail(email) {
            if (email.includes(" ")) return false;

            const parts = email.split("@");
            if (parts.length !== 2) return false;

            const [local, domain] = parts;
            if (local.length === 0) return false;

            if (!domain.includes(".")) return false;

            const domainParts = domain.split(".");
            for (const part of domainParts) {
                if (part.length === 0) return false;
            }

            return true;
        }

        function checkEmail() {
            const email = emailInput.value;
            const valid = isValidEmail(email);

            if (email.length === 0) {
                setFieldState(emailFeedback, emailIcon, emailHint, "", "Format: name@example.com");
            } else if (valid) {
                setFieldState(emailFeedback, emailIcon, emailHint, "valid", "Looks good");
            } else {
                setFieldState(emailFeedback, emailIcon, emailHint, "invalid", "Must be a valid email (e.g. name@example.com)");
            }
            return valid;
        }

        function checkPassword() {
            const password = passwordInput.value;
            const hasLength = password.length >= 8;
            const hasUpper = password !== password.toLowerCase();
            const hasNumber = /[0-9]/.test(password);
            const valid = hasLength && hasUpper && hasNumber;

            if (password.length === 0) {
                setFieldState(passwordFeedback, passwordIcon, passwordHint, "", "At least 8 characters, one uppercase letter, one number");
            } else if (valid) {
                setFieldState(passwordFeedback, passwordIcon, passwordHint, "valid", "Looks good");
            } else {
                const missing = [];
                if (!hasLength) missing.push("8+ characters");
                if (!hasUpper) missing.push("one uppercase letter");
                if (!hasNumber) missing.push("one number");
                setFieldState(passwordFeedback, passwordIcon, passwordHint, "invalid", "Missing: " + missing.join(", "));
            }
            return valid;
        }

        function updateSubmitState() {
            const emailOk = checkEmail();
            const passwordOk = checkPassword();
            submitBtn.disabled = !(emailOk && passwordOk);
        }

        emailInput.addEventListener("input", updateSubmitState);
        passwordInput.addEventListener("input", updateSubmitState);

        form.addEventListener("submit", function (event) {
            if (submitBtn.disabled) {
                event.preventDefault();
            }
        });
    }

    // Validation des dates de location (rent.html) — reste séparée
    const rentForm = document.querySelector('input[name="start_date"]')?.closest("form");
    const startInput = document.querySelector('input[name="start_date"]');
    const endInput = document.querySelector('input[name="end_date"]');

    if (rentForm && startInput && endInput) {
        rentForm.addEventListener("submit", function (event) {
            const start = new Date(startInput.value);
            const end = new Date(endInput.value);

            if (end <= start) {
                event.preventDefault();
                alert("End date must be after the start date.");
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const burgerBtn = document.getElementById("burger-btn");
    const navLinks = document.getElementById("nav-links");

    if (burgerBtn && navLinks) {
        burgerBtn.addEventListener("click", function () {
            navLinks.classList.toggle("open");
        });
    }
});