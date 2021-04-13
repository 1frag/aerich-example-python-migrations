# Example aerich to use python migrations

## Install fork
```bash
git clone git@github.com:1frag/aerich.git
cd aerich
pip install .
```

## Using current repo
```bash
docker-compose up -d  # make database
aerich upgrade
```

## Make own python migrations
```bash
cat template.py > migrations/app/"2_$(date +%Y%m%d%H%M%S)_another_change.py"
aerich upgrade
```
