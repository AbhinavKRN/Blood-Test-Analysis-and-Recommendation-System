from blood_test_parser import BloodTestParser
from summarization_agent import SummarizationAgent
from search_agent import SearchAgent
from recommendation_agent import RecommendationAgent

def main():
    report_path = 'data/sample_blood_test_report.pdf'
    parser = BloodTestParser(report_path)
    test_data = parser.parse()

    summarizer = SummarizationAgent(test_data)
    summary = summarizer.summarize()

    searcher = SearchAgent(summary)
    articles = searcher.search()

    recommender = RecommendationAgent(articles, summary)
    recommendations = recommender.recommend()

    print("Summary of Blood Test:")
    print(summary)
    print("\nRecommended Articles:")
    for article in articles:
        print(article)

    print("\nHealth Recommendations:")
    for recommendation in recommendations:
        print(recommendation)

if __name__ == "__main__":
    main()
