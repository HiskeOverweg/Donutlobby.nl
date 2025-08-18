Title: The impact of AI on Climate Change
slug: the-impact-of-ai-on-climate-change
lang: en
Date: 2025-08-18 10:00

The impact of AI on climate change is a hot topic. Proponents of AI will tell you that AI will soon be smart enough to solve a significant part of the climate crisis. Others are worried about the gigantic energy consumption of these models. In this post, I will discuss a four mechanisms in which AI impacts climate change, some of which are often overlooked.

### 1. Energy consumption of AI
How much energy does AI consume? Unfortunately this is not an easy question to answer, since Big Tech companies are getting less and less transparent about the energy use of their models. Current estimates are on the order of 0.7 EJ per year (thats 0.7 x 10<sup>18</sup> J)

![]({static}/images/ai/1.png)

The total worldwide energy consumption is currently on the order of 400 EJ per year, so currently AI consumes on the order of 0.2% of that, which is considerable, but not enormous I'd say. Two different angles to look at that number:

##### Net-zero pledges
When we look at the commitments Big Tech companies have made to reach net zero, we start to see a bigger and bigger gap between their promises and what they deliver so far. Below you see a graph of Microsoft's emissions in the past couple of years. This gap between pledges and results is illustrative for the whole industry.

![]({static}/images/ai/2.jpg)

##### Individual perspective
On the one hand you might conclude that 0.2% of the total energy consumption is not that much. On the other hand you could ask yourself whether the world is really better off after you generated a picture of farm animals wearing haute couture. It is energy which can be relatively easily saved, if you compare it to the energy needed to keep your fridge cool, for example.


### 2. AI solutions contributing to sustainability
Admittedly, AI can do more useful things than generating pictures of farm animals wearing haute couture. Here I'll illustrate a few. In case you want a more extensive overview, I refer you to the [paper](https://arxiv.org/abs/1906.05433) "Tackling Climate Change with Machine Learning" by David Rolnick et al.

##### Predictions of energy supply and demand
AI can make better forecasts of energy availability. This could help us make more use of renewable energy whenever it is available. An example would be to charge an electric car when plenty of wind energy is available. On top of that AI can help with predictive maintenance, reducing the downtime of solar panels. In En-ROADS we can model this boost in renewable energy. It is hard to put an exact number on it, but let's assume we manage to increase the consumption of renewables with 10% in 2040 (the blue line in the graph below), compared to the business-as-usual scenario (black line). This will lead to a reduction in temperature of roughly 0.1°C at the end of the century.

![]({static}/images/ai/3.png)

 In case you think my estimate is either too conservative or too optimistic, you are welcome to explore the effect yourself in the simulator. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?v=25.8.0&p16=-0.02)

##### Optimizing transport
AI can help improve the design of electric motors. [Here](https://eprints.whiterose.ac.uk/id/eprint/213146/1/Application_of_Artificial_Intelligence-Based_Technique_in_Electric_Motors_A_Review.pdf) you find a review paper on that topic. If we make more energy efficient and more lightweight electric motors, this can reduce the dependency of the transport sector on oil. Again, it is impossible to predict the exact impact, but let's work with a guesstimate of a 5% price reduction of electric vehicles and charging infrastructure. Below you see a graph showing the increased sales of electric vehicles (solid lines), compared to the baseline scenario (dashed lines).

![]({static}/images/ai/4.png)

AI can also increase transport efficiency by combining shipments in a clever way. The combined effect of these two measures leads again to a to a temperature reduction on the order of 0.1°C in the year 2100. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?v=25.8.0&p50=1.5&p373=5)

##### Heating of buildings and energy efficiency in industry
AI can combine weather forecast data with predictions of building occupancy to determine the most efficient strategy to heat a building. AI can also help design buildings which are easier to heat an cool. [This paper](https://www.mdpi.com/1996-1073/17/17/4277) estimates that the savings could be at least 20% for different building types. Now, that is an academic result and the proof of the pudding is in the eating.

An example of energy saving in industry which has been realized in practise would be the optimized data center cooling by DeepMind. According to their [blog](https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/) they managed to reduce energy needed for cooling by 40% with the help of machine learning models.

Currently the energy efficiency of buildings and industry is increasing 1.2% per year. If AI is be able to boost this number up to 2%, we'll consume significantly less energy in the next decades:

![]({static}/images/ai/5.png)

The result? A significant decrease in our energy demand and a temperature reduction at the end of the century of roughly 0.1°C. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?v=25.8.0&p47=2) - feel free to change the percentage if you don't agree with my guesstimate!

##### Preventing deforestation
AI can be combined with satellite or drone data to identify illegal logging practises and thereby making monitoring more efficient. While the identification is technologically feasible, the enforcement is harder. Or as the authors of [this paper](https://ieeexplore-ieee-org.utrechtuniversity.idm.oclc.org/abstract/document/11086053) put it:

> "Challenges these systems face, in common, include: (...) to get all these people and critters rights issues worked out in a way that doesn’t result in going to jail."

If we want to reach a reduction of 0.1°C of the temperature at the end of the century, we'll need a change in deforestation rate of about 5% per year (see graph below). Given the current enforcement limitations, I think it would be challenging do achieve such an impact with AI.

![]({static}/images/ai/6.png)

##### Detecting methane leaks
In recent years, satellites have been developed which can identify locations of methane leaks. Methane is a greenhouse gas which is about 80 times as potent as CO<sub>2</sub>. Machine learning models have been used to process this new source of data and were able to identify sources of large methane leaks. These often occur at fossil fuel extraction sites and landfills. These models have been instrumental at detecting these leaks at [coal mines in Australia](https://www.tno.nl/en/newsroom/2021/11/satellite-reveals-higher-methane/) and [oil fields in Turkmenistan](https://www.theguardian.com/world/2023/may/09/mind-boggling-methane-emissions-from-turkmenistan-revealed) for example. Just as for deforestation, the next question will be how to enforce reduction of these leaks. There seems to be some progress in this area, since the president of Turkmenistan did recently sign the Global Methane Pledge. Let's hope he sticks to his promise! If AI can help with 20% of the total reduction potential for methane emissions (see graph below), that will again save about 0.1°C. [Scenario link](https://en-roads.climateinteractive.org/scenario.html?v=25.8.0&p47=1.3&p61=20)

![]({static}/images/ai/7.png)


##### What about large language models?
The above applications typically make use of neural networks, transformer models or Bayesian models, none of which require as much energy as large language models, which are getting so much attention these days. So yes, AI can help reduce the impact of climate change, but so far I haven't seen any convincing application of its most energy intensive variant.

### 3. Drill agent, drill
In the last decades, an important application of AI has been to make fossil fuel extraction more efficient. As [this report](https://heinonline-org.utrechtuniversity.idm.oclc.org/HOL/Page?collection=journals&handle=hein.journals/euenj7&id=185&men_tab=srchresults) by the IEA from 2017 estimates, digital technologies can reduce production costs by 10%-20% and help increase recoverable oil and gas resources by 5%.

To understand the full extent to which this can harm our fight against global warming, let us do a little thought experiment in En-ROADS. Let's assume that our political leaders wake up and decide that the current level of fossil fuel subsidy is no longer acceptable in a world which is hit already so hard by the climate crisis. They decide to reduce the subsidies and thereby reduce global warming by 0.3°C compared to the baseline scenario ([scenario link](https://en-roads.climateinteractive.org/scenario.html?v=25.8.0&p1=60&p7=50&p10=2.9&p47=1.3&p177=105000&p178=15700&p179=15700)). "Hurray, finally some progress!" you might think. Now the tech industry enters play with AI models which helps Big Oil, with cheaper monitoring of transmission lines with drones, predictive maintenance of machinery etc. This way, they undo the government efforts and increase emissions compared to the business as usual scenario, leading to higher emissions and increased global warming 0.1°C compared to baseline scenario [scenario link](https://en-roads.climateinteractive.org/scenario.html?v=25.8.0&p1=-15&p7=-15&p10=-0.7&p47=1.3&p177=105000&p178=15700&p179=15700).

The sponsoring of the oil and gas industry by Big Tech deserves more of our attention. People in Tech can sign the "Tech Won't Drill it" [pledge](https://medium.com/@techwontdrillit/tech-wont-drill-it-a63594dc6e66) and anyone who wishes to hold Big Tech accountable can support the [Enabled Emissions Campaign](https://www.enabledemissions.com)

### 4. Increased productivity

Proponents of AI claim AI will lead to vast increases in productivity. Increases of productivity lead to increases in GDP. Let's increase GDP from 1.5% per year to 2% per year. The effect on the climate in En-ROADS can be illustrated with the Kaya graphs.
The total emissions from the energy sector can be obtained by multiplying the population with the GDP per capita, the energy insensity of the GDP and the carbon intensity of energy. So a higher GDP per capita (second graph) will lead to higher emissions (fifth graph), and an increase of the temperature at the end of the century by 0.2°C.
![]({static}/images/ai/8.png)

Personally, I am a bit skeptic of vast productivity increases - [here](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) is a recent study which shows that AI use is currently still slowing down software developers rather than speeding them up. This could still change in the future of course.

### Conclusion
It is too early to quantify any precise impacts which AI will have on climate change. In this posts I highlighted a few different ways in which AI might impact the climate: via energy consumption of AI, contribution to climate solutions, support of the fossil fuel industry and potential increases in productivity. Especially the threat of increased fossil fuel extraction by AI deserves more attention in my opinion.

### Acknowledgements
This blogpost was inspired by the [webinar](https://www.youtube.com/watch?v=4Mizufxhfqk) AI and the Climate: Solution or Environmental Threat? by Climate Interactive, which in its turn was based on the thesis report "The Net Climate Impact of AI: Balancing Current Costst with Future Benefits by Jennifer Turliuk.

##### More information on En-ROADS

Curious about the En-ROADS climate simulator? Checkout the [website](https://www.climateinteractive.org/) of Climate Interactive for various webinar, workshop and game formats. In case you are based in Europe, check my [agenda](({filename}../pages/agenda.md)) for public events, or get in touch to book a workshop via [e-mail](mailto:info@donutlobby.nl).
