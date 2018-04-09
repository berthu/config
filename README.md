# config
```
              |    |    |
             )_)  )_)  )_)
            )___))___))___)\
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
```
My config files. Currently contains:

## Python script to deploy files
- Usage: `python config.py` and follow the prompts.

## File directory is a csv file `files.csv`
- The structure is: repo file/directory, local file/directory, and type
- Types are: `g` for global file, `f` for global directory, and `l` for local only and `r` for remote only.
- If terminal does not have python installed, generate bash deployment scripts locally, SFTP this repo onto the target home directory and deploy.
