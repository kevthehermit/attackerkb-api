 
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from uuid import UUID
try:
    import requests
except ImportError:
    print("Error importing requests.")



class AttackerKB():

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_base_url = "https://api.attackerkb.com"
        self.headers = {
            'Authorization': 'basic ' + api_key
        }

        if not self.api_key:
            raise ApiError("You need to provide an attackerkb API key")

    def get_topics(self, page=0, size=10, **kwargs):
        """ Get a list of topics that match the kwargs

        :param page: An int that set the start page to search from
        :param size: An int that sets how many results per page are returned
        :param **kwargs: A set of Key=Values passed to the function to filter the search.
                         Must be in this list: 
                         ["id", "editorId" ,"name" ,"created" ,"revisionDate" ,"disclosureDate" ,"document", "metadata", "q", "sort"]


        : return: JSON Object with a list of results.

        """

        # Strip any invalid kwargs
        params = {
            "page": page,
            "size": size
        }
        valid_keys = ["id", "editorId" ,"name" ,"created" ,"revisionDate" ,"disclosureDate" ,"document", "metadata", "q", "sort"]
        for key, value in kwargs.items():
            if key in valid_keys:
                params[key] = value
            else:
                # Is it worth the raise if you have an invalid argument?
                pass

        topic_url = '{0}/topics'.format(self.api_base_url)
        api_response = requests.get(topic_url, headers=self.headers, params=params)
        result = parse_response(api_response)
        return result


    def get_single_topic(self, topic_id=None):
        """ Get a Single topic by its ID

        :param topic_id: A Valid UUID for a topic you want to retrieve

        : return: JSON Object with a single result or NoneType

        """
        if not topic_id or not valid_uuid(topic_id):
            raise ApiError("You need to provide a valid topic_id")
        topic_url = '{0}/topics/{1}'.format(self.api_base_url, topic_id)
        api_response = requests.get(topic_url, headers=self.headers)
        result = parse_response(api_response)
        return result

    def get_assessments(self, page=0, size=10, **kwargs):
        """ Get a list of assessments that match the kwargs

        :param page: An int that set the start page to search from
        :param size: An int that sets how many results per page are returned
        :param **kwargs: A set of Key=Values passed to the function to filter the search.
                         Must be in this list: 
                         ["id", "editorId" ,"topicId" ,"created" ,"revisionDate" ,"document", "score", "metadata", "q", "sort"] 


        : return: JSON Object with a list of results.

        """

        # Strip any invalid kwargs
        params = {
            "page": page,
            "size": size
        }
        valid_keys = ["id", "editorId" ,"topicId" ,"created" ,"revisionDate" ,"document", "score", "metadata", "q", "sort"]
        for key, value in kwargs.items():
            if key in valid_keys:
                params[key] = value
            else:
                # Is it worth the raise if you have an invalid argument?
                pass

        topic_url = '{0}/assessments'.format(self.api_base_url)
        api_response = requests.get(topic_url, headers=self.headers, params=params)
        result = parse_response(api_response)
        return result

    def get_single_assessment(self, assessment_id):
        """ Get a Single assesment by its ID

        :param assessment_id: A Valid UUID for a topic you want to retrieve

        : return: JSON Object with a single result or NoneType

        """
        if not assessment_id or not valid_uuid(assessment_id):
            raise ApiError("You need to provide a valid assessment_id")
        api_url = '{0}/assessments/{1}'.format(self.api_base_url, assessment_id)
        api_response = requests.get(api_url, headers=self.headers)
        result = parse_response(api_response)
        return result

    def get_contributors(self, page=0, size=10, **kwargs):
        """ Get a list of contributors that match the kwargs

        :param page: An int that set the start page to search from
        :param size: An int that sets how many results per page are returned
        :param **kwargs: A set of Key=Values passed to the function to filter the search.
                         Must be in this list: ["id", "username" ,"avatar" ,"created", "score", "q", "sort"] 


        : return: JSON Object with a list of results.

        """

        # Strip any invalid kwargs
        params = {
            "page": page,
            "size": size
        }
        valid_keys = ["id", "username" ,"avatar" ,"created", "score", "q", "sort"]
        for key, value in kwargs.items():
            if key in valid_keys:
                params[key] = value
            else:
                # Is it worth the raise if you have an invalid argument?
                pass

        topic_url = '{0}/contributors'.format(self.api_base_url)

        api_response = requests.get(topic_url, headers=self.headers, params=params)
        result = parse_response(api_response)
        return result

    def get_single_contributor(self, contributor_id):
        """ Get a Single assesment by its ID or Username

        :param assessment_id: A Valid UUID for a topic you want to retrieve or a username string

        : return: JSON Object with a single result or NoneType

        """
        if not contributor_id:
            raise ApiError("You need to provide a valid contributor_id")

        if valid_uuid(contributor_id):
            api_url = '{0}/contributors/{1}'.format(self.api_base_url, contributor_id)
            api_response = requests.get(api_url, headers=self.headers)
            result = parse_response(api_response)
            return result
        else:
            # try a username lookup
            api_url = '{0}/contributors'.format(self.api_base_url)
            params = {
                "username": contributor_id
            }
            api_response = requests.get(api_url, headers=self.headers, params=params)
            result = parse_response(api_response)
            return result[0]


class ApiError(Exception):
    pass


def valid_uuid(uuid_string):
    """
    return true if valid uuid4

    :param uuid_string: A string to check if valid UUID4

    : return bool: Based on the result
    """
    try:
        val = UUID(uuid_string, version=4)
        return True
    except ValueError:
        return False

def parse_response(api_response):
    if api_response.status_code == 200:
        return api_response.json()['data']
    elif api_response.status_code == 401:
        raise ApiError("Error Authenticating to the API check your key")
    elif api_response == 404:
        raise ApiError("You requested an invalid resource")
    elif api_response.status_code == 500:
        raise ApiError("There was an error with the API Server")