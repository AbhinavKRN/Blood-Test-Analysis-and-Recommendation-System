class RecommendationAgent:
    def __init__(self, articles, summary):
        self.articles = articles
        self.summary = summary

    def recommend(self):
        recommendations = [
            "Increase your fiber intake to manage cholesterol.",
            "Exercise regularly to maintain healthy blood sugar levels.",
            "Consult with a healthcare provider for personalized advice."
        ]
        return recommendations
