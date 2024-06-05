library(lme4)
library(car)
install.packages("rjson")
library("rjson")
data <- fromJSON("DF_reg.json")


m_AR0 <- glmer(data=df_sub_AR0, resp ~ 
                 
                 evidence_scaled +
                 prev_abs_evidence_scaled * prev_sign_evidence +
                 prev_resp * prev_conf_scaled +
                 
                 (1 + evidence_scaled|sub),
               family = binomial,control=glmerControl(optimizer='bobyqa',optCtrl = list(maxfun=100000)))

vif(m_AR0)
summary(m_AR0)
Anova(m_AR0)
plot(effect(c('prev_abs_evidence_scaled:prev_sign_evidence'), m_AR0)) 
plot(effect(c('prev_resp:prev_conf_scaled'), m_AR0)) 