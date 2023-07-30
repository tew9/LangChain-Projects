import os

import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
  Manually scrape the information from the LinkedIn profile

  Args:
      linkedin_profile_url (str): linkedIn profile url
  """
    # api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    gist_api_endpoint= "https://gist.githubusercontent.com/tew9/751838c1a9cc5bf2db75792a3c43fe78/raw/52bafe6af8c560032dffc155536bb2f0bd06b0dd/tango.tew.json"
    
    header_dic = {"Authorization": f'Bearer {os.environ["PROXYCURL_API_KEY"]}'}

    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    # )
    
    response = requests.get(gist_api_endpoint)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None, "null")
        and k not in ["people_also_viewed", "certifications", "background_cover_image_url", "profile_pic_url"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
