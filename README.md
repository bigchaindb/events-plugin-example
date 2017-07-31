# BigchainDB block plugin example

This repo contains a minimal implementation of a plugin for BigchainDB.
It listens to blocks and print the `id` of the block to the console.

It can be used as a baseline to publish the newly created blocks to different services, like RabbitMQ.

# Usage
Clone this repository and install the module:

```bash
$ pip install -e .
```

The module must be visible by BigchainDB. You can install it globally (you might need to use `sudo`) or in a virtual env.

Then, add the plugin to your `.bigchaindb` configuration:

```
{
    "server": { ... },
    "wsserver": { ... },
    ...
    "block_publishers": ["console_print"]
    ...
}
```

You can now run BigchainDB:
```
$ bigchaindb start
```

The log should display something like:
```
[2017-07-31 02:36:10] [INFO] (bigchaindb.processes) Loading block publisher plugin console_print (MainProcess - pid: 27894)
**************************************
Hello from bigchaindb_print_on_console
**************************************

...

************************* Got new block ************************
bdf87db2fefba96b9274928df511ee75e1db239cbce0752657eb8552d5344038
****************************************************************

...
```

# The Block model
Refer to the official documentation for the [Block Model](https://docs.bigchaindb.com/projects/server/en/v1.0.0/data-models/block-model.html)
