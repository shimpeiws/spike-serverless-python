## Deployment fron Docker

### Setup environment variables

`cp .envrc.example .envrc`
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
