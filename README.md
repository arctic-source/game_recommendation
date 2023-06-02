# Game Recommendation System
This project was created by Martin Čičala. Feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/martin-%C4%8Di%C4%8Dala-545638182/) or via email at martin.cicala[at]gmail.com.
![Neuron Animation](https://github.com/arctic-source/game_recommendation/blob/master/animations/best/2.gif)

## Introduction
As a gamer and an aspiring data scientist, I have often found myself yearning for a similar gaming experience after finishing an engaging game full of stories. I wanted to bridge this gap, and hence, I decided to leverage my data science skills to develop a recommendation system that would recommend similar games to players.

## Features
* **Extensive Game Database:** Utilizes a database of around 57,000 games from Steam.
* **Data Scraping and Cleaning:** Automated scraping of game details such as title, price, developers, tags, and more. The data is then cleaned and processed for use in the recommendation system.
* **Data Visualization and Preprocessing:** Incorporates data visualization for better understanding and preprocessing for preparing the data for recommendation.
* **Item-Item Collaborative Filtering:** Employs cosine similarity for an item-item collaborative filtering-based recommendation system.
* **User-Friendly UI:** Features a modern, dark-mode user interface built with pyqt6, which includes an autocomplete feature for easy game selection.
* **Real-Time Thumbnail Scraping:** Fetches game thumbnails in real-time based on the game's Steam URL.


## Data Collection
My first step involved exploring the Steam website to understand the structure of its game lists. After extensive exploration, I found that each game title page URL had a fixed form with a specific steam ID. With this knowledge, I wrote a script using Selenium to scroll through the website and scrape the games. This process presented certain challenges, but I overcame them by manually loading the Steam website with the list of all games and saving the HTML content of the website. Finally, I created a python script to get a list of about 57,000 steam game IDs.

## Data Scraping and Cleaning
Using the IDs, I constructed a URL for each game and scraped relevant attributes such as game title, game price, user-defined app tags, developers, and more. This process took around 12 hours, and the data was saved in individual JSON files for convenience. I then converted the data into a Pandas dataframe and saved it as a CSV file for further processing.

In the process, I encountered some inconsistencies in the data due to errors in the scraping process. I then reran the scraping process and cleaned the dataset by removing games with NaN information in crucial columns.

## Data Visualization and Preprocessing
Using scikit-learn, I built pipelines to load and visualize the data. Additionally, I built a data processing pipeline that included data type conversion, column selection, one-hot encoding, and scaling.

## Recommendation System
After learning about recommendation systems, I decided to use item-item collaborative filtering for my project. I used cosine similarity as a measure of similarity between games. Furthermore, I built an elegant dark-mode UI using pyqt6 for the user to interact with the recommendation system.

## UI and Real-Time Thumbnail Scraping
I also implemented a feature that scrapes the thumbnail of a game based on its steam URL in real time during the application run. The UI is also equipped with an autocomplete feature to aid the user in selecting a game.

## Final Steps
I modified the recommendation pipeline to process numerical and categorical-turned-numerical data separately, allowing the calculation of separate similarity scores. I then computed a weighted mean of these scores to generate the final recommendations.

Finally, I connected all the components, polished the UI, created a loading screen, and pushed the project to GitHub.

## Screenshots
![Screenshot 1](/screenshots/0.PNG)
![Screenshot 2](/screenshots/1.PNG)
![Screenshot 3](/screenshots/13.PNG)
![Screenshot 4](/screenshots/6.PNG)

## Installation & Usage
Pull the repository. The following libraries are needed to be downloaded in order for the code to run (e.g. using pip):
* numpy  
* pandas  
* matplotlib  
* pillow  
* scikit-learn  

## License


## Challenges & Learnings

This project presented numerous opportunities to apply my knowledge and improve my skills in data science. Here's a reflection on the key challenges I encountered and the valuable lessons I learnt:

1. **Web Scraping:** Initially, I built a web scraper to automatically scroll through Steam's infinite games page. However, I faced challenges in terms of speed and functionality. The solution came in the form of a more hands-on approach, where I manually loaded and scrolled the page in my browser. This experience taught me the importance of practicality in problem-solving, reinforcing the idea that the simplest methods can often be the most effective.

2. **Data Quality:** I encountered issues with the quality of my scraped data due to errors in my scraping script. I had to rework the script and run it again, leading to extra resource time. This challenge underscored the importance of attention to detail and pre-testing, especially when dealing with large datasets.

3. **Recommendation Systems:** Understanding and implementing a recommendation system was a learning curve. I chose an item-item recommendation model using cosine similarity, which taught me about the trade-offs between model complexity and resource feasibility. I learnt how to calculate similarity measures for different types of data (numerical and one-hot-encoded categorical) and how to combine them using weighted averages.

4. **Application Design:** Designing the user interface presented its own challenges. I had to learn how to run a separate thread for my loading screen while maintaining the main UI window. This experience deepened my understanding of multi-threading in application design.

In summary, this project has enriched my understanding of data science and machine learning, and I look forward to leveraging these lessons in my future endeavors.

## Future Enhancements
To further improve the project, in the future I would like to improve the application optimization by running more quickly - suggesting game titles more quickly and scraping the internet in real time more quickly. There are also other ways to rework the program - for example, using a reinforcement learning system where the user would rate the recommendations and so the system would learn from this input. Or, game descriptions could be turned into numerical data and included in similarity calculation, although this would likely not bring a huge positive impact in recommendation.

![Neuron Animation](https://github.com/arctic-source/game_recommendation/blob/master/animations/best/3.gif)
