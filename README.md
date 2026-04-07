# ai-preference-drf

* Project Description:
Build a backend system where users can track their usage of different AI platforms (like OpenAI, Anthropic, Google) and their models (like GPT-4, Claude Sonnet, Gemini Pro).

* Apps:
1. accounts (User)
2. providers (Company, AIProduct, AIModel)
3. usage (UsageLog)

* project folder : ai-preference-drf

* accounts app: 
tokens.py --> custmize JWT token --> it contains role & username
permissions.py --> authorization --> check role to allow access
Authentication (simpleJWT)
User Auth 
Role based permissions