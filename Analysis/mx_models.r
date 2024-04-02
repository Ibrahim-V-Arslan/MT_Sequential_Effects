library(lme4)
library(car)
library(effects)

data <- read.csv("DF_reg_r.csv")
data <- subset(data, previous_response != 'NAN')

data$choice <- ifelse(data$choice == 'Red', 1, 0)
data$resp <- as.factor(data$choice)

data$prev_resp <- ifelse(data$previous_response == 'Red', 1, -1)
data$prev_resp <- as.factor(data$previous_response)




# clean up the dataframe ####
# Choice 0 and 1, 0 is blue, 1 is red ####
# prev_resp -1 and 1, -1 is blue, 1 is red ####
# evidence is the same ####
# prev_evidence is the same ####
# 4 different models ####

## Model 1 ####
m_AR0 <- glmer(data=data, resp ~ 
                 
                 evidence +
                 prev_evidence + 
                 prev_resp +
                 (1|pt_num),
               family = binomial,control=glmerControl(optimizer='bobyqa',optCtrl = list(maxfun=100000)))

vif(m_AR0)
summary(m_AR0)
Anova(m_AR0)
plot(effect(c('prev_evidence'), m_AR0)) 
plot(effect(c('prev_resp'), m_AR0)) 

## Model 2 ####
m_AR1 <- glmer(data=data, resp ~ 
                 
                 evidence +
                 prev_evidence + 
                 prev_resp +
                 (1 + evidence|pt_num),
               family = binomial,control=glmerControl(optimizer='bobyqa',optCtrl = list(maxfun=100000)))

anova(m_AR0, m_AR1)
vif(m_AR1)
summary(m_AR1)
Anova(m_AR1)
plot(effect(c('prev_evidence'), m_AR1)) 
plot(effect(c('prev_resp'), m_AR1)) 

## Model 3 ####

m_AR2 <- glmer(data=data, resp ~ 
                 
                 evidence +
                 prev_evidence + 
                 prev_resp +
                 (1 + evidence + prev_evidence|pt_num),
               family = binomial,control=glmerControl(optimizer='bobyqa',optCtrl = list(maxfun=100000)))

anova(m_AR1, m_AR2)
vif(m_AR2)
summary(m_AR2)
Anova(m_AR2)
plot(effect(c('prev_evidence'), m_AR2))
plot(effect(c('prev_resp'), m_AR2))

## Model 4 ####

m_AR3 <- glmer(data=data, resp ~ 
                 
                 evidence +
                 prev_evidence + 
                 prev_resp +
                 (1 + evidence + prev_evidence + prev_resp|pt_num),
               family = binomial,control=glmerControl(optimizer='bobyqa',optCtrl = list(maxfun=100000)))

anova(m_AR2, m_AR3)
vif(m_AR3)
summary(m_AR3)
Anova(m_AR3)
plot(effect(c('prev_evidence'), m_AR3))
plot(effect(c('prev_resp'), m_AR3))

Anova(m_AR0, m_AR1, m_AR2,)
