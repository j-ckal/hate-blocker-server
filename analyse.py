from googleapiclient import discovery
import csv,json

class Analyzer():

    # on initialisation of class, read in blocked_words csv file
    # prevents file being re-read for every element.
    def __init__(self):
        self.blocked_words = []
        with open('blocked_words.csv', 'r') as data:
            reader = csv.reader(data)
            for line in reader:
                self.blocked_words.append(line)

    def perspective(self,text_content):
        # configuration of perspective API https://developers.perspectiveapi.com/s/docs-sample-requests
        client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey="",
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
            )

        # crafts the requests including text content and requested response.
        analyze_request = {
            'comment':{'text':text_content},
            'requestedAttributes':{'TOXICITY': {}}
        }

        # marks text as hateful if toxicity score is more than 0.5 (measured between 0-1)
        if text_content:
            response = client.comments().analyze(body=analyze_request).execute()
            if response['attributeScores']['TOXICITY']['summaryScore']['value'] > 0.5:
                return True
        else: 
            return False

    def local(self,text_content):

        # local method checks if element text intersects with blocked_words csv
        # detecting if any words match and if so marking the text as hateful.
        if set(self.blocked_words[0]).intersection(text_content.lower().split()):
            return True
        else: 
            return False

if __name__ == "__main__":
    import argparse
    a = Analyzer()
    parser = argparse.ArgumentParser()
    parser.add_argument("--text_content", type=str)
    args = parser.parse_args()

    response = a.local(args.text_content)
    print (response)