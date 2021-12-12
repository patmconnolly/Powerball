# Powerball

Originally published on [Patrick Connolly's Homepage and Blog](https://patrick.connolly.page/2021/12/12/powerball-prediction-based-on-statistical-analysis/)

The basic idea behind this is to use some basic statistics to determine the next Powerball (PB). Before I begin I wish to firmly state that this in no way is sponsored by PB or any state lotto, nor am I affiliated with them in any way. I simply wish to examine probability with PB as the example. Do not use these numbers as you will most likely lose.

There are some basic assumptions that must be made for this to work.

1. The balls used to draw the PB are used again and again though are eventually replaced.
2. Each ball has slight differences even though the manufacturing process is identical for each.
3. The process of drawing the balls does not change.

With these assumptions we can use a normal distribution as our basic statistical thought in that the most often drawn balls will continue to be drawn most often as long as they are not changed.

Thinking of the value of the X-axis not as a numerical value will allow us to do the simple calculation of counting the most recent n number of draws and apply that, similar to the Galton Board above, and find which numbers have the highest chances of being drawn. Remembering that the balls eventually must wear out and be replaced, we should think of how recent to keep the draws. For this example I chose 30 most recent draws as 10 weeks seems a fair guess in my humble opinion.

Please examine the program and let me know your thoughts in the comments below. If you would like a number to compare, the program predicts on December 13, 2021 the numbers to be:

3, 25, 44, 53, 64, PB 24