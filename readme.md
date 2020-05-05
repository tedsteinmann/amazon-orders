# Amazon Orders

Processing an Amazon orders file for budgeting purposes.

## Getting Started

Log in to Amazon.com, click on ```account & lists``` in the top right, then ```Download order reports```. Download a report of type ```items``` and place it in the [data/raw/](data/raw/) directory.

### Prerequisites

The script expects a ```categories.csv``` file for sensible budgeting categories in the [data/lookup/](data/lookup/) folder.


### Installing

There is a make file with basic functions ... it's a bit problematic, but demonstrates commands you will need.

Help:
```
make help
```

Build:
```
make build-all
```

Run:
```
make run
```

Files will be generated to the [data/processed/](data/processed/) folder.
