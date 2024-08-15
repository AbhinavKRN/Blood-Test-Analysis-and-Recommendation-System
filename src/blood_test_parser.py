import pdfplumber

class BloodTestParser:
    def __init__(self, report_path):
        self.report_path = report_path

    def parse(self):
        with pdfplumber.open(self.report_path) as pdf:
            full_text = ''
            for page in pdf.pages:
                full_text += page.extract_text()

        test_data = self.extract_test_data(full_text)
        return test_data

    def extract_test_data(self, text):
        test_data = {
            "Hemoglobin": self.find_value(text, "Hemoglobin"),
            "Cholesterol": self.find_value(text, "Cholesterol"),
            "Blood Sugar": self.find_value(text, "Blood Sugar")
        }
        return test_data

    def find_value(self, text, keyword):
        if keyword in text:
            start = text.find(keyword) + len(keyword)
            end = text.find('\n', start)
            return text[start:end].strip()
        return "Not found"
