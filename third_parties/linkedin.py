import os

import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile

    Args:
        linkedin_profile_url (str): linkedIn profile url
    """
    
    if linkedin_profile_url.__contains__("company"):
        linkedin_profile_url = linkedin_profile_url.replace("company", "in")

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

    header_dic = {"Authorization": f'Bearer {os.environ["PROXYCURL_API_KEY"]}'}

    """Uncomment this to really call the proxy curl api endpoint"""
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    # uncomment the below code to Use the gist api endpoint instead after being done with the free api calls
    # gist_api_endpoint = "https://gist.githubusercontent.com/tew9/751838c1a9cc5bf2db75792a3c43fe78/raw/5b2306aa78bd540f18f638f0dba7eabe1bb738c9/tango.tew.json"
    # response = requests.get(gist_api_endpoint)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "None", None, "null")
        and k
        not in [
            "people_also_viewed",
            "certifications",
            "background_cover_image_url",
            "Expires",
            "logo_url", 
            "Credential",
            "activities",
            "company_linkedin_profile_url",
            "description",
            "experiences",
            "education"
        ]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_url="linkedin_profile_url").get("profile_pic_url"))
