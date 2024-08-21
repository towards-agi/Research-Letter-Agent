# Research Letter Generator (自动陶瓷信生成器)

## Overview

The **Research Letter Generator** is a Flask-based web application that helps users generate personalized research interest letters to professors. Users can upload their resumes, and the application will use relevant academic information and research interests to generate tailored letters using the OpenAI GPT model. This tool is designed to help students apply for research opportunities, internships, or assistantships by creating high-quality, targeted correspondence.

## Features

- **Resume Upload:** Users can upload their resume directly through the interface.
- **Personalized Letters:** The application generates personalized research letters based on the user's resume, professor's research interests, and other inputs.
- **Multiple GPT Models:** Support for both `gpt-3.5-turbo` and `gpt-4` models for letter generation.
- **Google Scholar Integration:** Fetches academic information related to the professor using the SerpAPI Google Scholar engine.
- **User-Friendly Interface:** Simple and intuitive frontend to make the letter generation process easy.

## Project Structure

```
research_letter_generator/
│
├── app.py                            # Main application entry point
├── config.py                         # Configuration file for API keys and settings
├── controllers/
│   └── research_letter_controller.py # Handles request routing and business logic
├── services/
│   ├── letter_generator.py           # Core service for generating research letters
│   ├── serp_api_service.py           # Service for interacting with SerpAPI to get academic info
│   └── openai_service.py             # Service for interacting with OpenAI API
├── templates/
│   ├── research_interest_advanced.html # HTML template for the letter submission form
│   └── showCL.html                    # HTML template for displaying generated letters
└── static/
    └── css/
        └── styles.css                # Custom styles for the web application
```

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7+**
- **Flask**: Install Flask by running `pip install Flask`.
- **OpenAI API Key**: You need an API key from [OpenAI](https://beta.openai.com/signup/).
- **SerpAPI Key**: You need an API key from [SerpAPI](https://serpapi.com/).

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/research-letter-generator.git
   cd research-letter-generator
   ```

2. **Install Dependencies:**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration:**

   Create a `.env` file in the root directory with your API keys:

   ```
   SECRET_KEY=your_flask_secret_key
   API_KEY_SERP=your_serp_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the Application:**

   Start the Flask server:

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

### Usage

1. **Access the Application:**

   Open your web browser and go to `http://127.0.0.1:5000/research_interest_advanced`.

2. **Upload Your Resume:**

   Fill out the form with your name, professor's name, university, and any special preferences. Upload your resume in `.txt`, `.pdf`, or `.docx` format.

3. **Generate Letters:**

   Click "Submit" to generate two versions of the research interest letter.

4. **Review Letters:**

   The generated letters will be displayed on the next page. You can copy and use them as needed.

### Customization

- **Models:** You can choose between `gpt-3.5-turbo` and `gpt-4` for generating letters. This can be configured in the form.
- **Styling:** Customize the look and feel of the application by editing `static/css/styles.css`.
- **Templates:** Modify the HTML templates in the `templates` directory to adjust the UI.

### Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements and suggestions.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Contact

If you have any questions or feedback, feel free to contact:

- **Name:** 在学习的皮卡丘@小红书
---

### Additional Notes:

- **Error Handling:** Ensure that all exceptions, especially those involving external API calls, are handled gracefully.
- **Security:** Remember to secure your application properly, especially if deploying to a production environment.
