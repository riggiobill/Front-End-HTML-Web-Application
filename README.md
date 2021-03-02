![alt text](https://github.com/riggiobill/Web-Design-Challenge/blob/main/Screenshots/Web-Design-Screenshot-1.png?raw=true)



# Front-End-HTML-Web-Application - Visualization Dashboard

HTML and CSS  can be used to integrate a variety of pages into a single index, allowing for some fluid and information dashboard applications. To create a dashboard showing off the analysis I've done and the graphs I've charted, I used HTML, Javascript, CSS, and Bootstrap.

![alt text](https://github.com/riggiobill/Web-Design-Challenge/blob/main/Screenshots/Web-Design-Screenshot-2.png?raw=true)




# Latitude - Latitude Analysis Dashboard with Attitude
Created a visualization dashboard website using visualizations created in past assignments. Specifically, this program will be plotting weather data.

![alt text](https://github.com/riggiobill/Web-Design-Challenge/blob/main/Screenshots/Web-Design-Screenshot-3.png?raw=true)

In building this dashboard, I created individual pages for each plot and a means by which the user can navigate between them. These pages will contain the visualizations and their corresponding explanations. It also has a landing page, a page where one can see a comparison of all of the plots, and another page where one can view the data used to build them.




# Website Components:

The website consists of 7 pages total, including:

# # A landing page containing:
An explanation of the project.
Links to each visualizations page. There is a sidebar containing preview images of each plot, and clicking an image takes the user to that visualization.
Four visualization pages, each with:
A descriptive title and heading tag.
The plot/visualization itself for the selected comparison.
A paragraph describing the plot and its significance.


# # A "Comparisons" page that:
![alt text](https://github.com/riggiobill/Web-Design-Challenge/blob/main/Screenshots/Web-Design-Screenshot-4.png?raw=true)
Contains all of the visualizations on the same page so one can easily visually compare them.
Uses a Bootstrap grid for the visualizations.
The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.




# # A "Data" page that:
![alt text](https://github.com/riggiobill/Web-Design-Challenge/blob/main/Screenshots/Web-Design-Screenshot-5.png?raw=true)
Displays a responsive table containing the data used in the visualizations.
The table contains a bootstrap table component.
The data comes from exporting the .csv file as HTML, or converting it to HTML. Pandas has a nifty method approprately called to_html that allows one to generate a HTML table from a pandas dataframe.

The website, at the top of every page, has a navigation menu that:

Has the name of the site on the left of the nav which allows users to return to the landing page from any page.
Contains a dropdown menu on the right of the navbar named "Plots" that provides a link to each individual visualization page.
Provides two more text links on the right: "Comparisons," which links to the comparisons page, and "Data," which links to the data page.
Is responsive (using media queries). The nav has similar behavior as the screenshots "Navigation Menu" section.


