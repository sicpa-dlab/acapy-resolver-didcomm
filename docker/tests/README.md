## run integration test
`docker-compose run tests && docker-compose stop`
## lots of output
`docker-compose up`

## Individual service logs
`docker-compose logs <requester or resolver>`

From the documentation:
```
Usage: logs [options] [SERVICE...]

Options:

--no-color Produce monochrome output.

-f, --follow Follow log output.

-t, --timestamps Show timestamps.

--tail="all" Number of lines to show from the end of the logs for each container.
```
You can start Docker compose in detached mode and attach yourself to the logs of all container later. If you're done watching logs you can detach yourself from the logs output without shutting down your services.

Use `docker-compose up -d` to start all services in detached mode (-d) (you won't see any logs in detached mode)
Use `docker-compose logs -f -t` to attach yourself to the logs of all running services, whereas -f means you follow the log output and the -t option gives you timestamps (See Docker reference)
Use Ctrl + z or Ctrl + c to detach yourself from the log output without shutting down your running containers
If you're interested in logs of a single container you can use the docker keyword instead:

Use `docker logs -t -f <name-of-service>`
Save the output
To save the output to a file you add the following to your logs command:

`docker-compose logs -f -t >> myDockerCompose.log`

- service logs directions taken from bruno-bieri at [stackoverflow](https://stackoverflow.com/a/40721348)