**Introduction**

NLP is the technology used to teach computers to “understand” human language. It is necessary to have a representation (encoding) of text that is interpretable by a computer. To obtain such a representation, a strategy is used that transforms “strings” into numbers, also called the vectorization of text. It is important that these vectors contain information regarding interactions / semantic relationships between sentences, as this is of importance for language understanding. Let’s understand semantic similarity through an example.

“I have a bit of a cold, could this be the new corona virus?” and “I’m afraid I have COVID-19, since I have a cold.” These two sentences have the same meaning, but are formulated differently. It is important that, despite the differences, the computer understands that these sentences have a semantically similar meaning.
When it comes to chatbot, the chatbot should generate similar responses in both the cases so that there is accuracy in the information. In order to achieve this, let’s go through some concepts used behind this project.


**Our Chatbot will be able to perform the following functions:**

1)Answer queries regarding Coivd-19 Symptoms

2)Various Remedies to prevent Spread of covid-19

3)Statistics of Covid -19 include total cases, deaths and recoveries all over the world country wise.

4)Trends related to Covid -19 Graphs

5)Detailed Statistics of Spread of Covid-19 in INDIA


**Design:**

1)Platforms:

1)Visual Studio Code

2)Flask(Python Library)

**NLP Toolkits:**

1)**TensorFlow**: TensorFlow is a free and open-source software library for machine learning. It can be used across a range of tasks but has a particular focus on training and inference of deep neural networks. TensorFlow is a symbolic math library based on dataflow and differentiable programming

2)**Universal Sentence Encoder Model**: The Universal Sentence Encoder encodes text into high dimensional vectors that can be used for text classification, semantic similarity, clustering and other natural language tasks. The model is trained and optimized for greater-than-word length text, such as sentences, phrases or short paragraphs.


For Answering the questions Related to Statistics, we Have used the following APIs to get the data: 

1)India Data: https://api.covid19india.org/data.json 

2)India State wise Data: https://api.covid19india.org/v4/timeseries.json 

3)India District wise Data: https://api.covid19india.org/state_district_wise.json

4)World Data: https://coronavirus-19-api.herokuapp.com/countries

To Run:

1)Download all files to local system.

2)Run test.py.



