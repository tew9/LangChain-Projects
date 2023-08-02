# LangChain projects
This repo is the repo I used while learning to build applications empowered by [langchain](https://python.langchain.com/docs/get_started/installation)

## Setup
#### Create and Activate Environment
```pipenv shell```
The pipfile will be created and activated.
#### Install dependencies.
```pipenv install langchain black google-search-results openai python-dotenv```

### Created environment vairable
Get the Keys for the below services for this code to work correctly.
1. create the ````.env```` file in the root directory.
2. Signup for the below services(all have free trial tokens) and Fill out the api keys of the below services in the .env file.
  ### Services Used.
1. [proxycurl - to access linkedin information](https://nubela.co/proxycurl/auth/register) 
2. [serpAPI -  to crawl google](https://serpapi.com/dashboard)
3. [OpenAI - as the Large language model we'll use in our langchain](https://platform.openai.com/)

Example: 

OPENAI_API_KEY=sk-0m93sVqWTd7kf3u4zjkmT3BlbkFJeasdfadsfHadsfa
PROXYCURL_API_KEY=bqSZEbkfbasdfadjHH
SERPAPI_API_KEY=352a7bd1f2d982079dba939a2adsfjadfajjjjjjasdfasfasfsddklkdfaalsf