export PYTHONPATH='/opt/homebrew/Cellar/pdm/2.1.3/libexec/lib/python3.10/site-packages/pdm/pep582':$PYTHONPATH

## Vscode issues

### AREPL doesn't find imports

When using asdf, make sure that the repl is pointing to the right python

In settings.json
```json
    "AREPL.pythonPath": "/Users/pat/.asdf/shims/python",
```

### Pylance 3.10 syntax error

When using asdf and using 3.10 features, you may see this error
**alternative syntax for unions requires python 3.10 or newer?**

That is because pylance is global and not local to your project.
It will therefore default to the asdf global selected version.

Make sure your asdf global python version is >= 3.10.

## References
https://github.com/topics/copier-template
https://github.com/pawamoy/copier-poetry
https://github.com/Tecnativa/doodba-copier-template
https://github.com/pawamoy/copier-pdm
https://github.com/pykong/templates/blob/master/basic/copier.yml
https://github.com/pykong/templates
https://github.com/MaciejPatro/copier-cpp-cmake/blob/master/copier.yml