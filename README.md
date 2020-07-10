## Python Optimisation and Memory Management

> Author: <font color='#f78c40'>[Samuel Farrens](http://www.cosmostat.org/people/sfarrens)</font>    
> Year: 2020  
> Email: [samuel.farrens@cea.fr](mailto:samuel.farrens@cea.fr)  

## Contents

1. [Deterministic Profiling](#Deterministic-Profiling)
1. [Optimisation](#Optimisation)
1. [Memory Management](#Memory-Management)
1. [Further reading](#Further-Reading)

## Deterministic Profiling

Before attempting to optimise your code (*i.e.* make it run faster) it is essential to profile it. It can take a lot of time to improve a code and this effort can easily be wasted if you optimise the wrong parts. Profiling, in particular *deterministic profiling*, enables you to identify potential bottlenecks in your code so that your can better focus any optimisation measures.

> Deterministic profiling is meant to reflect the fact that all function call, function return, and exception events are monitored, and precise timings are made for the intervals between these events (during which time the user's code is executing). - [source](https://docs.python.org/2.0/lib/Deterministic_Profiling.html#:~:text=Deterministic%20profiling%20is%20meant%20to,the%20user's%20code%20is%20executing)

### cProfile

[cProfile](https://docs.python.org/3/library/profile.html) is a built-in Python profiler. The commands can be written directly into modules/scripts to track the number of calls to functions and the time spent on each call. Alternatively, cProfile can be passed as an option to the `python` command when executing a script. For this tutorial, we will use the latter option.

We will start by looking at the [`sleeper.py`](./sleeper.py) script. This script contains a function (`sleep_for_1s`) that calls Python's built-in [`sleep`](https://docs.python.org/3/library/time.html#time.sleep) method for one second. This will make it easy for us to assess the time spent on each call to this function. The other two functions in the script (`function1`, `function2`) simply make calls to the `sleep_for_1s` function.

Running the script on its own produces no output, however if we time the process we can see that it takes six seconds in total.

```bash
$ time python sleeper.py
python sleeper.py  0.02s user 0.01s system 0% cpu 6.045 total
```

cProfile will allow us to see how many calls were made to each function in the script and how long each call took.

```bash
$ python -m cProfile sleeper.py
```

The output should look something like this.

```
20 function calls in 6.009 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
1    0.000    0.000    6.009    6.009 sleeper.py:1(<module>)
1    0.000    0.000    5.008    5.008 sleeper.py:11(function1)
1    0.000    0.000    1.000    1.000 sleeper.py:27(function2)
1    0.000    0.000    6.009    6.009 sleeper.py:37(main)
6    0.000    0.000    6.009    1.001 sleeper.py:4(sleep_for_1s)
1    0.000    0.000    6.009    6.009 {built-in method builtins.exec}
1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
6    6.009    1.001    6.009    1.001 {built-in method time.sleep}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

We can also sort this output by *e.g.* the number of calls to a given function.

```bash
$ python -m cProfile -s calls sleeper.py
```

Which gives.

```
18 function calls in 6.016 seconds

Ordered by: call count

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
6    6.016    1.003    6.016    1.003 {built-in method time.sleep}
6    0.000    0.000    6.016    1.003 sleeper.py:4(sleep_for_1s)
1    0.000    0.000    6.016    6.016 {built-in method builtins.exec}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
1    0.000    0.000    5.016    5.016 sleeper.py:11(function1)
1    0.000    0.000    1.000    1.000 sleeper.py:27(function2)
1    0.000    0.000    6.016    6.016 sleeper.py:37(main)
1    0.000    0.000    6.016    6.016 sleeper.py:1(<module>)
```

Where we can see that `sleep_for_1s` was called a total of six times for a cumulative time of six seconds. `function1` was called once for a cumulative time of five seconds. If we look at the code we can indeed see that `function1` calls `sleep_for_1s` five times. Finally,  `function2` was called once for a cumulative time of one second. If we add the time of the these two function calls we get the total runtime of the script, as expected.

### gprof2dot

[`gprof2dot`](https://github.com/jrfonseca/gprof2dot) is a Python package for converting cProfile outputs into a [dot graph](http://www.graphviz.org/doc/info/lang.html). These graphs will make it easier for us to visualise the profiling information.

First we tell cProfile to output to a file (*e.g.* `sleeper.pstats`).

```bash
$ python -m cProfile -o sleeper.pstats sleeper.py
```

Then we can run `gprof2dot` on this output.

```bash
$ gprof2dot -f pstats sleeper.pstats | dot -Tpng -o sleeper.png
```

> Note that the `dot` command requires that [Graphviz](https://graphviz.org/) be installed (possible with `apt` and `brew`).

Which produces the following image.

<img src="./images/sleeper.png">

Here we can more easily see the hierarchy and the number of calls to each function.

### SnakeViz

[SnakeViz](https://jiffyclub.github.io/snakeviz/) is a browser based graphical viewer for cProfile output.

As before we need a cProfile output file.

```bash
$ python -m cProfile -o sleeper.pstats sleeper.py
```

Then we can run SnakeViz.

```bash
$ snakeviz sleeper.pstats
```

This will open a browser wind where you can navigate and search for function calls.

This is particularly useful for more complicated scripts such as [`complicated.py`](./complicated.py) that use a lot of built-in functions behind the scenes.

```bash
$ python -m cProfile -o complicated.pstats complicated.py
$ snakeviz complicated.pstats
```

### pyinstrument

Finally, if you prefer an alternative to cProfile, various other tools also exist such as [pyinstrument](https://github.com/joerick/pyinstrument).

To run simply replace calls to `python` with `pyinstrument`.

```bash
$ pyinstrument complicated.py
```

Which will produce something like the following.

```
Program: complicated.py

5.434 <module>  complicated.py:1
├─ 5.270 main  complicated.py:53
│  └─ 5.270 myfunc  complicated.py:40
│     └─ 5.270 mymethod  complicated.py:22
│        ├─ 4.986 prep_y  complicated.py:18
│        └─ 0.284 [self]
└─ 0.163 <module>  numpy/__init__.py:1
      [100 frames hidden]  numpy, pickle, struct, pathlib, ntpat...
```

pyinstrument also allows for more interactive profiling by rendering the output as HTML.

```bash
$ pyinstrument -r html complicated.py
```

## Optimisation

## Memory Management

## Further Reading
- [Python Profiling](https://medium.com/@antoniomdk1/hpc-with-python-part-1-profiling-1dda4d172cdf)
