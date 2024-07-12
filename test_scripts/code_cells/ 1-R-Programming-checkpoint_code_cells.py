install.packages("randomForest")

install.packages("aRtsy")

https://hub.docker.com/_/r-base/tags

installing: ‘blob’, ‘data.table’, ‘cellranger’, ‘ids’, ‘vroom’, ‘tzdb’,
‘progress’, ‘broom’, ‘crayon’, ‘dbplyr’, ‘dtplyr’, ‘forcats’, ‘googledrive’, ‘googlesheets4’, 
‘haven’, ‘hms’, ‘jsonlite’, ‘lubridate’, ‘modelr’, ‘readr’, ‘readxl’, ‘reprex’, ‘tidyr’

library(tidyverse)
library(Rcpp)
library(colourlovers)
library(reshape2)
library(cowplot)

# Import C++ code
sourceCpp('cyclic_funs.cpp')

#################################################################
# Functions
#################################################################

# This function creates a w x h matrix of random states
initial_grid <- function(s, w, h){
  matrix(sample(x = seq_len(s)-1,
               size = w *h,
               replace = TRUE),
         nrow = h,
         ncol = w)}

# This function implements neighborhoods
# You can add your own
convolution_indexes <- function(r, n){
  crossing(x = -r:r, y = -r:r) %>% 
    mutate(M = ((x != 0) | (y != 0)) * 1 ,
           N = (abs(x) + abs(y) <= r) * M,
           Mr = ((abs(x) == r) | (abs(y) == r)) * M,
           Nr = (abs(x) + abs(y) == r) * M,
           Cr = ((x == 0) | (y == 0)) * M,
           S1 = (((x > 0) & (y > 0))|((x < 0) & (y < 0))) * 1,
           Bl = (abs(x) == abs(y)) * M,
           D1 = (abs(x) > abs(y)) * M,
           D2 = ((abs(x) == abs(y)) | abs(x) == r) * M,
           C2 = M - N,
           Z = ((abs(y) == r) | (x == y)) * M,
           t = ((y == r) | (x == 0)) * M,
           U = ((abs(x) == r) | (y == -r)) * M,
           H = (abs(x) == r | y == 0) * M,
           TM = ((abs(x) == abs(y)) | abs(x) == r | abs(y) == r) * M,
           S2 = ((y==0) | ((x == r) & (y > 0)) |((x == -r) & (y < 0))) * M,
           M2 = ((abs(x) == r) | (abs(x) == abs(y) & y > 0)) * M) %>% 
    select(x, y, matches(n)) %>% 
    filter_at(3, all_vars(. > 0)) %>% 
    select(x,y)
}

#################################################################
# Initialization
#################################################################
range <- 5
thresold <- 29
states <- 5
neighborhood <- "M"
iter <- 600

width  <- 1500
height <- 1500
  
X <- initial_grid(s = states,
                  w = width,
                  h = height)

L <- convolution_indexes(r = range, n = neighborhood)
  
for (i in 1:iter){
    X <- iterate_cyclic(X, L, states, thresold)  
}
  
# Transform resulting environment matrix into data frame
df <- melt(X)
colnames(df) <- c("x","y","v") # to name columns
  
# Pick a top palette from colourlovers
palette <- sample(clpalettes('top'), 1)[[1]] 
colors <- palette %>% swatch %>% .[[1]]

# Do the plot
ggplot(data = df, aes(x = x, y = y, fill = v)) + 
  geom_raster(interpolate = TRUE) +
  coord_equal() +
  scale_fill_gradientn(colours = colors) +
  scale_y_continuous(expand = c(0,0)) + 
  scale_x_continuous(expand = c(0,0)) +
  theme_nothing() 


library(RcppArmadillo)
library(imager)
plot(boats)

library(generativeart)

# set the paths
IMG_DIR <- "img/"
IMG_SUBDIR <- "everything/"
IMG_SUBDIR2 <- "handpicked/"
IMG_PATH <- paste0(IMG_DIR, IMG_SUBDIR)

LOGFILE_DIR <- "logfile/"
LOGFILE <- "logfile.csv"
LOGFILE_PATH <- paste0(LOGFILE_DIR, LOGFILE)

# create the directory structure
generativeart::setup_directories(IMG_DIR, IMG_SUBDIR, IMG_SUBDIR2, LOGFILE_DIR)

# include a specific formula, for example:
my_formula <- list(
  x = quote(runif(1, -1, 1) * x_i^2 - sin(y_i^2)),
  y = quote(runif(1, -1, 1) * y_i^3 - cos(x_i^2))
)

# call the main function to create five images with a polar coordinate system
generativeart::generate_img(formula = my_formula, nr_of_img = 25, polar = TRUE, filetype = "png", color = "gold", background_color = "darkred")


RcppArmadillo.h
Error: Package 'RcppArmadillo' referenced from Rcpp::depends in source file cyclic_funs.cpp is not available.
Traceback:

https://cran.r-project.org/web/packages/imager/vignettes/gettingstarted.html

library(imager)
plot(boats)

install.packages("imager")

install.packages("imager")

install.packages("tidyverse")
install.packages("Rcpp")
install.packages("reshape2")
install.packages("colourlovers")
install.packages("cowplot")

https://generative.substack.com/p/generative-art-and-r

install.packages("/home/jack/Desktop/R-Studio/generativeart/", repos = NULL, type="source")

install.packages("/home/jack/Desktop/R-Studio/httr2_0.2.2.tar.gz", repos = NULL, type="source")

library(generativeart)

# include a specific formula, for example:
my_formula <- list(
  x = quote(runif(1, -1, 1) * x_i^2 - sin(y_i^2)),
  y = quote(runif(1, -1, 1) * y_i^3 - cos(x_i^2))
)

# call the main function to create five images with a polar coordinate system
generativeart::generate_img(formula = my_formula, nr_of_img = 20, polar = TRUE, 
                            filetype = "png", color = "gold", background_color = "blue4")


# generativeart

## Announcement

This package collects more and more stars here on Github and is widely used for NFTs. Just browse on NFT platforms - it won't take you long to discover  patterns be that might be decandents of this repository.

I would like to clarify: I am **not a fan** of Blockchain, NFT and Web3. 

Why? Read this text: ["The Third Web"](https://tante.cc/2021/12/17/the-third-web/) by [@tante](https://twitter.com/tante).

--- 

Create Generative Art with R.

![](img/generativeart.png)

[More on Instagram](https://www.instagram.com/cutterkom/)

## Description

> One overly simple but useful definition is that generative art is art programmed using a computer that intentionally introduces randomness as part of its creation process.
-- [Why Love Generative Art? - Artnome](https://www.artnome.com/news/2018/8/8/why-love-generative-art)

The `R` package `generativeart` let's you create images based on many thousand points.
The position of every single point is calculated by a formula, which has random parameters.
Because of the random numbers, every image looks different.

In order to make an image reproducible, `generative art` implements a log file that saves the `file_name`, the `seed` and the `formula`.

## Install

You can install the package with the `devtools` package directly from Github:

```r
devtools::install_github("cutterkom/generativeart")
```

`generativeart` uses the packages `ggplot2`, `magrittr`, `purrr` and `dplyr`.

## Usage

The package works with a specific directory structure that fits my needs best.
The first step is to create it with `setup_directories()`.
All images are saved by default in `img/everything/`. I use `img/handpicked/` to choose the best ones.
In `logfile/` you will find a `csv` file that saves the `file_name`, the `seed` and the used `formula`.

```r
library(generativeart)

# set the paths
IMG_DIR <- "img/"
IMG_SUBDIR <- "everything/"
IMG_SUBDIR2 <- "handpicked/"
IMG_PATH <- paste0(IMG_DIR, IMG_SUBDIR)

LOGFILE_DIR <- "logfile/"
LOGFILE <- "logfile.csv"
LOGFILE_PATH <- paste0(LOGFILE_DIR, LOGFILE)

# create the directory structure
generativeart::setup_directories(IMG_DIR, IMG_SUBDIR, IMG_SUBDIR2, LOGFILE_DIR)

# include a specific formula, for example:
my_formula <- list(
  x = quote(runif(1, -1, 1) * x_i^2 - sin(y_i^2)),
  y = quote(runif(1, -1, 1) * y_i^3 - cos(x_i^2))
)

# call the main function to create five images with a polar coordinate system
generativeart::generate_img(formula = my_formula, nr_of_img = 5, polar = TRUE, \
                            filetype = "png", color = "black", background_color = "white")

```

* You can create as many images as you want by setting `nr_of_img`.
* For every image a seed is drawn from a number between 1 and 10000.
* This seed determines the random numbers in the formula.
* You can choose between cartesian and polar coordinate systems by setting `polar = TRUE` or `polar = FALSE`
* You can choose the colors with `color = 'black'` and `background_color = 'hotpink'`
* You can save the output image in various formats.
Default is `png`, the alternatives are defined by the `device` options of [`ggplot::ggsave()`](https://ggplot2.tidyverse.org/reference/ggsave.html).
* the formula is a `list()`

## Examples

#It is a good idea to use the sine and cosine in the formula, since it guarantees nice shapes, especially when combined with a polar coordinate system. One simple example:
r
my_formula <- list(
  x = quote(runif(1, -1, 1) * x_i^2 - sin(y_i^2)),
  y = quote(runif(1, -1, 1) * y_i^3 - cos(x_i^2))
)

generativeart::generate_img(formula = my_formula, nr_of_img = 5, polar = TRUE, color = "black", background_color = "white")

```

Two possible images:

`seed = 1821`, `polar = TRUE`:
![](img/2018-11-16-17-13_seed_1821.png)

`seed = 5451`, `polar = FALSE`:
![](img/2018-11-16-17-12_seed_5451.png)

The corresponding log file looks like that:

| file_name                      | seed | formula_x                            | formula_y                            | 
|--------------------------------|------|--------------------------------------|--------------------------------------| 
| 2018-11-16-17-13_seed_1821.png | 1821 | runif(1, -1, 1) * x_i^2 - sin(y_i^2) | runif(1, -1, 1) * y_i^3 - cos(x_i^2) | 
| 2018-11-16-17-12_seed_5451.png | 5451 | runif(1, -1, 1) * x_i^2 - sin(y_i^2) | runif(1, -1, 1) * y_i^3 - cos(x_i^2) | 


## Inspiration

The basic concept is heavily inspired by [Fronkonstin's great blog](https://fronkonstin.com/).


library(httr2)

#install.packages("/home/jack/Desktop/R-Studio/rjson_0.2.13.tar.gz", repos=NULL, type="source")
#install.packages("twitteR")
library(twitteR)
setup_twitter_oauth(consumer_key = 'APIkey()[0]',
                    access_token = 'APIkey()[2]',
                    consumer_secret = 'APIkey()[1]',
                    access_secret = 'APIkey()[3]')


#tw <- updateStatus("Now I need to read Tweets using R in my Jupyter Notebook! #Jupyternotebook #rstudio #RStudio") 
#Download version 2.13 from http://cran.rstudio.com/src/contrib/Archive/rjson/rjson_0.2.13.tar.gz In R, run install.packages('path to the downloaded gz file>', repos=NULL, type='source')")
#https://cran.rstudio.com/

tw <- updateStatus("#Jupyternotebook #rstudio #RStudio Now I'll try to post an Image", mediaPath = "post-this.png")

library(twitteR)
setup_twitter_oauth(consumer_key = 'XXXXXXXXX',
                    access_token = 'YYYYYYYYYYYYY',
                    consumer_secret = 'ZZZZZZZZZZZZZZZZZZZZZ',
                    access_secret = 'WWWWWWWWWWWWWWWWWWWWWW')
tw <- updateStatus('#Jupyternotebook #rstudio #RStudio Now I'll try to post an Image', mediaPath = 'post-this.png')

library(twitteR)
library(httr)


ckey <- "X"
csecret <- "X"
atoken <- "X"
asecret <- "X"

setup_twitter_oauth(ckey, csecret, atoken, asecret)

tweet("")
There is a parameter in tweet() and updateStatus() called mediaPath which you can use to submit images. Try something like:

tweet("some status", mediaPath = "url-to-image.jpg")
tw <- updateStatus("some status", mediaPath = "url-to-image.jpg")

install.packages("/home/jack/Desktop/R-Studio/devtools_2.4.5.tar.gz", repos = NULL, type="source")

install.packages(path_to_file, repos = NULL, type="source")

R --version
R version 3.6.1 (2019-07-05) -- "Action of the Toes"
Copyright (C) 2019 The R Foundation for Statistical Computing
Platform: x86_64-conda_cos6-linux-gnu (64-bit)


https://cran.rstudio.com/
https://developer.twitter.com/en/docs/api-reference-index
https://www.tensorflow.org/lite/examples/style_transfer/overview

https://www.r-bloggers.com/2018/05/send-tweets-from-r-a-very-short-walkthrough/
http://zevross.com/blog/2017/06/19/tips-and-tricks-for-working-with-images-and-figures-in-r-markdown-documents/
https://bookdown.org/yihui/rmarkdown/notebook.html#using-notebooks
https://towardsdatascience.com/getting-started-with-generative-art-in-r-3bc50067d34b
https://www.earthdatascience.org/courses/earth-analytics/get-data-using-apis/use-twitter-api-r/
https://www.jumpingrivers.com/blog/r-knitr-markdown-png-pdf-graphics/
https://dgarcia-eu.github.io/SocialDataScience/4_SNA/047_TwitterNetwork/TwitterNetwork.html
https://dgarcia-eu.github.io/SocialDataScience/2_SocialDynamics/027_rtweet/rtweet.html
https://datatofish.com/r-jupyter-notebook/
https://github.com/plotly/plotly.R/issues/239

install.packages(plotly) # if you haven't installed the package
library(plotly)

df <- data.frame(Product = c('Oven', 'Microwave', 'Toaster'),
                 Price = c(850, 300, 120)
                 )
print (df)

# Function definition
# To check n is divisible by 5 or not
divisbleBy5 <- function(n){
  if(n %% 5 == 0)
  {
    return("number is divisible by 5")
  }
  else 
  {
    return("number is not divisible by 5")
  }
}
   
# Function call
divisbleBy5(100)
divisbleBy5(4)
divisbleBy5(20.0)


 R Programming

# load twitter library - the rtweet library is recommended now over twitteR
library(rtweet)
# plotting and pipes - tidyverse!
library(ggplot2)
library(dplyr)
# text mining library
library(tidytext)


#install.packages("/home/jack/Desktop/R-Studio/rjson_0.2.13.tar.gz", repos=NULL, type="source")
#install.packages("twitteR")
library(twitteR)
setup_twitter_oauth(consumer_key = 'APIkey()[0]',
                    access_token = 'APIkey()[2]',
                    consumer_secret = 'APIkey()[1]',
                    access_secret = 'APIkey()[3]')


tw <- updateStatus("#rstudio #RStudio #twitteR This is an old library, it only allows a Tweet of under 140 characters") 
#Download version 2.13 from http://cran.rstudio.com/src/contrib/Archive/rjson/rjson_0.2.13.tar.gz In R, run install.packages('path to the downloaded gz file>', repos=NULL, type='source')")
#https://cran.rstudio.com/

#' Generate data
#'
#' The generative images are based on values in a dataframe. This function creates the data by transforming the base values `seq(-pi, pi)` with a `formula`.
#' @param formula a list that contains formulas for transforming the x- and y-values.
#' @return data frame
#' @seealso \code{\link{generate_plot}} the returned data frame is the input to generate the plot
#' @export
#' @examples
#' \dontrun{
#' generate_data(formula)
#' }
#' # an example for a formula:
#' formula <- list(
#'   x = quote(runif(1, -1, 1) * pi_x^2 -sin(pi_y^2)),
#'   y = quote(runif(1, -1, 1) * pi_y^3-cos(pi_x^2))
#'  )
#' @importFrom dplyr mutate
#' @importFrom magrittr %>%

### create dataframe with starting points and transformed x and y depending on a formula
generate_data <- function(formula) {
  print("generate data")
  df <- seq(from = -pi, to = pi, by = 0.01) %>%
    expand.grid(x_i = ., y_i = .) %>%
    dplyr::mutate(!!!formula)
  return(df)
}


generate_data

formula

generate_data(formula)
 formula <- list(
   x = quote(runif(1, -1, 1) * pi_x^2 -sin(pi_y^2)),
   y = quote(runif(1, -1, 1) * pi_y^3-cos(pi_x^2))
  )
#@importFrom dplyr mutate
#@importFrom magrittr %>%


library(devtools)

install.packages("devtools", dependencies = TRUE)

https://cran.r-project.org/src/contrib/httr2_0.2.2.tar.gz

Downloading and Extracting Packages
r-lubridate-1.7.4    | 1.1 MB    | #################################### | 100% 
r-mass-7.3_51.3      | 1.1 MB    | #################################### | 100% 
r-stringr-1.4.0      | 221 KB    | #################################### | 100% 
r-tibble-2.1.1       | 316 KB    | #################################### | 100% 
r-markdown-0.9       | 143 KB    | #################################### | 100% 
r-readr-1.3.1        | 814 KB    | #################################### | 100% 
r-dbi-1.0.0          | 916 KB    | #################################### | 100% 
r-reshape2-1.4.3     | 129 KB    | #################################### | 100% 
r-ps-1.3.0           | 221 KB    | #################################### | 100% 
r-processx-3.3.0     | 190 KB    | #################################### | 100% 
r-whisker-0.3_2      | 82 KB     | #################################### | 100% 
r-openssl-1.3        | 1.2 MB    | #################################### | 100% 
r-munsell-0.5.0      | 254 KB    | #################################### | 100% 
r-plogr-0.2.0        | 20 KB     | #################################### | 100% 
r-callr-3.2.0        | 270 KB    | #################################### | 100% 
r-yaml-2.2.0         | 113 KB    | #################################### | 100% 
r-bh-1.69.0_1        | 10.9 MB   | #################################### | 100% 
r-r6-2.4.0           | 68 KB     | #################################### | 100% 
r-purrr-0.3.2        | 397 KB    | #################################### | 100% 
r-pillar-1.3.1       | 180 KB    | #################################### | 100% 
r-stringi-1.4.3      | 773 KB    | #################################### | 100% 
r-gtable-0.3.0       | 425 KB    | #################################### | 100% 
r-highr-0.8          | 60 KB     | #################################### | 100% 
r-broom-0.5.2        | 2.0 MB    | #################################### | 100% 
r-colorspace-1.4_1   | 2.5 MB    | #################################### | 100% 
r-xfun-0.6           | 189 KB    | #################################### | 100% 
r-fs-1.2.7           | 510 KB    | #################################### | 100% 
r-utf8-1.1.4         | 159 KB    | #################################### | 100% 
r-rstudioapi-0.10    | 240 KB    | #################################### | 100% 
r-glue-1.3.1         | 165 KB    | #################################### | 100% 
r-xml2-1.2.0         | 340 KB    | #################################### | 100% 
r-rvest-0.3.3        | 928 KB    | #################################### | 100% 
r-rematch-1.0.1      | 19 KB     | #################################### | 100% 
r-knitr-1.22         | 1.3 MB    | #################################### | 100% 
r-nlme-3.1_139       | 2.2 MB    | #################################### | 100% 
r-dplyr-0.8.0.1      | 1.9 MB    | #################################### | 100% 
r-fansi-0.4.0        | 193 KB    | #################################### | 100% 
r-haven-2.1.0        | 331 KB    | #################################### | 100% 
r-dbplyr-1.4.0       | 622 KB    | #################################### | 100% 
r-labeling-0.3       | 71 KB     | #################################### | 100% 
r-sys-3.2            | 47 KB     | #################################### | 100% 
r-clipr-0.6.0        | 66 KB     | #################################### | 100% 
r-forcats-0.4.0      | 373 KB    | #################################### | 100% 
r-httr-1.4.0         | 513 KB    | #################################### | 100% 
r-tidyverse-1.2.1    | 95 KB     | #################################### | 100% 
r-backports-1.1.4    | 65 KB     | #################################### | 100% 
r-modelr-0.1.4       | 226 KB    | #################################### | 100% 
r-dichromat-2.0_0    | 163 KB    | #################################### | 100% 
r-pkgconfig-2.0.2    | 25 KB     | #################################### | 100% 
r-askpass-1.0        | 27 KB     | #################################### | 100% 
r-progress-1.2.0     | 89 KB     | #################################### | 100% 
r-lazyeval-0.2.2     | 164 KB    | #################################### | 100% 
r-tidyselect-0.2.5   | 138 KB    | #################################### | 100% 
r-assertthat-0.2.1   | 74 KB     | #################################### | 100% 
r-ggplot2-3.1.1      | 3.6 MB    | #################################### | 100% 
r-matrix-1.2_17      | 3.8 MB    | #################################### | 100% 
r-cli-1.1.0          | 189 KB    | #################################### | 100% 
r-readxl-1.3.1       | 855 KB    | #################################### | 100% 
r-withr-2.1.2        | 181 KB    | #################################### | 100% 
r-rlang-0.3.4        | 1.0 MB    | #################################### | 100% 
r-rmarkdown-1.12     | 3.0 MB    | #################################### | 100% 
r-generics-0.0.2     | 82 KB     | #################################### | 100% 
r-ellipsis-0.1.0     | 35 KB     | #################################### | 100% 
r-mime-0.6           | 50 KB     | #################################### | 100% 
r-rcolorbrewer-1.1_2 | 62 KB     | #################################### | 100% 
r-tinytex-0.12       | 106 KB    | #################################### | 100% 
r-curl-3.3           | 406 KB    | #################################### | 100% 
r-viridislite-0.3.0  | 66 KB     | #################################### | 100% 
r-cellranger-1.1.0   | 116 KB    | #################################### | 100% 
r-selectr-0.4_1      | 474 KB    | #################################### | 100% 
r-hms-0.4.2          | 74 KB     | #################################### | 100% 
r-scales-1.0.0       | 580 KB    | #################################### | 100% 
r-magrittr-1.5       | 173 KB    | #################################### | 100% 
r-plyr-1.8.4         | 815 KB    | #################################### | 100% 
r-tidyr-0.8.3        | 446 KB    | #################################### | 100% 
r-mgcv-1.8_28        | 2.6 MB    | #################################### | 100% 
r-lattice-0.20_38    | 1.1 MB    | #################################### | 100% 
r-reprex-0.2.1       | 410 KB    | #################################### | 100% 
r-prettyunits-1.0.2  | 38 KB     | #################################### | 100% 
Preparing transaction: done


