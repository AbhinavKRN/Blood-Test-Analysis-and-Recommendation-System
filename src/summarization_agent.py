class SummarizationAgent:
    def __init__(self, test_data):
        self.test_data = test_data

    def summarize(self):
        summary = "The patient's blood test results are as follows:\n"
        for key, value in self.test_data.items():
            summary += f"{key}: {value}\n"
        return summary
