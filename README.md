# AttackerKB API

This is a python wrapper around the AttackerKB RESTful API. For more details on the API referer to https://api.attackerkb.com/api-docs/docs


## Status

[![codecov](https://codecov.io/gh/kevthehermit/attackerkb-api/branch/master/graph/badge.svg)](https://codecov.io/gh/kevthehermit/attackerkb-api)

[![Build Status](https://travis-ci.org/kevthehermit/attackerkb-api.svg?branch=master)](https://travis-ci.org/github/kevthehermit/attackerkb-api/)

## Installation

`python3 -m pip install attackerkb-api`
`pip3 install attackerkb-api`

## Usage

```python
import json
from attackerkb_api import AttackerKB

API_KEY = "GET AN API KEY FROM https://attackerkb.com/"

api = AttackerKB(API_KEY)

print("Get Single Topic")
result = api.get_single_topic('6f81bc44-c000-427d-b222-b64c29bda621')
print(json.dumps(result, indent=4, sort_keys=True))

print("Get Single Assessment")
result = api.get_single_assessment('7c324b6e-0d83-4392-a79f-b61220ebfff3')
print(json.dumps(result, indent=4, sort_keys=True))

print("Get the first 2 Assessments for a topic")
result = api.get_assessments(topicId='131226a6-a1e9-48a1-a5d0-ac94baf8dfd2', page=0, size=2)
print(json.dumps(result, indent=4, sort_keys=True))

print("Get a CVE")
result = api.get_topics(name="CVE-2020-10560")
print(json.dumps(result, indent=4, sort_keys=True))

print("Get Single User by ID")
result = api.get_single_contributor('7ff62803-e0a8-4121-b324-d4afe9f60d43')
print(json.dumps(result, indent=4, sort_keys=True))

print("Get Single User by Name")
result = api.get_single_contributor('KevTheHermit')
print(json.dumps(result, indent=4, sort_keys=True))


```


## Output


```json
Get Single Topic
{
    "created": "2020-03-30T13:30:05.033552Z",
    "disclosureDate": "2020-03-30T13:15:00Z",
    "document": "An issue was discovered in Open Source Social Network (OSSN) through 5.3. A user-controlled file path with a weak cryptographic rand() can be used to read any file with the permissions of the webserver. This can lead to further compromise. The attacker must conduct a brute-force attack against the SiteKey to insert into a crafted URL for components/OssnComments/ossn_com.php and/or libraries/ossn.lib.upgrade.php.",
    "editorId": "7191a637-aa4e-4885-98a0-f4f2da285b99",
    "id": "6f81bc44-c000-427d-b222-b64c29bda621",
    "metadata": {
        "baseMetricV3": {
            "cvssV3": {
                "attackComplexity": "HIGH",
                "attackVector": "NETWORK",
                "availabilityImpact": "NONE",
                "baseScore": 5.9,
                "baseSeverity": "MEDIUM",
                "confidentialityImpact": "HIGH",
                "integrityImpact": "NONE",
                "privilegesRequired": "NONE",
                "scope": "UNCHANGED",
                "userInteraction": "NONE",
                "vectorString": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
                "version": "3.1"
            },
            "exploitabilityScore": 2.2,
            "impactScore": 3.6
        },
        "references": [
            "CVE-2020-10560",
            "https://techanarchy.net/blog/cve-2020-10560-ossn-arbitrary-file-read",
            "https://github.com/LucidUnicorn/CVE-2020-10560-Key-Recovery"
        ],
        "vulnerable-versions": [
            "n/a"
        ]
    },
    "name": "CVE-2020-10560",
    "revisionDate": "2020-04-03T06:00:16.606546Z",
    "score": {
        "attackerValue": 1,
        "exploitability": 3
    },
    "tags": {
        "commonEnterprise": 0,
        "defaultConfiguration": 1,
        "difficultToDevelop": 0,
        "difficultToExploit": 0,
        "difficultToPatch": 0,
        "easyToDevelop": 1,
        "highPrivilegeAccess": 0,
        "noUsefulData": 1,
        "obscureConfiguration": 0,
        "postAuth": 0,
        "preAuth": 1,
        "requiresInteraction": 0
    }
}
Get Single Assessment
{
    "created": "2020-04-14T16:47:04.345906Z",
    "document": "This vulnerability was the Linux equivalent to Wanncry according to some journalists.  It was not.\r\nThis vulnerability (AKA SambaCry) worked by writing a link library (.so file) to a linux host running Sama in such a way that samba then loaded it.  On the face of it, this was a problem, but attackers had 2 large hurdles:\r\n1. Anonymous file creation had to be enabled and\r\n2. Attackers had to guess the right absolute path\r\n\r\nIn the first case, it is unlikely any enterprise will have anonymous file creation turned on, so immediately attackers are thwarted.  In the second case, an attacker must guess the absolute path to the share as it is mounted on the remote computer.  There are obvious guesses attackers could make, but nothing that was guaranteed.  This was the classic example of a terrifying exploit mitigated by large caveats.  Most common-sense approaches to SAMBA and SMB shared will mitigate this threat, namely not opening SMB/SAMBA shares to the internet, not allowing anonymous logins, and keeping software up to date.",
    "editorId": "ba7d1514-7156-496b-8642-ed75d18e5d9b",
    "id": "7c324b6e-0d83-4392-a79f-b61220ebfff3",
    "metadata": {
        "tags": [
            "obscure_configuration",
            "difficult_to_develop",
            "common_enterprise",
            "high_privilege_access",
            "pre_auth"
        ]
    },
    "revisionDate": "2020-04-14T16:47:04.349096Z",
    "score": 1,
    "topicId": "49aaf9a1-b710-4ca1-aafa-3c022294a5d4"
}
Get the first 2 Assessments for a topic
[
    {
        "created": "2020-03-29T16:46:17.144704Z",
        "document": "**Description**\r\n\r\nA vulnerability in the RDP windows service allows the execution of malicious code with the injection of code in the request for a RDP connection. The exploitation of this vulnerability may be used for performing a DoS (Denial Of Service) attack or executing code in a remote system.\r\n\r\nFor the safe and satisfactory exploitation of this vulnerability, it is recommended to identify the target machine so the exploit is reliably crafted.\r\n\r\n**Mitigation**\r\n\r\n- Apply the corresponding security patches released by Microsoft (supported and unsupported OSs)\r\n- Disabling RDP service where no needed and controlling its exposure using a FW internally and externally\r\n- Enabling network level authentication in RDP services\r\n\r\n**Affected Systems**\r\n\r\nThe following Operating System are affected if they have not been patched:\r\n\r\n- Windows Vista\r\n- Windows 7\r\n- Windows XP\r\n- Windows Server 2003\r\n- Windows Server 2008\r\n\r\n**References**\r\n\r\n- The exploit is now included in Metasploit. (The exploit may requier some tuning)\r\n- https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0708\r\n\r\n**Personal Notes**\r\n\r\nWhen I have released this assessment, the coronavirus crisis has required for a massive number of companies and entities to go \"remote work\", and an important increment in exposed RDP services on the internet has been detected. Need to emphasize ICS environments and the infrastructure supporting heath services.\r\n",
        "editorId": "10bfc743-3786-435c-88e8-56e791bbc053",
        "id": "a9be2b4f-415e-469b-b767-33ef3264d546",
        "metadata": {
            "attacker-value": 5,
            "exploitability": 3,
            "tags": [
                "common_enterprise",
                "high_privilege_access"
            ]
        },
        "revisionDate": "2020-03-29T16:46:17.149525Z",
        "score": 1,
        "topicId": "131226a6-a1e9-48a1-a5d0-ac94baf8dfd2"
    },
    {
        "created": "2020-03-03T16:18:02.422157Z",
        "document": "Due to public exploits being flaky and sometimes resulting in a Blue Screen on the victim, this exploit is still somewhat difficult to always replicate. If you have paid tools that have better versions of the exploit, it's more reliable.\r\n\r\nThe fact that an exploit is included in newer versions of metasploit massively lowers the bar for being able to exploit this vulnerability.\r\n\r\nThe damage potential is astronomical as there are so many machines that expose RDP to the internet.",
        "editorId": "8deaf797-2af1-4bd1-aea1-98640b61deda",
        "id": "b8769191-423f-4dc4-98c8-210a1ddab3ef",
        "metadata": {
            "attacker-value": 5,
            "exploitability": 3,
            "tags": [
                "high_privilege_access",
                "common_enterprise",
                "default_configuration"
            ]
        },
        "revisionDate": "2020-03-24T03:22:19.935651Z",
        "score": 2,
        "topicId": "131226a6-a1e9-48a1-a5d0-ac94baf8dfd2"
    }
]
Get a CVE
[
    {
        "created": "2020-03-30T13:30:05.033552Z",
        "disclosureDate": "2020-03-30T13:15:00Z",
        "document": "An issue was discovered in Open Source Social Network (OSSN) through 5.3. A user-controlled file path with a weak cryptographic rand() can be used to read any file with the permissions of the webserver. This can lead to further compromise. The attacker must conduct a brute-force attack against the SiteKey to insert into a crafted URL for components/OssnComments/ossn_com.php and/or libraries/ossn.lib.upgrade.php.",
        "editorId": "7191a637-aa4e-4885-98a0-f4f2da285b99",
        "id": "6f81bc44-c000-427d-b222-b64c29bda621",
        "metadata": {
            "baseMetricV3": {
                "cvssV3": {
                    "attackComplexity": "HIGH",
                    "attackVector": "NETWORK",
                    "availabilityImpact": "NONE",
                    "baseScore": 5.9,
                    "baseSeverity": "MEDIUM",
                    "confidentialityImpact": "HIGH",
                    "integrityImpact": "NONE",
                    "privilegesRequired": "NONE",
                    "scope": "UNCHANGED",
                    "userInteraction": "NONE",
                    "vectorString": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N",
                    "version": "3.1"
                },
                "exploitabilityScore": 2.2,
                "impactScore": 3.6
            },
            "references": [
                "CVE-2020-10560",
                "https://techanarchy.net/blog/cve-2020-10560-ossn-arbitrary-file-read",
                "https://github.com/LucidUnicorn/CVE-2020-10560-Key-Recovery"
            ],
            "vulnerable-versions": [
                "n/a"
            ]
        },
        "name": "CVE-2020-10560",
        "revisionDate": "2020-04-03T06:00:16.606546Z",
        "score": {
            "attackerValue": 1,
            "exploitability": 3
        },
        "tags": {
            "commonEnterprise": 0,
            "defaultConfiguration": 1,
            "difficultToDevelop": 0,
            "difficultToExploit": 0,
            "difficultToPatch": 0,
            "easyToDevelop": 1,
            "highPrivilegeAccess": 0,
            "noUsefulData": 1,
            "obscureConfiguration": 0,
            "postAuth": 0,
            "preAuth": 1,
            "requiresInteraction": 0
        }
    }
]
Get Single User by ID
{
    "avatar": "https://avatars2.githubusercontent.com/u/2545096?v=4",
    "created": "2020-02-21T15:42:43.332149Z",
    "id": "7ff62803-e0a8-4121-b324-d4afe9f60d43",
    "score": 52,
    "username": "kevthehermit"
}
Get Single User by Name
{
    "avatar": "https://avatars2.githubusercontent.com/u/2545096?v=4",
    "created": "2020-02-21T15:42:43.332149Z",
    "id": "7ff62803-e0a8-4121-b324-d4afe9f60d43",
    "score": 52,
    "username": "kevthehermit"
}
```

## Testing

```
export API_KEY=YOURAPIKEY
pytest -v --cov=attackerkb_api --cov-report html --cov-report term
```

## Tools using this Library

- [AKB-Explorer](https://github.com/horshark/akb-explorer)