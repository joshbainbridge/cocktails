Requirements:

- Apple Silicon Mac.
- Python 3.

When cloning, you may need to enter hugging face credentials:

```bash
git clone --recursive git@github.com:joshbainbridge/cocktails.git;
```

Once cloned, if the virtual environment does not exist:

```bash
python -m venv venv; source venv/bin/activate;
python -m pip install -r requirements.txt;
```

Else if the virtual environment already exists:

```bash
source venv/bin/activate;
```

For running the program with default args:

```bash
./cocktails;
```

Access help information with:

```bash
./cocktails --help;
```

And to deactivate the environment:

```
deactivate;
```
