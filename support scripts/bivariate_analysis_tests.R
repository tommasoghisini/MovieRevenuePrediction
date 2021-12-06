# the datasets used are the ones obtained after feature engineering, 
# filtering and regularization
library(DescTools)
data = read.csv(file= '/Users/gaspardugac/Downloads/data.csv') #replace path
data2 = read.csv(file= '/Users/gaspardugac/Downloads/data_gaspar.csv') #replace

tb1 = table(data$genre_1, data$profitable)

chisq.test(data$genre_1, data$profitable, correct=FALSE)
CramerV(tb1)

tb2 = table(data$production_country, data$profitable)

chisq.test(data$production_country, data$profitable, correct=FALSE)
CramerV(tb2)


data['holiday'] = 1 - data$X0...No.Holiday
tb3 = table(data$holiday, data$profitable)

chisq.test(data$holiday, data$profitable, correct=FALSE)
CramerV(tb3)

tb4 = table(data$year, data$profitable)

chisq.test(data$year, data$profitable, correct=FALSE)
CramerV(tb4)


t.test(data$budget~data$profitable)

t.test(data$runtime~data$profitable)

t.test(data$popularity.actor.1~data$profitable)

t.test(data$popularity.actor.2~data$profitable)

t.test(data$popularity.actor.3~data$profitable)

t.test(data$popularity.actor.4~data$profitable)

t.test(data$popularity.actor.5~data$profitable)

t.test(data$budget.actor.1~data$profitable)

t.test(data$budget.actor.2~data$profitable)

t.test(data$budget.actor.3~data$profitable)

t.test(data$budget.actor.4~data$profitable)

t.test(data$budget.actor.5~data$profitable)

t.test(data$popularity.production.company~data$profitable)

t.test(data$budget.production.company~data$profitable)

t.test(data2$revenue.actor.1~data$profitable)

t.test(data2$revenue.actor.2~data$profitable)

t.test(data2$revenue.actor.3~data$profitable)

t.test(data2$revenue.actor.4~data$profitable)

t.test(data2$revenue.production.company~data$profitable)

