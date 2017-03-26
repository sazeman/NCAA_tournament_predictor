# NCAA_tournament_predictor

CalcStatWeights.py is a script that uses NCAA Men's Basketball team statistics from the prior season to come up with a formula for retroactively predicting matchup outcomes.

The formula format is about as basic as it gets: (Statistic_X * Weight1) + (Statistic_Y * Weight2) + etc.

Weights are decimals randomly generated from -1 to 1.

Each team ends up with a "score" based on the formula, with higher scores (ideally) representing better teams.

The scores' accuracy is then tested by running a series of team vs team matchups from the previous NCAA tournament, and the number of correct predictions is recorded.

The program repeatedly loops with new sets of weights, and keeps track of which weights resulted in the most correct predictions.

Each time the program improves on its number of correct predictions, the new total and set of weights are printed as output.

After the program completes and the optimal weights are found, the user could apply the formula to statistics from the current season to attempt to predict future outcomes.  If this is done immediately upon completion of the NCAA regular season, the user would have a means of predicting matchups in the upcoming NCAA Tournament.

-----

StatsReader.py is a tool for parsing through team statistics pages obtained specifically from the NCAA website at http://web1.ncaa.org/stats/StatsSrv/ranksummary, and printing only the statistical values (with comma delimiters in-between the values).  This made it a lot easier for me to obtain all the stats rather than having to manually copy and paste from the NCAA site.
