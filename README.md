# lock
###### lock problem solver

## Installation
The software is developed in Python 3.8, so you should use it.

Clone the repo and go to its root directory.

install wheel: `pip install wheel`
run: `python setup.py sdist bdist_wheel`
install the wheel: `pip install dist/lock-{{version}}-py3-none-any.whl`

(Note: Input a correct {{version}}.)

There will be a script in your 
`Python/Scripts` directory. On Windows, if you run the last command as an Administrator, you can find it as `C:\Program Files\Python38\Scripts\lock.exe`.

## Example of the problem:
Can you open the three-digit-lock using these clues?

682 One digit is right and in its place<br>
614 One figit is right but in the wrong place<br>
206 Two digits are right but both are in the wrong place<br>
738 All digits are wrong<br>
380 One digit is right but in the wrong place<br>


## Usage
Running
`python lock/lock.py -h`
or on Windows:
`lock.exe -h`
you will get:

```
usage:lock.py [-h] file

Solve a lock problem defined in the given file

positional arguments:
  file                   <Required> file

optional arguments:
  -h, --help            Show this help message and exit

```
Structure of the file:

```
digits n
correct m d{n}
wrongplace m d{n}
allwrong d{n}
...
```

### Example

The command

`python lock/lock.py lock.txt`

with lock.txt containing:
```digits 3
correct 1 682
wrongplace 1 614
wrongplace 2 206
allincorrect 738
wrongplace 1 380
```
returns
042