# Progress

Video Selection [Now Majority English Is A Criterion ]
video id - RNXqM8vdw4M

Degree Of Disputability Of A Comment(Maybe Based On Reply Count)

- [x] Data Collection
	- [x] API Fetch
	- [x] TO CSV
	- [x] Find English Majority Comment Video

- [ ] Data Analysis
	- [ ] Get Sentiment Analysis
	- [ ] Hatespeech Score
	- [ ] Political Affiliation(Simple, Keyword involving party names)

- [ ] Data Visualization
	- [ ] How Sentiment Changes After Video Publishment (Timewise).
	- [ ] How Sentiment Is Different For Different Youtuber for same topic
	- [ ] ??	
	- [ ] Make Sort Of A Dashboard

## Issues
Require English Comments Only Since Models Are Trained Using English
# Opinion


## IDEAS

- [x] Data Collection

Input Features

- Video Like
- Video Dislike
- Video Title
- Video Description
- Video Views

- Comment Timing
- Comment Like
- Comment Reply count
- Comment (desc)




Like, Dislike -> Sentiment Analysis

1. Video Choose -> Feature
2. Feature, Video Analysis


Target Features

Modi Government Comment.
Congress Governement.
AAP Government Comment.
Neutral Comments.

- [x] How To Fetch All The Comments and Video from Youtube.
- [x] Given A Video How To Process Comments.


## TO DO

- [ ] What Features Should Be Extracted From Youtube Comments.


## References


- [ChatGPT Ques1][How to extract feature, from comments and what should be the features]

Processing comments on political discussions involves similar steps to the general approach for text data. However, when dealing with political discussions, there are specific considerations due to the nature of the content. Here's a guideline on how to process political comments and what features could be considered as target features:

### Steps for Processing Political Comments:

1. **Text Preprocessing:**
   - Remove irrelevant characters, punctuation, and special symbols.
   - Convert text to lowercase.
   - Tokenization: Break the text into individual words or tokens.
   - Remove stop words.
   - Address common issues like misspellings and abbreviations.

2. **Feature Extraction Techniques:**
   - Use Bag of Words (BoW) or TF-IDF to represent the comments.
   - Consider using word embeddings like Word2Vec or GloVe.
   - Explore N-grams for capturing sequences of words.
   - Conduct sentiment analysis to understand the overall sentiment of the comments.

3. **Topic Modeling:**
   - Apply techniques like Latent Dirichlet Allocation (LDA) to identify key topics within the political discussions.

4. **Named Entity Recognition (NER):**
   - Extract named entities to identify key political figures, organizations, and locations mentioned in the comments.

5. **Emotion Analysis:**
   - Analyze the emotional tone of the comments to understand the sentiment and intensity of emotions expressed.

### Target Features:


1. **Political Affiliation:**
   - Determine the political affiliation of the commenter (liberal, conservative, centrist, etc.). This could be a binary classification (e.g., liberal vs. conservative) or a multi-class classification task.

2. **Sentiment:**
   - Assign sentiment labels to comments (positive, negative, neutral) to understand the overall emotional tone.

3. **Topic Distribution:**
   - Identify the main topics or issues discussed in political comments. This can help in understanding the key themes within the political discourse.

4. **Named Entities:**
   - Count and analyze mentions of political figures, organizations, and locations. This could provide insights into which entities are frequently discussed.

5. **Polarization Index:**
   - Calculate a polarization index to measure the degree of polarization in the comments. This may involve assessing the divergence of opinions within the discussion.

6. **Engagement Metrics:**
   - Consider features related to user engagement, such as the number of likes, shares, or comments on a particular comment. This can indicate the impact and influence of a comment.

7. **Temporal Analysis:**
   - Explore how sentiments and topics change over time. This could involve analyzing comments in the context of specific events or periods.

8. **User Influence:**
   - Evaluate the influence of users by considering factors such as the number of followers, frequency of posting, or the level of engagement with their comments.

Remember that the choice of target features depends on your specific research question or goal. For instance, if you are interested in understanding political polarization, your target feature might be a polarization index based on sentiment and topic features. Alternatively, if you are building a sentiment analysis model, sentiment labels may be the primary target features.

- [ChatGPT Ques2][Polarization Index elaborate]

A polarization index is a quantitative measure that assesses the degree of polarization within a set of data, often in the context of opinions or sentiments. In the context of political discussions, a polarization index can be used to quantify the extent to which the opinions expressed in comments diverge or align along different ideological lines. Here's a more detailed explanation of how you might calculate and interpret a polarization index:

### Calculating a Polarization Index:

1. **Sentiment Analysis:**
   - Assign sentiment labels (positive, negative, neutral) to each comment using a sentiment analysis algorithm.

2. **Political Affiliation:**
   - Determine the political affiliation of the commenter (e.g., liberal, conservative, centrist). This can be done manually through labeled data or using machine learning models if the data is available.

3. **Pairwise Sentiment Comparison:**
   - For each pair of comments, determine whether they express similar or opposing sentiments. You may create a binary matrix indicating whether comment i and comment j have similar (1) or opposing (0) sentiments.

4. **Calculating the Polarization Index:**
   - Use the binary matrix to calculate the polarization index. One common method is to calculate the fraction of comment pairs with opposing sentiments. This can be expressed as the ratio of the number of opposing sentiment pairs to the total number of comment pairs.

   \[ \text{Polarization Index} = \frac{\text{Number of Opposing Sentiment Pairs}}{\text{Total Number of Comment Pairs}} \]

   The resulting index ranges from 0 to 1, where 0 indicates no polarization (all comments have similar sentiments), and 1 indicates maximum polarization (all comments have opposing sentiments).

### Interpreting the Polarization Index:

- **Low Polarization (Near 0):** Comments generally express similar sentiments, indicating a more cohesive or consensus-driven discussion. This could suggest a less polarized environment.

- **Moderate Polarization (0.3 - 0.7):** There is a mix of similar and opposing sentiments, suggesting a moderate level of polarization. This is a common scenario in diverse discussions where participants hold different views.

- **High Polarization (Near 1):** Most comments express opposing sentiments, indicating a highly polarized environment with strong ideological divides.

### Considerations:

- **Normalization:** Depending on the size of the dataset, you may want to normalize the polarization index to account for variations in the number of comments.

- **Thresholds:** You can set specific thresholds for defining low, moderate, and high polarization based on your context and research goals.

- **Temporal Analysis:** You can calculate the polarization index over different time periods to analyze how polarization evolves over time, especially in response to specific events.

The polarization index provides a quantitative measure that can be useful for researchers studying online political discussions, social dynamics, and the impact of polarization on public discourse. Keep in mind that it's just one of many possible metrics, and its interpretation should be considered in the broader context of your analysis.
