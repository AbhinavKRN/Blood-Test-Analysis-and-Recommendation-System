# Blood Test Analysis and Recommendation System

## AI Internship Assignment

### Project Overview

This project involves creating a system using the CrewAI framework to analyze blood test reports, search the internet for relevant health articles, and provide personalized health recommendations based on the findings.

### Objective

- **Input:** The system takes a sample blood test report.
- **Analysis:** It analyzes the blood test report, summarizing the findings in an easy-to-understand manner.
- **Article Search:** The system searches the web for articles that align with the individual's health needs based on the blood test results.
- **Recommendations:** Finally, it provides health recommendations and links to relevant articles.

### Technologies Used

- **CrewAI Framework:** Used to manage and coordinate the different AI agents in the system.
- **OpenAI API:** Utilized for natural language processing and summarization tasks.
- **Python:** Primary programming language for implementing the system.
- **Environment Variables:** The OpenAI API key is securely stored in an `.env` file.

### Project Structure

- **data/**
  - *Contains any data files or assets needed for the project.*
- **src/**
  - `__init__.py`: Initializes the module.
  - `blood_test_parser.py`: Parses and analyzes the blood test report.
  - `main.py`: The main script that coordinates the workflow.
  - `recommendation_agent.py`: Generates health recommendations based on analyzed data.
  - `search_agent.py`: Searches the web for articles that fit the individual's health profile.
  - `summarization_agent.py`: Summarizes the blood test report into a user-friendly format.
  - `utils.py`: Contains utility functions used across the project.
- **config.json:** Configuration file with settings and parameters for the project.
- **.env:** Stores sensitive environment variables like the OpenAI API key.
- **README.md:** Provides an overview of the project.
- **requirements.txt:** Lists the dependencies required to run the project.

### How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AbhinavKRN/blood-sample-analysis.git
   cd blood-sample-analysis
   ```

2. **Set Up the Environment:**
   - Ensure Python 3.8+ is installed on your machine.
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Environment Variables:**
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the Main Script:**
   ```bash
   python src/main.py
   ```

5. **Test the System:**
   - The system will process a sample blood test report, search for relevant health articles, and provide personalized recommendations.

### Approach

1. **Blood Test Parsing:** I implemented a parser in `blood_test_parser.py` that extracts relevant information from the blood test report.
2. **Summarization:** I used the OpenAI API in `summarization_agent.py` to convert complex medical data into a more comprehensible format.
3. **Search Agent:** The `search_agent.py` script fetches relevant articles from the internet based on the summarized data.
4. **Recommendations:** In `recommendation_agent.py`, I developed an agent that provides health tips and links to articles based on the analysis.

