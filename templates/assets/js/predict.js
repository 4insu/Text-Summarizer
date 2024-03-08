async function summarizeText() {
    // Get the input text
    var inputText = document.getElementById("inputText").value;

    // Make a POST request to your FastAPI endpoint
    const response = await fetch("http://localhost:8080/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: inputText,
        }),
    });

    if (response.ok) {
        const result = await response.json();
        displaySummary(result.summary);
    } else {
        console.error("Error:", response.status);
    }
}

function displaySummary(summary) {
    // Display the summary
    document.getElementById("outputSummary").innerText = summary;
}

function copyToClipboard() {
    // Similar to your existing copyToClipboard function
    // ...
}

// Attach event listeners after the DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("summarizeBtn").addEventListener("click", summarizeText);
    document.getElementById("copyBtn").addEventListener("click", copyToClipboard);
});
