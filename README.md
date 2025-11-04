# Bibliographic-Network-Representation-of-Pdf

Background
I am interested in analyzing information on the relations between words in a scientific article.
Semantic networks are a type of graph network used where individual words are assigned
grammar types and connected to each other. The individual word represents a node and the edges
connected between the nodes represent relations. For example, with the words fish and salmon
an edge relation could be “is a”. A salmon is a fish. In this way, semantic networks are used to be
trained by deep neural networks that are the basis for natural language processing models.
Semantic networks can be generated using Java Packages or Python packages such as nltk
(natural language processing package), iGraph, and NetworkX. However, when exploring
GitHub these scripts seemed out of reach for my understanding. I am particularly interested in
how different methods of word characteristics such as spacing within an article and paragraph
location compare to traditional semantic network. As such, I will obtain a semantic network and
generate my own bibliographic network to compare network metrics between the two network
representations.
Network datasets
I have already obtained the semantic network dataset from https://nocodefunctions.com/. This
website appeared to be legitimate. It is an open-source site developed in 2021 that allows
generation of semantic networks from articles as pdfs. The GitHub for the open-source code is:
https://github.com/seinecle/nocodefunctions-web-app. I have already used the website to
generate a .gefx file of the semantic network that can be used by Gephi. I have attached the
semantic network and the article (a geographic hazards article) that it was built on.
My interest in generating a bibliographic network is to compare how different data
representations in a network lead to different metric values. I will be generating the bibliographic
network as a .gdf file, as for the information I wish to use in the bibliographic network it will not
require a hierarchical or dynamic representation. The workflow for generating the network is as
follows: I will create a list of the top 100 words in the article with highest degree in the semantic
network, omitting common words such as “a, the, on, etc.”. I will parse each word in the .pdf
article using a python library such as nltk to produce a second list. I will assign each word in the
second list an index based on the paragraph it occurs in the article. Some words will be
duplicates or occur multiple times in the same paragraph. Then I will modify the second list to
only include the top 100 words from the semantic article. Next, I will merge duplicate words in
the list and create a count variable for their total occurrences and a set variable for each
paragraph they occur in. Finally, I will read all words in the list and write their node
representation into a .gdf file with the following attributes: (string word, int total_occurrences,
set paragraphs_included_in). Each edge would represent the relation where words occur in the
same paragraph and have the structure: (string word1, string word2, int paragraphs_in_common,
set paragraphs_in_common). (For a bibliographic network I may have to use a different file type
and matrix representation where a weight of 1 is added whenever two words are contained in the
same paragraph as another word.)
Metrics
The metrics should be calculated and compared between the semantic network and bibliographic
network. Since the network of words is similar to a social network, measures of
associativity/assortivity would be interesting, as well as comparing density, betweenness, and
closeness centrality measures.
