# Text Summarizer Web App

Welcome to my Text Summarizer Web App! This application utilizes Hugging Face Transformers, Python, and Streamlit to provide an efficient and user-friendly platform for text summarization.

## Features

- Summarizes text, PDF, and even audio files.
- Utilizes the powerful PEGASUS model by Google for summarization.
- Integrates seamlessly with Streamlit for a smooth web application experience.

## Hugging Face Model

The text summarization in this app is powered by the PEGASUS model from Hugging Face. PEGASUS is a pre-trained model fine-tuned on various datasets for summarization tasks. You can find more information about the model [here](https://huggingface.co/google/pegasus-cnn_dailymail).

## Dataset

The dataset used for training and fine-tuning the model is sourced from the Hugging Face Datasets library. Specifically, it uses the [SAMSum dataset](https://huggingface.co/datasets/samsum), which contains conversational summaries extracted from the SAMSum corpus.

## Usage

To use the Text Summarizer Web App, follow these steps:

1. Navigate to the web app URL.
2. Upload your text, PDF, or audio file using the provided interface.
3. Click on the "Summarize" button to generate a summary.
4. View the summarized text presented on the app interface.
5. Enjoy concise and accurate summaries of your content!

## Installation

To run this application locally, you can follow these steps:

1. Clone this GitHub repository:

```bash
git clone https://github.com/rikisupriyo/Text-Summarizer.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Generate the artifacts:

```bash
python main.py
```

4. Run the Streamlit application:

```bash
streamlit run app.py
```

5. Access the web app through the provided [URL](https://www.google.com/)

## Contribution

Contributions are welcome! If you have any suggestions, feature requests, or want to report issues, feel free to open an issue or submit a pull request in this repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## ECR repo to store/save docker image
- URI : 637423488242.dkr.ecr.ap-southeast-2.amazonaws.com/text-summarizer