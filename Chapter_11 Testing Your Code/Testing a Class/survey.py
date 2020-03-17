# Testing a Class
# A class to test

class AnonymousSurvey:
    """Collect anonymus answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store response."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a sigle response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the response that have been given."""
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")