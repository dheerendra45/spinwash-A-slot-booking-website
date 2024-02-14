<!-- Load Swiper JS -->
<script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>

<script>
    document.addEventListener('DOMContentLoaded', function () {
        const formSubmitBtn = document.querySelector('.formbold-btn');
        const formBackBtn = document.querySelector('.formbold-back-btn');

        const stepMenuOne = document.querySelector('.formbold-step-menu1');
        const stepMenuTwo = document.querySelector('.formbold-step-menu2');
        const stepMenuThree = document.querySelector('.formbold-step-menu3');

        const stepOne = document.querySelector('.formbold-form-step-1');
        const stepTwo = document.querySelector('.formbold-form-step-2');
        const stepThree = document.querySelector('.formbold-form-step-3');

        formSubmitBtn.addEventListener("click", function (event) {
            event.preventDefault();

            if (stepMenuOne.classList.contains('active')) {
                // Submit form for Step 1 (def book)
                document.querySelector('form').submit();
            } else if (stepMenuTwo.classList.contains('active')) {
                // Submit form for Step 2 (def save_booking)
                const xhr = new XMLHttpRequest();
                xhr.open("POST", "/save_booking", true);
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

                const formData = new FormData(document.querySelector('form'));
                const params = new URLSearchParams(formData).toString();

                xhr.send(params);

                xhr.onload = function () {
                    if (xhr.status >= 200 && xhr.status < 300) {
                        // If successful, update the page (e.g., show step 3)
                        stepMenuTwo.classList.remove('active');
                        stepMenuThree.classList.add('active');
                        stepTwo.classList.remove('active');
                        stepThree.classList.add('active');
                        formBackBtn.classList.remove('active');
                        formSubmitBtn.textContent = 'Submit';
                    } else {
                        // Handle error if needed
                        console.error(xhr.statusText);
                    }
                };
            } else if (stepMenuThree.classList.contains('active')) {
                // Submit form for Step 3 (def save_confirmation)
                document.querySelector('form').submit();
            }
        });

        // Initialize Swiper
        const swiper = new Swiper(".slide-content", {
            slidesPerView: 3,
            spaceBetween: 25,
            loop: true,
            centerSlide: true,
            fade: true,
            grabCursor: true,
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
                dynamicBullets: true,
            },
            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            breakpoints: {
                0: {
                    slidesPerView: 1,
                },
                520: {
                    slidesPerView: 2,
                },
                950: {
                    slidesPerView: 3,
                },
            },
        });
    });
</script>
