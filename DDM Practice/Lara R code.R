library(scales)
library(RColorBrewer)

rm(list = ls())
nsim <- 20
mu <- c(10, -10) # drift rate ## should this be the slope?
sigma <- 1# variance?
tau <- 0.0001 # precision
probs <- NULL
for (i in 1:length(mu)) {
  p <- 1/2 * (1 + (mu[i] * sqrt(tau))/sigma)
  q <- 1/2 * (1 - (mu[i] * sqrt(tau))/sigma)
  probs <- list(probs, c(p,q))
}
D <- sigma * sqrt(tau)
a <- 1
lower <- 0
slope <- 0.01
z <- 0.5 #0.5 #0.3 unequal z
T_er <- 300
time <- list(rep(T_er, 1))
evidencecount <- list(rep(z,1))
ms_trial <- rep(T_er, 1)
evidence_trial <- z
evidencecount_trial <- rep(z,1)
answer <- rep(NA,1)
for (i in 1:nsim) {
  prob_trial <- unlist(sample(probs, 1))
  while (evidence_trial > lower & evidence_trial < a) {
    a <- a - slope
    lower <- lower + slope
    ms_trial <- c(ms_trial, ms_trial[length(ms_trial)] + 1)
    evidence_trial <- evidence_trial + sample(c(D, -D),1, prob = prob_trial)
    evidencecount_trial <- c(evidencecount_trial, evidence_trial)
    if(ms_trial[length(ms_trial)] >= 1000){
      break
    }
  }
  #classify answers
  if(evidence_trial <= lower){
    answer[i] <- 0
  }else if(evidence_trial >= a){
    answer[i] <- 1
  }else{
    answer[i] <- NA
  }
  time[[i]] <- ms_trial
  evidencecount[[i]] <- evidencecount_trial
  evidence_trial <- z
  ms_trial <- T_er
  evidencecount_trial <- z
}
plot.new()
colors <- c('#2596BE', '#E28743', '#BBBFBE')
nlines <- 20
if (is.na(answer[1])){
  plot( evidencecount[[1]] ~ time[[1]] , type="l" , bty="l" , xlab="time (ms)" , ylab="Evidence" , col= alpha(colors[3], 0.8), lwd=2 , pch=17 , ylim=c(0,1), xlim=c(T_er, max(unlist(time[c(1:nlines)]))))
}else if (answer[1] == 1){
  plot( evidencecount[[1]] ~ time[[1]] , type="l" , bty="l" , xlab="time (ms)" , ylab="Evidence" , col= alpha(colors[1], 0.8), lwd=2 , pch=17 , ylim=c(0,1), xlim=c(T_er, max(unlist(time[c(1:nlines)]))))
}else if (answer[1] == 0){
  plot( evidencecount[[1]] ~ time[[1]] , type="l" , bty="l" , xlab="time (ms)" , ylab="Evidence" , col= alpha(colors[2], 0.8), lwd=2 , pch=17 , ylim=c(0,1), xlim=c(T_er, max(unlist(time[c(1:nlines)]))))
}
for (i in 2:nlines) {
  if (is.na(answer[i])){
    lines(evidencecount[[i]] ~ time[[i]] , col= alpha(colors[3], 0.8), lwd=2 , pch=19 , type="l" )
  }else if (answer[i] == 1){
    lines(evidencecount[[i]] ~ time[[i]] , col = alpha(colors[1], 0.8), lwd=2 , pch=19 , type="l")
  }else if (answer[i] == 0){
    lines(evidencecount[[i]] ~ time[[i]] , col = alpha(colors[2], 0.8), lwd=2 , pch=19 , type="l")
  }
}
abline(a= 1 + (300 * slope), b= -slope, col = 'black')
abline(a= 0 - (300 * slope), b= slope, col = 'black')
abline(a=z, b=0, col = 'red')
abline(v=1000, col = 'red')