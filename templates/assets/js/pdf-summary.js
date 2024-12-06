document.addEventListener('DOMContentLoaded', () => {
    const pdfUploadIcon = document.getElementById('pdf-upload-icon');
    const pdfInput = document.getElementById('pdf-input');
    const uploadedFileName = document.getElementById('uploaded-file-name');

    if (pdfUploadIcon && pdfInput && uploadedFileName) {
        // Trigger file input when the icon is clicked
        pdfUploadIcon.addEventListener('click', () => {
            pdfInput.click();
        });

        // Update the file name when a file is selected
        pdfInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                uploadedFileName.textContent = `Uploaded File: ${file.name}`;
            } else {
                uploadedFileName.textContent = 'No file selected.';
            }
        });
    } else {
        console.error('Some elements are missing in the DOM.');
    }
});
