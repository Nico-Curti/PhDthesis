## Dataset

In this case-control observational study, we evaluated $289$ old-age subjects referred to our Geriatric Memory Clinic.
The dataset comprises $189$ female and 100 male individuals with a mean age of 78.6 ($$\pm7.5$$) years.
The date were provided by the co-authors of this project at the Institute of Gerontology and Geriatrics at the University of Perugia (Department of Medicine).
For each patient a set of 26 cytokine expression level were computed with the additional informations about subject set, age and diagnosis label (AD, MCI or CTL).
Of the 289 enrolled subjects, the whole set of cytokines was available for 284 subjects (98%), specifically 87/88 CTL (99%), 70/73 MCI (96%), 127/129 AD (98%).

To approximate normal distribution, plasma cytokines and chemokines were log-transformed for data analyses.
For the analysis of single cytokines with respect to the CTL, MCI and AD group, we designed a linear model analysis, with the value of each cytokine as a linear combination of the subject group (with CTL samples as the baseline, and MCI, AD as conditions), age and sex, as factors (the formula representation would be \quotes{cytokine $\sim$ group + sex + age}).
The last two were included as possible confounding factors, even if the analyses revealed that their role for each cytokine is marginal.
Only IFN$$\alpha$$2, IL-1$$\alpha$$, and MCP-1 differed among groups after correction for age and sex.
A threshold $p<0.05$ was considered for significance at all levels (group, sex or age).

Then we applied the DNetPRO algorithm looking for a signature capable of discriminating between CTL and AD: to this purpose, we performed a Hold-Out cross-validation procedure to identify the cytokine signature, considering 2/3 of samples to train the model and then we tested the signature performance on the remaining 1/3 of the total samples.
In this analysis we did not separate male from female samples, to avoid the bias given by the uneven number of samples in these two groups, and since previous analysis at a single-cytokine level did not find significant differences due to sex.
Then, we classified MCI samples with the CTL-AD signature obtained in the previous step, that allowed labeling MCI samples as CTL or non-CTL.
