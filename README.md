Dynamic Stroop Test Web Application

This web application is designed to assess the impact of Instagram reels on user concentration through a dynamic Stroop Test. It measures cognitive performance before and after users engage with social media content to help understand how short-form videos may affect attention and focus.

Features

Pre-test Questionnaire: Collects user data before the test begins.
Stroop Test Implementation: Three phases of Stroop tests to measure concentration and attention.
Dynamic Test Generation: Randomly generates test cases to ensure variability and reliability.
Session Management: Tracks user progress throughout the test phases using Django's session framework.
Results Analysis: Saves and analyzes the results for each user to draw meaningful conclusions.

How It Works

Questionnaire Phase: Users start by filling out a questionnaire to provide baseline information.
Instructions: Users receive instructions on how to perform the test.
Testing Phases: The user goes through three phases of the Stroop test, each designed to measure different aspects of attention and focus.
Completion: Upon completing the tests, users are directed to a success page.

Installation

To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Set up a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

Install the requirements:

pip install -r requirements.txt

Run the development server:

python manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser.

Technology Stack

Backend: Django (Python)
Frontend: HTML, CSS, JavaScript

Contribution

If you would like to contribute to this project, please feel free to fork the repository and submit a pull request.

License

This project is open-source and available under the MIT License.

Enjoy testing and analyzing the cognitive impact of social media with our dynamic Stroop Test application!
