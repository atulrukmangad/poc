# Chatbot with Python Named Entity Recognition

This POC is a chatbot that uses Python Named Entity Recognition (NER) to get basic information from a customer and then send that information to an API to generate an insurance offer.

## Requirements

* Python 3.6+
* NLTK
* Flask

## Installation

1. Clone the repository

2. Install the required packages

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

## Usage

The chatbot can be accessed through the web browser at http://localhost

The chatbot will ask the customer for basic information such as name, age, address, etc. The customer can answer in natural language and the chatbot will use NER to extract the required information. Once the required information is collected, the chatbot will send it to the API to generate an insurance offer.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
