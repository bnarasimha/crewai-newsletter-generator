# Newsletter Generator with CrewAI

A Streamlit web application that generates newsletters on any topic using CrewAI. The application converts the generated content into a downloadable PDF format.

## Features

- 🤖 AI-powered newsletter generation using CrewAI
- 📝 Simple topic-based input interface
- 📄 Automatic PDF conversion
- 👀 Real-time PDF preview
- ⬇️ PDF download capability
- 🎯 User-friendly Streamlit interface

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/newsletter-generator.git
cd newsletter-generator
```

2. Create and activate a virtual environment:

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n newsletter-env python=3.9
conda activate newsletter-env
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Install wkhtmltopdf (required for PDF generation):

**For macOS:**
```bash
brew install wkhtmltopdf
```

**For Ubuntu/Debian:**
```bash
sudo apt-get install wkhtmltopdf
```

**For Windows:**
Download and install from: https://wkhtmltopdf.org/downloads.html

## Project Structure

```
newsletter-generator/
├── src/
│   └── crew_experiment/
│       ├── __init__.py
│       ├── crew.py
│       └── config/
├── app.py
├── htmltopdf.py
├── requirements.txt
└── README.md
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Enter a topic in the input field and click "Generate Newsletter"

4. Wait for the generation process to complete

5. View the generated PDF directly in the browser

6. Download the PDF using the "Download PDF" button

7. View your generation history in the table below

## Requirements

- Python 3.8+
- CrewAI
- Streamlit
- pdfkit
- wkhtmltopdf
- pandas

See `requirements.txt` for complete list of dependencies.

## Configuration

The application uses the following configuration files:
- CrewAI configuration in `src/crew_experiment/config/`
- PDF generation settings in `htmltopdf.py`

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- CrewAI for the AI generation capabilities
- Streamlit for the web interface
- wkhtmltopdf for PDF conversion

## Support

For support, please open an issue in the GitHub repository or contact [your-email@example.com].

## Roadmap

- [ ] Add support for custom templates
- [ ] Implement user authentication
- [ ] Add more customization options
- [ ] Enable sharing capabilities
- [ ] Add export options for different formats

## Authors

- Your Name (@yourgithubhandle)

## Version History

- 0.1.0
    - Initial Release
    - Basic newsletter generation
    - PDF conversion
    - History tracking
