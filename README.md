# PDF Generator Bash Script

This Bash script generates a personalized PDF document using a template and recipient information. It uses two custom Python modules, `pdfEdit` for PDF manipulation and `recipient` for creating recipient images.

## Usage

1. **Run the Script:**
   - Execute the script by running the following command in your terminal:

     ```bash
     ./generate_pdf.sh
     ```

2. **Provide Recipient Information:**
   - You will be prompted to enter the recipient's details, including their name, position, organization, and address.

3. **PDF Generation:**
   - The script will then create an image for the recipient using the provided information.
   - This image is then embedded into a PDF document using a template.
   - The generated PDF is saved in the `Output` folder with the filename based on the organization name.

## Dependencies

- [pdfEdit](./dependencies/pdfedit.py): A module for PDF editing.
- [recipient](./dependencies/recipient.py): A module for creating recipient images.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.x
- [pdfEdit](./dependencies/pdfedit.py)
- [recipient](./dependencies/recipient.py)

## Example

```bash
$(cat generate_pdf.sh)
```

Feel free to customize the script based on your needs and adjust the README accordingly."
