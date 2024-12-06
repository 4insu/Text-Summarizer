const textSummary = document.getElementById('text-summary');
const pdfSummary = document.getElementById('pdf-summary');
const audioSummary = document.getElementById('audio-summary');
const aboutUs = document.getElementById('about-us');

textSummary.addEventListener('click',()=>{
    window.open('text-summary.html','_blank');
})
pdfSummary.addEventListener('click',()=>{
    window.open('pdf-summary.html','_blank');
})
audioSummary.addEventListener('click',()=>{
    window.open('audio-summary.html','_blank');
})
aboutUs.addEventListener('click', () => {
    window.location.href = 'about-us.html';
});




document.addEventListener('DOMContentLoaded', () => {
    const pdfUploadIcon = document.getElementById('pdf-upload-icon');
    const pdfInput = document.getElementById('pdf-input');

    if (pdfUploadIcon && pdfInput) {
        pdfUploadIcon.addEventListener('click', () => {
            console.log("PDF icon clicked!"); // Debug message
            pdfInput.click(); // Open file dialog
        });

        pdfInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                alert(`File uploaded: ${file.name}`);
            } else {
                alert('No file selected.');
            }
        });
    } else {
        console.error('PDF upload icon or input field not found.');
    }
});
console.log('hello');



// Check saved theme in local storage
// const savedTheme = localStorage.getItem('theme');
// if (savedTheme) {
//     document.body.classList.toggle('dark-mode', savedTheme === 'dark');
//     themeIcon.src = savedTheme === 'dark' ? 'assets/images/sun.png' : 'assets/images/moon.png';
// }

// // Event listener for theme toggle
// themeToggle.addEventListener('click', () => {
//     // Toggle dark mode class
//     const isDarkMode = document.body.classList.toggle('dark-mode');
    
//     // Update the icon
//     themeIcon.src = isDarkMode ? 'assets/images/sun.png' : 'assets/images/moon.png';

//     // Save the theme preference to local storage
//     localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
// });
