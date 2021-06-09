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
   * **Civil Unrest (Civil-unrest)** - Violence or turmoil within the oil producing country
      * (S1) ....a fragile recovery in Libyan supply outweighed **fighting** in Iraq .....
      * (S2) ....a backdrop of the worst **strife** in Iran this decade...
   * **Embargo (Embargo, Prohibiting)** - Trade or other commercial activity of the com-modity is banned.
      * (S3) .... and **sanctions** against Iran.
      * (S4) ...prepared to impose “ strong and swift ” economic **sanctionson** Venezuela.....
   * **Geo-political Tension (Geo-political-tension)** - Political tension between oil-producingnation with other nations.
      * (S5) .... heightened **tensions** between the West and Russia..... 
      * (S6) ... despite geopolitical **war** in Iraq , Libya and Ukraine.
   * **Trade Tension (Trade-tensions)** - Trade-related tension between oil-producing andoil-consuming nations
      * (S7) .....escalating global **trade wars**, especially between the US and China. 
      * (S8) ....showing that OPEC is not ready to end its **trade tensions**......
   * **Other forms of Crisis (Crisis)**
      * (a) A time of intense difficulty, such as other forms of unspecified crisis that do not fallinto any of the above category
         * (S9)  .... Ukraine declared an end to an oil **crisis** that has .........
   
2. **Macro-Economic News**
   * **Strong Economy / GDP growth / US Employment (Grow-strong)** - Strong or growing economy / GDP of a nation; applicable to indicate strong status of US EmploymentData
   * **Weak or Contracting Economy / GDP / US Employment (Slow-weak)** - Weakening or contracting economy / GDP of a nation; applicable to indicate the weakening of USemployment data.
   * **Bearish technical view or outlook (Negative-sentiment)** - Bearish sentiment or outlook
 
3. **Commodity Supply (includes exports)**
   * **Oversupply (Oversupply)** - Situation where production goes into surplus
   * **Shortage (Shortage)** - Situation where demand is more than supply.
   * **Supply increase (Movement-up-gain)** - Situation where supply increased
   * **Action taken to increase supply (Cause-Movement-Up-gain)** - Deliberate action toincrease supply.
   * **Supply decrease (Movement-down-loss)** - Situation where supply decreased
   * **Action taken to decrease supply (ause-movement-down-loss)** - Deliberate action todecrease supply.
   
4. **Commodity Demand (includes imports)**
   * **Demand increase (Movement-up-gain)** - Situation where demand increased 
   * **Action taken to increase demand (Caused-movement-up-gain)** - Deliberate actiontaken to increase demand.
   * **Demand decrease (Movement-down-loss)** - Situation where demand decreased
   * **Action taken to decrease demand (Caused-movement-down-loss)** - Deliberate actiontaken to decrease demand
   
5. **Commodity Price Movement**
   Commodity price here includes *spot price*,*futures* and *futures contract*
   * **Price increase (Movement-up-gain)** Situation where commodity price rises
   * **Price decrease (Movement-down-loss)** - Situation where commodity price drops
   * **Price movement flat (Movement-flat)** - Situation where no or little change to commod-ity price
   * **Price position (Position-high, Position-low)** - Describes the position of the currentcommodity price
   
6. **Change in Forecasted value**
   * **Increase forecast target (Caused-movement-up-gain)** - Forecasted / target is raised,possible values are price target, growth target, demand and supply target
   * **Price target /forecast decrease (Caused-movement-down-loss)** - Forecasted / targetis lowered, possible values are commodity price target, growth target, demand and sup-ply target
   
 

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
