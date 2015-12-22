


# General 

We are usually interested to use the command line tools. 
They're well suited if you want to script your deployment through shell scripting (e.g. bash).

- AWS CLI : gives you only the basic commands, but they should be enough to deploy a static website to an S3 bucket. Small advantages such as being pre-installed on Amazon Linux if we work from.

- s3cmd: s3cmd supports everything AWS CLI does, plus adds some more extended functionality on top, although I'm not sure you would require any of it for your purposes. You can see all its commands here: http://s3tools.org/usage 



# Configuring AWS command line interface:
Information can be found here: 
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html


-  For general use, the aws configure command is the fastest way to setup your AWS CLI installation:
```
> aws configure
AWS Access Key ID [None]: XXX
AWS Secret Access Key [None]: XXX
Default region name [None]: eu-central-1
Default output format [None]: json
```
To update any of your settings, simply run aws configure again and enter new values as appropriate.  


The CLI stores credentials specified with aws configure in a local file named credentials in a folder named .aws in your home directory.  

Have a look in the files:
```
~/.aws/credentials
~/.aws/config
```

If the files are not there, we can create them in batch mode if needed:

```
AWS_CONFIG_DIR="/[home]/.aws"

STR_CRED=$'[default]\naws_access_key_id = xxx\naws_secret_access_key = xxxx'
echo "$STR_CRED" > $AWS_CONFIG_DIR/credentials

STR_CONF=$'[default]\noutput = json\nregion = eu-central-1'
echo "$STR_CONF" > $AWS_CONFIG_DIR/config
```


# Common actions


- See the data:
```
aws s3 ls s3://pthor-import-production/master/
```


- We want to list the last item in a bucket with some pattern

```
aws s3 ls s3://[my bucket]/ | grep server_log | grep 2014-12  | tail -1 | awk '{print $4}'
```

- We want to copy form S3 directly in our Hadoop system (overwrite if file exists):
hadoop distcp -overwrite s3n://<my_bucket>/<myfiles> hdfs://</path/to/myfiles>
