# SaasLite

[![build](https://github.com/meyer1994/saaslite/actions/workflows/build.yml/badge.svg)](https://github.com/meyer1994/saaslite/actions/workflows/build.yml)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Read only SQLite as a service

## Table of Contents

- [About](#about)
- [Install](#install)
- [Deploy](#deploy)
- [Usage](#usage)
- [Thanks](#thanks)

## About

Project that allows you to query [SQLite][1] databases hosted on AWS [S3][2]
with a very simple HTTP API. This is good when you have an static database that
you want to make available to your applications but you can't, or do not want,
to host the file yourself.

Some use cases might be:

- Making the database available for [JAMStack][3] applications hosted on
services like [Cloudflare][4] workers, [Vercel][5], [Netlify][6], or others
- Sharing a database with multiple services without the need of replicating it
- Something else... (I am not creative today)

I developed this based on the first use case, I needed to make a small database
available for an application I deployed in Vercel. However, I could not send the
database itself (couple hundreds of megabytes) with the built application. Also,
I did not want to spin up some expensive SQL database for it.

### Benefits

It is very cheap and fast enough if you do not need full scale of SQL queries
to work fast. Besides, by being deployed using AWS Lambda, it costs almost
nothing to run. Of course, if your application gets VERY popular, you should
consider migrating off this approach.

### Drawbacks

As you can imagine, this implementation has many drawbacks in comparison to
hosting the file yourself besides your application. Depending on the queries
you need to make, they become SLOW. Really slow. If your database is too big,
hundreds of megabytes, you MUST create the proper indexes for this approach to
be usable. Yet, even with indexes, some queries force a full table scan, like
`LIKE`, making this approach terribly slow.

## Install

This application was created to run on [Lambda][7] functions. It assumes you
have the S3 instance deployed and with the `GetObject` permission properly set.

```sh
$ pip install -r requirements.txt
```

If you want to run it locally:

```sh
$ pip install uvicorn
$ export SAASLITE_S3_BUCKET_NAME=bucket-name
$ export SAASLITE_S3_BUCKET_REGION=bucket-region
$ uvicorn handler:app
# Application should be available on `localhost:8000`
```

## Deploy

We use [Serverless][8] framework to deploy the project to AWS Lambda. So, to
deploy it is as easy as:

```sh
$ npx serverless deploy
```

[Docker][9] deployment is used because [APSW][10] did not like the default
Lambda python environment.

## Usage

To use this service is as easy as uploading your SQLite database to your S3
bucket and querying it using your favourite HTTP client:

```sh
$ aws s3 cp your.db s3://bucket/your.db
$ xh /your.db q=='SELECT 123 AS num'
[
    {
        "num": 123
    }
]
```

That is it! Have fun!

## Thanks

- [@rogerbinns][11] for creating the [APSW][10] which allowed me to
do this.
- [@uktrade][12] for the [implementation][13] that I used as a base to my own
VFS.

[1]: https://sqlite.org/
[2]: https://aws.amazon.com/s3/
[3]: https://jamstack.org/
[4]: https://workers.cloudflare.com/
[5]: https://vercel.com/
[6]: https://www.netlify.com/
[7]: https://aws.amazon.com/lambda/
[8]: https://www.serverless.com/
[9]: https://www.docker.com/
[10]: https://rogerbinns.github.io/apsw/
[11]: https://github.com/rogerbinns
[12]: https://github.com/uktrade/
[13]: https://github.com/uktrade/sqlite-s3vfs
