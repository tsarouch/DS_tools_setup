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


## Concerning the crontab
We can edit the crontab file with:
> crontab -e
And we can see what are the jobs in crontab with
> crontab -l
And we can remove a crontab job, either by removing the line in the file or by
> crontab -r


# +---------------- minute (0 - 59)
# |  +------------- hour (0 - 23)
# |  |  +---------- day of month (1 - 31)
# |  |  |  +------- month (1 - 12)
# |  |  |  |  +---- day of week (0 - 6) (Sunday=0 or 7)
# |  |  |  |  |
  *  *  *  *  *  command to be executed

example:
If I want to execute a script every 10 minutes:
*/10 * * * * /path/to/script


# Debug
If for any reason the crontab does not work you can print the output in a file:
e.g. 
```
* * * * * /home/john/bin/backup.sh > /home/cron_logs.log 2>&1
```

In the above:
cron_logs.log indicates that the standard output of the backup.sh script will be redirected to the backup.log file.
2>&1 indicates that the standard error (2>) is redirected to the same file descriptor that is pointed by standard output (&1).
So, both standard output and error will be redirected to cron_logs.log
