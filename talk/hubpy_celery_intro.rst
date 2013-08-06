Intro to celery
===============
@corbinbs
---------

----

Why celery?
===========


 * decouple site/system from external services
 * fire and forget API calls
 * easy deployment of scheduled tasks (no crontab sync'ing)
 * time and rate limits
 * auto scale worker pool


----

Brokers
==========

 * RabbitMQ
 * Redis
 * MongoDB
 * Amazon SQS
 * http://docs.celeryproject.org/en/latest/getting-started/brokers/index.html


----

Backends
===========

 * Not required but can be useful
    * Database
    * Cache (memcache)
    * MongoDB
    * Cassandra

----

Tasks
=====

 * Can call tasks inline just like other functions
 * .delay()
 * .apply_async()

----


Tools
=========

 * celery worker
    * celery worker --config=celeryconfig --loglevel=DEBUG -B
 * celery command line: http://docs.celeryproject.org/en/latest/userguide/monitoring.html#celery-command-line-management-utility
 * https://github.com/mher/flower  (Real-time monitor and web admin)

----

:data-x: 0
:data-y: 2500
:data-z: 4000
:data-rotate-x: 90

Other possibilities
===================

 * WebHooks: http://docs.celeryproject.org/en/latest/userguide/remote-tasks.html#module-celery.task.http