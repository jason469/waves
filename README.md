# Waves
> Created by Jason Liu and Kevin Guo<br>
> This app is currently in **Release 1.0** and has been deployed

### What is Waves?
This application is designed to be a music recommendation application, inspired by Spotify. <br>
Users are able to search for a song within our extensive database, and then categorise their songs within their own custom playlists. <br>
Each song also has additional metadata, such as the artist and genre. 

Using machine learning, our app also includes a trained model that's able to give song recommendations. For any song, users can get personalised feedback on specific songs that they might like (instead of just songs of the same genre or artist)

**Note that this app is not intended for any commercial use, rather it was just to practise our development skills** <br>
All information used in this apps database came from an open source library, and does not include any audio files. 

### What technologies does this app use?
While most applications use a traditional backend/frontend structure, I felt that that was unnecessarily complicated for this application. <br>
I'm aware that I'm building this application with a non-web developer, and so I didn't want to make the stack too complicated else it would make it difficult for him to understand. 

Hence, this application uses the following technologies:
- _**Django**_ makes up the backend and frontend. <br>
- _**HTMX**_ augments the frontend to achieve the same responsiveness and feel of a SPA (Single Page Application) <br>
- _**Django Rest Framework**_ is used to build a small API in the backend <br>
- **_Postgres_** will be used as the database
- _**Docker**_ is used to share the environment between collaborators 
- _**Render**_ was used to deploy the application to the internet

### Future plans for the app
This application is currently in active development, and will begin as a simple responsive web application.<br>
I intend to build this application with a **mobile first** approach.


In the future, I also have the following ideas
- Making the application a PWA, so that it can support offline and mobile-native access

# Where can I see Waves?
To visit Waves, please visit the following link: <br>
> [Waves](https://waves-app.onrender.com)