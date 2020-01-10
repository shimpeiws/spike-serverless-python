# spike-serverless-python

## Deployment from Docker

### Setup environment variables

If you are using direnv, you can follow this way. If not, you need to setup environment variables in .envrc.example by your self.

`cp .envrc.example .envrc`

Update `.envrc` to setup AWS Keys.

`direnv allow`

### Build Docker

`docker-compose build`

### Deploy from container

Run container with bash from host

`docker-compose run app bash`

Deploy from container

`yarn deploy`

e.g.

```
% docker-compose run app bash
root@9a228c81ce07:/app# yarn deploy
```
