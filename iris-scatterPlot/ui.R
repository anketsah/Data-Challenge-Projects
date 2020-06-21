library(shiny)
library(ggplot2)

shinyUI(fluidPage(
  headerPanel('Iris Scatterplot: Distribution of Length-Width of Petal and Sepal based on Species'),
  sidebarPanel(
    selectInput('Species', 'Choose Species', as.character(unique(iris$Species)))
  ),
  mainPanel(
    plotOutput('plot1',width = 800, height = 600)
  )
 )
)
