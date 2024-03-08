function summarizeText() {
    // Get the input text
    var inputText = document.getElementById("inputText").value;

    // Display the summary
    document.getElementById("outputSummary").innerHTML = inputText;
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