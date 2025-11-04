Below are some outputs for sampling with the Snowball_collector

> Started with celebrity:  Matthew McConaughey
Sampled 130 celebrities:  Matthew McConaughey, ..., Debbie Allen
Men: 55%, Women: 45%, Average Age: 71.36

> Started with celebrity:  Emma Watson
Sampled 130 celebrities:  Emma Watson, ..., John F. Kennedy
Men: 48%, Women: 52%, Average Age: 55.46

> Sampling ended early: Closed dating loop encountered.
Started with celebrity:  Cillian Murphy
Sampled 2 celebrities:  Cillian Murphy, ..., Yvonne McGuinness
Men: 50%, Women: 50%, Average Age: 51.00

Below is the output for sampling with Alphabet_collector

>Sampled 130 celebrities:  Ariana Grande, ..., Zoë Kravitz
Men: 43%, Women: 57%, Average Age: 42.43

In snowball sampling we could get different kinds of samples by changing the starting celebrity. Typically (our Matthew McConaughey and Emma Watson examples), the ratio of Men to women is close to 1:1 (within 5%). The average age varied greatly depending on who whe selected first, however the later celebrities we sampled were often wuite old and sometimes even passed away. This is because our Depth First search prioritized the first person the celebrity dated to be the next data point. I suspect many men and women's first relationship is with someone close to their age, but a non trivial number of women's first relationship shews a few years older, causing the snowball to drift to older ages. An example of this is starting with Emma Watson as the first sampled celebrity and finishing with John F Kennedy. This phenonmenon did cause the average age to be older than the inital celebrity's age.

One issue of this method is that it really depends on the starting celebrity. There are also certain celebrities that will never appear in this sample. Cillian Murphy only ever dataed Yvonne McGuinness who also only data Cillian. Starting with Cillian Murphy we can only sample two people. THerefore any snowball sample of 130 would not include Cillian Murphy.

The Alphabet sample has only one posible result (unless the website's popularity ranking changes). Our sample included a higher percentage of women, and average was was 42.43. The age was much younger than the snowball sample because we are taking tredning contemporary celebritys who tend to be younger. The slight skew towards women may just indicate that female celebrity profiles are just browsed more on this site putting them higher on the rankings for each alphabet letter. 

The alphabet method would liekly miss out on historical figures who typically are not trending, and lesser known celebritys. This will cause this method to bias slightly.