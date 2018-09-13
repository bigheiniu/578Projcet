## LeadLine Improvement



####There are four ways where we want to improve the LeadLine. 

1. Hierarchical Structure. Use a hierarchical relationship to give the user a better overview about the topic stream. We find there will be a lot of topics, if reveal all the topic, it will hard for the user to get the trend of the topic. So we would like to cluster topic firstly and make a hierarchical stream that user can click to get the specific topic stream. [Visually Exploring Large Text Collections Using Topic Hierarchies](https://ieeexplore.ieee.org/document/6634160/)
2. Top stories. We want to make a rank board, which will show a monthly the hottest topic. It may be similar to BILLBOARD. Besides this will allow users to click the trend, to get detail information about it.
3. Dynamic. We want to this system can handle stream data, and it will integrate the latest data with previous data. Currently, we would like to add a user defined time decay function so that the user can visualize dynamically. 
4. Keyword Score. In the right top of the previous plot, there is a context pooling, it does not show the importance of each keyword. We would like to make a word cloud. In this way, a word with higher importance will have a large size.





####Problems will meet:     

1. For the first improvement, how to set the particular metric for the topic similarities. 

2. For the third improvement, how to crawl live update news, if we cannot do that, we will simulate the stream data. We will stream static data, and the visualization system will just assume these data are dynamic.



####Structure of this System:

We would like to split the system into three parts: data crawling, data analysis, data visualization.

Each part coupling less with others so that we can work separately. Everyone can just focus on his or her own part. 



####Plan:

Sep. 16 - 19: Talk to Prof

Sep. 20 - Sep. 25: 1. Write documents about this system, we will set the database field and detail information about each systems' interface. 2. Find related package or code help us do the data crawling and natural language process and data visulization.

Sep. 25 - Oct. 20:  Finish basic part of the system. This system can handle a small amount of data. 

Oct. 20 - Oct. 22:  Prepare for the MileStone

Oct. 23 - Nov. 27: Optimize the system

Nov. 27 - Nov. 29: Prepartion for poster presentation

