from rasa_core_sdk import Action
import requests
import json


class ActionGetNewst(Action):

    def name(self):
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        url = 'https://api.nytimes.com/svc/news/v3/content/all/{category}.json'.format(category=category)
        params = {'api-key': "e5IdwHs4embgQCobxOcKz0WPAp6vL03C", 'limit': 5}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return[]

class ActionGetMovies(Action):
    def name(self):
        return 'action_get_movies'

    def run(self, dispatcher, tracker, domain):
        title = tracker.get_slot('title')
        print(title)
        url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json'
        params = {'api-key': "e5IdwHs4embgQCobxOcKz0WPAp6vL03C", 'query': str(title)}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['summary_short']
            dispatcher.utter_message(message)
        return[]

class ActionGetArticles(Action):
    def name(self):
        return 'action_get_stories'

    def run(self, dispatcher, tracker, domain):
        area = tracker.get_slot('area')
        print(area)
        url = 'https://api.nytimes.com/svc/topstories/v2/{section}.json'.format(section=area)
        params = {'api-key': "e5IdwHs4embgQCobxOcKz0WPAp6vL03C", 'num_results': 5}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return[]