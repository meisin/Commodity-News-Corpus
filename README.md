# Commodity News Corpus

This is the repository for the dataset introduced in "An Annotated Commodity News Corpus for Event Extraction"(https://arxiv.org/abs/2105.08214)

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
      * (b) Financial / Economic Crisis (which can be grouped under Macro-economic News)
         * (S10)  ....since the 2014/15 financial **crisis** as .......
   
2. **Macro-Economic News**
   * **Strong Economy / GDP growth / US Employment (Grow-strong)** - Strong or growing economy / GDP of a nation; applicable to indicate strong status of US EmploymentData
      * (S11) as **strong** U.S. employment data.... 
   * **Weak or Contracting Economy / GDP / US Employment (Slow-weak)** - Weakening or contracting economy / GDP of a nation; applicable to indicate the weakening of USemployment data.
      * (S12) ..... concerns over **slowing** global growth.... 
      * (S13) U.S. employment data contracts with the euro zone.....
   * **Bearish technical view or outlook (Negative-sentiment)** - Bearish sentiment or outlook
      * (S14) But in a market clouded by **uncertainties**.... 
      * (S15) ....supply **concerns** would ease even more ......
 
3. **Commodity Supply (includes exports)**
   * **Oversupply (Oversupply)** - Situation where production goes into surplus
      * (S16) ..... the region **surplus** of supply.....
      * (S17) ...the market is still working off the **gluts** built up....
   * **Shortage (Shortage)** - Situation where demand is more than supply.
      * (S18) ... increase a supply **shortage** from chaotic Libya.... 
      * (S19) ....and there is no **shortfall** in supply , the minister added
   * **Supply increase (Movement-up-gain)** - Situation where supply increased
      * (S20) ...further **increases** in U.S. crude production..... 
      * (S21) The **rise** in production is definitely benefiting the United States...
   * **Action taken to increase supply (Cause-Movement-Up-gain)** - Deliberate action toincrease supply.
      * (S22) The IEA **boosted** its estimate of production from ExxonMobil to 1.8 millionbpd in July 4 holiday weekend.
      * (S23) ...urged the kingdom to **ramp up** production....
   * **Supply decrease (Movement-down-loss)** - Situation where supply decreased
      * (S24) UAE ’s production has almost **halved** in two years to 31.6 million bpd... 
      * (S25) ...fears that global supplies will **drop** due to Washington ’s sanctions on theOPEC member nation.
   * **Action taken to decrease supply (ause-movement-down-loss)** - Deliberate action todecrease supply.
      * (S26) .....by **slashing** production by almost three quarters in the 1980s...  
      * (S27) ....an announcement by Iran that it would **cut** its production last week.
   
4. **Commodity Demand (includes imports)**
   * **Demand increase (Movement-up-gain)** - Situation where demand increased 
      * (S28) It expects consumption to **trend upward** by 1.05 million bpd , below 40,000bpd from July.
      * (S29) ...as **more** seasonal demand kicks in due to colder weather.
   * **Action taken to increase demand (Caused-movement-up-gain)** - Deliberate actiontaken to increase demand.
      * (S30) IEA tried to **boost** global oil demand by introducing......
   * **Demand decrease (Movement-down-loss)** - Situation where demand decreased
      * (S31) ...onto a market reeling from **falling** demand because of the virus outbreak. 
      * (S32) ...when global demand growth for air conditioning **collapses** from its summerpeak....
   * **Action taken to decrease demand (Caused-movement-down-loss)** - Deliberate actiontaken to decrease demand
      * (S33)  The pandemic has **zapped** demand to a level never seen before..
   
5. **Commodity Price Movement**
   Commodity price here includes *spot price*,*futures* and *futures contract*
   * **Price increase (Movement-up-gain)** Situation where commodity price rises
      * (S34) Oil price **rose** $105 a barrel on March.... 
      * (S35) ..oil prices have **jumped** as much as 20 percent since June.
   * **Price decrease (Movement-down-loss)** - Situation where commodity price drops
      * (S36) The **drop** in oil prices to their lowest in two years..... 
      * (S37) Oil prices **declined** back the final quarter of 1991 to 87 cents...
   * **Price movement flat (Movement-flat)** - Situation where no or little change to commod-ity price
      * (S38) Contango spread in Brent is **steady** at 15 cents per barrel.... 
      * (S39) U.S. crude is expected toholdaround $105 per barrel.
   * **Price position (Position-high, Position-low)** - Describes the position of the currentcommodity price
      * (S40) Oil price remained close to four-year **highs**...
      * (S41) Oil slipped more than 20% to its **lowest** level in two years on 1980s.... 
   
6. **Change in Forecasted value**
   * **Increase forecast target (Caused-movement-up-gain)** - Forecasted / target is raised,possible values are price target, growth target, demand and supply target
      * (S42) The IMF earlier said it **increased** its 2019 global economic growth forecast to 3.30%. 
      * (S43) The International Monetary Fund **doubled** its global growth forecast for 2013.....
   * **Price target /forecast decrease (Caused-movement-down-loss)** - Forecasted / targetis lowered, possible values are commodity price target, growth target, demand and sup-ply target
      * (S44) Germany’s Bundesbank this week **halved** its 2015 growth forecasts for Europe’s largest economy to 1 percent. 
      * (S45) OPEC also **lowered** forecast global demand for its crude oil..   
 

### 5. Citation
To use this dataset is made available for academic research purposes only, please cite this publication:
```
@misc{lee2021annotated,
      title={An Annotated Commodity News Corpus for Event Extraction}, 
      author={Meisin Lee and Lay-Ki Soon and Eu-Gene Siew and Ly Fie Sugianto},
      year={2021},
      eprint={2105.08214},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
