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