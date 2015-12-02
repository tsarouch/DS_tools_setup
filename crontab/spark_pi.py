import sys
import datetime
import os
from random import random
from operator import add
from pyspark import SparkContext

# we run this example like:
# [path]/spark-1.5.2-bin-hadoop2.6/bin/spark-submit spark_pi.py



if __name__ == "__main__":
    """
    Usage: pi [partitions]
    """
    sc = SparkContext(appName="PythonPi")
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(add)

    # The result of the calculation
    res = "Pi is roughly %f" % (4.0 * count / n)

    # Create a file and save the result

    # create the file name
    date_now = datetime.datetime.now()
    file_name = 'pi_calc_'
    file_name += str(date_now).replace(' ', '-').replace(':', '-').replace('.', '-')

    # change to the path of the python script - crontab runs elsewhere
    abs_path = os.path.abspath(__file__)
    script_path = os.path.dirname(abs_path)
    os.chdir(script_path)

    file = open(file_name, "w")
    file.write(res)
    file.close()

    sc.stop()
