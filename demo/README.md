# Running the Demo

## Local instance of universal resolver agent

```sh
$ docker-compose up -d resolver
```

Check the logs to copy the resolver invitation:

```sh
$ docker-compose logs resolver
```

Run the demo and paste in invite when prompted:

```sh
$ docker-compose run demo
```

## Live instance of universal resolver agent

```sh
$ docker-compose -f docker-compose.yml -f docker-compose.live.yml run demo
```

## Clean up

Don't forget to close down the containers running in the background:

```sh
$ docker-compose down
```

Or for the live instance:

```sh
$ docker-compose -f docker-compose.yml -f docker-compose.live.yml down
```
