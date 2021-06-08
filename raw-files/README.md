# Raw Files 
Annotation was done using [Brat Rapid Annotation Tool](https://brat.nlplab.org/). Annotation details are stored in *.ann* files in standoff format.

### 1. News articles
Due to copyright issues, original news articles are not made available. Instead URL link to each news articles are provided, they are listed in *data_source.csv*. Pre-processing codes to extract each articles are made available. The corresponding *.ann* files are provided in the *data* folder. 

Run the following codes to extract the news articles. The extracted artiles are saved in *.txt* format and saved into the *data* folder.

```
python content_scraping.py
## Note:  Make sure *data_source.csv* in the same folder as *content_scraping.py*
```


### 2. Augmented Data
In order to increase the size of the annotations, a number of sentences are augmented using the following approach:
1. Trigger word replacement using FrameNet.
2. Event argument replacement

For augmented data, original text are made available along with their corresponding *.ann* files.
 

