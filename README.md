# Game Recommendation System
**Date:** *Originally built on 2.6.2023, revisited on 2.2.2025*  
**Author:** *Martin Čičala*  
**Contact:** [LinkedIn](https://www.linkedin.com/in/martin-%C4%8Di%C4%8Dala-545638182/) | *martin.cicala[at]gmail.com*  


---

## Screenshots
**Main Window**
![Screenshot 1](/screenshots/0.PNG)
**Loading screen**
![Screenshot 0.6](/screenshots/0.6.PNG)
**Autocomplete**
![Screenshot 0.5](/screenshots/0.5.PNG)
**Example game recommendation**
![Screenshot 1](/screenshots/2.PNG) 

---

## About This Project  

This project was one of my earlier steps into **data science and machine learning**, created while I was working to break into the field. It showcases my ability to **scrape data, preprocess it, build recommendation systems, and develop a full PyQt6 desktop application**.  

Since then, I have gained experience as a **data analyst/scientist** and have worked on more advanced projects in **Python, machine learning, and data engineering**. While I can now use more sophisticated methods, I still include this project in my portfolio as a demonstration of my **clean code, structured pipelines, and ability to write a complete application from start to finish**.  

*(Last revisited on 2.2.2025 to give it some polish after the years :-) )*

---


## Table of contents
1. [Overview](#overview)  
2. [Key Features](#key-features)  
3. [Data for Similarity Calculation](#data-for-similarity-calculation)  
4. [Data Collection Process](#data-collection-process)  
5. [Data Scraping & Cleaning](#data-scraping--cleaning)  
6. [Data Visualization & Preprocessing](#data-visualization--preprocessing)  
7. [Recommendation System](#recommendation-system)  
8. [UI & Real-Time Thumbnail Scraping](#ui--real-time-thumbnail-scraping)  
9. [Screenshots](#screenshots)  
10. [Installation & Usage](#installation--usage)  
11. [Challenges & Learnings](#challenges--learnings)  
12. [Future Enhancements](#future-enhancements)  
13. [License](#license)  

---

## Overview
Have you ever finished an amazing game and wished for something equally good? This project addresses that desire by recommending **Steam** games that match a given “reference” game in terms of genre, popularity, and other attributes. Built in **Python** with a **PyQt6** frontend, this recommendation system uses **data science pipelines** to preprocess, transform, and apply **cosine similarity** to suggest new games.

The end result is a **desktop application** that runs on its own, allowing you to **search for a game**, **view its thumbnail**, and **find similar games** in real time. It reflects a blend of **data engineering**, **machine learning**, and **UI design** skills.

---

## Key Features
- **Extensive Game Database**  
  Leverages a dataset of ~57,000 Steam games for comprehensive coverage, including both mainstream and niche titles.

- **Automated Data Scraping**  
  Uses [Selenium](https://www.selenium.dev/) and manual scrolling to extract game details (titles, prices, developers, tags, etc.), saved in JSON files for flexible reprocessing.

- **Data Pipelines & Visualization**  
  Employs **scikit-learn pipelines** for data cleaning, imputation, type conversion, one-hot encoding and scaling.

- **Item-Item Collaborative Filtering**  
  Implements **cosine similarity** on both **numerical** and **categorical** features for an item-item recommendation approach.

- **Threaded PyQt6 UI**  
  A full-featured **desktop app** with:
  - Dark mode theme
  - **Autocomplete** for game titles
  - **Separate loading thread** to keep the interface responsive
  - Real-time game thumbnail retrieval

---

## Data for Similarity Calculation
### Numerical values
Used the following numerical attributes for finding the most similar games:
- price (example 4.99 eur)
- release date (scaled with start 1.1.1970 and converted to numerical value)
- steam rating (for example 4.5/10)
- total overall review count (e.g. 10k reviews in total)
- positive review count (e.g. 9k positive reviews)
- total recent reviews (e.g. 100 reviews in last 30 days)
- number of positive recent reviews (e.g. 90 positive reviews in last 30 days)
### Categorical values
Used so-called **app-tags**. These are genre tags that users add to games in high numbers. They include a much wider variety than just **genre** from Steam. Similarity search subjectively yields better results for app-tags than genres.

Example of several app-tags:
- 3D
- Action RPG
- Anime
- Co-op Campaign
- Female Protagonist
- First-Person
- Fishing
- Medieval
- Multiple Endings
- Nonlinear
- PvP
- RPG
- Racing
- Real-Time
- Sandbox
- Singleplayer
- Split Screen
- VR
- World War II

### Combining attributes
- I combined numerical and categorical attributes by:
  - computing cosine similarity of numerical attributes N
  - computing cosine similarity of categorical attributes C
  - taking a weighted mean = w1 * N + w2 * C
  - I experimented with weights but concluded that classical mean represents game themes and their prices and ratings well enough


---

## Data Collection Process
### Gathering Steam Game IDs
- Explored the [Steam Store](https://store.steampowered.com/search/?) to identify how game pages are structured.
- Attempted automated scrolling with Selenium but faced **anti-scraping blocks**.
- **Practical workaround**: Manually loaded and scrolled the store page, then saved the HTML containing game IDs. A Python script subsequently extracted ~57k game IDs.

---

## Data Scraping & Cleaning
### Scraping Details
- Constructed a URL for each game ID and scraped key attributes (title, price, app tags, developers, etc.).
- Stored results in individual **JSON files** to mitigate partial failures and allow easy re-runs.
- Combined JSONs into a **Pandas DataFrame** and saved as CSV for efficient reading. I converted the CSV into *feather* for fast reading during app run.

### Cleaning Steps
- Removed non-game entries (e.g., many soundtracks, hardware links, ...).
- Filtered out rows with incomplete or invalid data (e.g., NaNs in critical columns).
- De-duplicated and handled anomalies (e.g., inconsistent tags).

---

## Data Visualization & Preprocessing
- **Visualization**: Conducted exploratory analysis (e.g., distributions of prices, review scores, etc.) to spot outliers.
- **Preprocessing**: 
  - Converted date strings to numeric days.  
  - One-hot encoded **categorical attributes** (e.g., `app_tags`).  
  - Scaled continuous variables to `[0,1]`.  
  - Used **manual imputations** for popular games with missing data.

A set of **scikit-learn transformers** orchestrates this process, ensuring reproducible transformations at each stage.

---

## Recommendation System
- **Approach**: Item-item collaborative filtering, where the similarity between two games is measured via **cosine similarity** of their feature vectors.
- **Features**: 
  - Numerical: `price_eur`, `release_date`, user review counts, etc.  
  - Categorical: `app_tags` (e.g., `2D`, `Racing`, `Platformer`), coded via one-hot encoding.  
- **Weighted Averages**: Combined numerical and categorical similarities with adjustable weights.  
- **Result**: A ranked list of **similar games** for any input “reference” game of choice.

---

## UI & Real-Time Thumbnail Scraping
- **PyQt6**: A clean, modern interface with:
  - **Autocomplete**: Suggests game titles as you type.
  - **Threaded Loading**: A `QThread` handles recommendation logic in the background, preventing UI freeze.
  - **Clickable Links**: Each result links to the respective Steam store page for immediate access.
- **Real-Time Thumbnails**:  
  - During app runtime, the thumbnail is fetched from the game’s Steam URL.  
  - The thumbnail is displayed next to the recommendation for quick visual reference.

---

## Installation & Usage
1. **Clone or Download** this repository.
2. **Install Dependencies** (e.g. `pip install -r requirements.txt` or manually):
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**
   ```bash
   python main.py
   ```
4. **Interact**:
- Type a game name (Autocomplete assists you).
- Click **Recommend**.
- View the results, including **thumbnails** and **Steam store links**.

---

## Challenges & Learnings

- **Web scraping obstacles**
  - Steam's anti-bot measures made automated collection difficult. **Manual scrolling** combined with partial Selenium usage was the practical soltion.
- **Data quality**
  - Incomplete or invalid data from scraping demanded thorough cleaning. This reinforced how **data integrity** is crucial to model performance.
- **Recommendation system fundamentals**
  - Implementing cosine similarity across **mixed data types** (numerical vs. categorical) required some feature engineering and weighting strategies.
- UI and Threading
  - Handling long-running tasks on the UI thread would freeze the user interface. I used `QThread` to offload processing.

---

## Future enhancements

- Idea 1: Real-time title suggestion speed
- Idea 2: User feedback loop + reinforcement learning
- Idea 3: Textual analaysis of game description with NLP

## License
See LICENSE file.








## Introduction
As a gamer and a data scientist, I have often found myself yearning for a similar gaming experience after finishing an engaging game full of stories. I wanted to bridge this gap, and hence, I decided to leverage my data science skills to develop a recommendation system that would recommend similar games to players.

## Features
* **Extensive Game Database:** Utilizes a database of around 57,000 games from Steam.
* **Data Scraping and Cleaning:** Automated live web-scraping of game details such as title, price, developers, tags, and more. The data is then cleaned and processed for use in the recommendation system.
* **Data Visualization and Preprocessing:** Incorporates data visualization for better understanding and preprocessing for preparing the data for recommendation.
* **Item-Item Collaborative Filtering:** Employs cosine similarity for an item-item collaborative filtering-based recommendation system.
* **User-Friendly UI:** Features a modern, dark-mode user interface built with pyqt6, which includes an autocomplete feature for easy game selection.
* **Real-Time Thumbnail Scraping:** Fetches game thumbnails in real-time based on the game's Steam URL.


## Data Collection
My first step involved exploring the Steam website to understand the structure of its game lists. After extensive exploration, I found that each game title page URL had a fixed form with a specific steam ID. If I get this ID, I can get the details of the game. Hence, my first task was to get as many game IDs as possible. I wrote a script using Selenium which scrolled the [Steam website](https://store.steampowered.com/search/?) with an infinite load. However, it seems like anti-scraping mechanisms of Steam detected the bot and stopped it. Hence, I overcame this by manually loading the Steam website while scrolling occasionally for long enough. Finally, I downloaded the html site with the game IDs and extracted them with a python script.

## Data Scraping and Cleaning
Using the IDs, I constructed a URL for each game and scraped relevant attributes such as game title, game price, user-defined app tags, developers, and more. This process took around 12 hours, and the data was saved in individual JSON files for convenience. I then converted the data into a Pandas dataframe and saved it as a CSV file for further processing.

In the process, I encountered some inconsistencies in the data due to errors in the scraping process. For example, some "games" were not actually [typical games](https://store.steampowered.com/app/1551360/Forza_Horizon_5/) but links to [game soundtracks](https://store.steampowered.com/app/1271470/World_of_Goo_Soundtrack/), gaming products like the [Steam Deck](https://store.steampowered.com/steamdeck) etc. I then cleaned the dataset by removing games with NaN information in some columns.

## Data Visualization and Preprocessing
Using scikit-learn, I built data pipelines to load and visualize the data. To be exact, I built a data processing pipeline that included data type conversion, column selection, one-hot encoding, and scaling of numerical and categorical columns.

## Recommendation System
After learning about recommendation systems, I decided to use item-item collaborative filtering for my project. I used columns like 'price_eur', 'release_date', 'steam_rating', 'total_overall_reviews', 'positive_overall_reviews' and one-hot encoded categorical columns like 'app_tags' (for example '2D', 'racing', 'platformer' etc.). I created embeddings from the columns and used cosine similarity to find items represented by embeddings with the most similar angles. Additionally, I gave both categorical and numerical columns weights which I tuned by hand by trying the recommendation system.

## UI and Real-Time Thumbnail Scraping
I developed a full user interface using object oriented programming (OOP) in PyQt6. This should allow a user to use the full desktop app by simply running the main function. I also implemented a feature that scrapes the thumbnail of a game based on its steam URL in real time during the application run for even better user experience. The UI is also equipped with an autocomplete feature to aid the user in selecting a game. This works simply by comparing the user-typed text with the names of the scraped games.

Finally, I connected all the components, polished the UI, created a loading screen, and pushed the project to GitHub.

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

1. **Web Scraping:** Initially, I built a web scraper to automatically scroll through Steam's infinite games page. However, I didn't succeed with it. The solution came in the form of a more hands-on approach, where I manually loaded and scrolled the page in my browser. This experience taught me the importance of practicality in problem-solving, reinforcing the idea that the simplest methods can sometimes be the most effective.

2. **Data Quality:** I encountered issues with the quality of my scraped data due to errors in my scraping script. I had to rework the script and run it again, leading to extra resource time. This challenge underscored the importance of attention to detail and pre-testing, especially when dealing with relatively big datasets.

3. **Recommendation Systems:** Understanding and implementing a recommendation system was a learning curve. I chose an item-item recommendation model using cosine similarity based on game data like price, date, popularity, and genres, which taught me about the trade-offs between model complexity and resource feasibility. I learnt how to calculate cosine similarity measures for different types of data (numerical and one-hot-encoded categorical) and how to combine them using weighted averages.

4. **Application Design:** Designing the user interface presented its own challenges. I had to learn how to run a separate thread for my loading screen while maintaining the main UI window. This experience improved my understanding of multi-threading in application design.

In summary, this project has enriched my understanding of data science and machine learning, and I look forward to using these lessons in my future endeavors.

## Future Enhancements
To further improve the project, in the future I would like to improve the application optimization by running more quickly - suggesting game titles more quickly and scraping the internet in real time more quickly. There are also other ways to rework the program - for example, using a reinforcement learning system where the user would rate the recommendations and so the system would learn from this input. Or, game descriptions could be turned into numerical data and included in similarity calculation, although this would likely not bring a huge positive impact in recommendation.

