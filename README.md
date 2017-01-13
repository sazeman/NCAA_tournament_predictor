# NCAA_tournament_predictor

Script uses NCAA Men's Basketball team statistics from prior seasons to come up with a formula for retroactively predicting matchup outcomes.
The formula format is about as basic as it gets: (StatisticX * Weight1) + (StatisticY * Weight2) + etc.
Weights are randomly generated from -100 to 100.
Each team ends up with a "score" based on the formula, with higher scores (ideally) representing better teams.
The scores' accuracy is then tested by running a series of team vs team matchups from prior NCAA tournaments, and the number of correct predictions is recorded.
The program loops with new sets of weights, and keeps track of which weights resulted in the most correct predictions.
Each time the program improves on its number of correct predictions, the new total and set of weights are printed as output.

After the program completes and the optimal weight combination is found, the user could apply the formula to present-day statistics to attempt to predict future outcomes.  If this is done immediately upon completion of the NCAA regular season, the user would have a means of predicting matchups in the upcoming NCAA Tournament.
