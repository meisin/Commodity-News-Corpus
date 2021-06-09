# Commodity News Corpus

### 1. Annotation
Annotations are done using [Brat Rapid Annotation Tool](https://brat.nlplab.org/). 
 ![annotation](brat_annotation.png)
 
### 2. News Source
Commodity news articles were taken from from notable news agencies below:
* https://www.investing.com/commodities/crude-oil-news
* https://www.reuters.com/news/economy
* https://www.cnbc.com
* https://www.hellenicshippingnews.com/
* https://oilprice.com/Latest-Energy-News/
* https://www.marketwatch.com
* https://www.marketpulse.com
* https://www.fxempire.com/news/

**Note** Due to copyright issues, only the links to the original news articles are provided (without the actual news text). A corresponding URL link to the original news is given along with their corresponding annotation file. Augmented data, on the other hand, are made fully available (see raw-files/Augmented data/)

### 3. Data Processing 
Codes for Data processing to convert annotation data (in *.ann* files) from standoff format to CONLL format are provided.

### 4. Event Types
There are 19 Event Types
1. **Geo-political News**
   * **Civil Unrest**
3. **Macro-Economic News**
4. **Commodity Supply (includes exports)**
5. **Commodity Demand (includes imports)**
6. **Commodity Price Movement**
 

### 5. Citation
To use this dataset is made available for academic research purposes only, please cite this publication:
```
@article{lee2021commodities,
  title={The Commodities News Corpus: A Resource forUnderstanding Commodity News Better},
  author={Lee, Meisin and Soon, Lay Ki and Siew, Eu-gene},
  journal={arXiv preprint arXiv:2105.08214},
  year={2021}
}
```
