document.getElementById("summarizeBtn").addEventListener("click", function () {
    // Retrieve form data
    const formData = new FormData(document.getElementById("summarizeForm"));
    
    // Add input_type field
    formData.append("input_type", "text");  // Adjust the value based on your use case
    
    // Fetch options
    const fetchOptions = {
        method: "POST",
        body: formData,
    };

    // Fetch request
    fetch("/predict", fetchOptions)
        .then(response => {
            if (response.ok) {
                return response.text();
            } else {
                console.error("Error:", response.status);
                throw new Error("Failed to fetch summary");
            }
        })
        .then(summary => {
            // Display the summary in the output section
            document.getElementById("outputSummary").innerText = summary;
        })
        .catch(error => {
            console.error("Error:", error);
        });
});

function createFormData(inputType, inputData) {
    const formData = new FormData();
    formData.append("input_type", inputType);

    if (inputType === "text") {
        formData.append("text", inputData);
    } else if (inputType === "pdf") {
        formData.append("pdf_file", inputData);
    }

    return formData;
}

function copyToClipboard() {
    // Get the summary content
    var summaryContent = document.getElementById("outputSummary").innerText;

    // Create a temporary textarea element
    var textarea = document.createElement("textarea");
    textarea.value = summaryContent;

    // Append the textarea to the document
    document.body.appendChild(textarea);

    // Select and copy the content
    textarea.select();
    document.execCommand("copy");

    // Remove the temporary textarea
    document.body.removeChild(textarea);

    // Alert the user (you can customize this part)
    alert("Summary copied to clipboard!");
}