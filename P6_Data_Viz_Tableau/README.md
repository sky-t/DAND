# Udacity DAND P6 Project Write-Up

Scott Tse
05-25-2017

### Background

I chose to create a visualization of North Korean Missile Test data obtained from [data.world](https://data.world/). The data can also be accessed in this repo in the [data](https://github.com/sky-t/DAND/tree/master/P6_Data_Viz_Tableau/data) folder. 

Click [here](https://public.tableau.com/profile/scott.tse#!/vizhome/UdacityDANDP6Projectv2/Story1) for a link to the final version.

Previous versions can be accessed here:
* [iteration 1](https://public.tableau.com/profile/scott.tse#!/vizhome/UdacityDANDP6Projectv2/Story1)
* [iteration 2](https://public.tableau.com/profile/scott.tse#!/vizhome/UdacityDANDP6Projectv1/Story1)

With the new US administration delivering less predictable and possibly more hawkish rhetoric toward an increasingly belligerent North Korea, the timing seemed right to dive into a related dataset. The dataset obtained includes every known North Korean missile test starting from the first one in 1984 up to the latest one on 05-02-2017.

### Design
I chose to tell a data story using the Tableau Story tool. After doing exploratory data analysis on the dataset, I personally felt there was a central story I could tell (in my case, "North Korea Continues Missile Testing Amid International Pressure"), but I wanted to provide supplementary interesting information about the missile testing that would be educational and helpful to support the main story. 

From a 40K foot level, I tried to use a martini glass approach. The first visualization would tell the main story, then be followed by a series of other supplementary visualizations where the reader could explore the data further and, hopefully, reinforce the main idea. Paring down the data to one main story and 3 supplementary ones, my story outline was:

- **Card 1**: International efforts to curb North Korean missile tests efforts have not led to a reduction in the number of tests (main story)
- **Card 2**: Where do these tests occur? (supplementary story)
- **Card 3**: North Korea has tested missile types capable of various ranges (supplementary story)
- **Card 4**: The types of missiles that North Korea is testing continue to become more sophisticated (supplementary story)

Below, I explain some of the detail behind my design choices for each card. In all cases, I tried to keep the visualizations rich but simple and tried to maximize info to ink ratio.

**Card 1: International efforts to curb North Korean missile tests efforts have not led to a reduction in the number of tests** 
* I wanted to create the effect of an animated timeline so I chose a line chart plot of number of missile tests vs. year as a basis for the visualization  
* I thought this was an effective way to illustrate the main story since the number of tests rises sharply in the past several years 
* I chose red as a theme color for the line, circles and title text since it's evocative of danger, warnings, etc.
* In order to show that there were years that had no missile tests, I overlayed circle shapes on top of the trend line.
* I added text boxes to show the main sanctions and resolutions passed over the years and illustrate the fact that even after so many sanctions, the tests continue and are rising

**Feedback**
* In Tableau public, the chart gets compressed and appears too busy. Consider reducing density of info and text boxes
* Adding automatic animation to this card would really enhance it. Resolution: in Tableau Public this visualization does not have a play button for the pages widget, but in Tableau desktop this functionality is available. For the purposes of this project I thought this was good enough.



**Card 2: Where do these tests occur?**
* My intent here was to give the reader some geographic context as to where North Korea sits relative to the East Asia geopolitical theater and provide some useful information about where the missile tests occur (at least the launch sites).
* For the top visualization I chose a bubble map to show the number of tests at each launch site. I chose to use double encoding, using both an orange-red sequential color palette and circle size to encode the number of tests per site. 
* In order to enhance visual accuracy for the reader, I also included a sorted barplot underneath the bubble map, also displaying number of tests per site. 
* I used both visualizations as filters to enhance interactivity so that if a reader clicked on a facility in the barplot, it would highlight its location on the map and vice versa.

**Feedback**
* Lower barplot was compressed and text was unreadable in Tableau public so I moved the barplot to the right side and put the supporting text on top




**Card 3: North Korea has tested missile types capable of various ranges**
* I chose a scatterplot with apogee on the y-axis and distance on the x-axis which seemed intuitive to understand. Each point represents a single missile test.
* I chose a triangle for the points, hoping to evoke projectiles, and colored them by missile type.
* There were null values for both apogee and distance in some cases. I chose to encode them in the visualization and noted this to readers. I felt that conveying this information outweighed the possible confusion that might occur
* In the point tooltips, I chose to include the metrics apogee, distance, missile type, test result, and year of test. I chose not to encode test result using shape on the chart because I was concerned about cognitive load and confusing the chart with too much information up front.

**Feedback**
* The original visualization had two scatterplots of apogee vs time and distance vs time, with the distance chart over top of the apogee chart. In those charts ([Dashboard 1](https://public.tableau.com/profile/scott.tse#!/vizhome/UdacityDANDP6Projectv1/Dashboard1)), I used color and size to encode number of tests, then used shape to encode test result. The feedback received indicated that while distance and apogee were interesting dimensions to explore, the charts were hard to understand: there was too much going on, there was confusion about mapping a test in one chart to the same test in the other. The eye jumps from the lower chart to upper trying to understand how they relate. For this reason I switched to the single scatterplot chosen.



**Card 4: The types of missiles that North Korea is testing continue to become more sophisticated**
* I chose a stacked barplot with number of tests on the y-axis and year on the x-axis. I used color to encode test type, and included a filter for test result and a highlighter for missile type. 
* I also added mark annotations with test descriptions to further emphasize the progression of North Korean missile technology. I ordered the text annotations in a "staircase" manner from left to right, hoping to further emphasize technology progression 


**Feedback**
* In my initial [v1](https://public.tableau.com/profile/scott.tse#!/vizhome/UdacityDANDP6Projectv1/Story1) and [v2](https://public.tableau.com/profile/scott.tse#!/vizhome/UdacityDANDP6Projectv2/Story1) versions, I had a two charts on this card. 
* Cramming two charts into the card caused scrolling which was annoying and made the two charts hard to compare 
* The legend text became cropped, reducing its effectiveness
* Two charts of this complexity stacked on top of each other is too much. Can you try to do it in one chart?




### Additional Feedback (not card specific)
* The scrolling card boxes at the top of the data story take up valuable space. They could be shrunk to get more room. Resolution: I ended up doing this, but reducing the text in these boxes.
* Try to unify the color scheme more. There is red text and black text used. Resolution: I used red for all chart titles for more consistency. 


### Resources
* [The CNS North Korea Missile Test Database by Ian Greenleigh on data.world](https://data.world/ian/the-cns-north-korea-missile-test-database)
* [Wikipedia page for sanctions against North Korea](https://en.wikipedia.org/wiki/Sanctions_against_North_Korea) 
* [Connecting dots on a Tableau line chart](https://community.tableau.com/thread/145202)
* [Korean People's Army Strategic Force](https://en.wikipedia.org/wiki/Korean_People%27s_Army_Strategic_Force)

