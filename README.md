# KivyMD Monorepo

If you want to work on more than one project,
you can clone this repository.

```bash
git clone --recurse-submodules https://github.com/kivymd/kivymd_monorepo.git
cd kivymd_monorepo
git submodule foreach --recursive 'git checkout main || git checkout master'

python development_install.py
```

This repository contains all [@kivymd](https://github.com/kivymd) and
[@kivymd-extensions](https://github.com/kivymd-extensions) repositories except
private projects.

## Useful commands

```bash
# Checkout main branch on all submodules
git submodule foreach --recursive 'git checkout main || git checkout master'

# Sync main branch with remote
git submodule update --rebase --recursive

# Add your fork as remote
cd KivyMD
git remote add fork https://github.com/<USERNAME>/KivyMD.git
```

## Tools

### [development_install.py]development_install.py)

Run `python development_install.py` to install all Python packages inside this
monorepo in development mode (editable mode).
"Editable" install means that all imports will point to source code.

## License

[MIT License](LICENSE).

See LICENSE files in submodules.
