#!/usr/bin/env python

from __future__ import annotations

import os
from typing import Any
from uuid import UUID

import requests

ATTACKERKB_API_KEY = "ATTACKERKB_API_KEY"


class AttackerKB:
    def __init__(self, api_key: str | None = None) -> None:
        self.api_key: str = api_key or os.environ.get(ATTACKERKB_API_KEY, "")
        self.api_base_url: str = "https://api.attackerkb.com/v1/"
        self.api_version: str = "v1"
        self.version: str = "0.0.8"
        self.headers: dict[str, str] = {
            "Authorization": "basic " + self.api_key,
            "User-Agent": "AttackerKB-API " + self.version,
        }

        if not self.api_key:
            raise ApiError("You need to provide an attackerkb API key")

    def get_topics(self, page: int = 0, size: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        """Get a list of topics that match the kwargs

        :param page: An int that set the start page to search from
        :param size: An int that sets how many results per page are returned
        :param **kwargs: A set of Key=Values passed to the function to filter the search.
                         Must be in this list:
                         ["id", "editorId", "name", "created", "createdAfter", "createdBefore", "revisionDate", "revisedAfter", "revisedBefore", "disclosureDate", "document", "metadata", "featured", "rapid7AnalysisCreated", "rapid7AnalysisCreatedAfter", "rapid7AnalysisCreatedBefore", "rapid7AnalysisRevisionDate", "rapid7AnalysisRevisedAfter", "rapid7AnalysisRevisedBefore", "q", "sort", "expand"]


        : return: JSON Object with a list of results.

        """

        # Strip any invalid kwargs
        params = {"page": page, "size": size}
        valid_keys = [
            "id",
            "editorId",
            "name",
            "created",
            "createdAfter",
            "createdBefore",
            "revisionDate",
            "revisedAfter",
            "revisedBefore",
            "disclosureDate",
            "document",
            "metadata",
            "featured",
            "rapid7AnalysisCreated",
            "rapid7AnalysisCreatedAfter",
            "rapid7AnalysisCreatedBefore",
            "rapid7AnalysisRevisionDate",
            "rapid7AnalysisRevisedAfter",
            "rapid7AnalysisRevisedBefore",
            "q",
            "sort",
            "expand",
        ]
        for key, value in kwargs.items():
            if key in valid_keys:
                params[key] = value
            else:
                # Is it worth the raise if you have an invalid argument?
                pass

        topic_url = f"{self.api_base_url}/topics"
        api_response = requests.get(topic_url, headers=self.headers, params=params)
        result = parse_response(api_response)
        return result

    def get_single_topic(self, topic_id: str | None = None) -> dict[str, Any]:
        """Get a Single topic by its ID

        :param topic_id: A Valid UUID for a topic you want to retrieve

        : return: JSON Object with a single result or NoneType

        """
        if not topic_id or not valid_uuid(topic_id):
            raise ApiError("You need to provide a valid topic_id")
        topic_url = f"{self.api_base_url}/topics/{topic_id}"
        api_response = requests.get(topic_url, headers=self.headers)
        result = parse_response(api_response)
        return result

    def get_assessments(self, page: int = 0, size: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        """Get a list of assessments that match the kwargs

        :param page: An int that set the start page to search from
        :param size: An int that sets how many results per page are returned
        :param **kwargs: A set of Key=Values passed to the function to filter the search.
                         Must be in this list:
                         ["id", "editorId", "topicId", "created", "createdAfter", "createdBefore", "revisionDate", "revisedAfter", "revisedBefore", "document", "score", "metadata", "q", "sort", "expand"]


        : return: JSON Object with a list of results.

        """

        # Strip any invalid kwargs
        params = {"page": page, "size": size}
        valid_keys = [
            "id",
            "editorId",
            "topicId",
            "created",
            "createdAfter",
            "createdBefore",
            "revisionDate",
            "revisedAfter",
            "revisedBefore",
            "document",
            "score",
            "metadata",
            "q",
            "sort",
            "expand",
        ]
        for key, value in kwargs.items():
            if key in valid_keys:
                params[key] = value
            else:
                # Is it worth the raise if you have an invalid argument?
                pass

        topic_url = f"{self.api_base_url}/assessments"
        api_response = requests.get(topic_url, headers=self.headers, params=params)
        result = parse_response(api_response)
        return result

    def get_single_assessment(self, assessment_id: str) -> dict[str, Any]:
        """Get a Single assesment by its ID

        :param assessment_id: A Valid UUID for a topic you want to retrieve

        : return: JSON Object with a single result or NoneType

        """
        if not assessment_id or not valid_uuid(assessment_id):
            raise ApiError("You need to provide a valid assessment_id")
        api_url = f"{self.api_base_url}/assessments/{assessment_id}"
        api_response = requests.get(api_url, headers=self.headers)
        result = parse_response(api_response)
        return result

    def get_contributors(self, page: int = 0, size: int = 10, **kwargs: Any) -> list[dict[str, Any]]:
        """Get a list of contributors that match the kwargs

        :param page: An int that set the start page to search from
        :param size: An int that sets how many results per page are returned
        :param **kwargs: A set of Key=Values passed to the function to filter the search.
                         Must be in this list:
                         ["id", "username", "avatar", "created", "createdAfter", "createdBefore", "score", "q", "sort"]


        : return: JSON Object with a list of results.

        """

        # Strip any invalid kwargs
        params = {"page": page, "size": size}
        valid_keys = ["id", "username", "avatar", "created", "createdAfter", "createdBefore", "score", "q", "sort"]
        for key, value in kwargs.items():
            if key in valid_keys:
                params[key] = value
            else:
                # Is it worth the raise if you have an invalid argument?
                pass

        topic_url = f"{self.api_base_url}/contributors"

        api_response = requests.get(topic_url, headers=self.headers, params=params)
        result = parse_response(api_response)
        return result

    def get_single_contributor(self, contributor_id: str) -> dict[str, Any]:
        """Get a Single assesment by its ID or Username

        :param assessment_id: A Valid UUID for a topic you want to retrieve or a username string

        : return: JSON Object with a single result or NoneType

        """
        if not contributor_id:
            raise ApiError("You need to provide a valid contributor_id")

        if valid_uuid(contributor_id):
            api_url = f"{self.api_base_url}/contributors/{contributor_id}"
            api_response = requests.get(api_url, headers=self.headers)
            result = parse_response(api_response)
            return result
        else:
            # try a username lookup
            api_url = f"{self.api_base_url}/contributors"
            params = {"username": contributor_id}
            api_response = requests.get(api_url, headers=self.headers, params=params)
            result = parse_response(api_response)
            return result[0]


class ApiError(Exception):
    pass


def valid_uuid(uuid_string: str) -> bool:
    """
    return true if valid uuid4

    :param uuid_string: A string to check if valid UUID4

    : return bool: Based on the result
    """
    try:
        UUID(uuid_string, version=4)
        return True
    except ValueError:
        return False


def parse_response(api_response: requests.Response) -> list[dict[str, Any]] | dict[str, Any]:
    if api_response.status_code == 200:
        return api_response.json()["data"]
    elif api_response.status_code == 401:
        raise ApiError("Error Authenticating to the API check your key")
    elif api_response.status_code == 404:
        raise ApiError("You requested an invalid resource")
    elif api_response.status_code == 500:
        raise ApiError("There was an error with the API Server")
    else:
        raise ApiError(f"Unexpected status code: {api_response.status_code}")
