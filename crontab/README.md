# General information
Crontab is a very light weight to schedule jobs.
It is a simple text file with a list of commands meant to be run at specified times.


# Schedule a job executing python script
There are few things to take care:
- We write the python file that does the job we want to schedule
- we write a simple shell file that calls the python file
- we give to both these files executable rights, this we need since crontab will not run under our account
- in the shell file we need to have the full paths
- we need to add the necessary line #!/bin/bash

> chmod +x py_job.py
> chmod +x py_job.sh


# Schedule a job executing pyspark script
crontab is a very light/simple way to do scheduling in distributed sytems, other tools might be more
relevant and flexible, e.g. oozie.
Having said that, the configuration of crontab for pyspark jobs does not change much

- we need to have the python code and a shell script that calls it
- we give exec rights to both above
- we give full paths in the shell script
- we need to add the necessary line #!/bin/bash


For the above see the relavant code in this dir
