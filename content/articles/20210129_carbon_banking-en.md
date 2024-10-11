Title: Rabobank and Microsoft - carbon banking plans
Date: 2021-01-29
lang: en

You can also read this post [in Dutch]({filename}/articles/rabobank-en-microsoft-carbon-banking.md)

Yesterday Rabobank announced a [carbon banking plan](https://www.rabobank.com/en/press/search/2021/20210129-rabobank-to-announce-initiative-to-tackle-global-co2-challenge-while-enhancing-farmers-businesses.html?utm_medium=RSS) in collaboration with Microsoft. The figure below summarizes their ambitions: they aim to plant trees on a land area of 15 million ha in order to compensate for 150 Mton of CO2 emissions in 2025.

![]({static}/images/rabobank-and-microsoft-carbon-banking-plans/1.png)

Plan by Rabobank and Microsoft

Let's try to estimate ourselves how realistic this plan is. To do so I use the En-ROADS climate simulator (developed by MIT Sloan School of Management and the think tank Climate Interactive). The model has been [calibrated](https://youtu.be/M2zUFuXmhDs) using 6 "integrated assessment models", the most accurate climate models in the world.[^1]

##### Worldwide CO2 emission

According to En-ROADs today's global emissions are at 60 Gton per year. 150 Mton would correspond to 0.25% of the global CO2 emissions, so that would be a significant step!

![]({static}/images/rabobank-and-microsoft-carbon-banking-plans/2.png)

##### Afforestation in En-ROADS

Worldwide the maximal land area availabe for afforestation is estimated to be [roughly 700 million ha](https://science.sciencemag.org/content/365/6448/76). That is twice the size of India. The 15 million ha which Rabobank and Microsoft aim for, would be 2% of that. Let's be optimistic and assume that they manage to plant all the trees they want this year. In the graph below, you see a tiny green line, close to the horizontal axis (it is hard to spot, I admit). The amount of CO2 which would be removed from the atmosphere in 2025 is roughly 4 Mton.

![]({static}/images/rabobank-and-microsoft-carbon-banking-plans/3.png)

CO2 removal in case we'd manage to plant trees on 15 Mha this year

##### 2 x India

Let's do a more unrealistic thought-experiment. Suppose we'd plant trees on an area of twice the size of India this year. If we focus solely on the carbon removal capacity from trees, this would just about meet the target which Microsoft and Rabobank set themselves.[^2]

![]({static}/images/rabobank-and-microsoft-carbon-banking-plans/4.png)

CO2 removal in case we'd plant trees on an area of 2xIndia this year

##### Agricultural soil sequestration in En-ROADS

Agroforestry has one other major beneficial effect which leads to CO2 removal: it improves soil quality which in turn increases the ability of the soil to sequester carbon.[^3] Does this effect get us any closer to the 150 Mton Microsoft and Rabobank aim for? The global area of land in use for agriculture is approximately [5 billion ha](http://www.fao.org/sustainability/news/detail/en/c/1274219/). So in this project, we are talking about 3% of that area. Let's see how large the change is in En-ROADS. The extra carbon sequestered by the soil is 20 Mton (apologies for not being able to adapt the vertical scale of the graph!):

![]({static}/images/rabobank-and-microsoft-carbon-banking-plans/5.png)

CO2 removal by agricultural soil sequestration

##### Could we be missing something?

So far we have been able to explain 24 Mton of carbon removal of the 150 Mton Rabobank and Microsoft are aiming for. Perhaps our modeling assumptions are incorrect. With the default settings, En-ROADS assumes that an _average_ tree _in a forest_ takes 80 years to mature. The trees we are concerned with here, grow on farm land in Sub-Saharan Africa. They get exposed to a lot of sunlight and might therefore mature faster. On the other hand, they might grow in dry regions with poor soil quality, so perhaps they don't (any experts in the audience?). Let's look see what happens when trees mature faster. If we change the assumptions in En-ROADS such that our trees mature in 20 years time instead of 80, we actually reach the desired target.[^4]

![]({static}/images/rabobank-and-microsoft-carbon-banking-plans/6.png)

CO2 removal in case trees mature in 20 years

##### Conclusion

**According to the En-ROADS climate simulator the plan proposed by Microsoft and Rabobank would lead to removal of 24 Mton per year of CO2 from the atmosphere in 2025.** If tropical trees on farmland mature in 20 years instead of 80, the carbon removal could be an order of magnitude larger, which would be in agreement with the goal of Microsoft and Rabobank (in case you are an expert, please let me know whether these trees can mature in 20 years). It would be interesting to see how Rabobank and Microsoft came to their estimates. Their intentions are good, but a better explanation to support their claims would be welcome! Microsoft, [by their own claim](https://www.microsoft.com/en-us/legal/compliance/integrity), runs on trust. Well, I trust transparency.

##### Feedback

Let me know what does not make sense to you! You can reach me at _enroads \[at\] his.ke_ or via LinkedIn.

##### More information on En-ROADS

Curious about the En-ROADS climate workshop? Participate in the workshop [on the En-ROADS website](https://www.climateinteractive.org/get-involved/webinars/) (mostly in English), watch a [long](https://www.youtube.com/watch?v=R9W_KEXNzm4&t=0s) or a [short](https://www.youtube.com/watch?v=u5mrnkOJdso) workshop recording on YouTube or contact an [En-ROADS climate ambassador](https://www.climateinteractive.org/tools/en-roads/climate-ambassadors/) for an interactive workshop in your preferred language.

[^1]: You can find all assumptions made in the model in the [En-ROADS reference guide](https://img.climateinteractive.org/wp-content/uploads/2021/01/En-ROADS_Reference_Guide_012221.pdf). In case you disagree with them, you can adapt them in the simulator according to your own insights.

[^2]: [Here](https://docs.climateinteractive.org/projects/en-roads/en/latest/guide/afforestation.html) you can read more on the positive and negative side effects of large scale afforestation

[^3]: This is nicely illustrated in the documentary [Kiss the Ground](https://kisstheground.com/)

[^4]: Another aspect which isn't discussed in the Rabobank announcement is how to motivate farmers to participate. I am enthusiastic about the [PIP approach](https://www.wur.nl/en/Research-Results/Research-Institutes/Environmental-Research/Programmes/Sustainable-Land-Use/Sustainable-production-systems/The-PIP-approach-proud-farmers-better-soils-more-food.htm)
