# Miss Info (CruzHacks 2024)

A web page that detects any misinformation present in TikTok videos using AI and Large Language Models. The LLMs used for this project include LLama, ChatGPT, and Assembly-AI. OpenCV and CDN are also used to process video frames. After the provided TikTok video is processed, a summary of the misinformation analysis is displayed alongside relevant sources from [snopes.com](https://www.snopes.com). (Project for CruzHacks 2024)

![Screen Shot 2024-01-21 at 4 14 13 AM](https://github.com/inkyant/cruz-hacks-2024/assets/86862325/3f114ac2-ab5b-4b18-9644-d9bf31f7b6f5)

# Usage

Insert your OpenAI, AssemblyAI, Replicate, and CDN keys in [backend/api/api_keys.py](https://github.com/inkyant/cruz-hacks-2024/blob/main/backend/api/api_keys.py)

This project consists of two components: the React application for webpage rendering and the Flask application for running the LLM APIs and processing the TikTok video. Both components must be run for the web application to function.

In one terminal, run the following commands to start up the React application:

```
cd client
npm install
npm run start
```

In another terminal, run the following commands to start up the Flask application:

```
pip3 install -r requirements.txt
cd backend
python3 app.py
```
