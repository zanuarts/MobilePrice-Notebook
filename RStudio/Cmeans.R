data <- read.delim(file.choose(), header = T)
View(data)
data.features = data
View(data.features)
library(e1071)
hasil <- cmeans(data.features, 3, 20, verbose=TRUE, method="cmeans", m=2)
hasil
plot(data[c('BALANCE', 'PURCHASES', 'ONEOFF_PURCHASES', 'CREDIT_LIMIT',	'PAYMENTS',	'MINIMUM_PAYMENTS')], col=hasil$cluster)