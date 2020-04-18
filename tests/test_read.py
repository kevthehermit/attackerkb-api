import pytest
import os
from attackerkb_api import AttackerKB, ApiError

API_KEY = os.environ.get("API_KEY")

def test_api_fail():
    with pytest.raises(ApiError):
        api = AttackerKB(api_key="")

def test_api():
    api = AttackerKB(api_key=API_KEY)

api = AttackerKB(api_key=API_KEY)

def test_single_topic():
    result = api.get_single_topic('6685ce4d-9523-4078-92d3-f08418c9770a')
    assert result['id'] == '6685ce4d-9523-4078-92d3-f08418c9770a'

def test_search_topic():
    result = api.get_topics(name="CVE-2020-10560")
    assert result[0]['id'] == "6f81bc44-c000-427d-b222-b64c29bda621"

def test_search_topic_params():
    result = api.get_assessments(topicId='131226a6-a1e9-48a1-a5d0-ac94baf8dfd2', page=0, size=2, sort="score:asc")
    assert len(result) == 2

def test_single_topic_fail():
    with pytest.raises(ApiError):
        result = api.get_single_topic('not a uuid')

def test_single_assesment():
    result = api.get_single_assessment('7c324b6e-0d83-4392-a79f-b61220ebfff3')
    assert result['id'] == '7c324b6e-0d83-4392-a79f-b61220ebfff3'

def test_multi_assesment():
    result = api.get_assessments(topicId='131226a6-a1e9-48a1-a5d0-ac94baf8dfd2')
    assert len(result) >=2

def test_single_assesment_fail():
    with pytest.raises(ApiError):
        result = api.get_single_assessment('not a uuid')

def test_single_user_id():
    result = api.get_single_contributor('7ff62803-e0a8-4121-b324-d4afe9f60d43')
    assert result['id'] == '7ff62803-e0a8-4121-b324-d4afe9f60d43'

def test_single_user_name():
    result = api.get_single_contributor('KevTheHermit')
    assert result['username'] == 'kevthehermit'
