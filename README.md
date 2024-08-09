# DsuFlash
![Animation - 1720946671749](https://github.com/user-attachments/assets/a1796ec2-1658-49c0-a3e2-56c4cffa9957)


## Overview

This project implements a college information chatbot using Python and Flask. The chatbot provides users with instant access to information such as course fees, hostel facilities, campus infrastructure, location, application links, and contact details. It is designed to enhance user experience by offering 24/7 assistance and streamlining information retrieval processes.

## Features

- **User Interface**: Simple web interface for users to interact with the chatbot.
- **Information Retrieval**: Fetches data on course fees, hostel details, infrastructure, and more from JSON files.
- **External Links**: Provides links to the college's online application form and official website.
- **Error Handling**: Manages errors gracefully and provides meaningful feedback to users.

## Setup

To run the chatbot locally, follow these steps:

1. **Clone the repository**:

   ```bash
    git clone https://github.com/Spoidy-Gaming/DsuFlash
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000` to interact with the chatbot.

## Project Structure

```
college-info-chatbot/
│
├── app.py                    # Flask application for handling requests
├── config.py                 # Configuration settings
├── requirements.txt          # Dependencies
├── data/
│   └── data.json             # JSON data for courses, hostel, infrastructure, etc.
├── templates/
│   └── index.html            # HTML template for chatbot interface
├── static/
│   ├── styles.css            # CSS styles for the interface
│   └── script.js             # JavaScript for handling user interactions
└── tests/
    └── test_app.py           # Unit tests for the application
```

## Usage

- **Ask Questions**: Input queries such as "What are the course fees for Computer Science?" or "How can I apply to the college?".
- **Receive Responses**: Get instant responses with information fetched from `data.json`.
- **Explore Links**: Click on provided links for the online application form and official college website.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please create a new issue or submit a pull request.

## License

This project is licensed under the MIT License - see the MIT License file for details.
