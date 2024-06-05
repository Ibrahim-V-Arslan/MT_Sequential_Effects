library(lme4)
library(car)
library(effects)
# load data
data <- read.csv("DF_reg_rr.csv")
data <- subset(data, previous_response != 'NAN')

data$choice <- ifelse(data$choice == 'Red', 1, 0)
data$resp <- as.factor(data$choice)

data$prev_resp <- ifelse(data$previous_response == 'Red', 1, -1)

data$prev_resp[data$trial_nbr == 1] <- NA


data <- subset(data, select = -c(block_number))
data <- subset(data, select = -c(acc, true_value, difficulty, rt))
data <- subset(data, select = -c(X))
data <- subset(data, select = -c(choice))
data <- subset(data, select = -c(previous_response))

data <- data[, c("pt_num", "trial_nbr", "evidence", "prev_evidence", "resp", "prev_resp")]

colnames(data) <- c("subj", "trial", "evidence", "prev_evidence", "resp", "prev_resp")

data <- data[order(data$subj, data$trial), ]

data <- subset(data, trial != 1)
# Write data to CSV file
write.csv(data, file = "tokyo_driftV2.csv", row.names = FALSE)

# Define the subjects to exclude
exclude_subj <- c(2, 26, 43, 53, 56, 58)

# Exclude the subjects from the data
data <- data[!data$subj %in% exclude_subj, ]

write.csv(data, file = "tokyo_driftV3.csv", row.names = FALSE)

